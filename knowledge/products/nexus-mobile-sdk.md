# Nexus Mobile SDK
**Category:** Mobile | **Code:** NMS

## Product Overview
Nexus Mobile SDK is a software development kit that enables
organizations and technology partners to embed PKI-based
authentication, digital signing, and mobile credential
capabilities directly into their own iOS and Android
applications. Rather than directing users to a separate
Nexus Mobile Client app, the SDK allows organizations
to deliver a fully branded, seamlessly integrated mobile
identity experience within their existing customer-facing
or employee-facing applications.

The SDK provides all the cryptographic and credential
management capabilities of the Nexus Mobile Client —
certificate enrollment, biometric-protected key storage,
push notification approval, transaction signing, and
OTP generation — packaged as a library that developers
integrate into their own app. A bank embeds it into
their mobile banking app. A government agency integrates
it into their citizen services app. An enterprise embeds
it into their corporate mobile app. Users get a unified
experience without switching between multiple applications.

For organizations that have invested in their own mobile
applications and want to add strong PKI-based identity
without rebuilding from scratch, Nexus Mobile SDK is the
fastest path to mobile credential capability. It reduces
development time from months to weeks by providing
production-ready cryptographic components, tested
enrollment flows, and pre-built UI components that
developers can customize to match their brand.

## Key Features
- iOS and Android native SDK libraries
- Certificate enrollment via EST and SCEP
- Hardware-backed key generation and storage
- Biometric authentication integration (Face ID, Touch ID,
  Android fingerprint)
- Push notification approval framework
- QR code authentication module
- OATH TOTP and HOTP one-time password generation
- Transaction signing with dynamic linking
- Certificate lifecycle management APIs
- PIN management and biometric fallback
- Remote wipe and credential deregistration API
- Pre-built customizable UI components
- Offline authentication support
- Multi-certificate support per device
- Tamper detection and app shielding APIs
- Comprehensive developer documentation and sample apps

## Technical Specifications
**SDK Platforms:**
- iOS SDK — Swift and Objective-C compatible
  Minimum iOS 14, supports iOS 14 to latest
  Distributed as XCFramework via Swift Package Manager
  or CocoaPods

- Android SDK — Kotlin and Java compatible
  Minimum Android 9 (API 28)
  Distributed as AAR via Maven/Gradle

**Key Storage:**
- iOS — Secure Enclave for hardware-backed ECC keys
  iOS Keychain for certificate storage
- Android — Android Keystore for hardware-backed keys
  where StrongBox or TEE available
  Software fallback with AES encryption for older devices

**Cryptographic APIs:**
- RSA 2048/4096 key generation and signing
- ECC P-256/P-384 key generation and signing
- AES 256 symmetric encryption
- SHA-256/384/512 hashing
- ECDH key agreement for secure channel
- Hardware random number generation

**Enrollment Protocols:**
- EST (RFC 7030) — primary enrollment protocol
- SCEP (RFC 8894) — legacy device support
- REST API enrollment for custom backends

**Authentication Modules:**
- CertificateAuthModule — PKI certificate authentication
- BiometricAuthModule — Native biometric integration
- PushApprovalModule — Push notification approval
- QRCodeAuthModule — QR code session binding
- OTPModule — TOTP and HOTP generation
- DerivedCredentialModule — Derive from physical smartcard

**UI Components (customizable):**
- EnrollmentFlow — Certificate enrollment wizard
- PINSetupView — PIN creation and change screens
- BiometricPromptView — Biometric authentication prompt
- PushApprovalView — Transaction approval display
- CertificateListView — Credential management screen

## Key Use Cases
1. **Branded Mobile Banking Authentication** — A bank
   integrates Nexus Mobile SDK into their existing
   mobile banking app to add PKI-based strong
   authentication and PSD2-compliant transaction
   signing. Customers enroll their certificate
   within the bank app, approve transactions with
   biometric, and the bank maintains complete
   control over the user experience and branding
   without directing customers to a third-party app.

2. **Government Citizen Services App Integration** —
   A government agency integrates the SDK into their
   national citizen services mobile app, enabling
   citizens to enroll their mobile eID certificate
   directly within the official government app.
   Authentication to tax, health, and social services
   is handled within a single government-branded
   experience using PKI credentials backed by the
   national PKI infrastructure.

3. **Enterprise Mobile App PKI Integration** — An
   enterprise integrates the SDK into their existing
   corporate mobile app — adding smartcard-equivalent
   strong authentication for employees who access
   corporate resources from mobile devices. The SDK
   handles certificate enrollment, renewal, and
   authentication while the enterprise app maintains
   its existing user interface and workflow.

