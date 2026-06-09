# Telecommunications — Industry Knowledge

## Sector Overview
The telecommunications industry operates some of the world's
most complex and security-critical digital infrastructure —
mobile networks, fixed broadband, satellite communications,
and the interconnected systems that carry the voice, data,
and video traffic of billions of people and billions of
connected devices. PKI and digital identity are woven
throughout this infrastructure — securing network elements,
authenticating subscribers, protecting operational systems,
and enabling the trusted communications that consumers
and enterprises depend on.

Telcos face a unique dual challenge in PKI: they must
secure their own internal infrastructure — thousands of
network elements, operational support systems, and employee
credentials — while simultaneously providing identity and
authentication services to their subscribers and enterprise
customers as part of their service portfolio. A tier-1
telco operator may manage millions of certificates across
their network infrastructure while also operating as a
trust service provider issuing certificates to customers.

The shift to 5G has dramatically accelerated PKI requirements
in telecoms. 5G network functions require certificate-based
mutual authentication between network elements. Network
slicing creates new PKI management challenges. Edge computing
deployments need certificates at massive scale. IoT
connectivity over 5G requires device identity management
for billions of SIM-equipped devices. The telco sector
is entering a period of unprecedented PKI growth.

## Key Drivers and Challenges

### Drivers
- 5G rollout requiring certificate-based authentication
  for all network functions and network slices
- IoT explosion — billions of connected devices requiring
  device identity certificates managed by telcos
- Network function virtualization (NFV) and software
  defined networking (SDN) creating new certificate
  management requirements for virtual network functions
- GSMA security guidelines mandating PKI for network
  element authentication across interconnected operators
- Subscriber identity evolution — SIM to eSIM to
  software-based identity requiring PKI backbone
- Telco as trust service provider — operators offering
  PKI and identity services to enterprise customers
  as revenue-generating managed services
- Regulatory requirements for lawful interception
  and subscriber identity verification
- Fraud prevention — SIM swap fraud driving demand
  for stronger subscriber authentication

### Challenges
- Scale — tier-1 operators manage millions of network
  element certificates across thousands of sites
- Heterogeneous network estate — legacy 2G/3G/4G
  equipment alongside new 5G infrastructure, each
  with different certificate management capabilities
- Multi-vendor network environment — Ericsson, Nokia,
  Huawei, Cisco equipment with different PKI interfaces
- Operational complexity — network certificate expiry
  causes service outages, making certificate lifecycle
  management mission-critical
- Speed of network change — network elements added,
  moved, and decommissioned constantly, requiring
  automated certificate lifecycle
- Roaming and interconnect — certificates must be
  trusted across operator boundaries globally
- OT/IT convergence — network operations center
  systems increasingly converging with IT creating
  new identity management requirements

## Regulatory and Compliance Requirements

### GSMA Standards
- GSMA FS.16 — Network Equipment Security Assurance
  Scheme (NESAS) including PKI requirements
- GSMA FS.20 — 5G Cybersecurity Knowledge Base
- GSMA SGP.02 — M2M Embedded SIM specification
- GSMA SGP.22 — RSP Technical Specification for
  consumer eSIM
- GSMA IR.88 — LTE Roaming Guidelines including
  certificate requirements for IPX security

### 3GPP Standards
- 3GPP TS 33.210 — Network domain security for IP
  based protocols — certificate requirements for
  NDS/IP
- 3GPP TS 33.310 — Network domain security for
  authentication framework
- 3GPP TS 33.501 — Security architecture and
  procedures for 5G system
- 3GPP TS 33.511-33.517 — Security assurance
  specifications for 5G network functions

### Regional Regulatory
- EU NIS2 Directive — Security requirements for
  telecommunications operators as essential services
- EU Electronic Communications Code — Security
  measures for public electronic communications
  networks
- National telecommunications regulatory authority
  requirements for network security
- Lawful interception requirements — ETSI standards
  for lawful access to communications

