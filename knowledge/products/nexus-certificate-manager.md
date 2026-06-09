# Nexus Certificate Manager
**Category:** PKI | **Code:** NCM

## Product Overview
Nexus Certificate Manager (NCM) is an enterprise-grade Public Key 
Infrastructure platform that provides end-to-end certificate lifecycle 
management for organizations of all sizes. NCM serves as the core engine 
for issuing, renewing, revoking, and managing X.509 digital certificates 
across complex enterprise environments.

NCM supports both private PKI deployments and integration with external 
public Certificate Authorities including DigiCert, GlobalSign, Entrust, 
and cloud-based CA services such as AWS Private CA, Azure Key Vault, and 
Google Cloud CAS. It is designed to handle millions of certificates across 
diverse use cases including TLS/SSL, device authentication, user identity, 
code signing, and document signing.

The platform provides a centralized management console with role-based 
access control, full audit logging, and automated certificate lifecycle 
workflows — reducing manual effort and eliminating certificate expiry 
incidents that cause service outages.

## Key Features
- Full certificate lifecycle management: issuance, renewal, revocation
- Support for RSA, ECC, and post-quantum cryptographic algorithms
- Multi-CA support: internal CA, external public CA, cloud CA
- ACME protocol support for automated TLS certificate management
- REST API and SOAP API for seamless integration with DevOps pipelines
- Role-based access control with segregation of duties
- Automated expiry monitoring and renewal workflows
- Hardware Security Module (HSM) integration for key protection
- Certificate policy enforcement and compliance controls
- Full audit trail and compliance reporting
- High availability active-active clustering
- Support for certificate templates and profiles

## Technical Specifications
**Supported Protocols:**
- SCEP (Simple Certificate Enrollment Protocol)
- EST (Enrollment over Secure Transport)
- ACME (Automated Certificate Management Environment)
- CMP (Certificate Management Protocol)
- CMC (Certificate Management over CMS)
- LDAP for directory integration
- REST API and SOAP WebServices

**Integration Options:**
- HSM vendors: Utimaco, Thales, nCipher, AWS CloudHSM
- Directory services: Microsoft Active Directory, LDAP
- ITSM platforms: ServiceNow
- DevOps tools: Kubernetes, HashiCorp Vault, Ansible
- Cloud platforms: AWS, Azure, Google Cloud
- Monitoring: SNMP, Syslog, SIEM integration

**Platform Support:**
- Deployment: On-premises, private cloud, hybrid
- OS: Windows Server, Linux (RHEL, Ubuntu)
- Database: Microsoft SQL Server, Oracle, PostgreSQL
- High Availability: Active-active clustering, load balancing
- Containerization: Docker, Kubernetes

**Scalability:**
- Millions of certificates under management
- High-volume issuance for IoT and device PKI
- Multi-tenant architecture for service providers

## Key Use Cases
1. **Enterprise TLS Certificate Management** — Centralized management of 
   all internal and external TLS certificates, automated renewal, and 
   expiry alerting to eliminate outages caused by expired certificates.

2. **IoT and Device PKI** — High-volume certificate issuance for 
   connected devices, smart meters, industrial equipment, and 
   operational technology assets using SCEP or EST protocols.

3. **User and Employee Identity** — Issuing smart card certificates, 
   soft certificates, and mobile certificates for employee 
   authentication, email signing, and document signing.

4. **Government and Citizen PKI** — National PKI deployments issuing 
   certificates for eID cards, ePassports, and government employee 
   credentials compliant with national PKI policy frameworks.

5. **Code Signing Infrastructure** — Managed PKI for software code 
   signing certificates ensuring software integrity across development 
   and distribution pipelines.

## Industry Applications
- **eGovernment:** National PKI backbone, citizen eID, government 
  employee certificates, eService authentication
- **Banking and Finance:** Transaction signing, customer authentication, 
  open banking TLS infrastructure, PSD2 compliance
- **Telco:** SIM PKI, network device certificates, subscriber identity, 
  M2M authentication
- **Energy and Utilities:** Smart meter PKI, SCADA device certificates, 
  IEC 62351 compliance
- **Manufacturing:** Industry 4.0 device identity, code signing, 
  supply chain certificate management
- **Trust Centers:** TSP infrastructure, qualified certificate issuance, 
  eIDAS compliant CA operations

## Competitive Differentiators
- Protocol breadth: supports SCEP, EST, ACME, CMP, CMC simultaneously
- Proven at national scale — deployed in government PKI programs 
  serving millions of citizens
- Deep HSM integration with leading HSM vendors
- Flexible CA hierarchy support — works with any CA vendor or cloud CA
- Strong European presence and eIDAS compliance expertise
- Open API architecture enables integration with any existing 
  enterprise ecosystem
- Crypto-agility built in — ready for post-quantum migration

## Integration Capabilities
- Nexus OCSP Responder for certificate status checking
- Nexus Protocol Gateway for multi-protocol enrollment
- Nexus Smart ID for identity management integration
- Utimaco and Thales HSM for private key protection
- Microsoft AD CS as subordinate or peer CA
- AWS Private CA, Azure Key Vault, Google Cloud CAS
- DigiCert, GlobalSign, Entrust as external public CAs

## Compliance and Standards
- RFC 5280 — X.509 Certificate and CRL Profile
- RFC 8555 — ACME Protocol
- RFC 7030 — EST Protocol
- RFC 8894 — SCEP Protocol
- ETSI EN 319 411 — Policy requirements for CAs
- ETSI EN 319 401 — General Policy Requirements for TSPs
- FIPS 140-2/3 compliant key storage via HSM
- Common Criteria certified components
- WebTrust for CAs compliance support
- eIDAS Regulation (EU) 910/2014 compliance

## Customer Reference Profile
- National government PKI serving 5+ million citizens
  Products: NCM + OCSP + Protocol Gateway
  Scale: 2M active certificates, 50,000 daily issuances
- Tier-1 telecom operator device PKI
  Products: NCM + m2trust CLM
  Scale: 10M+ IoT device certificates
- Central bank PKI infrastructure
  Products: NCM + Smart ID + HSM integration
  Scale: Enterprise-wide employee and transaction certificates