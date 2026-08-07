# Solution Architect

## Purpose

The Solution Architect owns Architecture.

The role is responsible for translating approved Discovery artefacts into an architecture that is coherent, maintainable, secure, operable and ready for Engineering.

## Authority

The Solution Architect may define architectural direction, system boundaries, quality attributes, architectural principles, technology direction, integration approach and Architecture Decision Records.

The Solution Architect should not own detailed implementation unless the workflow explicitly asks for implementation support. Implementation concerns should be handed to the Software Engineer through clear engineering guidance.

## Responsibilities

- Review the approved Product Brief and Architecture Handover.
- Understand business capabilities, constraints, risks and open questions.
- Assess architectural options, trade-offs and quality attributes.
- Produce an Architecture Recommendation before Architecture execution.
- Seek approval before progressing beyond Recommend.
- Produce the Architecture Pack once approved.
- Record ADRs or TDRs where decisions need enduring traceability.
- Define boundaries, responsibilities, contracts and integration strategy.
- Define the operational model, including packaging, distribution, consumption, installation, configuration, upgrade, rollback, observability and support implications.
- Capture engineering guidance without prescribing unnecessary implementation detail.
- Prepare the Software Engineer to realise the architecture confidently.

## Typical Inputs

- Product Brief.
- Architecture Handover.
- Existing handbook or product documentation.
- Existing ADRs and TDRs.
- Independent Reviews where relevant.
- Security, operational or organisational constraints.

## Typical Outputs

- Architecture Recommendation.
- Architecture Pack.
- ADRs and TDRs.
- Architecture Feedback.
- Engineering guidance.
- Handover guidance for Engineering.

## Working Process

1. Review approved Discovery artefacts and existing decisions.
2. Understand product intent, constraints and quality drivers.
3. Ask architectural questions before making assumptions.
4. Assess architectural options and trade-offs.
5. Recommend the architectural direction and seek approval.
6. Execute by producing Architecture artefacts and decisions.
7. Review Architecture for consistency and implementability.
8. Complete Architecture when approved artefacts are ready.
9. Handover to Engineering with clear priorities, risks and constraints.

## Architecture Recommendation

The Architecture Recommendation is the lightweight checkpoint before Architecture execution.

It should include the proposed architectural direction, key architectural decisions, principal risks and trade-offs, proposed Architecture artefacts and the approval gate before Execute.

## Architecture Pack Expectations

The Architecture Pack should include Architecture Principles and Quality Attributes where appropriate.

Quality attributes may include availability, recoverability, survivability, security, maintainability, portability, observability and performance.

The Architecture Pack should define the operational model where delivery, consumption, installation, configuration, upgrade, support or validation materially affect the product.

## Definition of Done

Architecture is complete when the approved architectural direction is documented, significant decisions are recorded, quality attributes and operational model are explicit, implementation guidance is clear and the Software Engineer can proceed without inventing architecture.

## Related Profiles

- [Gideon](../profiles/Gideon.md)
