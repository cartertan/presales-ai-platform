# V2G and EV Charging — Industry Knowledge

## Sector Overview
Vehicle-to-Grid (V2G) and electric vehicle charging
infrastructure represents one of the fastest-growing
and most technically complex PKI deployment domains
emerging today. As the world transitions from internal
combustion engines to electric mobility, the charging
infrastructure connecting millions of EVs to electricity
grids requires a sophisticated PKI ecosystem to enable
secure, automated, and interoperable charging across
networks, borders, and operators.

The ISO 15118 standard — specifically the Plug and Charge
(PnC) feature — defines how electric vehicles automatically
authenticate to charging stations using PKI certificates,
enabling a seamless charging experience where the driver
simply plugs in and charging begins with no RFID card,
no app interaction, and no manual payment step. Behind
this simple user experience is a complex PKI hierarchy
spanning vehicle manufacturers, charging network operators,
eMobility service providers, and interoperability
platforms — all connected through a trusted certificate
ecosystem.

Nexus has deployed PKI infrastructure for V2G and
EV charging programs including a landmark deployment
with Hubject — one of the world's largest EV charging
interoperability platform operators and the operator
of the global V2G Root CA for Plug and Charge. This
reference positions Nexus as one of very few PKI vendors
with proven, production-deployed V2G PKI expertise at
global interoperability scale.

## The Hubject Reference — Global V2G Root CA
Hubject operates the global interoperability platform
connecting eMobility Service Providers (eMSPs) and
Charge Point Operators (CPOs) across Europe, North
America, and Asia. As the operator of the V2G Root CA
under the ISO 15118 PKI ecosystem, Hubject operates
the trust anchor that enables Plug and Charge across
the global EV charging network.

Nexus provided the PKI platform for Hubject's V2G
Root CA infrastructure — demonstrating:
- Production deployment at global interoperability scale
- ISO 15118 certificate profile expertise
- V2G PKI hierarchy design capability
- Integration with Hubject's OICP (Open Intercharge
  Protocol) and eMIP platform
- CA operations for a multi-stakeholder trust ecosystem
  where OEMs, eMSPs, and CPOs all participate

This reference is a significant differentiator — very
few PKI vendors have ISO 15118 V2G PKI in production
at global scale.

## V2G PKI Ecosystem Explained

### Certificate Hierarchy for Plug and Charge

V2G Root CA (operated by interoperability platform e.g. Hubject)
├── OEM Provisioning CA
│     └── Vehicle certificates (issued to each EV at manufacture)
│           Vehicle Sub-CA 1, Vehicle Sub-CA 2
├── CPO Sub-CA (Charge Point Operator)
│     └── EVSE certificates (issued to each charging station)
└── eMSP Sub-CA (eMobility Service Provider)
└── Contract certificates (issued to EV drivers)

### Certificate Types in V2G PKI

**V2G Root CA Certificate**
- The trust anchor for the entire ecosystem
- Operated by interoperability platform or national authority
- Embedded in vehicle ECUs at manufacture
- 40-year validity to outlast vehicle lifetimes

**OEM Provisioning Certificate**
- Issued to vehicle manufacturers (Tesla, VW, BMW, etc.)
- Used to provision contract certificates to vehicles OTA
- Links vehicle to driver contract automatically

**Vehicle Certificate (EVCC)**
- Unique certificate embedded in every EV
- Identifies the specific vehicle to the charging station
- Issued during vehicle manufacturing
- Validity: 15+ years matching vehicle lifetime

**EVSE Certificate (Charging Station)**
- Unique certificate in every charge point
- Identifies the charging station to the vehicle
- Enables TLS mutual authentication during charging session
- Issued to Charge Point Operator sub-CA

**Contract Certificate**
- Issued to the EV driver's contract with their eMSP
- Stored in vehicle after provisioning
- Presented to charging station for billing authorization
- Validity: Typically 6 months to 2 years

## Key Drivers and Challenges

### Drivers
- Rapid EV adoption — global EV fleet growing from
  millions to hundreds of millions by 2030 creating
  massive PKI certificate demand
- Government EV mandates — EU banning ICE vehicle
  sales by 2035, US and Asian equivalents creating
  certain long-term market growth
- Interoperability requirements — EV drivers need
  to charge anywhere, not just on their home network,
  requiring cross-operator PKI trust
