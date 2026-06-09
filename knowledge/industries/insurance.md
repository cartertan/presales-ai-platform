# Insurance — Industry Knowledge

## Sector Overview
The insurance industry manages risk, trust, and financial
commitments that span decades — life policies lasting
30 years, property coverage renewed annually, health
insurance covering millions of beneficiaries, and
commercial policies protecting business assets worth
billions. At the core of every insurance transaction
is identity — confirming who the policyholder is,
authenticating the agent issuing the policy, verifying
the adjuster processing the claim, and ensuring that
every document in the insurance lifecycle carries
legal validity and cannot be repudiated.

Digital transformation has fundamentally changed the
insurance industry. Direct-to-consumer digital channels
replace agent networks for simpler products. Telematics
devices monitor driving behavior for motor insurance.
Wearables collect health data for life and health
underwriting. IoT sensors monitor property for home
insurance. Automated claims processing uses digital
evidence. Every one of these digital touchpoints creates
identity and authentication requirements — device
identity for IoT sensors, customer identity for digital
channels, agent authentication for distribution systems,
and document signing for the legal instruments that
insurance represents.

Nexus serves insurance organizations across life,
general, health, and reinsurance sectors — providing
the PKI and identity infrastructure that secures
digital insurance operations, enables compliant
electronic signatures on insurance contracts, and
protects the sensitive personal and financial data
that insurers hold on their policyholders.

## Key Drivers and Challenges

### Drivers
- Digital distribution transformation — online and
  mobile insurance purchase requiring strong customer
  identity verification and authentication
- eIDAS and national electronic signature requirements
  for legally valid insurance contract execution
  without wet ink signatures
- Remote workforce — insurance agents, underwriters,
  and claims handlers working remotely requiring
  strong authentication to core insurance systems
- Insurance fraud — identity fraud in applications
  and claims driving investment in strong digital
  identity verification
- Regulatory compliance — Solvency II, GDPR, and
  national insurance regulatory requirements for
  data protection and operational resilience
- InsurTech competition — digital-native insurers
  using modern identity infrastructure creating
  pressure on incumbents to modernize
- IoT insurance products — telematics, smart home,
  wearables requiring device identity certificates
  for data integrity assurance
- Open insurance initiatives — APIs connecting
  insurers with distribution partners requiring
  certificate-based authentication

### Challenges
- Legacy policy administration systems — core
  insurance platforms with limited modern identity
  integration capability
- Agent network complexity — large independent
  agent networks with thousands of individuals
  requiring consistent identity management
- Cross-border operations — international insurers
  managing identity across multiple regulatory
  jurisdictions with different electronic signature
  requirements
- Customer friction — strong authentication must
  not create friction that drives customers to
  competitors with simpler but less secure login
- Document management complexity — insurance policy
  documents, endorsements, claims, and correspondence
  all potentially requiring digital signatures
- Outsourcing and third-party risk — TPAs, loss
  adjusters, and outsourced service providers
  requiring controlled access to insurer systems
- Long document retention — insurance documents
  must remain legally valid for 30+ years requiring
  long-term signature validation infrastructure

## Regulatory and Compliance Requirements

### Electronic Signatures
- eIDAS Regulation (EU) 910/2014 — Electronic
  identification and trust services defining
  validity of electronic signatures for insurance
  contracts
- eIDAS 2.0 — European Digital Identity Wallet
  impacting customer identity verification
- UNCITRAL Model Law on Electronic Commerce —
  international reference for electronic contract
  validity
- National insurance legislation defining
  requirements for electronic policy documents
  and signatures in each jurisdiction

### Insurance Specific Regulation
- Solvency II (EU) — Operational risk and IT
  security requirements for insurance undertakings
- EIOPA guidelines on information and communication
  technology security and governance
- Insurance Distribution Directive (IDD) — Requirements
  for agent identity and authorization
- GDPR — Policyholder data protection including
  identity and authentication data

### Data Protection
- GDPR Article 9 — Special categories of data
  protection for health insurance data
- National data protection requirements for
  insurance customer data
- Cross-border data transfer restrictions relevant
  to international insurance groups

### Financial Services
- PCI DSS — Premium payment processing security
- SWIFT requirements where applicable for
  large commercial insurance payments
- National financial regulatory requirements
  for insurance company IT security

