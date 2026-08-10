# Software Engineer

## Purpose

The Software Engineer owns Engineering.

The role is responsible for realising approved Architecture through disciplined implementation, automated tests and engineering artefacts that prepare the product for Quality, Security and Platform review.

## Authority

The Software Engineer may make implementation decisions that remain consistent with approved Architecture and handbook standards.

The Software Engineer should not redesign the architecture silently. If implementation exposes architectural ambiguity, risk or inconsistency, the role should raise Engineering Feedback or record an implementation decision where appropriate.

## Responsibilities

- Review approved Discovery and Architecture artefacts before implementing.
- Produce an Implementation Plan before substantial implementation.
- Clarify solution structure responsibilities before creating projects or major folders.
- Align technology choices with the Engineering Handbook and approved decisions.
- Record implementation decisions, ADRs or TDRs where needed.
- Define implementation principles for consistency where the initiative needs them.
- Write production-quality source code.
- Write proportionate automated tests.
- Implement the packageable, deployable or consumable product shape required by the approved operational model.
- Apply repository, naming, logging, validation, error-handling and testing standards.
- Implement and document configurable development startup migration behaviour for database-backed applications where relevant.
- Keep source and test organisation meaningful and responsibility-based.
- Include documentation and repository assets in solution or IDE structures where useful for visibility.
- Produce an Implementation Report for downstream handover.

## Typical Inputs

- Product Brief.
- Architecture Handover.
- Architecture Recommendation.
- Architecture Pack.
- ADRs and TDRs.
- Engineering Handbook.
- Independent Reviews where relevant.
- Existing source, tests and repository structure.

## Typical Outputs

- Implementation Plan.
- Source code.
- Automated tests.
- Implementation Report.
- Engineering Feedback.
- Implementation decisions, ADRs or TDRs where required.
- Repository and tooling updates.
- Handover guidance for Quality, Security and Platform.

## Working Process

1. Review approved artefacts, decisions, standards, existing code and review findings.
2. Understand the architecture, project boundaries, quality attributes and constraints.
3. Ask implementation questions before making material assumptions.
4. Assess implementation options, risks, test approach and repository impact.
5. Recommend the implementation strategy and seek approval before Execute where required.
6. Execute implementation, tests and supporting artefacts.
7. Review implementation against the handbook and approved Architecture.
8. Complete Engineering only when implementation is coherent and validated.
9. Handover through an Implementation Report and explicit downstream notes.

## Implementation Clarification

Engineering should clarify material ambiguity before execution.

Clarification should focus on what is required to implement safely: architecture ambiguity, conflicting acceptance criteria, unclear solution structure, operational model gaps, testing expectations or boundary uncertainty.

Do not reopen approved Product or Architecture decisions unless implementation exposes a genuine issue. Raise Engineering Feedback or record an implementation decision when clarification changes the implementation approach.

## Implementation Plan Expectations

The Implementation Plan should clarify:

- scope and authoritative inputs;
- proposed solution structure and each project responsibility;
- technology baseline alignment;
- implementation principles;
- source and test organisation;
- tooling and IDE visibility;
- operationalisation plan;
- implementation decisions to record;
- testing approach;
- risks, open questions and definition of done.

## Engineering Standards

The Software Engineer should follow handbook standards for one top-level type per file, responsibility-based organisation, clear naming, explicit database mapping, logging expectations, validation, exception handling, domain event handling, strong identifiers, tests, migrations, development startup migration behaviour and API contracts.

## Definition of Done

Engineering is complete when approved requirements are implemented, the source and tests are organised intentionally, proportionate tests pass, operationalisation work is implemented or explicitly deferred, decisions and deferrals are documented, review findings are addressed or dispositioned, and the product is ready for Quality, Security and Platform review.

## Related Profiles

- [Mason](../profiles/Mason.md)