- ISO 15118 adoption — OEMs including BMW, Mercedes,
  Volkswagen, Hyundai, Ford, GM, and others enabling
  Plug and Charge requiring V2G PKI infrastructure
- Charging network scale — CPOs deploying hundreds
  of thousands of charge points each requiring EVSE
  certificates managed at scale
- V2G grid services — bidirectional charging creating
  new PKI requirements for grid service authentication
  and energy transaction signing
- Public charging investment — EU Alternative Fuels
  Infrastructure Regulation (AFIR) mandating public
  charging deployment at massive scale
- Energy market participation — EVs participating
  in frequency regulation and energy trading requiring
  authenticated energy transaction records

### Challenges
- Multi-party ecosystem complexity — V2G PKI involves
  vehicle manufacturers, charging operators, eMobility
  service providers, grid operators, and interoperability
  platforms — coordinating certificate trust across
  all parties is a governance challenge
- Vehicle lifetime mismatch — vehicle certificates
  must remain valid for 15+ years while PKI algorithms
  evolve, requiring crypto-agility planning at design
- Mass deployment scale — hundreds of millions of
  vehicle certificates and millions of EVSE certificates
  requiring PKI platforms designed for IoT-grade scale
- OTA certificate provisioning — delivering contract
  certificates to vehicles over cellular network
  requires secure, reliable, and bandwidth-efficient
  certificate management protocols
- Cross-border interoperability — EV driving across
  national and operator boundaries requires PKI trust
  that spans jurisdictions and regulatory frameworks
- Charge point hardware diversity — thousands of
  different EVSE hardware models from dozens of
  manufacturers with varying PKI implementation quality
- Legacy charge point estate — installed base of
  OCPP 1.6 charge points without ISO 15118 capability
  requiring migration planning

## Regulatory and Compliance Requirements

### ISO Standards
- **ISO 15118-1** — Road vehicles — Vehicle to grid
  communication interface — General information and
  use-case definition
- **ISO 15118-2** — Road vehicles — Vehicle to grid
  communication interface — Network and application
  protocol requirements (AC charging, Plug and Charge)
- **ISO 15118-20** — Road vehicles — Vehicle to grid
  communication interface — Part 20 (bidirectional
  power transfer, V2G, V2H)
- **ISO 15118-8** — Physical layer and data link layer
  requirements for wireless communication

### Charging Protocol Standards
- **OCPP 2.0.1** — Open Charge Point Protocol —
  security profile for charge point to central
  system communication including TLS certificates
- **OCPP 1.6** — Widely deployed version with
  optional TLS security
- **OICP 2.3** — Open Intercharge Protocol by
  Hubject for cross-operator roaming
- **eMIP** — eMobility Interoperability Protocol
  for alternative roaming network

### Grid and Energy Standards
- **IEC 61851** — Electric vehicle conductive charging
  system standards
- **IEEE 2030.5** — Smart Energy Profile for grid
  communication including PKI requirements
- **OCPI** — Open Charge Point Interface for
  eMSP-CPO data exchange

### Regional Regulatory
- **EU AFIR** — Alternative Fuels Infrastructure
  Regulation mandating Plug and Charge capability
  at public fast charging by 2027
- **EU eIDAS** — Applicable to qualified electronic
  signatures on energy transaction records
- **US NIST EV Charging Cybersecurity Guidelines**
  — NIST guidelines for EV charging security
- **German BSI guidelines** — BSI technical guidelines
  for EV charging security in German market

## Typical PKI and IAM Requirements

### V2G Root CA Operations
- Offline HSM vault for Root CA key ceremony
- Root CA certificate embedded in all OEM vehicle ECUs
- 40-year root certificate validity
- Sub-CA issuance for OEMs, CPOs, and eMSPs
- Certificate profile compliance with ISO 15118
- Audit trail for CA/Browser Forum equivalent
  V2G PKI governance requirements
- Key ceremony documentation and third-party witness

### EVSE Certificate Management (CPO)
- Certificate issuance for every charge point
- OCPP 2.0.1 TLS certificate for backend communication
- ISO 15118 EVSE certificate for vehicle authentication
- Mass deployment — single CPO may deploy 10,000-100,000
  charge points
- Automated enrollment at charge point commissioning
- Certificate renewal without physical site visit —
  OTA renewal via charge point management system
- OCSP for real-time EVSE certificate validation

