# Banking and Finance — Industry Knowledge

## Sector Overview
The banking and financial services industry operates under
the most stringent security, compliance, and operational
resilience requirements of any commercial sector. Digital
identity and PKI are mission-critical infrastructure for
banks — underpinning every secure transaction, every
authenticated login, every digitally signed document,
and every encrypted communication that the modern
financial system depends on.

From central banks operating national payment systems
to retail banks serving millions of customers to
investment banks executing trillions in daily transactions,
PKI provides the cryptographic trust foundation that
makes digital finance possible. A bank without robust
PKI is a bank that cannot securely authenticate its
customers, cannot sign financial transactions with
legal validity, cannot protect its internal systems
from unauthorized access, and cannot comply with
the growing wave of financial services regulation
that mandates strong authentication and digital signatures.

Nexus serves the full spectrum of financial services —
central banks building national payment infrastructure,
commercial banks deploying employee and customer PKI,
investment banks securing trading platforms, and
insurance companies managing agent and customer identity.
Our deep understanding of financial services regulatory
requirements, operational resilience mandates, and
the security standards that financial regulators demand
positions Nexus as a trusted partner for banks that
cannot afford PKI failure.

## Key Drivers and Challenges

### Drivers
- PSD2 Strong Customer Authentication (SCA) requirements
  mandating multi-factor authentication for all payment
  transactions across the European Union
- Open banking and API security requiring certificate-based
  authentication for third-party provider access to
  banking APIs
- Digital banking transformation — branch closures
  driving investment in secure digital channel identity
- Regulatory pressure on operational resilience —
  DORA in Europe mandating robust digital infrastructure
  including PKI
- Transaction fraud and identity theft driving adoption
  of PKI-based signing for high-value transactions
- Remote working post-pandemic requiring strong
  authentication for employees accessing core banking
  systems from home
- SWIFT network security requirements for member
  institutions mandating strong authentication
- Central bank digital currency (CBDC) initiatives
  requiring PKI infrastructure for digital currency
  identity

### Challenges
- Legacy core banking systems — decades-old platforms
  with limited PKI integration capability requiring
  middleware or API gateway approaches
- Regulatory fragmentation — different PKI and
  authentication requirements across jurisdictions
  for international banks operating globally
- High availability requirements — banking PKI must
  achieve 99.999% uptime as certificate outages
  directly impact transaction processing
- Audit and compliance burden — every certificate
  operation must be logged, every access justified,
  every change controlled through change management
- Third-party risk — open banking requires extending
  PKI trust to external TPPs while maintaining security
- Insider threat — privileged access to core banking
  systems requires strong authentication and least
  privilege enforcement
- Cryptographic agility — banks must be able to
  migrate algorithms as standards evolve without
  service disruption

## Regulatory and Compliance Requirements

### Payment Services
- PSD2 — Payment Services Directive 2 (EU) 2015/2366
  Strong Customer Authentication and open banking
  security requirements
- PCI DSS — Payment Card Industry Data Security
  Standard for cardholder data environment protection
- SWIFT CSCF — Customer Security Controls Framework
  for SWIFT network participants

### Financial Regulation
- DORA — Digital Operational Resilience Act (EU)
  ICT risk management and operational resilience
  for financial entities
- Basel III / IV — Capital adequacy and operational
  risk management including cyber risk
- EBA Guidelines on ICT and Security Risk Management
- FCA rules (UK) on operational resilience and
  cyber security
- MAS TRM Guidelines (Singapore) — Technology Risk
  Management for financial institutions
- HKMA cybersecurity guidelines for authorized
  institutions

### Electronic Signatures
- eIDAS Regulation — Qualified electronic signatures
  for legally binding financial document signing
- UNCITRAL Model Law on Electronic Signatures
- National electronic signature legislation in
  each jurisdiction

### Data Protection
- GDPR — Customer identity data protection
- National data protection legislation
- Banking secrecy laws limiting data sharing

## Typical PKI and IAM Requirements

### Employee PKI
- Smart card certificates for all staff accessing
  core banking and trading systems
- Strong authentication replacing passwords for
  network logon to banking systems
- Privileged access management — separate certificates
  and strict controls for system administrators
- Email signing and encryption for internal and
  external sensitive communications
- Document signing for internal approvals and
  contracts
