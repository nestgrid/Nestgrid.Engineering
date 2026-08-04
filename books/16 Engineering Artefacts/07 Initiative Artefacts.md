# Initiative Artefacts

> Part of the **[Engineering Artefacts](README.md)**.

## Purpose

Initiative artefacts define how lifecycle outputs are stored for scoped engineering work inside an existing product repository.

## Guidance

The Engineering Lifecycle is not only for whole products.

It applies to any engineering initiative where structured discovery, design, implementation, validation, security review, platform readiness or release evidence is useful.

The scale and quantity of artefacts should be proportionate to the significance and risk of the initiative.

### Initiative Scope

An initiative may be:

- A major feature
- A significant enhancement
- A platform initiative
- A security initiative
- A migration programme
- A material operational change

Small features and bug fixes may not need a full artefact set.

### Storage

Initiative artefacts should live under `docs/initiatives/`.

Use a stable, readable folder name:

```text
docs/
  initiatives/
    <yyyy-mm>-<initiative-name>/
```

Example:

```text
docs/
  initiatives/
    2026-08-multi-currency/
```

### Standard Initiative Structure

```text
docs/
  initiatives/
    <yyyy-mm>-<initiative-name>/
      README.md
      artefacts/
        01 Discovery/
        02 Architecture/
        03 Implementation/
        04 Quality/
        05 Security/
        06 Platform/
        07 Release/
      decisions/
      reviews/
```

Not every initiative requires every artefact directory to contain documents.

The directory structure provides consistency; the content should remain proportionate.

### Product Artefacts

Product-level artefacts should remain in `docs/artefacts/`.

They describe the product as a whole.

Initiative artefacts should not be mixed into product-level artefact folders.

### Decisions

Initiative decisions may start under the initiative's `decisions/` folder.

If a decision becomes enduring product guidance, it should be promoted or linked from `docs/decisions/`.

### Reviews

Initiative-specific Sentinel reviews may live under the initiative's `reviews/` folder.

Product-level Sentinel reviews should remain in `docs/reviews/`.

Relevant initiative reviews should be read by downstream Engineering Agents before continuing initiative work.

### Completion

When an initiative completes:

- Update the product handbook where enduring knowledge has changed.
- Promote or link enduring product decisions.
- Leave initiative artefacts as historical delivery evidence.
- Leave initiative reviews as historical review evidence.
- Record release evidence where appropriate.

## Key Takeaways

- The lifecycle applies to any engineering initiative.
- Artefact depth should be proportionate to significance and risk.
- Initiative artefacts belong under `docs/initiatives/`.
- Product-level artefacts remain under `docs/artefacts/`.
- Initiative reviews belong with the initiative when they are initiative-specific.
- Completed initiative artefacts provide historical evidence.

## Related Reading

- [Repository Storage](04%20Repository%20Storage.md)
- [Lifecycle Flow](../15%20Engineering%20Workflow/03%20Lifecycle%20Flow.md)
- [Starting a Project Repository](06%20Starting%20a%20Project%20Repository.md)

---

## Navigation

**Previous**

- [06 Starting a Project Repository](06%20Starting%20a%20Project%20Repository.md)

**Next**

- [08 New Product Discovery Bootstrap](08%20New%20Product%20Discovery%20Bootstrap.md)

**Book**

- [Engineering Artefacts](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
