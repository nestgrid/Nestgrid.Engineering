# Hotfix

## Purpose

Define the standard workflow for urgent corrective work.

## Participants

1. Software Engineer
2. Quality Engineer
3. Security Engineer or Platform Engineer where relevant
4. Independent Reviewer where time permits
5. Project Sponsor

## Flow

```text
Problem Confirmation
  -> Minimal Fix
  -> Focused Verification
  -> Risk Review
  -> Release
  -> Post-fix Follow-up
```

## Required Inputs

- Incident, defect or urgent issue summary.
- Affected repository.
- Known production risk.
- Relevant logs, test failures or reproduction steps.

## Expected Outputs

- Fix summary.
- Focused tests.
- Risk assessment.
- Release note or incident follow-up where appropriate.
- Deferred clean-up initiative where the hotfix introduces debt.

## Approval Gates

- Project Sponsor approval is required when the hotfix affects production behaviour, data integrity, security, availability or customer-facing workflows.

## Notes

Hotfixes optimise for rapid risk reduction. They should not become a way to bypass the Engineering Operating System permanently.
