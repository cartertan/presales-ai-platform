# Nexus Mobile Client
**Category:** Mobile | **Code:** NMC

## Product Overview
Nexus Mobile Client is a mobile application platform that delivers
PKI-based authentication, digital signing, and secure identity
credentials to iOS and Android devices. It transforms a smartphone
or tablet into a trusted identity credential — enabling employees,
citizens, and customers to authenticate to systems, sign documents,
approve transactions, and access services using their mobile device
as a secure soft token or mobile smart ID.

The Nexus Mobile Client addresses the growing demand for mobile-first
identity in enterprises and government agencies where issuing physical
smartcards to every user is impractical, costly, or unnecessary.
It provides the same cryptographic strength as a physical smartcard —
using the mobile device secure element or software-based key storage
protected by device biometrics — while delivering the convenience
of a credential that users always carry with them.

For government agencies rolling out digital citizen identity programs,
enterprises enabling mobile workforce authentication, and banks
implementing mobile strong authentication for their customers,
Nexus Mobile Client provides the mobile credential layer that
integrates seamlessly with the Nexus PKI and IAM platform to
deliver a complete, managed mobile identity lifecycle.

## Key Features
- Mobile PKI certificate management on iOS and Android
- Biometric authentication — fingerprint and face recognition
- Push notification approval for transaction signing
- QR code authentication for desktop session login
- OATH TOTP and HOTP one-time password generation
- Derived credential from physical smartcard
- Mobile document signing with qualified certificates
- Offline authentication capability
- Certificate lifecycle management from mobile app
- PIN and biometric protection for credential access
- Remote wipe and device deregistration
- MDM integration for enterprise deployment
- App shielding and tamper detection
- In-app identity verification workflow
- Multi-account support for enterprise and personal use

## Technical Specifications
**Platform Support:**
- iOS 14 and later (iPhone and iPad)
- Android 9 and later (phone and tablet)
- Supports ARM64 architecture (modern devices)
- Secure Enclave integration (iOS)
- Android Keystore for hardware-backed key storage

**Authentication Methods:**
- PKI certificate-based authentication
- Biometric — Face ID, Touch ID (iOS), fingerprint (Android)
- PIN code as biometric fallback
- Push notification approval (tap to approve)
- QR code scan for desktop session binding
- OATH TOTP (RFC 6238) soft token
- OATH HOTP (RFC 4226) event-based OTP

**Cryptographic Capabilities:**
- RSA 2048/4096 key generation
- ECC P-256/P-384 key generation
- AES 256 symmetric encryption
- SHA-256/384/512 hashing
- Hardware-backed key storage via Secure Enclave or
  Android Keystore where available
- Software key storage with encryption for older devices

**Certificate Operations:**
- Certificate enrollment via EST and SCEP
- Certificate renewal and update
- Certificate revocation notification
- Multiple certificate support per device
- Certificate status checking via OCSP

**Enterprise Integration:**
- MDM platforms: Microsoft Intune, Jamf, VMware Workspace ONE
- SAML 2.0 and OpenID Connect federation
- Nexus Smart ID Digital Access integration
- Push notification via APNs (iOS) and FCM (Android)
- REST API for backend integration

## Key Use Cases
1. **Mobile Strong Authentication for Enterprise** — Employees
   use Nexus Mobile Client as their second factor or primary
   authenticator for corporate applications, VPN access, and
   cloud services. Push notification approval replaces OTP
   tokens — users receive a push on their phone showing
   the login request details and approve with biometric
   or PIN. Phishing-resistant and far more convenient than
   hardware tokens.

2. **Citizen Mobile eID** — National identity program
   provides citizens with a mobile identity app backed
   by a government-issued PKI certificate. Citizens
   authenticate to tax portals, health services, and
   government digital services using their smartphone
   instead of or in addition to a physical eID card —
   expanding digital service access to citizens who
   prefer mobile interaction.

3. **Mobile Transaction Signing** — Bank customers and
   employees approve high-value transactions using
   Nexus Mobile Client. The app displays transaction
   details and the user signs with biometric — creating
   a cryptographic proof of authorization that satisfies
   PSD2 dynamic linking requirements and provides a
   non-repudiable audit trail.

4. **Derived Mobile Credential** — Government employees
   who have a physical smartcard can derive a mobile
   credential from their card — binding their PKI
   identity to their mobile device. This gives them
   full PKI authentication capability on mobile without
   a separate issuance process — the mobile credential
   is derived from and linked to their existing
   physical identity credential.

