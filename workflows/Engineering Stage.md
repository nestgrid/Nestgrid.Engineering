# Engineering Stage

## Purpose

Define the standard workflow for moving approved Architecture into implementation.

## Participants

1. Mason
2. Sentinel
3. Harper
4. Morgan
5. Rowan
6. Commander

## Flow

```text
Implementation Recommendation
  -> Approval
  -> Implementation
  -> Engineering Review
  -> Quality
  -> Security
  -> Platform
  -> Commander Decision
```

## Required Inputs

- Approved Architecture Pack.
- Relevant decision records.
- Existing Sentinel reviews.
- Engineering Handbook.
- Product repository.

## Expected Outputs

- Implementation Plan.
- Implementation decisions where needed.
- Production code.
- Automated tests.
- Implementation Report.
- Sentinel Review where review evidence is required.

## Approval Gates

- Mason should wait for approval before moving beyond Recommend.
- Material Sentinel findings should be resolved, accepted or deferred before Quality handover.

## Notes

This workflow is also suitable for significant product enhancements where the full new-product workflow would be excessive.
