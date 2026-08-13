# Lifecycle Mini Sample

This sample demonstrates how the Nestgrid Engineering Operating System can be applied to a small fictional product and to a scoped product initiative.

It is intentionally lightweight. It is not a complete application, product repository or replacement for the Engineering Operating System. Its purpose is to show the shape of the work, the relationship between roles and the durable records that survive a conversation.

## Scenario

The fictional product is **Team Tasks**, a simple tool for small teams to capture tasks, assign responsibility and track completion.

The sample uses a small product so the methodology remains visible. The same lifecycle can be applied to a library, API, web application, console tool, service or mobile application. The operational artefacts change with the product type; the engineering responsibilities do not.

## The Complete EOS Flow

The sample demonstrates the current proportionate lifecycle:

```text
Opportunity Exploration (when the idea is uncertain)
  -> Product Discovery
  -> Architecture
  -> Engineering
  -> Quality
  -> Security
  -> Platform and Operationalisation
  -> Release
```

An initiative may stop, defer, use an existing solution, be reframed or become an existing-product change during Opportunity Exploration. It does not need to produce downstream artefacts unless it proceeds.

Independent Review is a risk-based, cross-cutting activity. It is represented by `docs/reviews/` at product scope and by an initiative `reviews/` directory where a review belongs only to that initiative.

## EOS Building Blocks

The sample applies the same separation used by the full repository:

- **Books** define methodology and standards.
- **Templates** define the shape of reusable artefacts.
- **Roles** define canonical responsibilities and handovers.
- **Profiles** provide named implementations of roles when agents are used.
- **Workflows** define repeatable paths and participating roles.
- **Reviews** provide independent assurance where risk justifies it.
- **Samples** demonstrate how the system is applied.
- **Decisions and initiatives** preserve the operating system's own evolution.

The sample is deliberately product documentation rather than an embedded copy of these operating-system resources. Use the links below to move from the example to the authoritative guidance.

## Sample Contents

`/docs/handbooks` contains concise product knowledge and a local explanation of the workflow. It is not a copy of the global books.

`/docs/artefacts` shows the seven standard lifecycle directories and the artefacts each stage owns.

`/docs/decisions` contains enduring product decisions. Initiative-specific decisions remain with the initiative until they become enduring product knowledge.

`/docs/reviews` is the product-level home for independent reviews. Reviews are durable engineering evidence and should be read by relevant downstream roles.

`/docs/initiatives` contains scoped lifecycle runs for features, enhancements, migrations and other material engineering work.

## Sample Handbook

1. [Philosophy](docs/handbooks/01%20Philosophy.md)
2. [Language](docs/handbooks/02%20Language.md)
3. [Discovery](docs/handbooks/03%20Discovery.md)
4. [Domain Modelling](docs/handbooks/04%20Domain%20Modelling.md)
5. [Architecture](docs/handbooks/05%20Architecture.md)
6. [Decisions](docs/handbooks/06%20Decisions.md)
7. [Engineering Workflow](docs/handbooks/07%20Engineering%20Workflow.md)
8. [Operationalisation](docs/handbooks/08%20Operationalisation.md)
9. [Engineering Standards](docs/handbooks/09%20Engineering%20Standards.md)

These pages demonstrate how a product repository can record its own knowledge while linking back to the global guidance.

## Artefacts and Records

- [Artefact structure](docs/artefacts/README.md)
- [Decision index](docs/decisions/README.md)
- [Review guidance](docs/reviews/README.md)
- [Initiative index](docs/initiatives/README.md)
- [Multi-Currency initiative](docs/initiatives/2026-08-multi-currency/README.md)

The initiative is a compact example of a feature following the same lifecycle as a product, with proportionate artefacts at each stage.

## Authoritative Guidance

- [Roles](../../roles/README.md)
- [Profiles](../../profiles/README.md)
- [Workflows](../../workflows/README.md)
- [Artefact Templates](../../templates/artefacts/README.md)
- [Engineering Operating System Context](../../ENGINEERING-CONTEXT.md)

## What This Sample Does Not Do

The sample does not include `src/` or `tests/`. During pure Discovery and Architecture, a repository may remain documentation-first. Those directories become required when Engineering begins, but adding empty folders here would imply that implementation has started.

The sample also does not prescribe one technology, hosting model or deployment target. Product type and approved architecture determine the concrete operational package.

## Navigation

**Samples Guidance**

- [Samples](../../books/14%20Samples/README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)
- [Engineering Context](../../ENGINEERING-CONTEXT.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
