# Energy and Utilities — Industry Knowledge

## Sector Overview
The energy and utilities sector encompasses electricity
generation, transmission, and distribution, natural gas
networks, water utilities, and the increasingly digital
operational technology that controls these critical
infrastructure systems. It is one of the most strategically
sensitive industries in the world — a cyber attack on
energy infrastructure can cause widespread societal
disruption, economic damage, and in extreme cases,
physical harm to populations who depend on electricity,
gas, and water for survival.

PKI and digital identity have become foundational security
controls in the energy sector as operational technology
converges with information technology and as critical
infrastructure operators face escalating nation-state
and criminal cyber threats. Smart meters communicate
using PKI certificates. Substation automation systems
authenticate using digital certificates. Grid management
systems require strong operator authentication. SCADA
networks protect their communications with PKI-based
encryption and authentication. The energy sector is
transforming from an industry that barely used PKI to
one that depends on it at massive scale.

Nexus brings specialized expertise in energy sector PKI —
understanding the unique constraints of operational
technology environments, the IEC 62351 security standard
for power systems, smart metering PKI at utility scale,
and the regulatory frameworks that energy operators
must navigate. Our experience in smart grid deployments
across Europe and Asia positions us as a credible
partner for utilities undertaking digital transformation.

## Key Drivers and Challenges

### Drivers
- Smart meter rollout requiring PKI certificates for
  every meter — hundreds of millions globally in
  deployment programs spanning 10-15 years
- IEC 62351 adoption mandating digital certificates
  for power system communication security
- Grid modernization — smart grid infrastructure
  requiring device identity and secure communication
- Nation-state cyber threats targeting energy
  infrastructure driving investment in strong
  authentication and device identity
- Renewable energy integration — distributed energy
  resources including solar inverters and wind
  turbines requiring device identity for grid integration
- Electric vehicle infrastructure — charging stations
  requiring PKI certificates for grid communication
  and payment authentication
- Energy market deregulation — multiple parties
  accessing grid data requiring PKI-based access control
- EU Network and Information Security (NIS2) Directive
  designating energy as essential service with mandatory
  security requirements

### Challenges
- OT/IT convergence — operational technology systems
  were never designed for PKI integration, creating
  significant integration complexity
- Legacy infrastructure — substations and control
  systems with 20-30 year lifetimes cannot easily
  be updated for certificate management
- Constrained devices — smart meters and IED
  protection relays have limited processing power
  and memory for PKI operations
- Remote and inaccessible locations — substations
  and field devices in remote locations make
  manual certificate management impossible
- Safety-critical systems — certificate management
  operations on live grid systems carry operational
  risk if not carefully managed
- Long lifecycle mismatch — energy infrastructure
  has 20-30 year lifetimes while PKI certificates
  have 1-10 year validity, requiring multiple
  certificate renewals over equipment lifetime
- Multi-vendor ecosystem — substation equipment
  from multiple vendors with different PKI interface
  standards

## Regulatory and Compliance Requirements

### International Standards
- IEC 62351 — Power Systems Management and
  Associated Information Exchange Data and
  Communications Security
  * Part 3: Communication network and system security
  * Part 4: Profiles including MMS
  * Part 5: Security for IEC 60870-5 and derivatives
  * Part 6: Security for IEC 61850 profiles
  * Part 8: Role-based access control for power systems
- IEC 61850 — Communication networks and systems
  in substations — security extensions
- IEC 61968/61970 — Common Information Model for
  energy management systems
- NERC CIP — North American Electric Reliability
  Corporation Critical Infrastructure Protection
  standards (widely referenced beyond North America)

### European Regulatory
- EU NIS2 Directive — Essential services security
  requirements for energy operators
- EU Network Codes — Grid connection codes including
  cybersecurity requirements for grid-connected assets
- ENTSO-E cybersecurity guidelines for European
  transmission system operators
- National energy regulator cybersecurity guidelines
  in each EU member state

### Smart Metering
- EU Mandate M/441 — Smart meter standardization
  including security requirements
- DLMS/COSEM security suite for smart meter
  communication security
- National smart meter technical specifications
  defining PKI certificate requirements
  (UK SMKI, Netherlands, Italy P2 standard)

