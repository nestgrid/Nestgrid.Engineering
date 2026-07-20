# Decisions

This directory contains decision records for significant choices made throughout the engineering lifecycle.

Decision records preserve context, rationale, alternatives and consequences so future readers can understand why decisions were made.

## Recommended Location

Decision records should live with the product documentation structure chosen by the repository.

Recommended locations are:

- `docs/handbooks/06 Decisions/`
- `docs/decisions/`

Choose one location and link to it consistently.

Start with all records directly in the chosen decision location. If the number of records grows, organise them into `adr/`, `bdr/`, `pdr/` and `tdr/` subdirectories.

## Decision Types

- `BDR` - Business Decision Record.
- `PDR` - Product Decision Record.
- `TDR` - Technical Decision Record.
- `ADR` - Architectural Decision Record.

## Decision Status

- `Proposed` - Under consideration.
- `Accepted` - Current agreed direction.
- `Deprecated` - No longer recommended for new work.
- `Superseded` - Replaced by a later decision.
- `Rejected` - Considered but not chosen.

## Records

| ID | Title | Type | Status | Date |
| --- | --- | --- | --- | --- |
| `<PREFIX-000>` | `<Decision title>` | `<Type>` | `<Status>` | `<YYYY-MM-DD>` |

## Guidance

Use [Decision.Template.md](Decision.Template.md) when creating a new decision record.

Decision records should be concise, specific and honest about trade-offs.

---

## Navigation

**Engineering Lifecycle**

- [Engineering Lifecycle](../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../README.md)