- VPN certificate authentication for remote access
- Volume: Hundreds to tens of thousands of employees

### Customer Authentication
- PSD2-compliant strong customer authentication
  for payment initiation and account access
- Mobile banking authentication — PKI certificate
  in mobile SDK or FIDO2 passkey
- Corporate banking customer certificates for
  high-value transaction signing
- Internet banking two-factor using software
  certificate or hardware token
- Volume: Hundreds of thousands to millions of
  customers

### Infrastructure PKI
- TLS certificates for all customer-facing and
  internal systems
- API gateway certificates for open banking
  third-party provider authentication
- HSM integration for key ceremony and protection
- Database encryption certificates
- Code signing for banking application releases
- Automated renewal — certificate expiry in
  payment systems causes transaction failures

### Transaction Signing
- Qualified electronic signatures for loan
  agreements, contracts, and regulatory documents
- Dynamic transaction signing for PSD2 compliance
- Non-repudiation for high-value transactions
- Timestamp authority for signed document validity

## Nexus Solutions Commonly Deployed

### Core PKI
- **Nexus Certificate Manager** — Central bank and
  commercial bank CA platform. Manages employee
  PKI, customer certificates, and infrastructure
  TLS certificates from single platform.

- **Nexus OCSP** — Real-time certificate validation
  for banking transactions. Sub-100ms response
  time for payment processing. HSM-protected
  signing keys meeting banking security requirements.

- **Nexus CLM** — Automated TLS certificate lifecycle
  for banking infrastructure. Prevents certificate
  expiry incidents in payment systems and online
  banking platforms.

- **Nexus Protocol Gateway** — Multi-protocol
  certificate enrollment for diverse banking
  technology estate including legacy systems.

### Identity and Access Management
- **Nexus Smart ID Digital Access** — Employee
  authentication platform. PKI smartcard logon
  for banking systems. PSD2 strong customer
  authentication for retail customers. Privileged
  access for system administrators.

- **Nexus Smart ID Identity Manager** — Employee
  identity governance. Joiner-mover-leaver
  automation for large banking workforces.
  Access recertification for SOX and audit
  compliance. Contractor governance.

### Physical Credentials
- **Cosmo Smartcard** — Employee smart card OS
  for banking grade security. Corporate banking
  customer hardware token OS.

- **IDPlug Middleware** — Trader and banker workstation
  smartcard integration. Core banking system
  certificate authentication via CryptoAPI.

- **Smart Desktop Application** — Employee credential
  management. Self-service PIN management reducing
  helpdesk costs at scale.

### Mobile
- **Nexus Mobile Client** — Mobile banking employee
  authentication. Customer mobile strong authentication
  for retail banking.

- **Nexus Mobile SDK** — Embedded in mobile banking
  app for PSD2-compliant customer authentication
  and transaction signing.

## Common Use Cases

### 1. PSD2 Strong Customer Authentication
Retail bank deploys Nexus Mobile SDK within their
mobile banking app to deliver PSD2-compliant strong
customer authentication. Customers authenticate
with biometric-backed PKI certificate stored in
mobile secure element. Transaction signing with
dynamic linking displays transaction details
requiring biometric approval — satisfying PSD2
Article 97 requirements with cryptographic proof
of customer authorization.

### 2. Central Bank PKI Infrastructure
Central bank operates national PKI infrastructure
supporting the national payment system, government
securities settlement, and inter-bank communication.
Nexus NCM provides the CA platform with HSM-protected
root CA in offline vault. OCSP validates certificates
for all participants in real time. Certificate
profiles meet central bank security policy and
national cryptographic standards.

### 3. Investment Bank Trading Platform Security
Investment bank secures trading infrastructure with
PKI smartcard authentication for traders accessing
execution systems. All trade confirmations digitally
signed for regulatory audit trail. Nexus CLM manages
thousands of server certificates across trading
platform with automated renewal preventing trading
outages. Privileged access to core systems requires
smartcard plus PIN.

### 4. Open Banking API Security
Bank implements open banking API gateway requiring
certificate-based mutual TLS authentication for
all third-party providers accessing customer account
data. Nexus NCM issues eIDAS qualified certificates
to regulated TPPs. OCSP validates TPP certificate
status in real time for every API call. Automated
revocation when TPP authorization is withdrawn.