## Typical PKI and IAM Requirements

### Smart Metering PKI
- Dedicated smart meter CA hierarchy separate from
  corporate IT PKI
- Mass certificate issuance — millions of meter
  certificates during rollout
- Meter device certificates: 10-15 year validity
  matching meter deployment lifetime
- Registration Authority (RA) for meter enrollment
  at scale through metering service provider
- Certificate management for handheld terminals
  used by meter engineers
- OCSP or CRL for meter certificate status
- Automated renewal for meters still in field
  after initial certificate expiry

### OT/SCADA PKI
- Certificates for substation automation systems —
  IEDs, RTUs, protection relays
- IEC 62351 compliant certificate profiles for
  power system devices
- Engineering workstation certificates for
  SCADA access
- Historian and data concentrator certificates
- Separation from corporate IT CA — OT PKI
  managed independently with dedicated HSM
- Long validity: 5-10 years for field devices
- Minimal footprint — constrained device support

### Corporate IT and Employee
- Employee PKI for network logon and email
- Strong authentication for SCADA access —
  no passwords for operational technology systems
- Privileged access management for grid operators
- Remote access certificates for field engineers
- VPN authentication for remote site access

### Volume
- Smart meters: 1M to 50M+ for national programs
- OT devices: Thousands to tens of thousands
  per large utility
- Employee certificates: Hundreds to thousands
- Annual renewal volume: 10-15% of meter population

## Nexus Solutions Commonly Deployed

### Smart Metering
- **Nexus Certificate Manager** — Mass certificate
  issuance for smart meter programs. Handles
  enrollment at utility scale with integration
  to meter management systems. Supports DLMS
  security suite certificate profiles.

- **Nexus Protocol Gateway** — SCEP and EST
  enrollment gateway for meter certificate
  requests from meter management systems.
  Handles bulk enrollment during rollout phase.

- **Nexus CLM** — Automated certificate lifecycle
  for meters still in field. Tracks 10+ million
  meter certificates, manages renewal campaigns
  for meters approaching expiry.

### OT Security
- **Nexus Certificate Manager** — Dedicated OT CA
  for substation and SCADA device certificates.
  IEC 62351 compliant certificate profiles.
  Physically separated from IT PKI with dedicated
  HSM.

- **Nexus OCSP** — Certificate status for OT
  device authentication. Deployed within OT
  network boundary with controlled IT/OT
  connectivity.

### Corporate IT
- **Nexus Smart ID Digital Access** — Grid operator
  strong authentication for SCADA access. No
  passwords on operational systems. Engineering
  team VPN certificate authentication.

- **Nexus Smart ID Identity Manager** — Utility
  workforce identity governance. Contractor
  access lifecycle for field engineering teams.

## Common Use Cases

### 1. National Smart Meter PKI Program
National utility or metering authority deploys
PKI infrastructure for smart meter rollout covering
millions of residential and commercial properties.
Nexus NCM provides the mass issuance CA platform.
Protocol Gateway handles bulk enrollment through
integration with meter management system. Each
meter receives a unique device certificate embedded
during manufacturing or enrolled at first installation.
Nexus CLM tracks all meter certificates and manages
renewal campaigns as meters approach certificate expiry.

### 2. Substation Automation Security (IEC 62351)
Electricity transmission operator deploys IEC 62351
security for substation automation — protecting
IEC 61850 communication between protection relays,
bay controllers, and substation HMI systems. Nexus
NCM provides OT-specific CA with IEC 62351 compliant
certificate profiles. Physically separate OT PKI
infrastructure with dedicated HSM prevents IT
compromise from affecting operational systems.

### 3. SCADA Operator Strong Authentication
Grid operator eliminates password-based access to
energy management system and SCADA. All grid
operators authenticate with PKI smartcard or mobile
credential. Privileged users — system administrators
and engineers — require additional factors for
access to critical control functions. Nexus Digital
Access enforces authentication policy across all
SCADA operator workstations.

### 4. Renewable Energy Asset Identity
Solar and wind farm operator deploys device identity
certificates for inverters, SCADA gateways, and
weather stations connecting to grid management
systems. Each device has a unique certificate
enabling mutual authentication and encrypted
communication. Nexus Protocol Gateway handles
SCEP enrollment for diverse device types across
multiple vendor platforms.

