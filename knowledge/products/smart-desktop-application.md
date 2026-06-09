# Smart Desktop Application
**Category:** Desktop | **Code:** SDA

## Product Overview
Nexus Smart Desktop Application is an enterprise desktop client
that provides employees with a unified interface for managing
their digital identity credentials, performing PKI operations,
and accessing identity-related self-service functions from their
Windows or macOS workstation. It bridges the gap between the
backend PKI and IAM infrastructure and the end user — giving
employees a simple, intuitive interface to manage their smartcard,
certificates, PIN, and digital identity without requiring IT
helpdesk intervention for routine credential operations.

Smart Desktop Application serves as the user-facing companion
to the Nexus platform — complementing IDPlug Middleware which
handles the low-level smartcard communication, while SDA provides
the management interface above it. Where IDPlug enables the OS
and applications to use smartcard certificates invisibly in the
background, Smart Desktop Application gives the user visibility
and control over their credential — PIN changes, certificate
status, renewal requests, and identity information — in a
clear, guided interface.

For large enterprise and government deployments where IT helpdesk
costs are significant, Smart Desktop Application dramatically
reduces support calls by empowering users to resolve common
credential issues themselves — unlocking blocked PINs, checking
certificate validity, initiating renewal, and troubleshooting
reader connectivity — without waiting for IT support.

## Key Features
- Smartcard PIN management — change, unblock, reset
- Certificate status display and expiry monitoring
- Self-service certificate renewal initiation
- Smartcard reader detection and diagnostics
- Multiple credential support on single workstation
- Digital signature workflow integration
- Identity information display from directory
- Credential health dashboard with status indicators
- Integration with Windows credential provider
- macOS keychain and smartcard integration
- Automated PIN unblock via administrator approval
- Audit logging of all credential operations
- Silent enterprise deployment via GPO and SCCM
- Configurable branding for government and enterprise
- Context-sensitive help and user guidance
- REST API integration with Nexus backend

## Technical Specifications
**Platform Support:**
- Windows 10 and Windows 11 (32-bit and 64-bit)
- Windows Server 2016, 2019, 2022 (server deployments)
- macOS 12 Monterey and later
- Citrix and VMware Horizon virtual desktop support