4. **Telco Customer Identity Integration** — A
   telecommunications operator integrates the SDK
   into their customer self-service app, enabling
   subscribers to authenticate using PKI credentials
   tied to their subscriber identity. Strong
   authentication replaces SMS OTP for SIM swap
   prevention and account takeover protection.

5. **Partner and ISV Integration** — Technology
   partners and independent software vendors
   building solutions for Nexus customers integrate
   the Mobile SDK to add mobile PKI credential
   support to their products — creating a complete
   solution without building cryptographic
   infrastructure from scratch.

## Industry Applications
- **Banking and Finance:** Mobile banking app PKI
  integration, PSD2 SCA compliance, transaction
  signing, privileged banking employee mobile access
- **eGovernment:** Citizen services app eID integration,
  government employee mobile credential in enterprise
  mobile apps
- **Telco:** Customer self-service app strong auth,
  subscriber identity protection, employee mobile
  credential in corporate apps
- **Insurance:** Mobile agent and customer app PKI
  integration, mobile policy signing, digital
  onboarding identity verification
- **Healthcare:** Clinical mobile app strong auth,
  mobile prescription signing, patient portal
  mobile identity
- **Energy and Utilities:** Field operations mobile
  app PKI integration, work order signing, remote
  system access credential

## Competitive Differentiators
- White-label architecture gives organizations full
  control over user experience and branding —
  no Nexus branding visible to end users
- Native SDK libraries (not web-based or hybrid)
  deliver optimal performance and full access to
  device hardware security capabilities
- Pre-built UI components dramatically reduce
  development time while remaining fully customizable
- Full integration with Nexus backend infrastructure —
  certificate management, OCSP, revocation all
  handled by the same proven platform used in
  national-scale deployments
- Offline capability ensures authentication works
  in low-connectivity environments critical for
  field operations and travel
- Derived credential support enables mobile enrollment
  from physical smartcard without separate backend
  registration process

## Integration Capabilities
- **Nexus Certificate Manager** — Backend certificate
  issuance and lifecycle management for SDK-enrolled
  mobile credentials
- **Nexus Smart ID Digital Access** — Authentication
  decisions for SDK-issued credentials handled by
  SIDA access control policies
- **Nexus Smart ID Identity Manager** — Identity
  lifecycle events trigger SDK credential provisioning
  via push notification enrollment workflows
- **Nexus OCSP** — Certificate status checking for
  SDK-managed credentials during authentication
- **Nexus Protocol Gateway** — EST and SCEP enrollment
  gateway for SDK certificate requests
- **MDM platforms** — App deployment and certificate
  pre-provisioning via Intune, Jamf, Workspace ONE
- **Push infrastructure** — Apple APNs and Google FCM
  integration for approval notification delivery

## Compliance and Standards
- RFC 6238 — TOTP implementation
- RFC 4226 — HOTP implementation
- RFC 7030 — EST enrollment protocol
- RFC 8894 — SCEP enrollment protocol
- FIDO2 — Mobile authenticator alignment
- eIDAS Regulation — Mobile eID substantial and
  high assurance level requirements
- PSD2 — Strong Customer Authentication dynamic
  linking requirements
- NIST SP 800-63B — Authenticator assurance levels
- Apple iOS App Store security and privacy guidelines
- Android Google Play security guidelines
- OWASP Mobile Application Security Verification
  Standard (MASVS)
- GDPR — Privacy by design in SDK data handling

## Developer Resources
- Full API documentation with code examples
- iOS Swift and Android Kotlin sample applications
- Integration guide for common use cases
- Postman collection for backend API testing
- Sandbox environment for development and testing
- Developer support portal and ticketing
- Regular SDK updates with new features and
  security patches

## Customer Reference Profile
- Tier-1 retail bank mobile banking integration
  Products: Nexus Mobile SDK + NCM + Digital Access
  Platform: iOS and Android native apps
  Scale: 1.2M enrolled mobile banking customers
  Use case: PSD2 SCA, transaction signing, account
  access strong authentication
  Integration time: 6 weeks from SDK evaluation
  to production deployment
  Outcome: SMS OTP completely replaced, fraud
  reduced, full PSD2 compliance achieved

- National government citizen services app
  Products: Nexus Mobile SDK + NCM + OCSP + Smart
  ID Identity Manager
  Platform: iOS and Android official government app
  Scale: 2M citizen mobile eID enrollments
  Use case: Authentication to all government
  digital services within single official app
  Outcome: Citizens authenticate to 15+ government
  services within single branded government app

- Telco customer self-service integration
  Products: Nexus Mobile SDK + NCM + Digital Access
  Platform: Android-first with iOS follow-on
  Scale: 5M subscriber strong authentication
  Use case: SIM swap prevention, account management
  strong authentication, subscriber identity
  Outcome: SIM swap fraud eliminated, customer
  satisfaction improved versus SMS OTP