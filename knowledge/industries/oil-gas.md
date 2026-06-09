# Oil and Gas — Industry Knowledge

## Sector Overview
The oil and gas industry operates some of the most complex,
geographically dispersed, and safety-critical operational
technology environments in the world. From offshore drilling
platforms in remote oceans to onshore refineries processing
millions of barrels daily to transcontinental pipeline
networks spanning thousands of kilometers, the industry
relies on industrial control systems, SCADA networks,
and distributed automation infrastructure that must operate
continuously, safely, and securely under extreme conditions.

Cyber security in oil and gas has moved from a theoretical
concern to a board-level priority following high-profile
incidents including the Saudi Aramco Shamoon attack,
the Colonial Pipeline ransomware incident, and multiple
state-sponsored intrusions targeting energy infrastructure.
These incidents demonstrated that cyber attacks on oil
and gas systems can cause physical damage, environmental
disasters, fuel shortages, and economic disruption at
national scale — making robust digital identity and PKI
security foundational requirements rather than optional
enhancements.

PKI addresses core oil and gas security requirements:
authenticating the identities of operational systems and
the engineers who access them, encrypting communications
between control centers and field devices, signing
operational commands to prevent unauthorized actions,
and providing the audit trail that safety regulators
and incident investigators require. Nexus brings oil
and gas sector experience, understanding of the unique
OT constraints in upstream, midstream, and downstream
operations, and the NERC CIP and IEC 62443 compliance
knowledge that operators need.

## Key Drivers and Challenges

### Drivers
- Nation-state cyber threats specifically targeting
  oil and gas infrastructure as strategic assets
- Colonial Pipeline and similar incidents creating
  board-level urgency for OT security investment
- IEC 62443 industrial cybersecurity standard
  adoption mandating zone-based security including
  identity and authentication controls
- Digital oilfield transformation — sensor networks,
  IoT devices, and remote monitoring systems
  requiring device identity at scale
- Remote operations — pandemic-driven shift to
  remote operations creating permanent demand
  for secure remote access to OT systems
- Mergers and acquisitions — integrating disparate
  security estates from acquired companies
- ESG and regulatory pressure driving operational
  transparency requiring audit-ready systems
- Contractor and supply chain security — complex
  contractor ecosystems accessing OT systems
  requiring strong identity controls

### Challenges
- Extreme operational continuity requirements —
  unplanned downtime in a refinery or pipeline
  costs millions per hour, making security changes
  operationally risky
- Air-gapped and isolated OT networks — offshore
  platforms, remote pipeline stations, and
  classified defense-related facilities operate
  with strict network isolation
- Harsh physical environments — offshore platforms,
  desert locations, and arctic operations subject
  devices to extreme temperature, humidity, and
  vibration
- Legacy OT systems — process control systems
  with 20-40 year lifetimes running proprietary
  operating systems with no PKI support
- Multi-contractor environment — hundreds of
  contractors and vendors accessing OT systems
  with complex identity lifecycle requirements
- Safety-critical interdependencies — PKI
  infrastructure failure could impact safety
  instrumented systems if not carefully architected
- Offshore communications bandwidth — limited
  satellite bandwidth constrains certificate
  management protocol options for offshore assets
- Regulatory complexity — multiple overlapping
  frameworks: NERC CIP, IEC 62443, national
  petroleum authority regulations, HSE requirements

## Regulatory and Compliance Requirements

### Industrial Cybersecurity Standards
- IEC 62443 — Industrial Automation and Control
  Systems Security
  * IEC 62443-2-1: Security management system
  * IEC 62443-3-3: System security requirements
    and security levels
  * IEC 62443-4-2: Technical security requirements
    for IACS components — including authentication
    requirements for control system components
- ISA/IEC 62443 Security Level requirements for
  zones and conduits defining authentication
  strength per security level

### North American Standards
- NERC CIP — Critical Infrastructure Protection
  standards (widely adopted as reference globally)
  * CIP-005: Electronic Security Perimeters
  * CIP-006: Physical Security
  * CIP-007: Systems Security Management
    including patch management and authentication
  * CIP-010: Configuration Change Management
  * CIP-011: Information Protection

### Offshore and Process Safety
- IEC 61511 — Functional Safety: Safety Instrumented
  Systems — cyber security requirements for SIS
- ISO/IEC 27001 — Information security management
  system for oil and gas operators
- API RP 780 — Security Risk Assessment Methodology
  for the Petroleum and Petrochemical Industries
- IOGP Report 456 — Cybersecurity guidance for
  upstream oil and gas operators

### Regional Regulatory
- HSE (UK) — Process safety and cyber security
  guidance for major hazard facilities
