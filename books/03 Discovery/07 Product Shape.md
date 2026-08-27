# Product Shape

> Part of the **[Discovery](README.md)**.

## Purpose

Product shape describes the product characteristic that may influence later architectural organisation.

It is a Discovery concern, not a technical architecture decision.

## Guidance

Discovery should consider whether the product is expected to remain one cohesive capability or evolve as a composition of multiple independently meaningful customer or business capabilities.

This consideration helps Architecture understand the likely shape of the product without prescribing projects, assemblies, services or a particular architectural style.

### Cohesive Product

A product may be a single cohesive capability with one dominant language, workflow and change boundary.

For these products, a traditional layered physical structure is often the appropriate default while preserving the logical responsibilities of Clean Architecture.

### Composed Product

A product may bring together multiple independently meaningful capabilities.

This may justify Architecture considering a capability-first physical organisation, such as a modular monolith, if the benefits outweigh the additional boundary and coordination cost.

### Ask Product Questions

Where relevant, Discovery should explore:

- What customer or business capabilities does the product provide?
- Is there one dominant capability or several meaningful capabilities?
- Which capabilities are expected to change independently?
- Are different capabilities likely to have different ownership, language or priorities?
- Is the product expected to remain one deployable product?

The answers are product evidence for Architecture. They do not determine the physical solution structure.

## Product Brief

Where this consideration is material, record it in the Product Brief under a section such as **Product Shape**.

The section should capture the observed product characteristic, supporting evidence and uncertainty, without selecting a technical architecture.

## Key Takeaways

- Product shape is a product characteristic, not an architectural decision.
- Discovery should identify whether a product is cohesive or composed of meaningful capabilities.
- A composed product does not automatically require modularisation.
- Architecture uses the product-shape evidence when selecting physical organisation.

## Related Reading

- [04 Requirements](04%20Requirements.md)
- [Architecture](../05%20Architecture/03%20Architectural%20Style.md)
- [Product Brief Template](../../templates/artefacts/Product%20Brief.Template.md)

---

## Navigation

**Previous**

- [06 Scope and Priorities](06%20Scope%20and%20Priorities.md)

**Next**

- [Domain Modelling](../04%20Domain%20Modelling/README.md)

**Book**

- [Discovery](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)

