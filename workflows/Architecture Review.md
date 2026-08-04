# Architecture Review

## Purpose

Define the standard workflow for reviewing Architecture before Engineering begins.

## Participants

1. Gideon
2. Sentinel
3. Commander

## Flow

```text
Architecture Pack
  -> Sentinel Review
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

- Sentinel Review.
- Architecture feedback where required.
- Updated Architecture Pack or accepted deferrals.
- Commander approval before Engineering.

## Approval Gates

- Architecture should not proceed to Engineering until material Sentinel findings are resolved, accepted or explicitly deferred.

## Notes

Sentinel does not replace Gideon. Sentinel independently tests whether the Architecture is clear, coherent and ready for implementation.
