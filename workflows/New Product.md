# New Product

## Purpose

Define the standard workflow for taking a new product from initial discovery through release readiness.

New Product begins after a positive Opportunity Decision or an explicit Project Sponsor decision that the opportunity should be formally defined as a product or library.

## Participants

1. Product Owner
2. Independent Reviewer
3. Solution Architect
4. Independent Reviewer
5. Software Engineer
6. Independent Reviewer
7. Quality Engineer
8. Security Engineer
9. Platform Engineer
10. Independent Reviewer
11. Project Sponsor

## Flow

```text
Opportunity Decision
  -> Discovery
  -> Discovery Review
  -> Architecture
  -> Architecture Review
  -> Engineering
  -> Engineering Review
  -> Quality
  -> Security
  -> Platform
  -> Release Readiness Review
  -> Project Sponsor Approval
```

## Required Inputs

- Positive Opportunity Decision, or explicit Project Sponsor direction to define a new product or library.
- Engineering Operating System.
- Relevant existing organisational constraints.

## Expected Outputs

- Product Brief.
- Architecture Handover.
- Architecture Recommendation.
- Architecture Pack.
- Decision records where required.
- Implementation Plan.
- Implementation Report.
- Test Strategy.
- Security Assessment.
- Deployment Guide or Operational Readiness Review.
- Release Report.
- Independent Reviews where review evidence is required.

## Approval Gates

- Product Definition approval before Architecture.
- Architecture recommendation approval before Architecture execution.
- Engineering recommendation approval before implementation.
- Final release approval by the Project Sponsor.

## Notes

Not every new product requires every artefact at full depth. Artefact depth should be proportionate to product complexity and risk.
