# Runner Vision

```yaml
title: Engineering Operating System Runner
version: 0.2
status: Proposed
owner: Nestgrid Engineering
contributors:
  - Project Sponsor
  - Codex
produced_by: Product Owner
consumed_by: Project Sponsor, Solution Architect, Software Engineer
date: 2026-08-07
supersedes:
related_decisions:
related_work_items:
related_repositories:
  - engineering
```

## Context

The Nestgrid Engineering Operating System defines the methodology for moving engineering work through roles, workflows, artefacts, decisions, reviews and approval gates.

Today, the Project Sponsor manually orchestrates much of that flow.

The Runner vision explores how the EOS could eventually become executable: a system that can inspect repository state, select workflows, assign roles, invoke profiles, manage artefacts, request Independent Reviews and pause for approval gates.

This is future capability work, not current implementation scope.

## Objective

Define the long-term direction for an Engineering Operating System Runner without turning the vision into premature handbook doctrine or delivery work.

The Runner should eventually reduce manual handover effort while preserving the EOS principles of role accountability, artefact traceability, review discipline and Project Sponsor approval.

## Scope

The Runner vision covers:

- workflow orchestration;
- role and profile assignment;
- artefact creation and validation;
- review-loop coordination;
- approval gate management;
- repository state inspection;
- lifecycle progress tracking;
- and handover between lifecycle stages.

The Runner vision does not currently cover:

- implementation technology;
- hosting model;
- user interface;
- integration contracts;
- agent runtime selection;
- or automation of Project Sponsor approval.

## Vision

The future Runner should allow roles and profiles to collaborate with one another without requiring the Project Sponsor to manually copy context between every stage.

The Project Sponsor should become involved when direction, risk, approval or arbitration is required, not for routine handover mechanics.

The target experience is:

```text
Project Sponsor starts or approves work
  -> Runner selects the workflow
  -> Runner invokes the responsible role or profile
  -> Role produces or updates artefacts
  -> Independent Reviewer reviews the output
  -> Responsible role addresses, defers or accepts findings
  -> Runner repeats the review loop where needed
  -> Runner pauses for Project Sponsor approval at the gate
```

## Evolution Path

The Runner should not be implemented before the EOS is sufficiently stable through real product use.

The likely evolution is:

```text
Written EOS
  -> Commandable EOS
  -> Runnable EOS
  -> Orchestrated EOS
```

### Written EOS

The current state.

Books, roles, profiles, workflows, templates, artefacts, decisions and initiatives define how engineering work should proceed.

### Commandable EOS

The next likely step.

Standard commands or prompts make lifecycle actions easier to invoke consistently while still being executed manually.

Examples:

- `start-opportunity`
- `run-discovery`
- `architecture-recommend`
- `engineering-plan`
- `sentinel-review`
- `release-check`

### Runnable EOS

A Runner can inspect a repository, identify lifecycle state, select a workflow, create missing artefact folders, invoke the right role and check expected outputs.

### Orchestrated EOS

The Runner coordinates multiple roles, profiles and Independent Reviews, only pausing when approval, risk acceptance or strategic direction is required.

## Example Review Loop

```text
Software Engineer completes implementation
  -> Independent Reviewer reviews implementation
  -> Software Engineer resolves, accepts or defers findings
  -> Independent Reviewer reviews again
  -> Runner records review outcome
  -> Runner pauses for Project Sponsor approval
```

The Project Sponsor is no longer reviewing routine handbook compliance, naming, folder structure, logging or test gaps by default.

Those responsibilities should already be discharged by the responsible role and Independent Reviewer.

The Project Sponsor reviews direction, intent, risk, trade-offs and approval readiness.

## Candidate Capabilities

A future Runner may need to:

- inspect repository structure;
- read lifecycle status from artefacts;
- determine the current workflow stage;
- identify missing required artefacts;
- select the responsible role;
- select an approved profile where applicable;
- construct role-specific prompts;
- create artefact directories;
- run validation checks;
- request Independent Reviews;
- track review findings;
- resume after findings are resolved;
- and pause at approval gates.

## Relationship to Commandable EOS

The Runner should build on the Commandable EOS initiative.

Commandable EOS defines standard invocations.

Runner executes or coordinates those invocations.

The command layer should be validated manually before a Runner attempts to automate it.

## Relationship to Independent Review

Independent Review is central to the Runner vision.

The Runner should be able to route completed work to an Independent Reviewer and return findings to the responsible role.

Findings should be resolved, accepted or explicitly deferred before the Runner proceeds to approval.

## Open Questions

- What minimal repository state must the Runner understand?
- Should the Runner execute workflows from Markdown, structured data or both?
- How should approval gates be represented?
- How should review findings be tracked across cycles?
- How should the Runner distinguish between product-level and initiative-level work?
- Which validation checks should be built in first?
- How should the Runner operate when human specialists, AI profiles and automation are mixed?

## Recommendation

Do not implement the Runner yet.

Continue refining the written EOS through real products.

Design and validate the Commandable EOS first.

Return to the Runner when manual orchestration becomes the bottleneck and the command catalogue is stable enough to automate.

## Navigation

**Related Initiative**

- [Commandable Engineering Operating System](../2026-08-commandable-engineering-operating-system/README.md)

**Initiative**

- [Engineering Operating System Runner](README.md)

**Repository**

- [Nestgrid Engineering Operating System](../../../README.md)
