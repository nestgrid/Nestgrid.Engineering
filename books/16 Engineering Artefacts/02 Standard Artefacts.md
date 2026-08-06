# Standard Artefacts

> Part of the **[Engineering Artefacts](README.md)**.

## Purpose

Standard artefacts define the expected outputs of each engineering workflow stage.

## Guidance

The standard artefact set should be used as the default across Nestgrid product repositories.

Teams may add specialist artefacts when needed, but should not bypass the standard set without a clear reason.

## Artefact Set

| Stage | Owner Role | Primary Artefact | Main Consumer Role |
| --- | --- | --- | --- |
| Opportunity Exploration | Product Owner | Opportunity Decision | Project Sponsor |
| Discovery | Product Owner | Product Brief / Architecture Handover | Solution Architect |
| Architecture | Solution Architect | Architecture Recommendation / Architecture Pack | Software Engineer |
| Implementation | Software Engineer | Implementation Plan / Report | Quality Engineer, Security Engineer |
| Quality | Quality Engineer | Test Strategy / Release Readiness Report | Project Sponsor, Software Engineer |
| Security | Security Engineer | Security Assessment | Project Sponsor, Software Engineer, Platform Engineer |
| Platform | Platform Engineer | Deployment Guide / Operational Readiness Review | Project Sponsor, Operations |
| Release | Project Sponsor | Release Report | Stakeholders, Operations |

### Feedback Artefacts

Feedback artefacts should be used when a role cannot proceed confidently.

Common examples:

- Product Feedback
- Architecture Feedback
- Engineering Feedback
- Quality Feedback
- Security Feedback
- Operational Feedback

### Review Artefacts

Review artefacts should be used when independent review adds useful lifecycle evidence.

Independent Review is the standard artefact for independent reviews.

Independent Reviews are recognised but not mandatory.

They may review a lifecycle stage, repository, product, decision, implementation, release readiness or handbook compliance.

Relevant Independent Reviews should be read by downstream roles during their Review step.

Findings should be resolved, accepted or explicitly deferred by the responsible role.

### Template Location

Reusable templates live in:

```text
templates/artefacts/
```

Completed project artefacts should live in the relevant product repository, not in this methodology repository.

### Discovery Approval and Handover

Opportunity Exploration may produce an Opportunity Decision before a Product Brief exists.

The Opportunity Decision answers:

> Does this opportunity deserve engineering work?

It is optional for informal brainstorming and should be created when the evidence, rationale or follow-up should endure.

The Product Brief is the Product Definition approval artefact.

It answers:

> What have we discovered?

Once the Product Brief is approved, the Product Owner should produce an Architecture Handover as the final act of Discovery.

The Architecture Handover answers:

> What should Architecture do next?

The Solution Architect should receive both artefacts:

- Product Brief
- Architecture Handover

The Architecture Handover should be concise and should not repeat the full Product Brief.

### Architecture Recommendation

Architecture Recommendation is a lightweight checkpoint before Architecture executes substantial documentation work.

It answers:

> Are we comfortable with this architectural direction before Architecture produces the full artefact set?

It should include proposed architectural direction, key architectural decisions, principal risks and trade-offs, proposed Architecture artefacts and approval to Execute.

Once approved, Architecture should produce the Architecture Pack and related Architecture Decision Records where needed.

## Key Takeaways

- Each lifecycle stage has a primary artefact.
- Opportunity Decision is optional but recognised before Product Definition.
- The Product Brief is the Product Definition approval artefact.
- The Architecture Handover is the final Discovery handover to Architecture.
- Architecture Recommendation provides approval before Architecture Execute.
- Feedback artefacts make concerns explicit.
- Independent Reviews provide independent review history where used.
- Templates provide consistent structure.
- Completed artefacts belong with the product repository.

## Related Reading

- [04 Repository Storage](04%20Repository%20Storage.md)
- [Templates](../13%20Templates/README.md)

---

## Navigation

**Previous**

- [01 Artefact Purpose](01%20Artefact%20Purpose.md)

**Next**

- [03 Artefact Metadata](03%20Artefact%20Metadata.md)

**Book**

- [Engineering Artefacts](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