## Typical PKI and IAM Requirements

### Network Infrastructure PKI
- CA hierarchy for network element certificates
- Certificates for: base stations, core network
  elements, routers, switches, OSS/BSS systems
- SCEP and EST enrollment for network devices
- Automated renewal — network elements cannot
  have certificate expiry causing outages
- High volume — tier-1 operator may have 100,000+
  network element certificates
- Multi-vendor support — Ericsson, Nokia, Cisco,
  Huawei device enrollment via standard protocols
- Certificate validity: 1-3 years with automated renewal

### 5G Specific Requirements
- Network function certificates for AMF, SMF, UPF,
  NRF, AUSF and all 5G core network functions
- Service-based architecture (SBA) TLS mutual
  authentication between network functions
- Network slice specific certificate management
- Edge cloud certificate automation via ACME
- Short-lived certificates for dynamic network
  functions: hours to days validity

### Subscriber Identity
- eSIM PKI for GSMA RSP infrastructure
- Certificate management for M2M and consumer eSIM
- SIM OTA (over the air) security certificates
- Subscriber authentication infrastructure

### Employee and Operational
- Network operations center employee authentication
- Privileged access management for network systems
- VPN and remote access for field engineers
- Multi-factor authentication for OSS/BSS systems

### Volume
- Network element certificates: 100K-1M+ for tier-1
- eSIM/IoT certificates: Millions to billions
- Employee certificates: Thousands to tens of thousands
- Certificate lifecycle: Fully automated — no manual
  renewal acceptable for network element PKI

## Nexus Solutions Commonly Deployed

### Core PKI Infrastructure
- **Nexus Certificate Manager** — Network element
  PKI platform. Manages all network device certificates.
  Handles high-volume automated issuance for 5G rollout.
  Integrates with multi-vendor network equipment.

- **Nexus CLM** — Certificate lifecycle management
  for network element certificates. Discovers all
  certificates across network, tracks expiry,
  automates renewal. Critical for preventing
  network outages from expired certificates.

- **Nexus OCSP** — Certificate status for network
  authentication. High-performance responder meeting
  telco-grade availability requirements.

- **Nexus Protocol Gateway** — Multi-protocol
  enrollment gateway for heterogeneous network
  estate. SCEP for legacy equipment, EST for
  modern devices, ACME for cloud-native 5G functions.

### Identity and Access Management
- **Nexus Smart ID Digital Access** — Network
  operations center and OSS/BSS authentication.
  Employee strong authentication for privileged
  network system access.

- **Nexus Smart ID Identity Manager** — Large
  workforce identity governance. Contractor
  lifecycle management for network field engineers.

### Mobile and Subscriber
- **Nexus Mobile Client** — Field engineer mobile
  credential. Subscriber strong authentication
  for customer self-service portal.

- **Nexus Mobile SDK** — Embedded in telco customer
  app for subscriber authentication and SIM
  swap prevention.

## Common Use Cases

### 1. Network Element Certificate Management
Automated certificate lifecycle for all network
infrastructure — base stations, core network
functions, OSS/BSS systems. Nexus CLM discovers
existing certificates, Nexus NCM manages issuance
and renewal, Protocol Gateway handles multi-vendor
enrollment. Zero manual intervention — certificates
renew automatically before expiry.

### 2. 5G Core Network Function Authentication
5G service-based architecture requires TLS mutual
authentication between all network functions.
Nexus NCM issues short-lived certificates for
AMF, SMF, UPF, and all 5G NFs. High-volume,
fast issuance supporting dynamic 5G network
scaling. ACME protocol for cloud-native NF
certificate automation.

### 3. IoT Device Identity for Telco-Managed Devices
Telco as connectivity provider manages device
identity certificates for IoT customers. Smart
meters, connected vehicles, industrial sensors
connecting via telco network receive device
certificates from telco-operated PKI. Nexus NCM
and Protocol Gateway handle mass enrollment at
IoT scale.

