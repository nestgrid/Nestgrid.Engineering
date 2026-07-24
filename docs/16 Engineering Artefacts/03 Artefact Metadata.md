# Artefact Metadata

> Part of the **[Engineering Artefacts](README.md)**.

## Purpose

Metadata makes artefacts versionable, reviewable and traceable.

## Guidance

Each engineering artefact should begin with a short metadata block.

The metadata should be accurate enough to identify ownership, status and relationships without creating unnecessary overhead.

## Standard Metadata

```yaml
title:
version:
status:
owner:
contributors:
produced_by:
consumed_by:
date:
supersedes:
related_decisions:
related_work_items:
related_repositories:
```

## Status Values

Use simple status values.

- Draft
- In Review
- Approved
- Superseded
- Rejected

## Versioning

Use version numbers when an artefact is expected to evolve.

Example:

```text
v0.1 Draft
v1.0 Approved
v1.1 Minor update
v2.0 Major revision
```

## Key Takeaways

- Metadata should appear at the start of each artefact.
- Status values should be consistent.
- Versioning should reflect meaningful change.
- Related artefacts should be linked where possible.

## Related Reading

- [05 Artefact Lifecycle](05%20Artefact%20Lifecycle.md)
- [Decision Records](../06%20Decisions/01%20Decision%20Records.md)

---

## Navigation

**Previous**

- [02 Standard Artefacts](02%20Standard%20Artefacts.md)

**Next**

- [04 Repository Storage](04%20Repository%20Storage.md)

**Book**

- [Engineering Artefacts](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