### 5. EV Charging Infrastructure PKI
Electric vehicle charging network operator deploys
PKI certificates to all charging stations for
communication security with central management
system, payment processing, and grid integration.
Nexus NCM manages charger certificate lifecycle
with automated renewal ensuring charging network
remains fully operational as initial certificates
approach expiry.

## Competitive Landscape

### Key Competitors
- **Siemens / Siemens Energy** — OT systems vendor
  with integrated security capabilities for own
  equipment. Limited to Siemens ecosystem. Nexus
  provides vendor-neutral PKI across all OT vendors.

- **ABB** — Substation automation and OT security
  solutions. Proprietary approach tied to ABB
  equipment. Nexus integrates across ABB, Siemens,
  GE, Schneider Electric.

- **Honeywell** — Industrial cybersecurity with
  PKI capabilities for process industry. Limited
  smart meter PKI expertise compared to Nexus.

- **Xage Security** — Zero trust security for OT
  environments. Newer entrant with identity focus
  but limited PKI depth.

- **General PKI vendors** — Entrust, DigiCert
  offering enterprise PKI. Limited OT-specific
  expertise, IEC 62351 knowledge, and smart meter
  PKI experience compared to Nexus.

### Nexus Positioning
- Smart meter PKI at national scale — proven in
  large utility deployments covering millions of
  meters with decade-long support commitment
- IEC 62351 expertise — deep knowledge of power
  system security standards that general PKI
  vendors cannot match
- OT-aware architecture — understanding of OT
  network constraints, air-gapped environments,
  and safety-critical system requirements
- Vendor-neutral — integrates across all major
  OT vendors: Siemens, ABB, GE, Schneider Electric
- Long-term partnership — energy infrastructure
  has 20-30 year lifetimes, Nexus commits to
  supporting deployments through the full lifecycle

## Key Buying Personas

### Operational Technology
- **Head of OT Security / OT CISO** — Owns
  operational technology security. Understands
  IEC 62351, NERC CIP, NIS2 for OT. Concerned
  about impact of security changes on operational
  stability.

- **Grid Automation Engineer** — Technical
  owner of substation automation systems.
  Evaluates IEC 61850 and IEC 62351 compatibility.
  Concerned about interoperability and operational
  risk.

- **Smart Metering Program Manager** — Owns meter
  rollout and operation. Cares about mass enrollment
  scale, integration with meter management system,
  long-term certificate lifecycle.

### Information Technology
- **CISO** — Overall security posture including
  both IT and OT. Evaluates NIS2 compliance,
  incident response capability, vendor security.

- **Enterprise Architect** — IT/OT convergence
  architecture. Integration between corporate IT
  PKI and OT PKI. Identity federation.

- **Head of IAM** — Employee and operator
  authentication. SCADA access control. Privileged
  access management.

## Win Themes for Energy

### 1. Smart Grid Scale Without Compromise
"Nexus has delivered PKI for smart meter programs
covering millions of devices. We understand the
mass enrollment challenges, the long certificate
lifetimes, and the renewal operations that utility
programs face over their 15-year deployment horizon."

### 2. OT-Aware PKI
"Nexus understands the difference between IT PKI
and OT PKI. We know IEC 62351. We know the
constraints of protection relays and RTUs. We know
why a 5-minute OCSP outage is unacceptable in a
substation. We design PKI for operational technology,
not around it."

### 3. Vendor-Neutral Integration
"Your substation runs Siemens. Your SCADA is GE.
Your meters are Landis+Gyr. Nexus integrates with
all of them via standard protocols — one PKI platform
for your entire operational estate regardless of
equipment vendor."

### 4. Long-Term Commitment
"Your smart meters will be in the field for 15 years.
Your substations for 30. Nexus commits to supporting
your PKI infrastructure for the full lifecycle —
software updates, algorithm migrations, post-quantum
readiness, and operational support for as long as
your infrastructure is in service."

### 5. NIS2 and Regulatory Compliance
"NIS2 designates energy as essential services with
mandatory security requirements. Nexus delivers
the PKI and identity controls that NIS2 compliance
requires — device authentication, operator strong
authentication, audit logging, and incident response
capability."