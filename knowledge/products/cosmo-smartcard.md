# Cosmo Smartcard
**Category:** Hardware | **Code:** COSMO

## Product Overview
Cosmo Smartcard is an enterprise-grade smartcard operating system
that provides the secure hardware foundation for physical identity
credentials. It runs on a tamper-resistant smartcard chip and
delivers the cryptographic capabilities, secure key storage, and
applet execution environment that government eID cards, employee
access cards, health cards, and payment credentials depend on.

The Cosmo operating system is designed for deployment at national
scale — powering citizen identity cards, government employee
credentials, healthcare professional cards, and transport passes
that must remain secure, reliable, and functional for years in
the field. It supports Java Card applets enabling multiple
applications to coexist securely on a single card — combining
identity, access, PKI, and payment on one physical credential.

Cosmo Smartcard is the hardware trust anchor in the Nexus identity
platform. While Nexus Certificate Manager manages the certificate
lifecycle and Smart ID Digital Access manages authentication,
Cosmo is the physical secure element where private keys are
generated, stored, and used — never exposed, never extractable,
protected by hardware tamper resistance certified to the highest
international security standards.

## Key Features
- Java Card compliant smartcard operating system
- Multiple application support on single card
- Hardware-protected private key generation and storage
- PKI certificate storage and cryptographic operations
- Tamper-resistant secure element with attack detection
- PIN and biometric protection for credential access
- Contact and contactless interface support (ISO 7816, ISO 14443)
- Extended access control for ePassport and eID compliance
- Secure messaging for protected communication
- Card lifecycle management support
- FIPS 140-2 and Common Criteria certified
- High durability for 10+ year card lifetime
- Personalization API for card production integration
- Support for multiple PKI certificates per card

## Technical Specifications
**Card Interface Standards:**
- ISO 7816 — Contact smartcard interface
- ISO 14443 — Contactless smartcard interface (NFC)
- ISO 18013 — Mobile driving license standard
- ICAO 9303 — ePassport and eMRTD standard
- PC/SC — Personal Computer Smart Card standard

**Cryptographic Capabilities:**
- RSA 2048, 3072, 4096 bit key generation and operations
- ECC P-256, P-384, P-521 key generation and operations
- AES 128, 192, 256 bit symmetric encryption
- SHA-256, SHA-384, SHA-512 hashing algorithms
- ECDH key agreement for secure messaging
- Hardware random number generator (TRNG)
- Post-quantum algorithm readiness roadmap

**Applet Support:**
- PKI applet for certificate storage and signing
- Physical access control applet (PACS)
- OATH OTP applet for one-time passwords
- Payment applet (EMV compliant)
- Biometric data storage applet
- Custom applets via Java Card API

**Certifications:**
- Common Criteria EAL5+ or EAL6+
- FIPS 140-2 Level 3
- EMVCo for payment applications
- ICAO compliant for travel document applications
- BSI, ANSSI, DKSC national certifications

## Key Use Cases
1. **National eID Card** — Citizen identity card combining
   visual identity, machine-readable zone, contactless
   ePassport chip, PKI certificates for authentication
   and signing, and optionally biometric data — all
   secured on Cosmo Smartcard OS meeting ICAO and
   eIDAS requirements for national identity documents.

2. **Government Employee Smart Card** — Combined physical
   access card and PKI credential for government staff —
   one card opens office doors and provides logical
   access to government networks, email signing, and
   classified systems with certificate-based strong
   authentication.

3. **Healthcare Professional Card** — Identity credential
   for doctors, nurses, and healthcare workers that
   provides physical access to healthcare facilities,
   logical access to patient record systems, and
   qualified electronic signatures for prescriptions
   and medical documents.

4. **Transport and Multipurpose Cards** — National or
   city-level multipurpose card combining transit pass,
   identity credential, loyalty program, and payment
   on a single Cosmo-powered card — reducing wallet
   clutter and card production costs for issuers.

5. **Military and High Security Credentials** — Defense
   and intelligence agency credentials requiring
   Common Criteria EAL6+ certification, hardware
   tamper resistance, and classified applets for
   access to highly sensitive systems and facilities.

## Industry Applications
- **eGovernment:** National eID cards, government employee
  credentials, civil servant smart cards, border control
  documents
- **Citizen ID:** National identity card OS, biometric
  passport chip, residence permit card, voter ID card
- **Banking and Finance:** Bank employee credentials,
  secure token for transaction authorization, corporate
  banking smart card
- **Healthcare:** Healthcare professional card, patient
  identity card, prescription signing credential
- **Telco:** SIM-based identity for mobile PKI,
  embedded secure element for connected devices
- **Manufacturing:** High-security employee access cards
  for sensitive production facilities

## Competitive Differentiators
- Multi-application architecture allows government to
  consolidate multiple cards into one — reducing issuance
  cost and citizen credential complexity
- Proven in national eID programs serving millions of
  citizens with 10-year card lifetimes in diverse
  climatic and usage conditions
- Highest security certifications — Common Criteria
  EAL5+ and EAL6+ for the most demanding government
  and defense requirements
- Native integration with Nexus Smart ID platform
  creates end-to-end credential lifecycle from
  identity registry to physical card personalization
- Flexible applet model allows new applications to be
  added post-issuance where card supports over-the-air
  update capability
- Full eIDAS compliance for European qualified
  electronic signature credential deployments

## Integration Capabilities
- **Nexus Smart ID Identity Manager** — Identity lifecycle
  events trigger card personalization and issuance workflows
- **Nexus Certificate Manager** — PKI certificates loaded
  onto card during personalization and renewed over card
  lifecycle
- **Nexus Smart ID Digital Access** — Card used as
  authentication credential for physical and logical access
- **IDPlug Middleware** — Desktop middleware enabling
  Windows and macOS to use Cosmo smartcard for logon,
  email signing, and document signing
- **Card personalization bureaus** — Standard personalization
  API for integration with card production systems
- **Physical access control systems** — PACS applet
  integration with HID, Lenel, Genetec, CCURE systems
- **EMV payment networks** — Payment applet for combined
  ID and payment card deployments

## Compliance and Standards
- ISO 7816 — Smartcard contact interface standard
- ISO 14443 — Contactless proximity card standard
- ICAO 9303 — Machine Readable Travel Documents
- ISO 18013 — Mobile driving license
- Java Card specification — Oracle Java Card platform
- GlobalPlatform — Secure element management standard
- Common Criteria EAL5+ / EAL6+ — Security evaluation
- FIPS 140-2 Level 3 — Cryptographic module standard
- EMVCo — Payment card security standard
- eIDAS Regulation — Qualified signature creation device
  requirements for electronic signatures
- BSI TR-03110 — German eID card technical guideline
- ANSSI — French national cybersecurity certification

## Customer Reference Profile
- National eID program — European government
  Products: Cosmo Smartcard + NCM + Smart ID Identity
  Manager + Digital Access
  Scale: 8M citizen eID cards issued
  Lifetime: 10-year card validity
  Applications: ePassport, PKI auth, qualified signature
  Outcome: Single national credential replacing
  4 separate documents

- Government ministry employee credential
  Products: Cosmo Smartcard + NCM + Digital Access
  + IDPlug Middleware
  Scale: 120,000 employee smart cards
  Applications: Physical access, network logon,
  email signing, document signing
  Outcome: Unified credential replacing separate
  access card and soft token

- National healthcare professional card
  Products: Cosmo Smartcard + NCM + Smart ID
  Scale: 200,000 healthcare worker cards
  Applications: Facility access, patient record
  access, prescription signing
  Outcome: Paperless prescription signing adopted
  across national health service