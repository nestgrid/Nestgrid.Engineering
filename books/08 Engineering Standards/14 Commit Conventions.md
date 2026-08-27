# Commit Conventions

> Part of the **[Engineering Standards](README.md)**.

## Purpose

Commit messages should make the owning engineering responsibility visible in the repository history.

## Standard Format

Use:

```text
[Prefix] Capitalised title
```

The prefix represents the engineering responsibility owning the change, not merely the Profile or person performing the commit.

## Responsibility Prefixes

| Responsibility | Prefix |
| --- | --- |
| Product | `[Product]` |
| Architecture | `[Architecture]` |
| Engineering | `[Engineering]` |
| Quality | `[Quality]` |
| Security | `[Security]` |
| Platform | `[Platform]` |
| Independent Review | `[Review]` |
| EOS governance, methodology, workflow, orchestration, templates and policy | `[Governance]` |

## Examples

```text
[Architecture] Record package dependency decision
[Engineering] Clarify serializer support boundary
[Quality] Extend result mapping regression coverage
[Security] Document dependency provenance risk
[Platform] Add release validation workflow
[Review] Update release readiness findings
[Governance] Add Engineering Room orchestration model
```

## Guidance

- Use one responsibility prefix per commit.
- Choose the responsibility that owns the change's purpose.
- Use `[Governance]` for changes to the EOS itself.
- Keep the title concise, specific and capitalised.
- Do not use a Profile name as the prefix.

## Key Takeaways

- Commit history should reveal who owns the change by responsibility.
- EOS maintenance uses `[Governance]`.
- The convention supports human, agent and automated contributors equally.

## Related Reading

- [Contribution Guidance](../../CONTRIBUTING.md)
- [Roles and Responsibilities](../15%20Engineering%20Workflow/02%20Roles%20and%20Responsibilities.md)

---

## Navigation

**Previous**

- [13 Implementation Planning](13%20Implementation%20Planning.md)

**Next**

- [Testing](../09%20Testing/README.md)

**Book**

- [Engineering Standards](README.md)
