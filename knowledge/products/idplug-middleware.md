# IDPlug Middleware
**Category:** Middleware | **Code:** IDPLUG

## Product Overview
IDPlug Middleware is a smartcard middleware platform that enables
Windows, macOS, and Linux operating systems to communicate with
smartcards and hardware tokens for authentication, digital signing,
and encryption operations. It acts as the software bridge between
the physical smartcard — including Cosmo Smartcard and other
compatible cards — and the applications, operating systems, and
security infrastructure that need to use the credentials stored
on that card.

Without middleware, a smartcard inserted into a card reader is
invisible to the operating system and applications. IDPlug solves
this by providing the PKCS#11, PC/SC, and minidriver interfaces
that Windows logon, browsers, email clients, document signing
applications, and VPN clients need to interact with smartcard
certificates and perform cryptographic operations using the
private keys stored securely on the card.

IDPlug is designed for large-scale enterprise and government
deployments where tens of thousands of employees use smartcards
daily for network logon, email signing, document signing, and
VPN access. It provides centralized management, silent deployment
via group policy, and consistent cross-platform behavior — making
it the operational backbone of any large smartcard deployment.

## Key Features
- PKCS#11 provider for Linux and macOS applications
- Windows minidriver for native OS smartcard integration
- PC/SC interface for smartcard reader communication
- Windows smart card logon support
- Browser integration for Chrome, Firefox, Edge, Safari
- Email signing and encryption via S/MIME
- Document signing support for Adobe Acrobat and Office
- VPN client integration for certificate-based authentication
- Silent installation and GPO deployment for enterprise rollout
- Card management client for PIN operations
- Multi-card and multi-reader support
- Virtual smartcard support
- Automatic card detection and initialization
- Centralized configuration management
- Cross-platform consistency across Windows, macOS, Linux

## Technical Specifications
**Supported Interfaces:**
- PKCS#11 — Cryptographic Token Interface Standard
- Microsoft CryptoAPI (CAPI) — Windows cryptographic API
- Microsoft CNG (Cryptography Next Generation)
- Microsoft Smart Card Minidriver
- PC/SC — Personal Computer Smart Card standard
- OpenSC compatible interface

**Operating System Support:**
- Windows 10, Windows 11
- Windows Server 2016, 2019, 2022
- macOS 12 Monterey and later
- Linux — RHEL, Ubuntu, Debian, CentOS