## Typical PKI and IAM Requirements

### Employee and Agent PKI
- Employee smart card authentication for corporate
  system access replacing passwords
- Agent authentication for distribution portals —
  certificate-based strong authentication for
  independent agents accessing insurer systems
- Underwriter signing certificates for policy
  authorization above threshold
- Claims handler authentication for claims
  management systems
- Privileged access certificates for IT
  administrators with access to policyholder data
- Volume: Thousands to tens of thousands of
  employees, thousands to hundreds of thousands
  of agents

### Customer Identity
- Customer authentication for self-service portals —
  certificate-based or FIDO2 replacing password
- Mobile app strong authentication for policyholders
- Identity verification for new customer onboarding
- Step-up authentication for sensitive operations —
  policy changes, beneficiary updates, large claims
- Volume: Hundreds of thousands to millions
  of policyholders

### Document Signing
- Policy document signing — legally binding
  electronic signature on insurance contracts
- Endorsement and amendment signing
- Claims settlement agreement signing
- Large commercial policy signing with qualified
  electronic signatures
- Regulatory submission document signing
- Long-term signature validation — signatures
  must remain verifiable for policy lifetime

### Infrastructure PKI
- TLS certificates for customer-facing portals,
  agent portals, and APIs
- Automated certificate lifecycle for insurance
  IT infrastructure
- API gateway certificates for open insurance
  and broker integration

## Nexus Solutions Commonly Deployed

### Core PKI
- **Nexus Certificate Manager** — Insurance company
  CA platform. Employee and agent certificate
  issuance. Document signing certificate management.
  Integration with insurance core systems.

- **Nexus OCSP** — Real-time certificate validation
  for agent portal access and document signing
  verification. Long-term validation support
  for historical document verification.

- **Nexus CLM** — Automated TLS and infrastructure
  certificate lifecycle. Prevents certificate
  expiry causing portal outages that impact
  customer service.

### Identity and Access Management
- **Nexus Smart ID Digital Access** — Employee
  and agent authentication platform. Strong
  authentication for insurance system access.
  Customer portal authentication with step-up
  for sensitive operations.

- **Nexus Smart ID Identity Manager** — Employee
  and agent lifecycle management. Large
  independent agent network governance.
  Access recertification for Solvency II
  and GDPR compliance. Third-party access
  lifecycle for TPAs and loss adjusters.

### Mobile
- **Nexus Mobile Client** — Field adjuster and
  agent mobile authentication. Customer mobile
  strong authentication for insurance app.

- **Nexus Mobile SDK** — Embedded in insurance
  customer app for policyholder authentication
  and claim submission signing.

### Physical Credentials
- **Cosmo Smartcard** — Employee smart card OS
  for high-security insurance environments.

- **IDPlug Middleware** — Underwriter and agent
  workstation smartcard integration for
  document signing workflows.

## Common Use Cases

### 1. Agent Network Strong Authentication
Life insurance company manages network of 50,000
independent agents accessing policy administration
and sales portals. Nexus Smart ID Digital Access
provides certificate-based strong authentication
replacing passwords. Nexus Smart ID Identity
Manager automates agent onboarding when licensed
by regulator, manages role changes across agent
career lifecycle, and immediately revokes access
when license is suspended or agent relationship
ends. Agents authenticate via mobile credential
or hardware token depending on their operating
model. Full audit trail for regulatory inspection
of agent activity.

### 2. Digital Policy Execution with eSignature
General insurer deploys digital policy lifecycle
eliminating paper documents for commercial
property insurance. Policy schedule, terms and
conditions, and endorsements signed with
qualified electronic signatures by underwriting
authority and countersigned by client using
eIDAS qualified certificate. Nexus NCM provides
qualified certificate issuance. Long-term
signature validation ensures documents remain
legally provable for 30-year policy lifetime.
Signature validation service integrated with
document management system.

### 3. Claims Handler Authentication and Signing
Large general insurer secures claims management
system with strong authentication for all
claims handlers. Nexus Smart ID Digital Access
enforces smart card logon replacing easily shared
passwords — preventing internal claims fraud.
Settlement agreements above threshold require
qualified electronic signature from claims
authority. Mobile credential for field loss
adjusters accessing claims system from
insured premises.

