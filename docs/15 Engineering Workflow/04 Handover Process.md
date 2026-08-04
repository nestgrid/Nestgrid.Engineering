# Handover Process

> Part of the **[Engineering Workflow](README.md)**.

## Purpose

The handover process defines how one role passes work to another without losing context.

## Guidance

A handover should provide enough context for the next role to act without reading the full conversation, meeting notes or private working history.

### Use the Latest Approved Artefact

The latest approved artefact is the primary handover input.

Drafts may be shared for review, but downstream work should normally begin from approved or explicitly accepted artefacts.

### Separate Approval From Handover

Some lifecycle stages have both an approval artefact and a handover artefact.

For Discovery, the Product Brief is the approval artefact.

Once approved, Product should produce an Architecture Handover for Architecture.

The handover should explain what the next role should do, not repeat every detail already captured in the approved artefact.

### Include Metadata

Each artefact should identify its title, version, status, owner, date and related artefacts.

This supports traceability and review.

### Capture Open Questions

Open questions should be visible.

The next role should not have to rediscover uncertainty by accident.

### Escalate With Feedback Artefacts

When a downstream role cannot proceed confidently, it should produce feedback.

Feedback should explain the concern, impact and recommended next action.

### Include Review History

Where Sentinel reviews exist, they should be treated as part of the handover context.

The next Engineering Agent should not need review comments copied from a chat.

Relevant Sentinel reviews should live in `docs/reviews/` or in the relevant initiative's `reviews/` folder.

Open findings should be resolved, accepted or explicitly deferred before a downstream handover depends on them.

## Key Takeaways

- Handovers should not rely on memory.
- Approved artefacts are the primary handover input.
- Approval artefacts and handover artefacts may be separate.
- Metadata supports traceability.
- Sentinel reviews should be included in handover context where they exist.
- Feedback artefacts make blockers visible.

## Related Reading

- [Engineering Artefacts](../16%20Engineering%20Artefacts/README.md)
- [06 Handover Commands](06%20Handover%20Commands.md)

---

## Navigation

**Previous**

- [03 Lifecycle Flow](03%20Lifecycle%20Flow.md)

**Next**

- [05 Review Gates](05%20Review%20Gates.md)

**Book**

- [Engineering Workflow](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
