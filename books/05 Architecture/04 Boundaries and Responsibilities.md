# Boundaries and Responsibilities

> Part of the **[Architecture](README.md)**.

## Purpose

Boundaries and responsibilities define how the solution is divided into coherent parts and what each part owns.

They help teams control complexity, reduce coupling and preserve the intent of the domain model.

## Guidance

Architecture should create boundaries that make the solution easier to understand, change, test and operate.

Boundaries may appear between systems, services, modules, components, layers, contexts or teams.

### Align with Domain Boundaries

Domain boundaries should influence technical boundaries.

Bounded contexts, aggregate boundaries and language differences provide important signals, but they should be balanced with operational and delivery concerns.

### Qualify Capability Modules

Capability-first modularisation is an architectural option, not a default.

A capability module should normally represent an enduring business concept or customer capability that owns meaningful behaviour, rules and change. It should not be created merely because an operation, workflow, entity or collection of files deserves a folder.

Useful qualification signals include:

- a coherent business language;
- identifiable business rules or invariants;
- clear responsibilities and boundary ownership;
- meaningful inputs and outputs;
- independent change, testing or ownership value; and
- reduced coupling or improved discoverability when separated.

Capability modules should normally be named after the enduring business concept or customer capability that owns the behaviour. Avoid naming modules after a single operation, workflow, implementation detail or generic label such as `Management`.

The absence of these signals is a reason to keep the behaviour within the existing logical or layered structure, not to manufacture a module.

### Define Clear Responsibilities

Each architectural element should have a clear responsibility.

Unclear responsibility leads to duplicated logic, conflicting ownership and fragile dependencies.

### Manage Dependencies

Dependencies should point in deliberate directions.

Teams should avoid dependency structures that make core domain logic depend unnecessarily on infrastructure, presentation or external systems.

### Protect Core Behaviour

Important domain rules and behaviours should be protected from accidental coupling.

Architecture should make it difficult to bypass business rules or spread them across unrelated parts of the solution.

### Keep Boundaries Reviewable

Boundaries should be revisited when the model, team structure, deployment needs or operational constraints change.

Architecture should evolve when boundaries no longer support clarity or maintainability.

## Key Takeaways

- Boundaries help control complexity and coupling.
- Domain boundaries should influence technical boundaries.
- Capability modules should represent meaningful enduring capabilities, not arbitrary folders.
- Module names should reflect the business capability or concept that owns the behaviour.
- Responsibilities should be clear and owned.
- Dependencies should be intentional.
- Core domain behaviour should be protected.
- Boundaries should evolve when they stop helping.

## Related Reading

- [03 Architectural Style](03%20Architectural%20Style.md)
- [05 Data Architecture](05%20Data%20Architecture.md)

---

## Navigation

**Previous**

- [03 Architectural Style](03%20Architectural%20Style.md)

**Next**

- [05 Data Architecture](05%20Data%20Architecture.md)

**Book**

- [Architecture](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
