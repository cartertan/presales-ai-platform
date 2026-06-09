# Nexus CLM
**Category:** PKI | **Code:** CLM

## Product Overview
Nexus CLM is an automated certificate lifecycle management platform
purpose-built for machine identity — managing the certificates
that secure server-to-server communications, application workloads,
microservices, APIs, and operational technology assets. As
organizations scale their digital infrastructure, the number of
machine certificates grows exponentially, making manual certificate
management impossible and certificate expiry incidents inevitable.

Nexus CLM solves this by providing full visibility and automated
control over every machine certificate across the enterprise —
from on-premises servers and virtual machines to containers,
Kubernetes workloads, cloud instances, and OT devices. It
discovers existing certificates, tracks their lifecycle, enforces
renewal policies automatically, and integrates with CI/CD pipelines
to ensure certificates are always valid without human intervention.

For enterprises running thousands of servers, financial institutions
managing trading infrastructure, telcos operating core network
equipment, and energy companies securing SCADA systems, Nexus CLM
eliminates the operational risk of certificate expiry incidents
while reducing the burden on PKI and security operations teams.
A single expired certificate can bring down a production system,
trigger a security audit finding, or cause a regulatory breach —
Nexus CLM ensures this never happens.

## Key Features
- Automated certificate discovery across entire infrastructure
- Continuous certificate inventory and lifecycle tracking
- Automated renewal before expiry with configurable lead time
- Policy-based certificate lifecycle enforcement
- Integration with CI/CD pipelines for DevOps workflows
- ACME protocol for cloud-native and container environments
- Agent-based and agentless discovery modes
- Certificate health scoring and risk dashboard
- Expiry alerting with escalation workflows
- Multi-CA support for all certificate sources
- Crypto-agility assessment and migration planning
- REST API for full automation and ITSM integration
- Role-based access for distributed administration
- Compliance reporting for audit requirements

## Technical Specifications
**Discovery Methods:**
- Network scanning for TLS certificate discovery
- Agent-based discovery for comprehensive server inventory
- Cloud API integration for AWS, Azure, GCP certificate discovery
- Kubernetes and container platform scanning
- Active Directory integration for Windows certificate stores
- HSM and key store integration
- Manual import for legacy and air-gapped systems

**Certificate Sources Supported:**
- Nexus Certificate Manager (native integration)
- Microsoft AD CS
- AWS Private CA
- Azure Key Vault
- Google Cloud CAS
- DigiCert, GlobalSign, Entrust (public CA APIs)
- Any ACME-compatible CA
- Any REST API-enabled CA

**Automation Protocols:**
- ACME (RFC 8555) for automated renewal
- EST (RFC 7030) for enterprise enrollment
- SCEP (RFC 8894) for network device renewal
- REST API for custom automation workflows
- PowerShell and Ansible modules for Windows environments

**Platform Support:**
- Deployment: On-premises, private cloud, SaaS
- OS: Windows Server, Linux (RHEL, Ubuntu, CentOS)
- Container: Docker, Kubernetes, OpenShift
- Cloud: AWS, Azure, GCP
- High Availability: Active-active clustering
- Database: SQL Server, PostgreSQL

## Key Use Cases
1. **Enterprise Certificate Inventory and Visibility** — Complete
   discovery and ongoing tracking of every TLS, client, and
   code signing certificate across on-premises, cloud, and
   hybrid environments. Security and PKI teams gain a single
   dashboard showing every certificate, its expiry date,
   issuing CA, risk score, and renewal status — eliminating
   certificate sprawl and shadow PKI.

2. **Automated Certificate Renewal** — Policy-driven automatic
   renewal of server certificates before expiry, with no manual
   intervention required. Nexus CLM detects upcoming expiry,
   requests renewal from the appropriate CA, installs the new
   certificate, and updates the service — all automatically.
   Eliminates production outages caused by expired certificates.

3. **DevOps and Cloud-Native Certificate Automation** — ACME
   protocol integration with Kubernetes cert-manager, HashiCorp
   Vault, and CI/CD pipelines ensures that containers and
   microservices always have valid certificates throughout
   their lifecycle, from deployment through scaling and teardown.

4. **OT and Industrial Certificate Management** — Certificate
   lifecycle management for SCADA systems, industrial controllers,
   smart meters, and operational technology assets in energy,
   manufacturing, and utilities — where certificate expiry in
   production systems has physical safety implications.

