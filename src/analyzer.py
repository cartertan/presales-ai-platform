"""RFP analysis module: calls Ollama to extract structured requirements."""

import json
import logging
import os
import re
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
ANALYSIS_MODEL = os.getenv("OLLAMA_ANALYSIS_MODEL", "qwq:latest")
COMPLIANCE_MODEL = os.getenv("OLLAMA_COMPLIANCE_MODEL", "granite4.1:30b")
FALLBACK_MODEL = os.getenv("OLLAMA_REASONING_BACKUP", "deepseek-r1:32b")

_NEXUS_PRODUCTS = [
    "Nexus Certificate Manager",
    "Nexus Smart ID Digital Access",
    "Nexus Smart ID Identity Manager",
    "Nexus OCSP",
    "Nexus Protocol Gateway",
    "Nexus m2trust CLM",
    "Cosmo Smartcard",
    "IDPlug Middleware",
    "Nexus Mobile Client",
    "Smart Desktop Application",
]

_INDUSTRIES = [
    "eGovernment",
    "Citizen ID",
    "Telco",
    "Banking and Finance",
    "Energy",
    "Oil and Gas",
    "Insurance",
    "Trust Centers",
    "Manufacturing",
]

_SYSTEM_PROMPT = (
    "You are a presales expert analyst specialising in PKI, digital identity, and cybersecurity solutions.\n\n"
    "Your task is to analyse an RFP (Request for Proposal) document and extract structured information.\n\n"
    "Nexus Group products available to match requirements:\n"
    + "\n".join(f"  - {p}" for p in _NEXUS_PRODUCTS)
    + "\n\nIndustries we serve:\n"
    + "\n".join(f"  - {i}" for i in _INDUSTRIES)
    + """

You MUST respond with ONLY valid JSON — no markdown fences, no explanation, no preamble.

Return this exact JSON structure:
{
  "executive_summary": "<2-3 sentence summary of what the customer wants>",
  "requirements": [
    {
      "id": "RFP-001",
      "section": "<section or page reference>",
      "requirement": "<full requirement text>",
      "type": "MANDATORY",
      "scoring_weight": "<percentage or descriptor if stated, else null>",
      "nexus_solution": "<most relevant Nexus product name or null>",
      "risk_flag": false,
      "remarks": "<gaps or concerns, empty string if none>"
    }
  ],
  "customer_objectives": ["<objective 1>", "<objective 2>"],
  "evaluation_criteria": [
    {"criterion": "<name>", "weight": "<% or descriptor>"}
  ],
  "submission_deadline": "<date string or null>",
  "budget": "<budget string or null>",
  "industry_vertical": "<best matching industry from the list>",
  "win_themes": ["<theme 1>", "<theme 2>"],
  "risk_areas": ["<risk 1>", "<risk 2>"]
}

Rules:
- type must be exactly MANDATORY or OPTIONAL
- id must follow RFP-001, RFP-002, ... sequential format
- nexus_solution must be one of the listed product names or null
- risk_flag is true when: unclear scope, tight timeline, missing specification, or no matching product
- Extract ALL requirements — do not summarise or skip any
"""
)

# Maximum characters to send to the model (~20k tokens at 4 chars/token)
_MAX_CHARS = 80_000