### Contract Certificate Management (eMSP)
- Contract certificate issuance to EV driver accounts
- OTA provisioning to vehicle over cellular
- Short validity: 6-24 months requiring automated renewal
- Revocation on contract cancellation
- Volume: Hundreds of thousands to millions per eMSP
- Integration with eMSP billing and CRM systems

### Vehicle Certificate Management (OEM)
- Manufacturing-time certificate embedding
- Provisioning sub-CA for OTA contract delivery
- 15+ year certificate validity for vehicle lifetime
- Fleet management for post-sale certificate operations

## Nexus Solutions for V2G

### Core V2G PKI Platform
- **Nexus Certificate Manager** — V2G CA platform
  for Root CA, OEM provisioning CA, CPO Sub-CA,
  and eMSP Sub-CA operations. ISO 15118 certificate
  profiles. Hubject interoperability platform
  integration. Mass issuance for EVSE and contract
  certificates. Proven in production at Hubject scale.

- **Nexus OCSP** — Certificate status for V2G
  ecosystem. Real-time EVSE and contract certificate
  validation during charging session establishment.
  High availability matching charge point availability
  requirements. Pre-signed response support for
  offline charge point scenarios.

- **Nexus CLM** — Automated certificate lifecycle
  for EVSE certificate estate. Discovers all charge
  point certificates across CPO estate. Tracks
  expiry. Automates renewal via OCPP 2.0.1 certificate
  management. Prevents certificate expiry causing
  charge point failures.

- **Nexus Protocol Gateway** — Certificate enrollment
  for charge points via SCEP, EST, and ACME.
  Handles diverse charge point hardware with
  different enrollment capabilities.

### Identity and Access Management
- **Nexus Smart ID Digital Access** — Charging
  network operations center authentication. CPO
  and eMSP portal access. Grid operator strong
  authentication for V2G grid service management.

- **Nexus Smart ID Identity Manager** — eMSP
  customer identity management. Contractor
  and field engineer lifecycle for charge point
  installation and maintenance teams.

## Common Use Cases

### 1. V2G Root CA Operations (Hubject Model)
Interoperability platform operator deploys Nexus
NCM as the V2G Root CA platform enabling Plug and
Charge across the global EV charging ecosystem.
Root CA key ceremony with HSM protection and
third-party audit. Sub-CA issuance to participating
OEMs, CPOs, and eMSPs. Certificate policy enforcement
ensuring all participants meet ISO 15118 profile
requirements. Nexus OCSP provides real-time certificate
status for the global ecosystem. This is the proven
Hubject deployment model.

### 2. Charge Point Operator EVSE Certificate Management
CPO operating 50,000 fast charging stations across
Europe deploys Nexus for EVSE certificate management.
New charge points automatically enrolled at
commissioning via EST protocol integration with
charge point management system. Nexus CLM tracks
all 50,000 EVSE certificates, monitors expiry,
and triggers automated OTA renewal via OCPP 2.0.1
certificate management messages. Zero manual
intervention for certificate operations across
the entire charge point estate.

### 3. eMobility Service Provider Contract Certificates
eMSP with 500,000 EV driver subscribers deploys
Nexus for contract certificate lifecycle management.
New subscriber receives contract certificate
provisioned OTA to their vehicle. Automated renewal
before expiry maintains seamless Plug and Charge
experience. Immediate revocation on subscription
cancellation. Integration with eMSP billing platform
links certificate lifecycle to commercial subscription
status. Multi-OEM vehicle support across Tesla,
BMW, Mercedes, VW, Hyundai, and other ISO 15118
enabled vehicles.

### 4. National V2G PKI Infrastructure
National government or energy authority establishes
national V2G PKI to ensure domestic EV charging
interoperability and energy data integrity. Nexus
NCM operates the national V2G CA hierarchy trusted
by all charge points and EVs registered in the
country. Integration with national energy management
system for authenticated V2G grid service transactions.
Interoperability with international V2G Root CAs
via cross-certification.

### 5. Automotive OEM Vehicle Certificate Program
Vehicle manufacturer embedding ISO 15118 Plug and
Charge in new model range deploys Nexus for vehicle
certificate operations. Manufacturing-time certificate
embedding into vehicle ECU. OEM provisioning CA
for OTA contract certificate delivery to customers.
Fleet management for post-sale certificate operations
across millions of vehicles over their 15+ year
operational lifetime. Integration with OEM connected
vehicle platform for certificate lifecycle events.

