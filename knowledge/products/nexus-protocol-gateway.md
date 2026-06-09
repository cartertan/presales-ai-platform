# Nexus Protocol Gateway
**Category:** PKI | **Code:** NPG

## Product Overview
Nexus Protocol Gateway (NPG) is a multi-protocol certificate enrollment
gateway that bridges diverse client enrollment protocols to backend PKI
infrastructure. It acts as a universal front door for certificate
requests — accepting enrollment requests in any supported protocol
format and translating them to the appropriate backend CA communication,
regardless of which CA platform is deployed behind it.

NPG solves one of the most common PKI integration challenges in
enterprise environments: different devices, applications, and systems
speak different enrollment protocols. Network devices use SCEP. Modern
DevOps pipelines use ACME. Industrial systems use CMP. Legacy systems
use CMC or custom APIs. Rather than forcing all clients to use a single
protocol or requiring multiple separate enrollment endpoints, NPG
provides a single, unified enrollment gateway that handles them all.

For large enterprises, government agencies, and telecommunications
operators managing thousands of heterogeneous devices and systems,
NPG dramatically reduces PKI integration complexity and accelerates
certificate enrollment across the entire technology estate.

## Key Features
- Multi-protocol support: SCEP, EST, ACME, CMP, CMC simultaneously
- Protocol translation between enrollment clients and backend CA
- Policy enforcement at enrollment gateway level
- Certificate profile selection based on request attributes
- Authentication of enrollment requests before forwarding to CA
- Load balancing across multiple backend CA instances
- Request throttling and rate limiting for DoS protection
- Full audit logging of all enrollment requests and responses
- High availability active-active deployment
- REST management API for configuration and monitoring
- Support for pre-shared key and certificate-based enrollment auth
- Automated certificate renewal workflow support

## Technical Specifications
**Supported Enrollment Protocols:**
- SCEP (Simple Certificate Enrollment Protocol) — RFC 8894
- EST (Enrollment over Secure Transport) — RFC 7030
- ACME (Automated Certificate Management Environment) — RFC 8555
- CMP (Certificate Management Protocol) — RFC 4210
- CMC (Certificate Management over CMS) — RFC 5272
- Proprietary REST API for custom integrations

**Backend CA Integration:**
- Nexus Certificate Manager (native integration)
- Microsoft AD CS
- EJBCA
- OpenCA
- AWS Private CA
- Azure Key Vault
- Any CMP-compatible CA

**Authentication Methods:**
- Pre-shared key (PSK) for SCEP
- Client certificate authentication
- One-time password (OTP) challenge
- RADIUS authentication integration
- Active Directory / LDAP integration

**Platform Support:**
- Deployment: On-premises, private cloud, DMZ
- OS: Windows Server, Linux (RHEL, Ubuntu)
- High Availability: Active-active clustering
- Load Balancing: Built-in and external load balancer support

## Key Use Cases
1. **Network Device Certificate Enrollment** — Issues certificates to
   routers, switches, firewalls, and access points using SCEP protocol
   for 802.1X network authentication and device identity across
   enterprise and service provider networks.

2. **IoT and Smart Device Enrollment** — High-volume certificate
   issuance for IoT devices, smart meters, and connected assets
   using lightweight SCEP or EST protocols optimized for
   resource-constrained devices.

3. **DevOps and Cloud-Native Enrollment** — ACME protocol support
   enables automated TLS certificate issuance and renewal for
   Kubernetes workloads, microservices, and CI/CD pipelines
   without manual intervention.

4. **Industrial and OT System Enrollment** — CMP protocol support
   for industrial control systems, SCADA components, and
   operational technology assets in energy, manufacturing,
   and critical infrastructure environments.

5. **Multi-CA Consolidation** — Single enrollment endpoint for
   organizations with multiple CAs — consolidates SCEP, EST,
   and ACME traffic through one gateway, enforcing consistent
   policy regardless of which backend CA issues the certificate.

## Industry Applications
- **eGovernment:** Enrollment gateway for government device PKI —
  workstations, servers, network devices, and citizen kiosks
- **Telco:** Network device certificate enrollment for core network
  infrastructure, base stations, and CPE devices
- **Energy and Utilities:** Smart meter enrollment gateway handling
  millions of device certificate requests using SCEP/EST
- **Banking and Finance:** Secure enrollment for ATMs, POS terminals,
  banking kiosks, and HSM-protected infrastructure
- **Manufacturing:** Industry 4.0 device enrollment for PLCs,
  sensors, robots, and connected manufacturing equipment
- **Oil and Gas:** Certificate enrollment for SCADA systems,
  remote terminal units, and operational technology assets

## Competitive Differentiators
- Broadest protocol support in the market — SCEP, EST, ACME,
  CMP, and CMC from a single gateway
- CA-agnostic design — works with any backend CA, not just Nexus
- Policy enforcement at gateway prevents unauthorized enrollment
  before requests reach the CA backend
- Designed for high-volume IoT scenarios — handles thousands of
  simultaneous enrollment requests
- Proven in national-scale deployments — government device PKI
  programs with millions of enrolled devices
- Simplified operations — one gateway to manage instead of
  multiple protocol-specific enrollment endpoints

## Integration Capabilities
- **Nexus Certificate Manager** — Primary backend CA for certificate
  issuance and policy enforcement
- **Nexus OCSP Responder** — Paired deployment for complete PKI
  enrollment and validation infrastructure
- **Active Directory / LDAP** — Request authentication and
  authorization before enrollment
- **RADIUS servers** — Challenge-response authentication for
  SCEP device enrollment
- **HSM vendors** — Gateway TLS termination keys protected
  by Utimaco or Thales HSM
- **Network management systems** — Integration for automated
  device certificate lifecycle management
- **Kubernetes / cert-manager** — ACME protocol integration
  for cloud-native certificate automation

## Compliance and Standards
- RFC 8894 — Simple Certificate Enrollment Protocol (SCEP)
- RFC 7030 — Enrollment over Secure Transport (EST)
- RFC 8555 — Automatic Certificate Management Environment (ACME)
- RFC 4210 — Certificate Management Protocol (CMP)
- RFC 5272 — Certificate Management over CMS (CMC)
- ETSI EN 319 411 — Supporting enrollment infrastructure
  for qualified certificate issuance
- FIPS 140-2/3 — Via HSM integration for gateway signing keys
- IEC 62351 — Supporting enrollment for energy sector OT devices
- NERC CIP — Supporting device certificate requirements for
  bulk electric system cyber security

## Customer Reference Profile
- National telecommunications operator
  Products: Protocol Gateway + NCM + OCSP
  Scale: 500,000+ network device certificates
  Protocols: SCEP for legacy, EST for modern devices
  Outcome: Unified enrollment replacing 3 separate systems

- Smart grid utility company
  Products: Protocol Gateway + NCM + m2trust CLM
  Scale: 2M smart meter certificate enrollments
  Protocol: SCEP over constrained IoT network
  Outcome: Automated mass enrollment in 6-month rollout

- Government enterprise device PKI
  Products: Protocol Gateway + NCM + Smart ID
  Scale: 50,000 government workstations and devices
  Protocols: SCEP, EST, ACME across mixed estate
  Outcome: Single enrollment gateway replacing legacy manual process