### 4. Telco as Trust Service Provider
Operator offers PKI and identity services to
enterprise customers as managed service. Nexus
NCM operates as the multi-tenant CA platform
serving multiple enterprise customers from
shared infrastructure. Operator manages CA
hierarchy, customers manage their own certificates
through delegated access.

### 5. Employee and NOC Authentication
Network operations center staff authenticate
with PKI smartcards or mobile credentials to
OSS/BSS systems, network management platforms,
and privileged access to network elements.
Strong authentication prevents unauthorized
access to network infrastructure.

## Competitive Landscape

### Key Competitors
- **Ericsson and Nokia** — Network equipment vendors
  include basic PKI capabilities in their network
  management systems. Limited to own equipment.
  Nexus differentiates with vendor-neutral platform
  managing multi-vendor networks.

- **Venafi** — Machine identity management platform
  with telco customers. Strong in certificate
  discovery and lifecycle automation. Less strong
  in CA platform and network device enrollment.
  Nexus offers complete stack including CA.

- **DigiCert** — Public CA with enterprise PKI
  platform. Cloud-based. Less suitable for telcos
  requiring on-premises sovereign PKI for network
  element certificates.

- **Sectigo (formerly Comodo CA)** — Certificate
  management platform. Primarily commercial CA.
  Less telco-specific expertise.

### Nexus Positioning
- Telco-proven at scale — multiple tier-1 operator
  deployments with millions of certificates under
  management
- Multi-vendor network support — open protocol
  support handles Ericsson, Nokia, Huawei, Cisco
  without vendor-specific dependencies
- Complete stack — CA, CLM, OCSP, Protocol Gateway,
  IAM — single vendor for entire telco PKI estate
- On-premises deployment — network element certificates
  must stay within operator infrastructure, Nexus
  delivers full on-premises capability

## Key Buying Personas

### Technical Decision Makers
- **Head of Network Security / CISO** — Owns network
  security architecture. Cares about threat coverage,
  certificate expiry risk, 5G security compliance.

- **Network Architecture Director** — Defines network
  technology standards. Evaluates PKI integration
  with network management systems and vendor equipment.

- **PKI / Cryptography Specialist** — Deep technical
  evaluator. Reviews CA architecture, certificate
  profiles, HSM integration, GSMA compliance.

- **OSS/BSS Architect** — Integration with operational
  support systems. API requirements, automation,
  ITSM integration.

### Business Decision Makers
- **CTO** — Technology strategy. 5G security posture,
  IoT platform capability, trust service business case.

- **CISO** — Risk owner. Certificate expiry incidents,
  network breach risk, regulatory compliance.

- **VP Network Operations** — Operational efficiency.
  Automated certificate management reducing NOC
  workload and preventing outages.

## Win Themes for Telco

### 1. Scale Without Compromise
"Nexus manages certificate lifecycles for millions
of network elements with full automation. No manual
intervention. No expiry-induced outages. Proven at
tier-1 operator scale."

### 2. Multi-Vendor Network Support
"Your network runs Ericsson, Nokia, Huawei, and Cisco.
Nexus speaks SCEP, EST, and ACME to all of them from
one platform. One certificate management system for
your entire heterogeneous network estate."

### 3. 5G Ready
"5G service-based architecture demands certificate-based
mutual authentication at cloud-native scale. Nexus
delivers high-volume, automated certificate issuance
for 5G network functions via ACME — ready for your
5G rollout today."

### 4. Prevent Network Outages
"An expired network element certificate causes a
service outage. Nexus CLM discovers every certificate
in your network, tracks expiry, and renews automatically
— before the expiry date, every time, without manual
intervention."

### 5. Telco as Trust Service Provider
"Your subscribers and enterprise customers trust you
with their connectivity. Extend that trust to identity.
Nexus enables you to operate a multi-tenant PKI platform,
offering certificate and identity services to enterprise
customers as a managed service revenue stream."