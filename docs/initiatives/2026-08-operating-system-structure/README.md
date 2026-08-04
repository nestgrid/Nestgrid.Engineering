# Operating System Structure

This initiative captures the repository restructure that formalises Nestgrid Engineering Operating System as more than a handbook.

## Context

The agents, handbook, templates, samples, decisions and initiatives now operate together as one engineering operating system.

Before this initiative, the handbook books lived directly under `docs/` and the Engineering Agents lived outside the repository. That made the operating model harder to discover and version as one system.

## Objective

Move Engineering Agents into the repository, move canonical handbook books into `handbook/`, and leave `docs/` for operating-system decisions and initiatives.

## Scope

- Move Engineering Agent documents into `agents/`.
- Move handbook books into `handbook/`.
- Preserve product repository guidance that product handbooks live under `docs/handbooks/`.
- Update links and navigation.
- Rebrand the repository as Nestgrid Engineering Operating System.
- Record the structural decision.

## Outputs

- [ADR-002: Adopt Engineering Operating System Structure](../../decisions/ADR-002-adopt-engineering-operating-system-structure.md)
- [Implementation Report](artefacts/03%20Implementation/Implementation%20Report.md)

## Status

Complete.

## Navigation

**Initiatives**

- [Initiatives](../README.md)

**Repository**

- [Nestgrid Engineering Operating System](../../../README.md)