- BSEE (US) — Bureau of Safety and Environmental
  Enforcement cybersecurity requirements for
  offshore facilities
- Saudi Aramco SACS — Saudi Aramco Cybersecurity
  Standards for suppliers and contractors
- Abu Dhabi ADNOC cybersecurity requirements

## Typical PKI and IAM Requirements

### OT Infrastructure PKI
- Dedicated OT CA hierarchy physically separate
  from corporate IT PKI
- Device certificates for DCS controllers, PLCs,
  RTUs, SCADA servers, and historian systems
- Engineering workstation certificates for
  control system access
- IEC 62443 zone-based certificate management
  with separate PKI per security zone
- Air-gapped certificate management capability
  for isolated OT networks
- Offline CA operations for highest security zones
- Long certificate validity: 5-10 years for
  embedded OT devices
- HSM for CA key protection in OT environment

### Remote Access and Field Operations
- Strong authentication for remote access to
  OT systems — no passwords for SCADA access
- VPN certificate authentication for remote
  engineers and contractors
- Mobile credential for field engineers accessing
  portable devices and tablets in the field
- Time-limited access certificates for contractor
  work orders — certificate expires when job
  is complete
- Two-person integrity for critical operations —
  dual certificate authorization for high-risk
  commands

### Employee and Contractor PKI
- Employee smart card for corporate network
  and OT system access
- Privileged access management certificates
  for DCS and SCADA administrators
- Contractor identity lifecycle — short-term
  certificates with sponsor-based renewal
- Cross-certification for contractor company
  identity federation
- Offshore crew rotation — certificate management
  for rotating offshore crews with predictable
  lifecycle tied to rotation schedule

### Document Signing
- Permit to work digital signatures — legally
  binding certificates for safety-critical
  work authorization
- Management of change documentation signing
- Incident investigation report signing
- Regulatory submission document signing
- Engineering drawing approval signatures

## Nexus Solutions Commonly Deployed

### OT Security Foundation
- **Nexus Certificate Manager** — Dedicated OT
  CA platform for control system device certificates.
  Separate from corporate IT PKI. Air-gapped
  deployment capability for isolated OT networks.
  IEC 62443 security level compliant certificate
  profiles.

- **Nexus OCSP** — Certificate status for OT
  authentication. Deployed within OT network
  boundary. Pre-signed response mode for
  air-gapped and offline environments where
  real-time OCSP queries are not possible.

- **Nexus Protocol Gateway** — Certificate
  enrollment for OT devices via SCEP and EST.
  Handles diverse OT vendor equipment with
  different enrollment capabilities.

- **Nexus CLM** — OT certificate lifecycle
  automation. Discovers all certificates across
  OT environment. Prevents certificate expiry
  causing process control disruptions.

### Access Control
- **Nexus Smart ID Digital Access** — Strong
  authentication for OT system access. No passwords
  for SCADA and DCS. Remote access certificate
  authentication for engineers and contractors.

- **Nexus Smart ID Identity Manager** — Contractor
  lifecycle management. Time-limited access for
  work orders. Offshore crew rotation identity
  management. Sponsor-based contractor approval.

### Mobile and Field
- **Nexus Mobile Client** — Field engineer mobile
  credential for tablet and mobile device access
  to field systems and work management applications.

- **Nexus Mobile SDK** — Embedded in oil and gas
  operator mobile work management apps for field
  engineer strong authentication.

## Common Use Cases

### 1. Refinery OT Network Certificate Management
Downstream operator deploys dedicated PKI for
refinery OT network — issuing device certificates
to DCS controllers, safety systems servers,
historian, and engineering workstations. Nexus NCM
operates as dedicated OT CA physically separated
from corporate IT network. IEC 62443 zone-based
architecture creates separate certificate domains
for safety instrumented systems versus process
control versus enterprise integration zone.
Certificate changes require formal management of
change approval before deployment.

### 2. Offshore Platform Secure Remote Access
Operator enables secure remote monitoring and
remote assistance for offshore platforms over
satellite link. All remote engineers authenticate
with PKI certificates before establishing encrypted
sessions to offshore SCADA. Time-limited remote
access certificates expire automatically after
session or work order completion. Nexus Mobile
Client provides remote engineer credentials on
laptop and tablet. Audit log of all remote access
sessions with certificate identity for safety
investigation capability.

### 3. Contractor Identity Lifecycle Management
Major upstream operator manages thousands of
contractors from dozens of companies accessing
OT systems across multiple facilities. Nexus
Smart ID Identity Manager automates contractor
lifecycle — sponsor approval workflow, certificate
issuance on approval, automatic expiry when work
order ends, immediate revocation on security
incident. Contractor certificates are time-limited
and facility-specific — a contractor authorized
for one platform cannot access another. Full
audit trail for security investigation.

