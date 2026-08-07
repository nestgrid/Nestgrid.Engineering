# Commandable Engineering Operating System

This initiative captures the future direction for making the Nestgrid Engineering Operating System easier to invoke through standard commands and prompts.

## Context

The Nestgrid Engineering Operating System is currently readable and executable by humans or agents who understand the methodology.

It defines books, roles, profiles, workflows, templates, artefacts, decisions, initiatives and review expectations.

Comparing the EOS with agent workflow toolkits such as GStack highlighted a useful distinction:

- GStack is strong as an immediate agent workflow and command layer.
- Nestgrid EOS is stronger as an engineering methodology, artefact system and organisational operating model.

The opportunity is to learn from the command-driven ergonomics without reducing the EOS to a prompt pack.

## Objective

Define a future command layer that makes the EOS easier to run manually today and prepares it for a future Runner.

The command layer should make lifecycle actions easier to invoke consistently while preserving the role-based, artefact-led methodology.

## Scope

- Identify canonical EOS commands and prompts.
- Keep commands role-based rather than tied to named profiles.
- Ensure commands can be used manually before automation exists.
- Design commands so a future Runner could execute them deterministically.
- Preserve artefact discipline, approval gates and review loops.
- Avoid implementing the Runner in this initiative.

## Candidate Commands

Initial command candidates include:

- `start-opportunity`
- `run-discovery`
- `architecture-recommend`
- `architecture-execute`
- `engineering-plan`
- `engineering-execute`
- `quality-review`
- `security-review`
- `platform-readiness`
- `sentinel-review`
- `release-check`

Command names are provisional.

They should be refined against real product usage before becoming handbook standards.

## Relationship to Runner

The commandable EOS is a stepping stone toward the Engineering Operating System Runner.

The likely evolution is:

```text
Written EOS
  -> Commandable EOS
  -> Runnable EOS
  -> Orchestrated EOS
```

The written EOS defines the methodology.

The commandable EOS defines standard invocations.

The runnable EOS allows a tool to inspect a repository, select workflows, invoke roles, create artefacts and manage gates.

The orchestrated EOS coordinates multiple roles, profiles and Independent Reviews with reduced Project Sponsor involvement until approval is required.

## Open Questions

- Should commands live in `workflows/`, `prompts/`, `commands/` or another top-level directory?
- Should commands be written as prompt samples, structured workflow files or both?
- Should command names be tool-neutral or optimised for a specific runner interface?
- How much repository inspection should a command expect before producing output?
- Which commands require Project Sponsor approval gates?

## Status

Proposed.

## Artefacts

- [Discovery Note](artefacts/01%20Discovery/Discovery%20Note.md)

## Navigation

**Related Initiative**

- [Engineering Operating System Runner](../2026-08-engineering-operating-system-runner/README.md)

**Initiatives**

- [Initiatives](../README.md)

**Repository**

- [Nestgrid Engineering Operating System](../../../README.md)
