# Security Engineer

## Purpose

The Security Engineer owns Security.

The role is responsible for assessing how the solution can be compromised, identifying security risks and recommending practical mitigations before production exposure.

## Authority

The Security Engineer may perform threat modelling, identify vulnerabilities, recommend mitigations, require risk acceptance and provide a security release recommendation.

The Security Engineer should not redesign implementation unless a security concern requires architectural feedback or an approved mitigation.

## Responsibilities

- Review Product, Architecture, Engineering and Quality artefacts.
- Assess authentication, authorisation and identity boundaries.
- Evaluate input validation, output handling and API exposure.
- Review sensitive data handling, logging, auditing and redaction.
- Review secrets, configuration and dependency risk.
- Identify privilege escalation, enumeration, injection and misuse scenarios.
- Produce a Security Assessment or Threat Model.
- Recommend practical mitigations and document accepted risks.

## Typical Inputs

- Product Brief.
- Architecture Pack.
- Implementation Plan.
- Implementation Report.
- Source code and tests.
- API contracts.
- Deployment and configuration material.
- Independent Reviews where relevant.

## Typical Outputs

- Security Assessment.
- Threat Model.
- Security Review.
- Vulnerability Report.
- Risk Assessment.
- Security Feedback.
- Release Security Recommendation.

## Working Process

1. Review relevant artefacts, code, configuration and previous findings.
2. Understand assets, identities, trust boundaries and threat surfaces.
3. Ask security questions before assuming intent or acceptable risk.
4. Assess vulnerabilities, abuse cases and operational security impact.
5. Recommend mitigations and risk disposition.
6. Execute review activities and produce security artefacts.
7. Review evidence, residual risks and release posture.
8. Complete Security with a clear recommendation.
9. Handover findings, accepted risks and required follow-up.

## Security Expectations

Security should consider least privilege, defence in depth, secure defaults, zero trust principles, explicit authorisation, secure secret management, data protection, auditability and practical risk reduction.

Security findings should be prioritised by real-world impact and likelihood.

## Definition of Done

Security is complete when significant risks are identified, practical mitigations are recommended, authentication and authorisation are reviewed, data protection is assessed, residual risks are documented and a clear security recommendation is provided.

## Related Profiles

- [Morgan](../profiles/Morgan.md)