### 5. Corporate Banking Customer PKI
Bank issues PKI certificates to corporate banking
customers for high-value payment authorization and
account management. Corporate treasury teams use
hardware tokens with Cosmo Smartcard OS containing
signing certificates. Payments above threshold require
qualified electronic signature. Non-repudiation
provides legal certainty for large value transfers.

## Competitive Landscape

### Key Competitors
- **Entrust** — Strong in banking PKI with good
  financial services references particularly in
  North America. Full PKI platform with HSM
  integration. Less strong in European eIDAS
  qualified services.

- **DigiCert** — Cloud CA platform with enterprise
  PKI. Good for TLS and infrastructure certificates.
  Less suitable for on-premises banking PKI requiring
  data sovereignty and air-gapped root CA.

- **Thales (formerly Gemalto)** — Strong in HSM
  hardware and payment card production. PKI
  software less differentiated versus Nexus.
  Often leads with HSM and bundles PKI.

- **Keytos / AppViewX** — Certificate lifecycle
  management platforms focused on automation.
  Do not provide CA platform — depend on third-party CA.

- **EJBCA (PrimeKey/Keyfactor)** — Open-source CA
  with enterprise support. Lower cost entry point.
  Less professional services and banking-specific
  expertise versus Nexus.

### Nexus Positioning
- Banking-grade security — Common Criteria certified
  components, HSM integration with leading vendors,
  eIDAS qualified trust service capability
- European regulatory expertise — PSD2, DORA, eIDAS
  compliance built into product and delivery methodology
- Complete identity stack — from CA to customer mobile
  authentication in one platform, reducing integration
  complexity
- Operational resilience — active-active HA, no
  single point of failure, proven 99.999% availability
- Qualified electronic signatures — Nexus delivers
  eIDAS-compliant qualified signing for financial
  documents with full legal validity

## Key Buying Personas

### C-Suite and Senior Leadership
- **CISO** — Primary security owner. Evaluates
  threat coverage, certification compliance, vendor
  security posture. Will review Common Criteria
  certificates and penetration test results.

- **CTO / CIO** — Technology strategy and architecture.
  Integration with core banking platforms, cloud
  strategy alignment, vendor roadmap.

- **Chief Risk Officer** — Operational resilience,
  cyber risk quantification, regulatory compliance
  risk.

### Technical Decision Makers
- **Head of Cybersecurity Architecture** — PKI
  design authority. Reviews CA hierarchy, HSM
  integration, certificate profiles, protocol support.

- **Head of Identity and Access Management** —
  Owns IAM strategy. Authentication methods,
  privileged access management, customer identity.

- **Head of Payments Technology** — PSD2 compliance,
  payment API security, transaction authentication
  architecture.

### Compliance and Risk
- **Head of Compliance** — Regulatory requirements,
  audit readiness, evidence of control effectiveness.

- **Internal Audit** — Control testing, evidence
  collection, audit trail completeness.

## Win Themes for Banking

### 1. PSD2 Compliance Delivered
"Nexus delivers PSD2-compliant strong customer
authentication with dynamic linking, qualified
electronic signatures, and the complete audit
trail that regulators require. We have delivered
PSD2 compliance for banks across Europe."

### 2. Zero Tolerance for Downtime
"Banking PKI must be available 99.999% of the time.
An OCSP outage stops transactions. A certificate
expiry takes down online banking. Nexus delivers
active-active high availability with automated
certificate lifecycle — PKI that banking operations
can depend on."

### 3. Regulatory Expertise Built In
"We understand PSD2, DORA, eIDAS, PCI DSS, and
MAS TRM. Our products are designed to meet these
requirements, not adapted after the fact. Our
implementation teams have delivered compliant
banking PKI programs across multiple jurisdictions."

### 4. Qualified Signatures for Legal Certainty
"Nexus delivers eIDAS qualified electronic signatures
with the legal certainty that high-value financial
transactions require. Loan agreements, corporate
banking mandates, and regulatory submissions signed
with Nexus qualified certificates carry the same
legal weight as handwritten signatures."

### 5. Complete Identity Platform
"From employee PKI smartcard to customer mobile
authentication to infrastructure TLS management —
Nexus delivers the complete identity security
platform for banking. One vendor, one support
relationship, one integration framework for
your entire identity and PKI estate."