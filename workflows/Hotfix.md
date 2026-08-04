# Hotfix

## Purpose

Define the standard workflow for urgent corrective work.

## Participants

1. Mason
2. Harper
3. Morgan or Rowan where relevant
4. Sentinel where time permits
5. Commander

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

- Commander approval is required when the hotfix affects production behaviour, data integrity, security, availability or customer-facing workflows.

## Notes

Hotfixes optimise for rapid risk reduction. They should not become a way to bypass the Engineering Operating System permanently.
