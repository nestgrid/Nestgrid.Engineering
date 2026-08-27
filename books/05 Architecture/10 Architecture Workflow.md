# Architecture Workflow

> Part of the **[Architecture](README.md)**.

## Purpose

Architecture workflow defines how Architecture moves from approved Discovery input to approved architectural artefacts.

It prevents substantial Architecture documentation from being produced before the architectural direction has been reviewed and accepted.

## Guidance

Architecture should proceed through five steps:

1. Review
2. Understand
3. Assess
4. Recommend
5. Execute

Architecture should clarify material uncertainty before producing substantial artefacts.

The Solution Architect should not silently fill important gaps that could reasonably be clarified with the Project Sponsor.

The depth of each step should be proportionate to the size, risk and uncertainty of the product or initiative.

### Review

Architecture should review the approved Discovery inputs.

Typical inputs include:

- Product Brief
- Architecture Handover
- Discovery assumptions
- Open questions
- Known risks

### Understand

Architecture should understand the product intent, business capabilities, constraints, quality needs and important domain concepts before proposing a solution.

The goal is shared understanding, not premature design.

Where the approved Discovery artefacts leave material uncertainty, Architecture should use focused conversation to clarify drivers, constraints, priorities and assumptions before proceeding.

Some open questions may still remain, but they should be explicit and intentional.

### Assess

Architecture should assess architectural drivers, quality attributes, boundaries, data, integrations, security, operations, risks and trade-offs.

This assessment should distinguish logical responsibilities from physical organisation. Architecture should consider whether the product is cohesive or composed of meaningful capabilities, but should select physical boundaries only where they provide clear architectural value.

This assessment should identify where decisions are needed and where assumptions may affect architecture.

### Recommend

Architecture should produce a lightweight recommendation before substantial Architecture artefacts are created.

The recommendation should include:

- Proposed architectural direction
- Key architectural decisions
- Principal risks and trade-offs
- Proposed Architecture artefacts
- Approval gate before Execute

The Architecture Recommendation should be concise and should support approval to proceed.

### Execute

Once the recommendation is approved, Architecture should produce the agreed Architecture artefacts.

Typical outputs include:

- Architecture Pack
- Architecture Decision Records
- The selected physical solution organisation and its rationale.
- Qualified capability modules and their boundaries, where applicable.
- Technical risk notes
- Architecture feedback where upstream clarification is needed

## Key Takeaways

- Architecture should not jump straight from Discovery input to detailed documentation.
- Architecture should clarify material uncertainty before turning assumptions into artefacts.
- The Recommend checkpoint provides directional approval before Execute.
- Architecture Recommendation should be lightweight.
- Architecture Pack and related decisions are produced during Execute.
- The workflow should scale with the significance and risk of the work.

## Related Reading

- [01 Architectural Drivers](01%20Architectural%20Drivers.md)
- [02 Quality Attributes](02%20Quality%20Attributes.md)
- [09 Architecture Validation](09%20Architecture%20Validation.md)
- [Architecture Recommendation Template](../../templates/artefacts/Architecture%20Recommendation.Template.md)
- [Architecture Pack Template](../../templates/artefacts/Architecture%20Pack.Template.md)

---

## Navigation

**Previous**

- [09 Architecture Validation](09%20Architecture%20Validation.md)

**Next**

- [Decisions](../06%20Decisions/README.md)

**Book**

- [Architecture](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