**Smartcard and Token Support:**
- Cosmo Smartcard OS (native integration)
- ISO 7816 contact smartcard (via PC/SC)
- ISO 14443 contactless cards (via NFC reader)
- USB hardware tokens (PKCS#11 compatible)
- Virtual smartcards (Windows TPM-based)

**Reader Support:**
- All PC/SC compliant USB contact readers
- NFC contactless readers
- Integrated laptop readers
- Secure PIN pad readers
- Multi-reader environments

**Integration:**
- IDPlug Middleware — smartcard communication layer
- Nexus Certificate Manager — certificate lifecycle backend
- Nexus Smart ID Digital Access — authentication status
- Nexus Smart ID Identity Manager — identity data display
- Active Directory — user identity and group information
- LDAP — directory integration for identity display
- Windows Credential Provider — logon integration
- REST API — backend communication

**Deployment:**
- MSI installer for Windows GPO deployment
- PKG installer for macOS
- Microsoft SCCM and Intune deployment support
- Silent installation with administrative configuration
- Centralized configuration via Group Policy
- Configurable corporate branding and logo

## Key Use Cases
1. **Self-Service PIN Management** — Employees change
   their smartcard PIN, unblock a locked card after
   failed PIN attempts, or reset a forgotten PIN
   through a guided self-service workflow — without
   calling the IT helpdesk. For large organizations
   with thousands of smartcard users, PIN-related
   helpdesk calls typically represent the highest
   volume of PKI support tickets. SDA eliminates most
   of these entirely through secure self-service.

2. **Certificate Status and Renewal Management** —
   Employees see the status of all certificates
   on their smartcard — validity period, issuing CA,
   expiry countdown, and renewal eligibility. When
   a certificate approaches expiry, SDA presents
   a clear renewal prompt and handles the renewal
   request to Nexus Certificate Manager automatically
   — no user understanding of PKI required, no
   helpdesk involvement needed.

3. **Smartcard Reader Diagnostics and Troubleshooting**
   — When a smartcard is not being recognized by
   the system, SDA provides step-by-step diagnostic
   guidance — checking reader connectivity, card
   insertion, driver status, and IDPlug middleware
   health — resolving the most common issues without
   IT intervention and providing clear escalation
   information when hardware replacement is needed.

4. **Digital Signature Workflow** — Employees initiate
   and manage digital signing of documents directly
   from Smart Desktop Application — selecting
   documents, choosing the appropriate signing
   certificate, entering PIN for authorization,
   and completing qualified electronic signatures
   for contracts, approvals, and official documents
   with a guided, audit-logged workflow.

5. **Identity Information and Credential Dashboard** —
   Employees access a unified view of their digital
   identity — their certificates, their access rights,
   their identity attributes from Active Directory,
   and the validity status of all their credentials.
   This single dashboard reduces confusion about
   which certificate to use for which purpose and
   provides clear visibility of upcoming expirations.

## Industry Applications
- **eGovernment:** Government employee credential
  management dashboard, official document signing
  workflow, civil servant self-service PKI portal
- **Citizen ID:** Citizen-facing desktop application
  for national eID card management, citizen PIN
  management, eID card diagnostic tool for
  citizen self-service
- **Banking and Finance:** Employee PKI credential
  management, trader workstation certificate
  dashboard, privileged user credential management
- **Healthcare:** Clinical workstation smartcard
  management, healthcare professional card
  self-service, prescription signing workflow
- **Insurance:** Agent credential management,
  policy document signing workflow, broker
  desktop identity management
- **Manufacturing:** Engineering workstation
  credential management, technical document
  signing, IP access credential dashboard

## Competitive Differentiators
- Zero helpdesk model — designed specifically to
  eliminate the most common PKI support calls through
  guided self-service workflows that any user can
  complete without technical knowledge
- Full Nexus platform integration creates consistent
  credential management experience across card,
  desktop, and mobile without multiple separate
  management interfaces
- Configurable branding allows government agencies
  and enterprises to present a consistent corporate
  or national identity interface rather than a
  third-party tool
- Diagnostics engine resolves the most common
  smartcard issues — reader detection, card
  recognition, middleware status — without IT
  escalation in the majority of cases
- Designed for non-technical users — clear language,
  guided workflows, visual status indicators, and
  context-sensitive help make PKI operations
  accessible to all employees regardless of
  technical background
- Virtual desktop support via Citrix and VMware
  ensures consistent experience for remote workers
  and thin client users

## Integration Capabilities
- **IDPlug Middleware** — Core smartcard communication
  layer that SDA uses for all card operations —
  PIN management, certificate access, cryptographic
  operations
- **Nexus Certificate Manager** — Certificate lifecycle
  backend for renewal requests, status checking,
  and revocation notification
- **Nexus Smart ID Digital Access** — Authentication
  status integration showing current access rights
  and credential validity
- **Nexus Smart ID Identity Manager** — Identity
  data source for displaying user profile, role,
  and entitlement information within SDA
- **Active Directory** — User account information,
  group membership, and password policy integration
- **Microsoft SCCM and Intune** — Enterprise
  deployment, configuration management, and
  software update distribution
- **Windows Credential Provider** — Integration
  with Windows logon for PIN change triggered
  at logon screen
- **SIEM platforms** — Credential operation audit
  events forwarded for security monitoring

## Compliance and Standards
- ISO 7816 — Smartcard interface standard
- PC/SC — Personal Computer Smart Card standard
- PKCS#11 — Cryptographic token interface
- Microsoft Smart Card Minidriver specification
- eIDAS Regulation — Qualified signature creation
  and management application requirements
- ETSI TS 119 432 — Electronic signature creation
  application standards
- Common Criteria — Desktop application security
  evaluation alignment
- FIPS 140-2 — Cryptographic operations via
  IDPlug and smartcard hardware
- GDPR — User credential data privacy in
  desktop application context
- WCAG 2.1 — Accessibility standards for
  government deployments requiring accessible
  citizen-facing applications
- ISO 27001 — Credential management controls
  for desktop security

## Customer Reference Profile
- National government employee credential portal
  Products: Smart Desktop Application + IDPlug
  + Cosmo Smartcard + NCM
  Scale: 95,000 government workstations
  OS: Windows 10 and 11
  Use case: Employee PIN management, certificate
  renewal, document signing, credential dashboard
  Deployment: GPO silent rollout
  Outcome: PIN-related helpdesk calls reduced by
  87%, certificate expiry incidents eliminated,
  document signing adoption increased to 100%
  of contracts within 6 months

- National eID citizen desktop application
  Products: Smart Desktop Application + IDPlug
  + Cosmo Smartcard
  Scale: Public download — 3M+ citizen installs
  OS: Windows and macOS
  Use case: Citizen PIN management for national
  eID card, card diagnostics, certificate status,
  eService authentication helper
  Outcome: Citizen helpdesk calls for PIN issues
  reduced by 70%, card diagnostic tool resolved
  60% of reported card issues without technician
  visit

- Healthcare network clinical workstation
  Products: Smart Desktop Application + IDPlug
  + Cosmo Smartcard + NCM
  Scale: 55,000 clinical workstations
  Use case: Healthcare professional card management,
  prescription signing workflow, clinical system
  access credential dashboard
  Outcome: Clinical staff can manage their own
  credentials without IT support, prescription
  signing fully digital across all facilities