## Competitive Landscape

### Key Competitors
- **Volkswagen ELLI / CharIN** — Industry consortium
  developing V2G PKI standards. Not a commercial
  PKI vendor but influences standards. Nexus
  aligns with CharIN certificate management
  working group outputs.

- **PKI vendors without V2G experience** — Most
  PKI vendors claim V2G capability based on
  general PKI knowledge but lack ISO 15118
  specific expertise and production references.
  Nexus differentiates with the Hubject reference.

- **Sectigo / DigiCert** — Commercial CAs offering
  IoT certificate management that can be adapted
  for V2G. Limited ISO 15118 specific expertise.
  Cloud-based approaches may not meet some
  operator data sovereignty requirements.

- **Keyfactor / EJBCA** — Open-source CA platform
  used by some V2G deployments. Lower initial
  cost but requires more internal PKI expertise
  to operate. Nexus offers more complete managed
  service capability.

### Nexus V2G Positioning
- **Only vendor with Hubject V2G Root CA reference** —
  This is the most significant V2G PKI reference
  globally. No other PKI vendor can claim the
  same credential.
- ISO 15118 certificate profile expertise from
  production deployment — not theoretical knowledge
- Multi-stakeholder ecosystem experience — designed
  for the OEM/CPO/eMSP/interoperability complexity
  of V2G PKI
- Scale — proven at global interoperability scale
  with Hubject handling certificates for multiple
  OEMs, hundreds of CPOs, and millions of vehicles
- Long-term commitment — V2G infrastructure will
  operate for 20-30 years, Nexus provides lifecycle
  commitment matching this horizon

## Key Buying Personas

### Interoperability Platforms
- **CTO / Head of Platform** — V2G PKI architecture.
  Interoperability protocol compliance. OEM and
  CPO onboarding capability.

- **Head of Trust Services** — CA operations,
  audit compliance, ecosystem governance.

### Charge Point Operators
- **Head of Network Operations** — Charge point
  availability. Certificate expiry prevention.
  OCPP 2.0.1 security profile deployment.

- **Head of Technology / CTO** — ISO 15118
  implementation. PKI integration with charge
  point management system. Scale.

### eMobility Service Providers
- **Head of Product** — Customer experience.
  Plug and Charge feature delivery. Contract
  certificate lifecycle.

- **Head of Technology** — OTA provisioning
  integration. Multi-OEM vehicle compatibility.
  Billing system integration.

### Automotive OEMs
- **Head of Connected Vehicle / Head of EV Platform**
  — Vehicle certificate program. Manufacturing
  integration. Customer fleet operations.

### Energy and Grid
- **Head of Grid Digitalization** — V2G grid
  services authentication. Energy transaction
  signing. Grid security.

## Win Themes for V2G and EV Charging

### 1. The Hubject Reference — Proven in Production
"Nexus provided the PKI platform for Hubject's
V2G Root CA — the trust anchor for Plug and Charge
interoperability across Europe and beyond. We do
not claim V2G capability — we have delivered it
at the highest level of the global V2G PKI ecosystem."

### 2. ISO 15118 Expertise From Real Deployment
"ISO 15118 V2G PKI is complex — certificate profiles,
multi-party trust hierarchies, OTA provisioning,
and EVSE lifecycle management all have ISO 15118
specific requirements. Nexus has implemented these
in production, not in a lab."

### 3. EV Scale Certificate Management
"Millions of vehicles. Hundreds of thousands of
charge points. Short-lived contract certificates
requiring constant renewal. Nexus manages V2G
certificate lifecycles at the scale the EV
transition demands — fully automated, zero
manual intervention."

### 4. Multi-Stakeholder Ecosystem Design
"V2G PKI is not a single organization problem —
it involves OEMs, CPOs, eMSPs, and interoperability
platforms operating under shared trust. Nexus
designed and deployed the PKI governance model
for exactly this multi-stakeholder complexity
at Hubject."

### 5. Future-Proof for ISO 15118-20 and V2G
"ISO 15118-20 extends Plug and Charge to bidirectional
V2G energy services. Nexus platform evolution follows
the ISO 15118 roadmap — your V2G PKI investment
grows with the standard, from unidirectional charging
today to full V2G grid service participation tomorrow."
