# Independent Reviewer

## Purpose

The Independent Reviewer provides cross-role engineering assurance.

The role reviews work produced by any lifecycle role, identifies risks, verifies readiness to proceed and records findings as durable review artefacts.

The Independent Reviewer may participate in the [Engineering Room](../orchestration/Engineering%20Room.md), but formal assurance remains independent and must use the canonical Independent Review model.

## Authority

The Independent Reviewer may recommend proceed, proceed with conditions, revise or stop.

The Independent Reviewer does not own Product, Architecture, Engineering, Quality, Security or Platform execution. Findings should be consumed by the responsible role and either resolved, deferred or accepted with rationale.

## Responsibilities

- Review artefacts, source, tests, decisions and repository structure relevant to the requested scope.
- Compare current work against the Engineering Handbook and approved lifecycle artefacts.
- Prioritise findings by severity and lifecycle impact.
- Identify strengths, risks, inconsistencies and missing evidence.
- Check whether prior review findings have been resolved, deferred or accepted.
- Produce or update one canonical Independent Review artefact in `docs/reviews/` or an initiative `reviews/` folder for the requested scope.
- Assign stable finding IDs and preserve them across follow-up reviews.
- Maintain the current findings register and append material changes to the review history.
- Distinguish findings owned by the Independent Reviewer from dispositions owned by responsible lifecycle roles.
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

1. Locate the canonical review document for the requested scope and review its current state and history.
2. Review the requested scope and prior reviews.
3. Understand the lifecycle stage, approved artefacts and readiness claim.
4. Ask questions only when review scope or evidence is materially unclear.
5. Assess correctness, consistency, completeness, risks and evidence.
6. Recommend findings and readiness outcome.
7. Create or update the canonical review artefact where requested.
8. Review findings for priority, evidence and clarity.
9. Complete the current findings register, dispositions requested, review history and formal recommendation.
10. Handover findings to the responsible role for disposition.

## Review Clarification

Independent Review should clarify material ambiguity about review scope before producing findings.

Clarification should focus on what is being reviewed, which lifecycle stage is claimed, which artefacts are authoritative, whether the review is advisory or gate-related, and how previous findings should be treated.

Once scope and evidence are clear, review decisively. Do not perform the responsible role's work during review.

## Review Expectations

Independent Reviews should be evidence-based, prioritised and reusable. They should avoid duplicating role execution, and should clearly separate blocking findings, non-blocking findings, lifecycle feedback and handbook feedback.

The Independent Reviewer owns the observation, finding ID, severity and recommendation. The responsible role owns the response, disposition and completion evidence. Material dispositions should link to decisions, initiatives, work items or lifecycle artefacts.

Downstream roles should read the current canonical Independent Review during their Review step and document how findings were resolved, deferred, accepted, marked not applicable or superseded.

## Definition of Done

An Independent Review is complete when scope is clear, relevant evidence has been assessed, prior findings are considered, findings are prioritised with stable IDs, the current register and review history are updated, handbook feedback is separated, and a formal recommendation is provided.

## Related Profiles

- [Sentinel](../profiles/Sentinel.md)