def check_ollama(base_url: str) -> bool:
    """Check whether the Ollama server is reachable.

    Args:
        base_url: The base URL of the Ollama API (e.g. http://localhost:11434).

    Returns:
        True if the server responds with HTTP 200, False otherwise.
    """
    try:
        response = requests.get(f"{base_url}/api/tags", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException as exc:
        logger.debug("Ollama health check failed: %s", exc)
        return False


def _list_available_models(base_url: str) -> list[str]:
    """Return model names currently available in the Ollama instance."""
    try:
        response = requests.get(f"{base_url}/api/tags", timeout=5)
        response.raise_for_status()
        data = response.json()
        return [m["name"] for m in data.get("models", [])]
    except requests.exceptions.RequestException as exc:
        logger.warning("Could not list Ollama models: %s", exc)
        return []


def _model_available(model: str, available: list[str]) -> bool:
    """Return True if model name appears in the available list.

    Matches exact names and base names (strips tag suffix for comparison).
    """
    if not available:
        return True  # Cannot list; attempt anyway
    base = model.split(":")[0]
    return any(m == model or m.split(":")[0] == base for m in available)


def _call_ollama(model: str, prompt: str, base_url: str, timeout: int = 300) -> str:
    """Send a generation request to Ollama and return the raw response text.

    Args:
        model: Ollama model name (e.g. qwq:latest).
        prompt: User prompt to send.
        base_url: Ollama API base URL.
        timeout: Request timeout in seconds.

    Returns:
        The model's raw text response.

    Raises:
        requests.exceptions.RequestException: On network or HTTP errors.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "system": _SYSTEM_PROMPT,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.1,
            "num_predict": 8192,
        },
    }
    logger.info("Calling Ollama model '%s' at %s/api/generate", model, base_url)
    response = requests.post(
        f"{base_url}/api/generate",
        json=payload,
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json().get("response", "")


def _extract_json(raw: str) -> dict[str, Any]:
    """Extract and parse the first JSON object found in a raw string.

    Tries: direct parse → strip markdown fences → find outermost braces.

    Args:
        raw: Raw text potentially containing a JSON object.

    Returns:
        Parsed dict.

    Raises:
        ValueError: If no valid JSON object can be found.
    """
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    stripped = re.sub(r"```(?:json)?", "", raw).strip()
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        pass

    start = raw.find("{")
    end = raw.rfind("}")
    if start != -1 and end > start:
        try:
            return json.loads(raw[start : end + 1])
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Could not parse JSON from model response: {exc}"
            ) from exc

    raise ValueError("No JSON object found in model response")


def analyze_rfp(text: str, config: dict[str, Any]) -> dict[str, Any]:
    """Analyse RFP text using Ollama and return a structured extraction dict.

    Attempts OLLAMA_ANALYSIS_MODEL first; falls back to OLLAMA_REASONING_BACKUP
    if the primary model is unavailable or the call fails.

    Args:
        text: Full RFP document text (from extractor.extract_pdf_text).
        config: Configuration overrides:
            - base_url (str): Ollama base URL.
            - analysis_model (str): Override for analysis model name.
            - timeout (int): HTTP request timeout in seconds.

    Returns:
        Structured analysis dict matching the schema in _SYSTEM_PROMPT, plus
        a '_model_used' key recording which model produced the result.

    Raises:
        RuntimeError: If Ollama is unreachable or all models fail.
        ValueError: If the model response cannot be parsed as JSON.
    """
    base_url = config.get("base_url", OLLAMA_BASE_URL)
    timeout = config.get("timeout", 300)
    primary_model = config.get("analysis_model", ANALYSIS_MODEL)

    if not check_ollama(base_url):
        raise RuntimeError(
            f"Ollama is not reachable at {base_url}. Is 'ollama serve' running?"
        )

    available = _list_available_models(base_url)
    logger.info("Available Ollama models: %s", available)

    if _model_available(primary_model, available):
        model_to_use = primary_model
        logger.info("Using primary analysis model: %s", model_to_use)
    else:
        logger.warning(
            "Primary model '%s' not available. Falling back to '%s'.",
            primary_model,
            FALLBACK_MODEL,
        )
        model_to_use = FALLBACK_MODEL

    if len(text) > _MAX_CHARS:
        logger.warning(
            "RFP text truncated from %d to %d chars to fit model context window",
            len(text),
            _MAX_CHARS,
        )
        text = text[:_MAX_CHARS]

    prompt = f"Analyse this RFP document and extract all requirements:\n\n{text}"

    try:
        raw_response = _call_ollama(model_to_use, prompt, base_url, timeout)
    except requests.exceptions.RequestException as exc:
        if model_to_use != FALLBACK_MODEL:
            logger.warning(
                "Primary model '%s' call failed (%s). Trying fallback '%s'.",
                model_to_use,
                exc,
                FALLBACK_MODEL,
            )
            try:
                raw_response = _call_ollama(FALLBACK_MODEL, prompt, base_url, timeout)
                model_to_use = FALLBACK_MODEL
            except requests.exceptions.RequestException as fallback_exc:
                raise RuntimeError(
                    f"All models failed. Last error: {fallback_exc}"
                ) from fallback_exc
        else:
            raise RuntimeError(
                f"Fallback model '{model_to_use}' also failed: {exc}"
            ) from exc

    logger.info("Received response from '%s', parsing JSON…", model_to_use)
    analysis = _extract_json(raw_response)
    analysis["_model_used"] = model_to_use
    return analysis
