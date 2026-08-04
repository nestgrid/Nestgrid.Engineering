# Domain Modelling

> Part of the **[Lifecycle Mini Sample](../../README.md)**.

## Purpose

Domain modelling turns the discovery findings into a small model of the sample problem space.

The model captures the core concepts, rules and boundaries needed before architecture is chosen.

## Guidance

The sample has one simple bounded context: task coordination.

This does not mean the final software must have one technical module forever. It means the current domain language and rules are coherent enough to model together.

### Bounded Context

`Task Coordination`

This context owns the meaning of tasks, assignees, statuses and due dates.

### Core Concepts

`Task`

A piece of work that needs to be completed.

`Assignee`

The person currently responsible for the task.

`Status`

The current state of the task.

### Value Objects

`TaskTitle`

Represents the short description of the task.

`DueDate`

Represents the expected completion date when one is provided.

### Aggregate

`Task` is the aggregate root.

It protects rules about title, assignee, status and completion.

### Invariants

- A task must have a title.
- A completed task cannot be moved back to a new state without an explicit reopen action.
- A task can have at most one assignee at a time.

### Domain Events

- `TaskCreated`
- `TaskAssigned`
- `TaskCompleted`

## Key Takeaways

- A small product can still benefit from explicit modelling.
- Aggregate boundaries follow rules, not database tables.
- Domain events capture meaningful changes.

## Related Reading

- [Architecture](05%20Architecture.md)
- [Domain Modelling Guidance](../../../../handbook/04%20Domain%20Modelling/README.md)

---

## Navigation

**Previous**

- [Discovery](03%20Discovery.md)

**Next**

- [Architecture](05%20Architecture.md)

**Sample**

- [Lifecycle Mini Sample](../../README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../../../README.md)