### 4. Pipeline SCADA Authentication
Transmission pipeline operator secures SCADA
access for pipeline control centers and remote
pump station access. All pipeline operators
authenticate with smart card certificates for
SCADA logon. Remote terminal units at pump
stations use device certificates for encrypted
communication with control center. Certificate-based
mutual authentication between control center
servers and field RTUs prevents unauthorized
command injection.

### 5. Permit to Work Digital Signature
Operator deploys digital permit to work system
replacing paper-based safety permits. Qualified
electronic signatures on work permits provide
legally binding authorization for hazardous
work activities. Signing authority certificates
held on smart cards by area authority and
performing authority. Audit trail of all permit
signatures for safety investigation and regulatory
inspection.

## Competitive Landscape

### Key Competitors
- **Claroty / Medigate** — OT security visibility
  and threat detection platforms. Asset discovery
  focus rather than PKI. Nexus complements rather
  than competes — CLM can use Claroty discovery data.

- **Nozomi Networks** — OT network monitoring and
  anomaly detection. No PKI capability. Different
  use case from Nexus but often evaluated together.

- **Honeywell Forge** — Industrial cybersecurity
  suite including identity components. Primarily
  for Honeywell process control environments.
  Nexus is vendor-neutral.

- **Siemens Industrial Security** — OT security
  for Siemens automation environments. Proprietary
  approach. Nexus integrates across all OT vendors.

- **Generic PKI vendors** — Entrust, DigiCert
  — enterprise PKI without OT-specific knowledge.
  Lack understanding of IEC 62443, air-gapped
  OT networks, and process safety implications.

### Nexus Positioning
- OT PKI specialization — not an IT vendor adapting
  to OT, but a vendor with genuine OT security
  understanding and references
- Air-gapped deployment capability — fully functional
  in isolated OT networks without internet connectivity
- IEC 62443 compliance knowledge — understanding
  security levels, zones, conduits, and component
  authentication requirements
- Safety-aware implementation — understanding that
  PKI changes in safety-critical environments
  require formal change management and testing
- Long-term support commitment matching OT
  infrastructure lifetimes of 20-30 years

## Key Buying Personas

### OT Security and Operations
- **OT Security Manager / OT CISO** — Primary
  sponsor. Owns OT security program. Understands
  IEC 62443 and NERC CIP. Concerned about
  operational risk of security changes and
  justified to board on cyber investment.

- **DCS/SCADA System Owner** — Technical authority
  for control systems. Evaluates impact on
  operational systems. Requires proof of concept
  in non-production environment before production
  deployment.

- **Process Safety Manager** — Concerned about
  any change to safety instrumented systems.
  Requires formal safety assessment for PKI
  integration with SIS.

### IT and Enterprise Security
- **CISO** — Overall enterprise security including
  OT. IT/OT convergence strategy. Vendor risk
  management.

- **Enterprise Architect** — IT/OT integration
  architecture. Directory services, identity
  federation, monitoring integration.

### Operations and HSE
- **VP Operations** — Operational continuity.
  Concerned about unplanned downtime from
  security implementation. Needs proven approach
  with references from similar operators.

- **HSE Director** — Permit to work digitization.
  Safety case for digital signatures on safety
  permits. Regulatory acceptance of digital
  signatures for safety documentation.

## Win Themes for Oil and Gas

### 1. OT Security Without Operational Risk
"Nexus understands that in a refinery or offshore
platform, security changes must be implemented
without operational disruption. Our OT PKI
implementation methodology includes formal change
management, staged rollout, and rollback procedures
designed for safety-critical environments."

### 2. Air-Gapped OT Capability
"Your most critical systems are air-gapped for
good reason. Nexus delivers fully functional PKI
for isolated OT networks — offline CA operations,
pre-signed OCSP responses, sneakernet certificate
management — without requiring connectivity
that compromises your security architecture."

### 3. IEC 62443 Compliance
"Nexus delivers the authentication controls that
IEC 62443 Security Level 2 and 3 require for
industrial control systems. Zone-based certificate
management, strong authentication for all human
machine interfaces, and device identity for all
control system components."

### 4. Contractor Security at Scale
"Oil and gas operations depend on hundreds of
contractors from dozens of companies. Nexus Smart
ID Identity Manager gives you complete visibility
and control of every contractor identity — time-limited
access, sponsor-based approval, automatic expiry,
and immediate revocation — without manual overhead."

### 5. Proven in Critical Infrastructure
"Nexus secures critical infrastructure across
energy, utilities, and industrial sectors globally.
We understand the stakes in oil and gas operations
and we bring the operational maturity and security
depth that critical infrastructure protection requires."