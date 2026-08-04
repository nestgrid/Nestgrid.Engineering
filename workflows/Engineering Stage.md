# Engineering Stage

## Purpose

Define the standard workflow for moving approved Architecture into implementation.

## Participants

1. Software Engineer
2. Independent Reviewer
3. Quality Engineer
4. Security Engineer
5. Platform Engineer
6. Project Sponsor

## Flow

```text
Implementation Recommendation
  -> Approval
  -> Implementation
  -> Engineering Review
  -> Quality
  -> Security
  -> Platform
  -> Project Sponsor Decision
```

## Required Inputs

- Approved Architecture Pack.
- Relevant decision records.
- Existing Independent Reviews.
- Engineering Handbook.
- Product repository.

## Expected Outputs

- Implementation Plan.
- Implementation decisions where needed.
- Production code.
- Automated tests.
- Implementation Report.
- Independent Review where review evidence is required.

## Approval Gates

- The Software Engineer should wait for approval before moving beyond Recommend.
- Material independent review findings should be resolved, accepted or deferred before Quality handover.

## Notes

This workflow is also suitable for significant product enhancements where the full new-product workflow would be excessive.