### 4. Customer Portal and Mobile App Security
Health insurer deploys strong authentication for
member portal and mobile app. Nexus Mobile SDK
embedded in insurer app provides PKI-based
customer authentication with biometric. Step-up
authentication required for policy changes and
benefit queries above threshold. New customer
digital onboarding with identity verification
and certificate issuance to mobile device
during enrollment. Claim submission on mobile
includes customer signature for authorization.

### 5. Broker and TPA Access Management
Commercial insurer manages access for 200 broker
firms and 15 third-party administrators accessing
underwriting and claims systems. Nexus Smart ID
Identity Manager automates broker onboarding
with sponsor approval from relationship manager.
Certificate-based authentication for all broker
portal access. Time-limited access for specific
underwriting facilities. Automatic access expiry
when broker panel appointment ends. Quarterly
access recertification for Solvency II compliance
evidence.

## Competitive Landscape

### Key Competitors
- **Okta / Auth0** — Cloud identity platform with
  insurance customers. Strong customer identity
  and workforce SSO. Limited PKI depth and
  document signing capability. No on-premises
  deployment for regulated data sovereignty requirements.

- **Microsoft Azure AD / Entra ID** — Widely used
  in insurance for employee identity. Limited
  qualified electronic signature and OT PKI
  capability. Nexus complements Microsoft for
  PKI-specific requirements.

- **Entrust** — PKI platform with financial services
  and insurance references. US-centric. Less
  European eIDAS expertise versus Nexus.

- **ForgeRock / Ping Identity** — Identity and
  access management platforms. Strong in CIAM
  for customer identity. Limited PKI CA platform
  and document signing capability.

### Nexus Positioning
- Insurance-specific document signing — understanding
  of policy document lifecycle, long-term signature
  validation, and regulatory requirements for
  electronic insurance contracts
- Agent network scale — experience managing large
  independent agent populations with complex
  lifecycle requirements
- eIDAS qualified signatures — legally valid electronic
  signatures for insurance contracts meeting
  European regulatory requirements
- Complete platform — from employee PKI to customer
  mobile authentication to document signing
  from one specialist vendor

## Key Buying Personas

### Business and Compliance
- **Chief Digital Officer** — Digital transformation
  strategy. Customer experience, digital distribution,
  agent portal modernization.

- **Chief Compliance Officer** — Solvency II, GDPR,
  IDD compliance. Electronic signature legal validity.
  Regulatory audit evidence.

- **Head of Distribution** — Agent network management.
  Agent portal security. Distribution system access
  control.

### Technology and Security
- **CISO** — Security architecture. Authentication
  standards. Third-party risk. Data protection.

- **Head of IAM** — Identity governance. Employee
  and agent lifecycle. Customer identity.

- **Enterprise Architect** — Integration with core
  insurance platforms. API security. Cloud strategy.

### Operations
- **Head of Claims** — Claims system authentication.
  Settlement document signing. Fraud prevention
  through strong identity.

- **Head of Underwriting** — Policy authorization
  signing. Underwriting system access. Delegated
  authority management.

## Win Themes for Insurance

### 1. Legally Valid Digital Insurance Documents
"Nexus delivers eIDAS qualified electronic signatures
that give insurance contracts, policy schedules,
and claims settlements the same legal standing as
wet ink signatures — enabling fully digital insurance
processes with complete legal certainty."

### 2. Agent Network at Scale
"Managing 50,000 independent agents requires robust
identity governance. Nexus Smart ID Identity Manager
automates agent onboarding, manages access across
their career lifecycle, and ensures immediate revocation
when the relationship ends — without manual overhead
or compliance gaps."

### 3. Fraud Prevention Through Strong Identity
"Insurance fraud costs the industry billions annually.
Nexus replaces shareable passwords with cryptographic
identity — PKI certificates that cannot be phished,
shared, or stolen. Every claims handler, every
underwriter, every agent is who they say they are."

### 4. Customer Experience Without Compromise
"Strong authentication does not have to mean customer
friction. Nexus Mobile SDK delivers biometric-backed
PKI authentication within your insurance app —
customers authenticate with a fingerprint, you get
cryptographic-grade identity assurance."

### 5. Long-Term Document Validity
"An insurance policy signed today must remain legally
verifiable in 30 years. Nexus delivers long-term
signature validation infrastructure ensuring that
every digitally signed insurance document remains
provably authentic throughout its legal lifetime."