5. **Remote Identity Verification and Onboarding** —
   New employees or customers complete identity
   verification through the mobile app — capturing
   identity document images, biometric selfie, and
   completing liveness detection — to receive their
   mobile PKI credential without visiting a physical
   registration authority.

## Industry Applications
- **eGovernment:** Mobile government employee authentication,
  citizen mobile eID for digital services, remote identity
  verification for government onboarding
- **Citizen ID:** National mobile identity app, citizen
  digital signature for e-services, mobile border
  crossing document verification
- **Banking and Finance:** Mobile strong authentication
  for online banking, PSD2 dynamic linking transaction
  signing, mobile banking employee credential
- **Insurance:** Mobile agent authentication, mobile
  policy signing, customer identity verification
  for digital onboarding
- **Telco:** Mobile employee authentication, customer
  mobile identity for self-service portal access
- **Energy and Utilities:** Field engineer mobile
  credential for remote system access and work
  order signing

## Competitive Differentiators
- Native PKI foundation provides cryptographic strength
  far beyond OTP tokens or SMS-based authentication —
  certificate-based mobile credentials cannot be
  phished, replayed, or intercepted
- Derived credential capability links mobile identity
  to existing physical smartcard — no separate
  registration or issuance process required
- Biometric authentication leverages device hardware
  security — Face ID and Secure Enclave on iOS,
  Android Keystore with biometric binding
- Push notification approval with transaction detail
  display satisfies PSD2 dynamic linking requirements
  for payment authentication
- Full lifecycle management from mobile app — users
  can renew certificates, update PINs, and manage
  their credentials without IT helpdesk involvement
- Offline capability ensures authentication works
  even without network connectivity for field workers
  and remote locations

## Integration Capabilities
- **Nexus Certificate Manager** — Certificate issuance,
  renewal, and revocation for mobile PKI credentials
- **Nexus Smart ID Digital Access** — Mobile client
  credentials used for authentication decisions in
  SIDA access control policies
- **Nexus Smart ID Identity Manager** — Identity
  lifecycle events trigger mobile credential
  provisioning and deprovisioning
- **Cosmo Smartcard** — Physical card used as trust
  anchor for derived mobile credential issuance
- **MDM platforms** — Microsoft Intune, Jamf, and
  VMware Workspace ONE for enterprise app deployment
  and policy enforcement
- **Push notification infrastructure** — Apple APNs
  and Google FCM for real-time approval notifications
- **SAML and OIDC providers** — Federation with
  enterprise identity providers for SSO scenarios

## Compliance and Standards
- RFC 6238 — TOTP time-based one-time password
- RFC 4226 — HOTP event-based one-time password
- RFC 7030 — EST certificate enrollment
- RFC 8894 — SCEP certificate enrollment
- FIDO2 — Mobile authenticator alignment
- eIDAS Regulation — Mobile eID requirements for
  substantial and high assurance levels
- PSD2 — Strong Customer Authentication and dynamic
  linking requirements for payment services
- NIST SP 800-63B — Mobile authenticator assurance
  level requirements
- ISO 27001 — Mobile credential security controls
- GDPR — Mobile identity data privacy requirements
- Apple iOS security guidelines and App Store policies
- Android security guidelines and Google Play policies

## Customer Reference Profile
- National mobile eID program
  Products: Nexus Mobile Client + NCM + Smart ID
  Identity Manager + Digital Access
  Scale: 1.5M citizen mobile eID activations
  Use case: Tax portal, health services, government
  digital services authentication
  Outcome: 40% of citizens now use mobile eID
  as primary authentication method — physical
  card usage declining as mobile adoption grows

- Major retail bank — PSD2 compliance
  Products: Nexus Mobile Client + NCM + Digital Access
  Scale: 800,000 mobile banking customers
  Use case: PSD2 strong customer authentication,
  transaction signing, account management approval
  Outcome: Full PSD2 compliance achieved, fraud
  incidents reduced significantly versus SMS OTP,
  customer satisfaction improved with biometric UX

- Government ministry mobile workforce
  Products: Nexus Mobile Client + NCM + Cosmo Smartcard
  Scale: 25,000 field officers and mobile workers
  Use case: Derived credential from physical smart
  card, remote system access, field report signing
  Outcome: Field workers fully equipped with mobile
  PKI credential without additional issuance process