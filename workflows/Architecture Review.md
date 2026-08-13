# Architecture Review

## Purpose

Define the standard workflow for reviewing Architecture before Engineering begins.

## Participants

1. Solution Architect
2. Independent Reviewer
3. Project Sponsor

## Flow

```text
Architecture Pack
  -> Independent Review (create or update canonical review)
  -> Architecture Feedback
  -> Revision or Approval
```

## Required Inputs

- Product Brief.
- Architecture Handover.
- Architecture Recommendation.
- Architecture Pack.
- Relevant decision records.

## Expected Outputs

- Independent Review.
- Architecture feedback where required.
- Updated Architecture Pack or accepted deferrals.
- Project Sponsor approval before Engineering.

The Independent Review should identify the canonical review document, current version, finding dispositions and recommendation used by the gate.

## Approval Gates

- Architecture should not proceed to Engineering until material independent review findings are resolved, accepted or explicitly deferred.

## Notes

Independent Review does not replace Architecture. It tests whether the Architecture is clear, coherent and ready for implementation.
