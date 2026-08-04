# Roles

Roles define the canonical engineering disciplines used by the Nestgrid Engineering Operating System.

A role describes responsibility, authority, inputs, outputs, working process, artefacts and handover expectations. It is independent of who performs the work.

Roles are authoritative for lifecycle ownership.

Profiles, humans, automation or mixed teams may fulfil roles, but they should not redefine role responsibilities.

Profiles are named implementations of roles. See [Profiles](../profiles/README.md).

## Standard Roles

| Role | Lifecycle Stage | Primary Question |
| --- | --- | --- |
| [Project Sponsor](Project%20Sponsor.md) | Sponsorship and approval | Should this proceed? |
| [Product Owner](Product%20Owner.md) | Discovery | What should we build? |
| [Solution Architect](Solution%20Architect.md) | Architecture | What is the right solution? |
| [Software Engineer](Software%20Engineer.md) | Engineering | How should it be engineered? |
| [Quality Engineer](Quality%20Engineer.md) | Quality | How do we know it works? |
| [Security Engineer](Security%20Engineer.md) | Security | Can it be trusted? |
| [Platform Engineer](Platform%20Engineer.md) | Platform | Can it reliably serve its users? |
| [Independent Reviewer](Independent%20Reviewer.md) | Review | Is the work ready to proceed? |

## Principles

- Roles are canonical.
- Profiles are optional implementations.
- Workflows coordinate roles.
- Artefacts move work between roles.
- The Project Sponsor owns approval authority.
- Role documents should contain enough guidance for a human or runner to perform the role without reading a named profile.
- Profile documents should provide tone, emphasis and execution style rather than duplicate role ownership.

## Navigation

**Profiles**

- [Profiles](../profiles/README.md)

**Workflows**

- [Workflows](../workflows/README.md)

**Books**

- [Engineering Handbook](../books/README.md)

**Repository**

- [Nestgrid Engineering Operating System](../README.md)