**Browser Support:**
- Microsoft Edge (native Windows integration)
- Google Chrome (via PKCS#11 or minidriver)
- Mozilla Firefox (via PKCS#11)
- Apple Safari (via macOS keychain integration)

**Application Integration:**
- Microsoft Outlook — S/MIME email signing and encryption
- Microsoft Office — Document signing
- Adobe Acrobat — PDF signing
- OpenVPN, Cisco AnyConnect, Palo Alto GlobalProtect
- Citrix Workspace and VMware Horizon (virtual desktop)
- Any PKCS#11 or CryptoAPI compatible application

**Card Reader Support:**
- USB contact card readers (PC/SC compatible)
- Contactless NFC readers
- Integrated laptop card readers
- Secure PIN pad readers (SPR, Gemalto, HID)

**Deployment:**
- MSI installer for Windows GPO deployment
- PKG installer for macOS
- RPM and DEB packages for Linux
- Silent installation with configuration parameters
- Microsoft SCCM and Intune deployment support
- Centralized configuration via registry or config file

## Key Use Cases
1. **Windows Smart Card Logon** — Enables employees to log
   into Windows workstations and domain-joined systems
   using their PKI smartcard instead of a password.
   IDPlug provides the minidriver that Windows requires
   for certificate-based domain authentication — the
   smartcard replaces the password entirely for network
   logon, screen unlock, and Remote Desktop access.

2. **S/MIME Email Signing and Encryption** — Enables
   Microsoft Outlook and other email clients to use
   the signing and encryption certificates stored on
   the employee smartcard for digitally signed and
   encrypted email communications — ensuring message
   authenticity and confidentiality without any
   additional software beyond IDPlug and the email client.

3. **PDF and Document Signing** — Provides the PKCS#11
   or CryptoAPI interface that Adobe Acrobat, Microsoft
   Word, and document signing applications need to
   access the employee qualified signature certificate
   on the smartcard for legally binding electronic
   signatures on contracts, approvals, and official
   documents.

4. **VPN Certificate Authentication** — Enables VPN
   clients including Cisco AnyConnect, Palo Alto
   GlobalProtect, and OpenVPN to use smartcard
   certificates for remote access authentication —
   replacing password-based VPN access with
   cryptographically strong certificate authentication
   that cannot be phished or stolen.

5. **Virtual Desktop and Citrix Integration** — Enables
   smartcard passthrough in virtual desktop environments
   where the physical smartcard on the user endpoint
   is made available to the virtual desktop session —
   allowing remote workers and thin client users to
   use their physical smartcard for authentication
   and signing within their virtual workspace.

## Industry Applications
- **eGovernment:** Government employee workstation logon,
  classified network access, official document signing,
  inter-agency secure email
- **Citizen ID:** Citizen-facing desktop software enabling
  use of national eID card for online service authentication
  and qualified electronic signature
- **Banking and Finance:** Trader workstation authentication,
  privileged access using smartcard, transaction approval
  signing, secure email for sensitive communications
- **Healthcare:** Clinical workstation smartcard logon,
  prescription signing, patient record access, secure
  clinical communication
- **Insurance:** Agent and broker desktop authentication,
  policy document signing, secure internal communication
- **Manufacturing:** Engineering workstation access,
  technical document signing, IP protection through
  strong authentication

## Competitive Differentiators
- Cross-platform consistency — same middleware behavior
  on Windows, macOS, and Linux reduces support complexity
  in mixed OS enterprise environments
- Deep integration with Cosmo Smartcard and the full
  Nexus platform creates a tested, supported end-to-end
  stack from card OS to desktop middleware to PKI
- Silent enterprise deployment via GPO and SCCM enables
  rollout to tens of thousands of workstations without
  user intervention or IT desk visits
- Virtual desktop support addresses the growing need
  for smartcard use in Citrix and VMware environments
  where remote and hybrid workers operate
- Broad application compatibility — any PKCS#11 or
  CryptoAPI application works with IDPlug without
  custom integration

## Integration Capabilities
- **Cosmo Smartcard** — Primary supported smartcard OS
  providing the hardware credential that IDPlug exposes
  to the operating system and applications
- **Nexus Certificate Manager** — Certificates issued
  by NCM and stored on Cosmo card are accessed by
  IDPlug for all cryptographic operations
- **Nexus Smart ID Digital Access** — Combined with
  IDPlug to provide complete smartcard authentication
  infrastructure — SIDA handles policy and access
  control while IDPlug handles the desktop interface
- **Microsoft Active Directory** — IDPlug minidriver
  enables Windows domain smartcard logon against AD
  using Kerberos PKINIT
- **Microsoft Intune and SCCM** — Enterprise deployment
  and configuration management for large-scale rollout
- **Citrix and VMware Horizon** — Virtual desktop
  smartcard passthrough for remote and thin client users

## Compliance and Standards
- PKCS#11 v2.40 — Cryptographic Token Interface Standard
- Microsoft Smart Card Minidriver specification
- PC/SC workgroup specifications
- ISO 7816 — Smartcard communication standard
- RFC 5272 — Certificate Management over CMS
- ETSI TS 119 312 — Cryptographic suites alignment
- eIDAS Regulation — Qualified signature creation
  device middleware requirements
- Common Criteria — Middleware security evaluation
- FIPS 140-2 — Cryptographic module usage via
  smartcard hardware
- NIST SP 800-73 — PIV card interface specification
  for US government deployments

## Customer Reference Profile
- National government ministry desktop deployment
  Products: IDPlug + Cosmo Smartcard + NCM + Digital Access
  Scale: 85,000 government workstations
  OS: Windows 10 and 11, some macOS
  Use case: Domain logon, email signing, document signing
  Deployment: Silent GPO rollout over 3 months
  Outcome: Password-based logon eliminated across
  all government workstations

- National eID citizen software
  Products: IDPlug + Cosmo Smartcard
  Scale: Public download — 2M+ citizen installations
  OS: Windows, macOS, Linux
  Use case: Citizen use of national eID card on
  personal computers for government portal access
  and qualified electronic signature
  Outcome: Single middleware supporting all major
  OS and browser combinations for citizen use

- Large healthcare network
  Products: IDPlug + Cosmo Smartcard + NCM
  Scale: 40,000 clinical workstations
  Use case: Clinical smartcard logon, prescription
  signing, patient record access
  Outcome: Password resets reduced by 95%, clinical
  workflow time saved through fast card-based logon