5. **Crypto-Agility and Post-Quantum Migration** — Assessment
   of entire certificate estate for cryptographic algorithm
   compliance, identification of weak or deprecated algorithms,
   and orchestrated migration to stronger algorithms or
   post-quantum cryptography as standards evolve.

## Industry Applications
- **eGovernment:** Server and application certificate lifecycle
  for government IT infrastructure, automated renewal for
  citizen-facing service certificates
- **Banking and Finance:** Trading platform TLS certificate
  management, core banking server certificates, automated
  renewal for payment infrastructure
- **Telco:** Core network element certificate management,
  5G network function certificate automation, OSS/BSS
  application certificate lifecycle
- **Energy and Utilities:** Smart meter certificate lifecycle,
  SCADA server certificate management, IEC 62351 compliant
  OT certificate automation
- **Oil and Gas:** Remote terminal unit certificate lifecycle,
  SCADA and DCS system certificate management, operational
  technology PKI automation
- **Manufacturing:** Industry 4.0 machine certificate lifecycle,
  production line controller certificates, supply chain
  code signing certificate management

## Competitive Differentiators
- Unified visibility across every certificate type and source —
  internal CA, external public CA, and cloud CA certificates
  all managed from one platform
- OT and industrial focus — purpose-built for the certificate
  management challenges of operational technology environments
  where downtime is not an option
- Native integration with Nexus Certificate Manager creates
  a closed-loop lifecycle — discovery, tracking, renewal,
  and revocation all orchestrated within the Nexus platform
- Crypto-agility capability helps organizations assess and
  migrate their entire certificate estate as cryptographic
  standards evolve toward post-quantum algorithms
- Agent and agentless modes accommodate both modern
  cloud-native environments and legacy systems that
  cannot run agents
- Proven at telco scale managing millions of network
  element certificates with automated renewal

## Integration Capabilities
- **Nexus Certificate Manager** — Primary CA integration
  for enterprise certificate issuance and renewal
- **Nexus Protocol Gateway** — Multi-protocol enrollment
  for diverse device types needing certificate renewal
- **HashiCorp Vault** — Secrets management integration
  for cloud-native certificate workflows
- **Kubernetes cert-manager** — ACME-based certificate
  automation for container workloads
- **ServiceNow** — ITSM integration for change management
  workflows around certificate renewal
- **Ansible and Terraform** — Infrastructure as code
  integration for automated certificate deployment
- **SIEM platforms** — Certificate expiry events and
  policy violations forwarded for security monitoring
- **AWS, Azure, GCP** — Native cloud API integration
  for cloud-hosted certificate discovery and management

## Compliance and Standards
- RFC 8555 — ACME automated certificate management
- RFC 7030 — EST certificate enrollment
- RFC 8894 — SCEP certificate enrollment
- ETSI EN 319 411 — Certificate policy compliance tracking
- FIPS 140-2/3 — Cryptographic algorithm compliance
  assessment and enforcement
- IEC 62351 — Power systems security certificate
  management requirements
- NERC CIP — Bulk electric system cyber security
  certificate lifecycle requirements
- NIST SP 800-57 — Key management lifecycle guidance
- ISO 27001 — Certificate management control requirements
- PCI DSS — TLS certificate management for cardholder
  data environment compliance

## Customer Reference Profile
- Tier-1 telecommunications operator
  Products: Nexus CLM + NCM + Protocol Gateway
  Scale: 2M+ network element certificates
  Use case: Automated renewal for core network TLS
  and device authentication certificates
  Outcome: Zero certificate expiry incidents since
  deployment, 90% reduction in PKI operations effort

- National smart grid utility
  Products: Nexus CLM + NCM
  Scale: 500,000 smart meter and SCADA certificates
  Use case: Automated OT certificate lifecycle with
  IEC 62351 compliance reporting
  Outcome: Full certificate visibility achieved for
  first time, automated renewal eliminating manual
  field operations for certificate updates

- Global investment bank
  Products: Nexus CLM + NCM + Digital Access
  Scale: 45,000 server and application certificates
  Use case: Trading platform certificate automation,
  crypto-agility assessment for post-quantum migration
  Outcome: Certificate inventory reduced from 6-week
  manual audit to real-time dashboard, all SHA-1
  certificates identified and migrated