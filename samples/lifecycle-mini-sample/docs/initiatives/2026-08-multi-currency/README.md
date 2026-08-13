# 2026-08 Multi-Currency

This sample initiative demonstrates how a scoped engineering effort can follow the same proportionate lifecycle as a product.

The initiative is intentionally lightweight. It shows structure rather than a complete delivery record.

## Structure

```text
artefacts/
  01 Discovery/
  02 Architecture/
  03 Implementation/
  04 Quality/
  05 Security/
  06 Platform/
  07 Release/
decisions/
reviews/
```

## Lifecycle

The Project Sponsor approved this as a significant enhancement to Team Tasks. The roles and representative outputs are:

```text
Product Owner
  Product Brief and Architecture Handover
    -> Solution Architect
       Architecture Recommendation, Architecture Pack and decisions
      -> Software Engineer
         Implementation Plan, implementation, tests and Engineering Assurance
        -> Quality Engineer
           Test Strategy and release readiness evidence
          -> Security Engineer
             Security Assessment
            -> Platform Engineer
               Deployment Guide and Operational Readiness Review
              -> Project Sponsor
                 Release decision and Release Report
```

The Independent Reviewer may review the initiative at any point where the risk or change impact justifies it. The initiative's artefact folders are present to make the expected repository shape visible; the depth and number of documents should remain proportionate.

## Operationalisation

Because Multi-Currency changes an existing product, its operational requirements include:

- upgrading existing data without losing balances;
- validating configuration and supported currencies;
- verifying the feature after deployment;
- documenting rollback or recovery expectations;
- updating user and support documentation.

These requirements are considered during Discovery and Architecture, implemented and tested during Engineering and Quality, reviewed by Security where relevant, and realised by Platform before Release.

## Guidance

Use initiative folders for significant features, enhancements, migrations, platform work and other scoped engineering efforts.

When the initiative completes, enduring product knowledge should be reflected in the product handbook and enduring product decisions should be promoted or linked from `docs/decisions/`.

## Navigation

**Initiatives**

- [Initiatives](../README.md)

**Sample**

- [Lifecycle Mini Sample](../../../README.md)

**Initiative Artefacts**

- [Initiative Artefacts](../../../../../books/16%20Engineering%20Artefacts/07%20Initiative%20Artefacts.md)

**Engineering Workflow**

- [Engineering Workflow](../../../../../books/15%20Engineering%20Workflow/README.md)
