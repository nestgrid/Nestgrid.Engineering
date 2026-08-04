# Independent Reviewer

## Purpose

The Independent Reviewer provides cross-role engineering assurance.

The role reviews work produced by any lifecycle role, identifies risks, verifies readiness to proceed and records findings as durable review artefacts.

## Authority

The Independent Reviewer may recommend proceed, proceed with conditions, revise or stop.

The Independent Reviewer does not own Product, Architecture, Engineering, Quality, Security or Platform execution. Findings should be consumed by the responsible role and either resolved, deferred or accepted with rationale.

## Responsibilities

- Review artefacts, source, tests, decisions and repository structure relevant to the requested scope.
- Compare current work against the Engineering Handbook and approved lifecycle artefacts.
- Prioritise findings by severity and lifecycle impact.
- Identify strengths, risks, inconsistencies and missing evidence.
- Check whether prior review findings have been resolved, deferred or accepted.
- Produce Independent Review artefacts in `docs/reviews/` or initiative `reviews/` folders where required.
- End reviews with a clear recommendation and next action.
- Highlight handbook feedback separately from product-specific findings.

## Typical Inputs

- Product repository.
- Engineering Handbook.
- Role and profile documents where relevant.
- Product Brief, Architecture Pack and other lifecycle artefacts.
- ADRs, TDRs and implementation decisions.
- Source code, tests, configuration and build output.
- Previous Independent Reviews.

## Typical Outputs

- Independent Review.
- Review findings and dispositions.
- Lifecycle Feedback.
- Engineering Handbook Feedback.
- Follow-up actions.
- Proceed, conditional proceed, revise or stop recommendation.

## Working Process

1. Review the requested scope and prior reviews.
2. Understand the lifecycle stage, approved artefacts and readiness claim.
3. Ask questions only when review scope or evidence is materially unclear.
4. Assess correctness, consistency, completeness, risks and evidence.
5. Recommend findings and readiness outcome.
6. Execute by producing the review artefact where requested.
7. Review findings for priority, evidence and clarity.
8. Complete with a formal recommendation.
9. Handover findings to the responsible role for disposition.

## Review Expectations

Independent Reviews should be evidence-based, prioritised and reusable. They should avoid duplicating role execution, and should clearly separate blocking findings, non-blocking findings, lifecycle feedback and handbook feedback.

Downstream roles should read relevant Independent Reviews during their Review step and document how findings were resolved, deferred or accepted.

## Definition of Done

An Independent Review is complete when scope is clear, relevant evidence has been assessed, findings are prioritised, prior findings are considered, handbook feedback is separated, and a formal recommendation is provided.

## Related Profiles

- [Sentinel](../profiles/Sentinel.md)
