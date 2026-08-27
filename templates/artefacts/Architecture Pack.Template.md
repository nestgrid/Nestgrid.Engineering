# Architecture Pack

```yaml
title:
eos_version:
version:
status:
owner:
contributors:
produced_by: Solution Architect
consumed_by: Software Engineer, Quality Engineer, Security Engineer, Platform Engineer
date:
supersedes:
related_decisions:
related_work_items:
related_repositories:
```

## Context

Summarise the product intent and architectural context.

## Architecture Goals

- Goal 1
- Goal 2
- Goal 3

## Architecture Principles

Capture the core architectural principles that should guide Engineering implementation.

- Principle 1
- Principle 2
- Principle 3

## Quality Attributes

Document the primary quality attributes driving the architecture.

Examples include availability, recoverability, survivability, security, maintainability, portability, observability and performance.

| Quality Attribute | Architectural Implication | Priority |
| --- | --- | --- |
|  |  |  |

## Key Decisions

| Decision | Rationale | Related ADR |
| --- | --- | --- |
|  |  |  |

## Architecture Overview

Describe the proposed solution architecture.

## Logical Architecture

Describe the logical responsibilities and dependency direction, including how Domain, Application, Infrastructure and presentation or delivery concerns are separated where relevant.

## Physical Solution Organisation

Describe how the logical architecture is mapped to projects, assemblies, packages, modules, services or other physical boundaries.

State the selected architectural style and explain why it is appropriate.

The traditional layered physical structure is an appropriate default for cohesive products. If a capability-first organisation is selected, explain the qualified capabilities, their ownership and the value of the physical separation.

## Capability Modules

Where applicable, list each first-class capability module and the enduring business concept or customer capability it represents.

| Module | Owned Capability or Concept | Responsibilities | Boundary Rationale |
| --- | --- | --- | --- |
|  |  |  |  |

## Boundaries and Responsibilities

Describe system boundaries, modules, services or bounded contexts.

## Domain Model

Describe core domain concepts, aggregates, value objects and domain events where relevant.

## API Strategy

Describe APIs, contracts, consumers and compatibility considerations.

## Integration Strategy

Describe external systems, messaging, events and integration responsibilities.

## Data Strategy

Describe data ownership, persistence, migrations and consistency requirements.

## Security Considerations

Describe security-sensitive design decisions and expected controls.

## Operational Considerations

Describe deployment, observability, scaling, resilience and support considerations.

## Operational Model

Describe how the product, library, service or application will be delivered and made usable in its target environment.

Cover where relevant:

- packaging, publication or distribution model;
- installation, deployment or consumption model;
- runtime, hosting or service model;
- configuration and secrets model;
- upgrade, rollback, uninstall and recovery approach;
- operational documentation and validation expectations;
- support and ownership implications.

## Trade-offs

| Trade-off | Decision | Consequence |
| --- | --- | --- |
|  |  |  |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
|  |  |  |

## Open Questions

- Question 1

## Engineering Guidance

Provide implementation guidance for Engineering.

## Recommendation

Summarise the architecture recommendation and readiness for implementation.
