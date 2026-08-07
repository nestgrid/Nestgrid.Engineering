# Review Gates

> Part of the **[Engineering Workflow](README.md)**.

## Purpose

Review gates define the points where work should be checked before moving to the next lifecycle stage.

## Guidance

Review gates should improve clarity and confidence without becoming unnecessary bureaucracy.

Where Independent Reviews exist, review gates should consider unresolved independent review findings.

Findings do not automatically block progress, but they should be resolved, accepted or explicitly deferred.

### Discovery Gate

The Discovery Gate has two distinct checkpoints. Do not use the Product Definition checkpoint to force an early idea into a Product Brief.

#### Checkpoint 1: Opportunity Decision

Opportunity Exploration is ready to conclude when the idea, problem, affected users, desired change, assumptions, uncertainty and relevant alternatives have been explored proportionately.

Valid outcomes:

- Pursue as a new product or library.
- Pursue as an existing-product change.
- Reframe or research further.
- Use an existing solution.
- Defer.
- Stop because nothing should be built.

Only the first outcome proceeds to New Product Discovery. The final five outcomes do not require a Product Brief or Architecture Handover.

Record an Opportunity Decision only when durable rationale or follow-up is useful.

Primary artefact:

- Opportunity Decision

#### Checkpoint 2: Product Definition

Product Definition is ready for Architecture when product intent, goals, scope, requirements, constraints and open questions are documented.

Primary artefact:

- Product Brief

Final handover artefact:

- Architecture Handover

### Architecture Gate

Architecture is ready for Engineering when system boundaries, key decisions, risks, trade-offs and implementation guidance are documented.

Architecture should normally pass through a lightweight Recommend checkpoint before Execute.

The recommendation should summarise the proposed architectural direction, key architectural decisions, principal risks and trade-offs, proposed Architecture artefacts and approval to proceed.

Primary artefact:

- Architecture Pack

Pre-execution checkpoint:

- Architecture Recommendation

### Engineering Gate

Engineering is ready for Quality and Security when the implementation is complete enough to validate and the implementation decisions are documented.

Primary artefact:

- Implementation Report

### Quality Gate

Quality is ready for release consideration when requirements have been validated, regression risk is understood and a release recommendation exists.

Primary artefact:

- Release Readiness Report

### Security Gate

Security is ready for release consideration when significant security risks have been identified, mitigated or accepted.

Primary artefact:

- Security Assessment

### Platform Gate

Platform is ready for release consideration when operationalisation, deployment, monitoring, rollback and support procedures are documented and repeatable.

Primary artefact:

- Operational Readiness Review

### Release Gate

Release is ready to proceed when Quality, Security and Platform recommendations are available, unresolved findings are dispositioned and the Project Sponsor has approved release.

Primary artefact:

- Release Report

## Key Takeaways

- Review gates should protect delivery quality.
- Each gate should have a clear primary artefact.
- Gates should scale with risk and complexity.
- Review should produce clear approval, feedback or deferral.
- Release approval belongs to the Project Sponsor.
- Independent review findings should have clear disposition where they affect stage readiness.

## Related Reading

- [03 Lifecycle Flow](03%20Lifecycle%20Flow.md)
- [Engineering Artefacts](../16%20Engineering%20Artefacts/README.md)

---

## Navigation

**Previous**

- [04 Handover Process](04%20Handover%20Process.md)

**Next**

- [06 Handover Commands](06%20Handover%20Commands.md)

**Book**

- [Engineering Workflow](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
