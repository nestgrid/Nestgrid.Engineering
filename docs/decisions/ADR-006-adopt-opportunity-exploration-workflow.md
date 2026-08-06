# ADR-006: Adopt Opportunity Exploration Workflow

> Decision record for **Architecture**.

## Status

Accepted

## Type

Architecture

## Date

2026-08-05

## Owners

- Nestgrid Engineering Operating System maintainers

## Context

The Product Owner role and Evelyn profile were strengthened so Discovery can begin as collaborative exploration rather than document production.

That clarified behaviour, but the operating system still implied that new product work begins with Product Discovery and a Product Brief.

Some ideas should become products or libraries. Some should become features of existing products. Some should be researched further, deferred, solved with existing tools or stopped entirely.

The methodology needs an explicit entry workflow for deciding whether an opportunity deserves engineering work before product artefacts are created.

## Decision

Adopt Opportunity Exploration as the standard entry workflow for early ideas and observed problems.

Opportunity Exploration precedes formal New Product Discovery unless the Project Sponsor has already explicitly decided that a new product or library should be defined.

Valid Opportunity Decision outcomes are:

- Pursue as a new product or library.
- Pursue as an existing-product change.
- Reframe or research further.
- Use an existing solution.
- Defer.
- Stop because nothing should be built.

The Opportunity Decision artefact is optional. It should be used when the evidence, rationale or follow-up should endure.

## Rationale

This keeps Discovery honest.

It avoids forcing early ideas into Product Briefs before there is enough shared understanding.

It also recognises that a no-build decision can be a successful Product Owner outcome.

## Alternatives Considered

### Keep Opportunity Exploration Inside Product Owner Guidance Only

This was rejected because prompts and workflows could still push the Product Owner straight into Product Brief production.

### Require an Opportunity Decision for Every Idea

This was rejected because informal brainstorming should remain lightweight. Durable artefacts should be created only when the rationale needs to be preserved.

## Consequences

New Product work should normally begin after a positive Opportunity Decision.

The Discovery Gate now has two checkpoints: Opportunity Decision and Product Definition.

The Product Brief remains the approved Product Definition artefact for opportunities that proceed.

Prompt samples should support collaborative Opportunity Exploration before Product Brief production.

## Related Decisions

- [ADR-004: Adopt Role-Based Methodology](ADR-004-adopt-role-based-methodology.md)
- [ADR-005: Adopt Roles and Profiles Separation](ADR-005-adopt-roles-and-profiles-separation.md)

## Related Documentation

- [Opportunity Exploration](../../workflows/Opportunity%20Exploration.md)
- [Product Owner](../../roles/Product%20Owner.md)
- [Evelyn](../../profiles/Evelyn.md)
- [Review Gates](../../books/15%20Engineering%20Workflow/05%20Review%20Gates.md)

---

## Navigation

**Decision Index**

- [Decisions](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)

