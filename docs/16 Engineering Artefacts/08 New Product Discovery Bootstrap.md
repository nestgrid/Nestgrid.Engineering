# New Product Discovery Bootstrap

> Part of the **[Engineering Artefacts](README.md)**.

## Purpose

New product Discovery bootstrap defines the minimum documentation set needed when starting a product repository with no existing product handbook or lifecycle artefacts.

It gives Discovery agents and engineers a consistent starting sequence without requiring them to assemble the process from several handbook pages.

## Guidance

New product Discovery should create only enough structure to make the first handover to Architecture clear.

Do not fill every handbook page before the product is understood.

The initial Discovery output should establish repository purpose, product intent, decision traceability and the first durable artefact.

Architecture Handover is the final mandatory artefact produced by Discovery before Architecture begins.

The minimum Discovery bootstrap is intentionally documentation-first.

It does not require empty `src/` or `tests/` folders before Engineering begins.

## Bootstrap Checklist

When bootstrapping Discovery for a new product repository:

1. Create the standard repository documentation structure.
2. Add a root `README.md` that explains the product purpose and current lifecycle state.
3. Add README files to the main documentation folders.
4. Create `docs/decisions/README.md` as the decision index.
5. Create `docs/artefacts/01 Discovery/`.
6. Produce the initial Product Brief from the standard template.
7. Add only the handbook seed pages needed to preserve current understanding.
8. Record open questions, assumptions and risks in the Product Brief.
9. Approve the Product Brief when Discovery is complete.
10. Produce an Architecture Handover as the final act of Discovery.
11. Hand both the Product Brief and Architecture Handover to Architecture.

## Minimum Initial Files

A new product repository should normally start with:

```text
README.md
docs/
  README.md
  handbooks/
    README.md
  artefacts/
    README.md
    01 Discovery/
      Product Brief.md
      Architecture Handover.md
  decisions/
    README.md
  initiatives/
    README.md
```

Additional handbook pages should be created when they contain useful product knowledge, not merely to mirror the global Engineering Handbook.

`src/` and `tests/` should be added when Engineering begins and implementation work is planned.

## Optional Handbook Seeds

For a new product, the following seed pages are often useful:

- Product philosophy or purpose
- Product language and glossary
- Initial Discovery notes
- Initial domain concepts
- Known constraints

These pages should remain brief until the product has enough validated understanding to justify fuller handbook content.

## Feedback to the Engineering Handbook

If product work exposes a gap in the Engineering Handbook, capture the feedback in the product repository first.

Use a Discovery artefact, feedback artefact or initiative note depending on the context.

When the feedback affects reusable Nestgrid Engineering practice, promote it into a central Engineering initiative under `docs/initiatives/` in this repository.

Product work should not be blocked by non-critical handbook improvement feedback unless the gap prevents safe handover.

## Key Takeaways

- New product Discovery should start lean.
- New product Discovery does not require empty `src/` or `tests/` folders.
- `src/` and `tests/` become required when Engineering begins.
- The Product Brief is the Discovery approval artefact.
- The Architecture Handover is the final Discovery handover artefact.
- Decision traceability should exist from the beginning.
- Handbook seed pages should preserve real understanding, not empty structure.
- Reusable handbook feedback should be promoted into a central Engineering initiative.

## Related Reading

- [Starting a Project Repository](06%20Starting%20a%20Project%20Repository.md)
- [Repository Storage](04%20Repository%20Storage.md)
- [Product Brief Template](../../templates/artefacts/Product%20Brief.Template.md)
- [Architecture Handover Template](../../templates/artefacts/Architecture%20Handover.Template.md)
- [Architecture Workflow](../05%20Architecture/10%20Architecture%20Workflow.md)
- [Discovery](../03%20Discovery/README.md)

---

## Navigation

**Previous**

- [07 Initiative Artefacts](07%20Initiative%20Artefacts.md)

**Next**

- [Engineering Workflow](../15%20Engineering%20Workflow/README.md)

**Book**

- [Engineering Artefacts](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
