# Nexus Smart ID Digital Access
**Category:** IAM | **Code:** SIDA

## Product Overview
Nexus Smart ID Digital Access is an enterprise Identity and Access
Management platform that provides secure, flexible authentication
and access control for both physical and logical resources. It
enables organizations to manage how their employees, citizens, and
customers authenticate to systems, buildings, applications, and
digital services — using smartcards, mobile credentials, biometrics,
or a combination of factors.

Smart ID Digital Access serves as the authentication layer that
sits between users and the resources they need to access. It
enforces authentication policies, manages credential lifecycle,
and provides a unified access experience across legacy systems
and modern cloud applications. For government agencies, it powers
national eID authentication infrastructure. For enterprises, it
replaces fragmented authentication silos with a single, policy-driven
access platform.

The product is designed for high-security environments where strong
authentication is mandatory — government networks, financial
institutions, healthcare systems, and critical infrastructure
operators. It supports a broad range of credential types and
authentication methods, making it adaptable to diverse workforce
and citizen populations with different device capabilities.

## Key Features
- Multi-factor authentication (MFA) with smartcard, mobile, OTP
- Physical and logical access control from single platform
- PKI-based authentication using X.509 certificates
- SAML 2.0 and OpenID Connect for federated identity
- Active Directory and LDAP integration
- Biometric authentication support
- Mobile smart ID for iOS and Android
- Self-service credential management portal
- Role-based access control with fine-grained policies
- Risk-based adaptive authentication
- Single Sign-On (SSO) across enterprise applications
- Full audit trail and compliance reporting
- High availability clustering
- REST API for custom integration

## Technical Specifications
**Authentication Methods:**
- Smartcard with PKI certificate (X.509)
- Mobile smart ID application
- Hardware OTP tokens
- Software OTP (TOTP/HOTP — RFC 6238)
- Biometric (fingerprint, face — via integration)
- Username and password (legacy fallback)
- Push notification approval
- QR code authentication

**Federation and Standards:**
- SAML 2.0 Identity Provider and Service Provider
- OpenID Connect / OAuth 2.0
- FIDO2 / WebAuthn
- Kerberos for Windows domain authentication
- RADIUS for network access authentication
- WS-Federation for legacy applications

**Integration Options:**
- Microsoft Active Directory and Azure AD
- LDAP directory services
- Nexus Certificate Manager for certificate issuance
- Cosmo Smartcard OS for hardware credentials
- IDPlug Middleware for desktop smartcard integration
- Physical access control systems (PACS)
- SIEM platforms for security event forwarding
- ServiceNow for access request workflows

**Platform Support:**
- Deployment: On-premises, private cloud, hybrid, SaaS
- OS: Windows Server, Linux
- Clients: Windows, macOS, Linux, iOS, Android
- High Availability: Active-active clustering
- Database: SQL Server, Oracle, PostgreSQL

## Key Use Cases
1. **Government Employee Authentication** — PKI smartcard-based
   logical access for government staff to access classified networks,
   workstations, email, and sensitive government applications with
   certificate-based strong authentication meeting national security
   requirements.

2. **Citizen eID Authentication** — National eID portal authentication
   where citizens use their national identity card or mobile eID
   to authenticate to tax, health, social services, and other
   government digital services.

3. **Physical and Logical Access Convergence** — Single credential
   for both building access and IT system login — employee uses
   one smartcard to enter the office and log into their workstation,
   eliminating the need for separate access cards and IT credentials.

4. **Financial Services Strong Authentication** — Bank employee
   and customer strong authentication for transaction authorization,
   privileged access to core banking systems, and regulatory-compliant
   customer identity verification.

5. **Remote Access and VPN Authentication** — Certificate-based
   smartcard or mobile authentication for remote workers accessing
   corporate resources via VPN, replacing vulnerable password-based
   remote access with cryptographically strong credentials.

## Industry Applications
- **eGovernment:** National employee PKI authentication, citizen
  portal access, inter-agency federation, classified network access
- **Citizen ID:** National eID program authentication layer,
  citizen self-service portal, digital signature workflows
- **Banking and Finance:** Employee privileged access, customer
  strong authentication, transaction signing, PSD2 compliance
- **Energy and Utilities:** Operational technology access control,
  NERC CIP compliant privileged access management
- **Insurance:** Agent authentication, policy system access,
  document signing workflows
- **Manufacturing:** Production system access control, IP
  protection through strong authentication

## Competitive Differentiators
- Unified physical and logical access from one platform reduces
  complexity and total cost of ownership
- Native PKI integration with Nexus Certificate Manager provides
  end-to-end certificate and credential lifecycle management
- Proven in national-scale government deployments serving
  millions of citizens and hundreds of thousands of employees
- Mobile Smart ID enables digital-first credential delivery
  without physical card infrastructure where appropriate
- Adaptive risk-based authentication reduces friction for
  low-risk access while enforcing step-up for high-risk actions
- Strong European and government market heritage with deep
  understanding of regulatory compliance requirements

## Integration Capabilities
- **Nexus Certificate Manager** — Certificate issuance for
  smartcard and mobile credentials
- **Nexus Smart ID Identity Manager** — Identity lifecycle
  management feeding into access management
- **Cosmo Smartcard** — Hardware credential platform for
  physical smartcard deployments
- **IDPlug Middleware** — Desktop smartcard reader integration
  for Windows and macOS
- **Microsoft AD / Azure AD** — Directory synchronization
  and Kerberos/SAML federation
- **Physical Access Control Systems** — HID, Lenel, Genetec,
  CCURE for converged physical-logical access
- **SIEM platforms** — Splunk, Microsoft Sentinel, QRadar
  for authentication event monitoring

## Compliance and Standards
- FIDO2 / WebAuthn — W3C and FIDO Alliance standards
- SAML 2.0 — OASIS standard for federated identity
- OpenID Connect / OAuth 2.0 — IETF standards
- RFC 6238 — TOTP time-based one-time password
- ETSI EN 319 411 — Supporting qualified certificate use
- eIDAS Regulation — Strong authentication requirements
  for electronic identification schemes
- FIPS 140-2/3 — Via HSM and smartcard integration
- Common Criteria — Smartcard and middleware evaluation
- GDPR — Privacy by design in authentication workflows
- NIST SP 800-63 — Digital identity guidelines alignment
- PSD2 — Strong Customer Authentication (SCA) requirements
  for payment services

## Customer Reference Profile
- National government ministry network
  Products: Smart ID Digital Access + NCM + Cosmo Smartcard
  Scale: 80,000 government employees
  Use case: PKI smartcard logon, email signing, VPN access
  Outcome: Eliminated password-based access across all systems

- National eID citizen authentication
  Products: Smart ID Digital Access + NCM + OCSP
  Scale: 3M active citizen eID users
  Use case: Tax portal, health records, social services access
  Outcome: Single national authentication standard across
  all government digital services

- Tier-1 commercial bank
  Products: Smart ID Digital Access + NCM + Smart ID
  Identity Manager
  Scale: 15,000 employees, 500 privileged users
  Use case: Core banking access, transaction authorization,
  PSD2 strong customer authentication
  Outcome: Regulatory compliance achieved, fraud incidents
  reduced significantly