# Roles and Profiles Separation

This initiative captures the final structural refinement that separates canonical roles from named profiles.

## Context

The Engineering Operating System had already adopted role-based methodology, but the profile documents still lived under `agents/`.

That structure made it less obvious that roles are canonical and profiles are implementations. It also risked placing too much responsibility guidance in named profiles, forcing humans or future automation to read profile documents to understand role ownership.

## Objective

Create top-level `roles/` and `profiles/` directories, move named profile documents into `profiles/`, and add canonical role documents under `roles/`.

## Scope

- Move existing named agent documents into `profiles/`.
- Add canonical role documents with enough guidance for humans, profiles or automation to perform the role.
- Update prompt samples to reference both `/engineering/roles/` and `/engineering/profiles/`.
- Update repository structure documentation.
- Record the structural decision.

## Outputs

- [ADR-005: Adopt Roles and Profiles Separation](../../decisions/ADR-005-adopt-roles-and-profiles-separation.md)
- [Implementation Report](artefacts/03%20Implementation/Implementation%20Report.md)

## Status

Complete.

## Navigation

**Initiatives**

- [Initiatives](../README.md)

**Repository**

- [Nestgrid Engineering Operating System](../../../README.md)
