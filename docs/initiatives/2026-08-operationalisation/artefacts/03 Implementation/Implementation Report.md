# Implementation Report

```yaml
title: Operationalisation
version: 1.0
status: Complete
owner: Nestgrid Engineering
contributors:
  - Codex
produced_by: Software Engineer
consumed_by: Product Owner, Solution Architect, Quality Engineer, Security Engineer, Platform Engineer, Project Sponsor
date: 2026-08-06
supersedes:
related_decisions:
  - ADR-007
related_work_items:
related_repositories:
  - engineering
```

## Scope

Updated the Nestgrid Engineering Operating System to treat operationalisation as a cross-cutting lifecycle concern.

## Files Changed

- Roles updated for Product Owner, Solution Architect, Software Engineer, Quality Engineer, Security Engineer and Platform Engineer.
- Profiles updated for Evelyn and Rowan.
- Product Brief, Architecture Pack, Implementation Plan, Test Strategy, Security Assessment, Deployment Guide and Operational Readiness Review templates updated.
- Discovery, Engineering Workflow and Deployment books updated.
- New Operationalisation chapter added to Deployment.
- ADR-007 and this initiative record added.

## Links Updated

- Deployment navigation now links Rollback and Recovery to Operationalisation before Operations.
- Decision and initiative indexes now include operationalisation records.

## Inconsistencies Corrected

- Operational concerns were previously split between non-functional requirements, Architecture operational considerations and Platform readiness.
- The EOS now distinguishes functional requirements, quality attributes and operational requirements.

## Recommendation

Future product and initiative discovery should explicitly capture operational requirements proportionate to product type and risk.
