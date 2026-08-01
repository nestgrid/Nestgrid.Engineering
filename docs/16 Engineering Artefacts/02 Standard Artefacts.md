# Standard Artefacts

> Part of the **[Engineering Artefacts](README.md)**.

## Purpose

Standard artefacts define the expected outputs of each engineering workflow stage.

## Guidance

The standard artefact set should be used as the default across Nestgrid product repositories.

Teams may add specialist artefacts when needed, but should not bypass the standard set without a clear reason.

## Artefact Set

| Stage | Owner | Primary Artefact | Main Consumer |
| --- | --- | --- | --- |
| Discovery | Product | Product Brief / Architecture Handover | Architecture |
| Architecture | Architecture | Architecture Recommendation / Architecture Pack | Engineering |
| Implementation | Engineering | Implementation Plan / Report | Quality, Security |
| Quality | Quality | Test Strategy / Release Readiness Report | Release, Engineering |
| Security | Security | Security Assessment | Release, Engineering, Platform |
| Platform | Platform | Deployment Guide / Operational Readiness Review | Operations, Release |
| Release | Delivery | Release Report | Stakeholders, Operations |

### Feedback Artefacts

Feedback artefacts should be used when a role cannot proceed confidently.

Common examples:

- Product Feedback
- Architecture Feedback
- Engineering Feedback
- Quality Feedback
- Security Feedback
- Operational Feedback

### Template Location

Reusable templates live in:

```text
templates/artefacts/
```

Completed project artefacts should live in the relevant product repository, not in this methodology repository.

### Discovery Approval and Handover

The Product Brief is the Discovery approval artefact.

It answers:

> What have we discovered?

Once the Product Brief is approved, Product should produce an Architecture Handover as the final act of Discovery.

The Architecture Handover answers:

> What should Architecture do next?

Architecture should receive both artefacts:

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
- The Product Brief is the Discovery approval artefact.
- The Architecture Handover is the final Discovery handover to Architecture.
- Architecture Recommendation provides approval before Architecture Execute.
- Feedback artefacts make concerns explicit.
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

- [Nestgrid.Engineering](../../README.md)
