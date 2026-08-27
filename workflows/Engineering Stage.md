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
Engineering Readiness Assessment
  -> Implementation Plan
  -> Architecture conformance confirmation where required
  -> Implementation
  -> Engineering Review
  -> Quality
  -> Security
  -> Platform
  -> Project Sponsor Decision
```

## Required Inputs

- Approved Architecture Pack.
- Approved physical solution organisation and module boundaries, where applicable.
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

- The Software Engineer should proceed after readiness and conformance are confirmed when the work remains within the authorised boundary.
- Sponsor approval is required only for a reserved decision or where the assignment explicitly requires it.
- Material independent review findings should be resolved, accepted or deferred before Quality handover.

## Notes

This workflow is also suitable for significant product enhancements where the full new-product workflow would be excessive.
