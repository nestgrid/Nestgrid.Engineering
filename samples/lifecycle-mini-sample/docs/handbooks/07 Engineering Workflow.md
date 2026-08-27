# Engineering Workflow

> Part of the **[Lifecycle Mini Sample](../../README.md)**.

## Purpose

This page shows how the sample moves from an idea to a releasable product through role-based collaboration.

Roles describe the engineering discipline. A human or an agent profile may perform the role. The sample does not depend on a particular name or tool.

## Role Flow

```text
Project Sponsor
  -> Product Owner
  -> Solution Architect
  -> Software Engineer
  -> Quality Engineer
  -> Security Engineer
  -> Platform Engineer
  -> Project Sponsor release decision
```

The Independent Reviewer may review any stage where the risk, novelty or change impact justifies independent assurance.

## How Work Moves

Conversation comes before formal documentation when uncertainty is material.

Each role should:

- read the approved inputs and relevant previous reviews;
- investigate available evidence before asking the Sponsor to resolve discoverable facts;
- ask focused questions where product intent or constraints remain unclear;
- challenge assumptions respectfully;
- recommend a proportionate next step;
- produce or update durable artefacts only when the shared understanding is sufficient.

The common reasoning pattern is:

```text
Review -> Explore -> Question -> Investigate -> Challenge
  -> Synthesise -> Recommend -> Confirm boundary -> Execute
  -> Verify -> Complete artefacts -> Handover
```

Routine, reversible work within the approved boundary should not wait for repeated Sponsor approval. Material scope, architecture, standards, risk, cost, production or release decisions remain with the appropriate authority.

## Handover

Chats support thinking. Approved artefacts, decisions and reviews preserve engineering state.

Typical handovers are:

```text
Product Brief + Architecture Handover
  -> Architecture Recommendation + Architecture Pack
  -> Implementation Plan + Implementation Report + Engineering Assurance
  -> Test Strategy + Release Readiness Report
  -> Security Assessment
  -> Deployment Guide + Operational Readiness Review
  -> Release Report
```

The receiving role should pick up from the repository state rather than requiring conversation history to be copied into a new discussion.

## Related Reading

- [Discovery](03%20Discovery.md)
- [Architecture](05%20Architecture.md)
- [Operationalisation](08%20Operationalisation.md)
- [Engineering Workflow](../../../../books/15%20Engineering%20Workflow/README.md)

---

## Navigation

**Previous**

- [Decisions](06%20Decisions.md)

**Next**

- [Operationalisation](08%20Operationalisation.md)

**Sample**

- [Lifecycle Mini Sample](../../README.md)

**Repository**

- [Nestgrid Engineering Operating System](../../../../README.md)
