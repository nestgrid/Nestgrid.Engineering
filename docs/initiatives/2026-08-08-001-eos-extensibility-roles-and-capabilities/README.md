# EOS Extensibility: Roles and Capabilities

This initiative captures future evolution ideas for broadening the Nestgrid Engineering Operating System beyond Nestgrid's internal delivery model while keeping the EOS lean, role-based and platform-independent.

## Context

The EOS has crossed an important threshold.

It is no longer only documentation for how Nestgrid works. It is becoming a general Engineering Operating System that has been proven by Nestgrid first.

The current core roles cover engineering delivery well:

- Product Owner
- Solution Architect
- Software Engineer
- Quality Engineer
- Security Engineer
- Platform Engineer
- Independent Reviewer
- Project Sponsor

As the EOS moves toward open source use and possible commercial tooling, it should support broader organisational needs without becoming heavy or technology-specific.

## Objective

Capture candidate future roles, cross-cutting concerns and capability concepts that may make the EOS more useful to other organisations and future Runner-style execution.

This initiative should preserve the direction without forcing premature adoption.

## Scope

This initiative considers:

- optional specialist roles;
- cross-cutting engineering concerns;
- capabilities or skills as reusable execution units;
- relationship to the Commandable EOS and Runner initiatives;
- and how to keep the EOS broadly useful without adding unnecessary process.

This initiative does not immediately add new roles, profiles, books, workflows or templates.

## Candidate Roles

### Product Designer

Product Design is the strongest near-term candidate.

This role would not be only "UI" or "UX". It would own product experience where human interaction materially affects success.

Possible responsibilities:

- user journeys;
- information architecture;
- interaction design;
- accessibility;
- usability;
- design systems;
- prototypes;
- experience acceptance criteria;
- and experience review.

This role may not be needed for every product. It is likely unnecessary for backend libraries or low-level infrastructure, but valuable for user-facing products such as Finance, portals, dashboards, mobile applications, developer tools and complex command-line experiences.

Possible profile names include Iris or Nova.

### Technical Writer

Technical Writing becomes valuable for open source, SDKs, APIs, libraries, onboarding-heavy products and commercial tooling.

Possible responsibilities:

- tutorials;
- onboarding;
- API documentation;
- package and installation guidance;
- examples;
- user-facing release notes;
- and documentation quality review.

This should remain optional unless documentation becomes a material product requirement.

### Data Engineer

Data Engineering may be needed for products with analytical, reporting, event, telemetry, projection or warehousing concerns.

Possible responsibilities:

- projections;
- analytics pipelines;
- reporting models;
- ETL;
- data quality;
- warehouse integration;
- and analytical operational concerns.

This is a different mindset from Software Engineering and should be introduced only where product needs justify it.

### Performance Engineer

Performance Engineering may be needed when products reach meaningful scale or have demanding latency, throughput, memory, storage or cost constraints.

Possible responsibilities:

- performance modelling;
- load testing;
- profiling;
- capacity analysis;
- bottleneck investigation;
- optimisation recommendations;
- and performance regression evidence.

This should be specialist and risk-based, not mandatory.

### Developer Experience Engineer

Developer Experience may be valuable if Nestgrid and external adopters build libraries, SDKs, CLIs, plugins or internal developer platforms.

Possible responsibilities:

- consumer ergonomics;
- quick-starts;
- samples;
- package usability;
- local development experience;
- contribution flow;
- and developer-facing documentation.

This role may overlap with Product Design and Technical Writing, so boundaries would need Discovery before adoption.

### Data Protection or Compliance Specialist

Data Protection and Compliance may become important for regulated, privacy-sensitive or audit-heavy products.

Possible responsibilities:

- data classification;
- retention;
- privacy impact;
- auditability;
- compliance evidence;
- regulatory constraints;
- and risk acceptance guidance.

This could be a role or a cross-cutting concern depending on organisational maturity.

### Site Reliability Engineer

Site Reliability Engineering is related to Platform but not identical.

Platform makes products deployable and operationally ready. SRE may own reliability targets, production feedback loops, SLOs, capacity, incident learning and resilience improvement.

This should be considered later, especially for products with demanding production availability expectations.

## Cross-Cutting Concerns

Some ideas may be better expressed as guidance rather than roles.

Candidate concerns include:

- Operationalisation;
- Observability;
- Performance;
- Accessibility;
- Localisation;
- Privacy;
- Compliance;
- Resilience;
- Cost efficiency;
- Developer experience;
- and documentation quality.

These concerns should flow through Discovery, Architecture, Engineering, Quality, Security and Platform where relevant.

They should not all become mandatory lifecycle stages.

## Capability and Skills Model

The EOS may eventually need a capability layer between roles/profiles and Runner execution.

The Runner should not need to know "Evelyn" or "Mason" directly.

It should be able to execute a capability such as:

- produce Product Brief;
- produce Architecture Pack;
- review repository;
- review ADRs;
- review logging;
- review solution structure;
- review tests;
- review security;
- review deployment;
- execute Platform readiness.

Profiles define behaviour.

Roles define responsibility.

Capabilities define reusable actions.

The Runner eventually coordinates capabilities through roles and profiles.

## What Not To Add

The EOS should avoid technology-specific roles such as:

- UI Agent;
- Database Agent;
- API Agent;
- React Agent;
- EF Agent.

Those are implementation technologies or areas of expertise, not durable engineering operating-system roles.

Technology-specific guidance belongs in standards, samples, implementation decisions or product documentation.

## Relationship to Existing Initiatives

This initiative relates to:

- [Commandable Engineering Operating System](../2026-08-commandable-engineering-operating-system/README.md)
- [Engineering Operating System Runner](../2026-08-engineering-operating-system-runner/README.md)
- [Operationalisation](../2026-08-operationalisation/README.md)
- [Roles and Profiles Separation](../2026-08-roles-and-profiles-separation/README.md)

## Recommendation

Do not add all candidate roles immediately.

The strongest near-term role candidate is Product Designer.

The strongest near-term capability concepts are Skills and a reusable capability model, but these should be explored after the Commandable EOS direction matures.

The EOS should broaden carefully: add optional specialist roles and cross-cutting concerns only when real product usage proves the need.

## Status

Proposed.

## Artefacts

- [Discovery Note](artefacts/01%20Discovery/Discovery%20Note.md)

## Navigation

**Initiatives**

- [Initiatives](../README.md)

**Repository**

- [Nestgrid Engineering Operating System](../../../README.md)
