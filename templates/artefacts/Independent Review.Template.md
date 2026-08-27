# Independent Review

Use one canonical Independent Review document for each review scope or review series. Update that document for follow-up reviews rather than creating a separate "latest" document for every pass.

Use a stable scope-based filename, for example:

```text
docs/reviews/Finance Architecture Independent Review.md
docs/initiatives/2026-08-001-finance-read-model/reviews/Read Model Independent Review.md
```

The review date and version belong in the document metadata. Do not use the date as the identity of the review document.

```yaml
title:
eos_version:
review_series_id:
version:
status:
owner: Independent Reviewer
contributors:
produced_by: Review
consumed_by: Product Owner, Solution Architect, Software Engineer, Quality Engineer, Security Engineer, Platform Engineer, Project Sponsor
date:
supersedes:
review_scope:
review_stage:
review_type: Initial | Follow-up | Targeted | Exit
recommendation: Proceed | Proceed with conditions | Revise | Pause | Stop
next_review_trigger:
related_decisions:
related_work_items:
related_repositories:
related_artefacts:
```

## Review Identity and Versioning

`review_series_id` remains stable for the scope being reviewed. `version` increments whenever the review is updated after new evidence, a follow-up review or a material change in finding disposition.

The current document is the authoritative state. The Review History records what changed between versions, while repository history preserves the exact prior document contents.

Do not renumber an existing finding because its status changes. Stable finding IDs allow roles, decisions, actions and later reviews to refer to the same concern.

## Purpose

Summarise the purpose and scope of the independent review.

## Overall Assessment

Provide a concise current assessment of the repository, lifecycle stage, artefacts or implementation reviewed. State what may proceed, what must wait and why.

## Scope and Evidence Reviewed

List the artefacts, source areas, tests, decisions, environments, review versions and lifecycle stages reviewed.

- Item 1

## Strengths

List meaningful strengths that should be preserved.

- Strength 1

## Current Findings Register

This is the canonical current register. Keep resolved findings visible for traceability, but make their status explicit.

| ID | Severity | Finding | Impact | Required Response | Owner Role | Status | Evidence or Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IR-001 |  |  |  |  |  | Open |  |

Use stable IDs such as `IR-001`. Severity describes the concern; status describes its current disposition.

Recommended statuses:

- `Open` - requires a response or action.
- `In Progress` - the responsible role is actively addressing it.
- `Resolved` - the concern has been addressed and evidence is recorded.
- `Accepted` - the risk remains and an authorised owner has accepted it.
- `Deferred` - the work is intentionally postponed with a reason and review point.
- `Not Applicable` - new evidence shows that the finding does not apply.
- `Superseded` - a later finding or decision replaces it.

## Finding Dispositions

Record the responsible role's response separately from Sentinel's observation. Link material architectural, product, security, operational or risk decisions.

| ID | Disposition | Rationale | Owner | Evidence | Decision or Action Link | Date |
| --- | --- | --- | --- | --- | --- | --- |
| IR-001 |  |  |  |  |  |  |

The distinction is important:

- A **finding** records what the Independent Reviewer observed.
- A **disposition** records what the responsible role decided to do.
- A **decision record** preserves why a material choice was made.
- An **action** records work still required.
- **Evidence** demonstrates completion or supports acceptance.

## Lifecycle Feedback

Summarise lifecycle concerns, readiness observations or stage-transition risks.

## Engineering Handbook Feedback

Capture reusable handbook improvements separately from product-specific findings.

## Deferred or Accepted Risks

List risks that have been accepted or deferred. Link the relevant disposition and review point.

| Risk | Reason | Owner | Authority | Review Date | Status |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Follow-up Actions

List actions for the responsible roles. The action register may link to PBIs, initiatives, decisions or implementation artefacts.

| Action | Owner Role | Target Stage | Status | Evidence | Due or Review Date |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Review History

Append one row for each material review update. Do not overwrite the history when the current findings change.

| Version | Date | Review Type | Scope or Evidence Change | Finding Changes | Recommendation |
| --- | --- | --- | --- | --- | --- |
| 0.1 |  | Initial |  |  |  |

## Overall Recommendation

State the current recommended next step.

Examples:

- Proceed.
- Proceed with conditions.
- Address findings before handover.
- Continue to the next validation stage but do not approve release.
- Pause and resolve blockers.
- Stop.

The recommendation is not a release approval. The responsible gate owner retains approval authority.

## Next Review

State whether another Independent Review is needed, what evidence should be available and what event triggers it.
