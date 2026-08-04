# Readability

> Part of the **[Engineering Standards](README.md)**.

## Purpose

Readability ensures that code can be understood by engineers beyond the original author.

Readable code reduces maintenance cost, review effort and the risk of incorrect changes.

## Guidance

Code is read more often than it is written. It should communicate intent clearly and avoid unnecessary mental overhead.

Readable code is not simply code that works. It is code that explains itself through structure, naming and focused behaviour.

### Express Intent

Names, types, functions and modules should reveal purpose.

A reader should be able to understand what the code represents before studying every implementation detail.

### Keep Units Focused

Functions, classes and modules should have clear responsibilities.

Large or mixed-purpose units are harder to test, review and change safely.

### Prefer Simple Control Flow

Control flow should be easy to follow.

Deep nesting, hidden side effects and clever shortcuts should be avoided unless they deliver clear value.

### Use Comments Carefully

Comments should explain why something is done when the reason is not obvious.

Comments should not compensate for unclear names, poor structure or avoidable complexity.

### Optimise for Future Readers

Code should be written for the person who will maintain it later.

That person may not have the same context as the original author.

## Key Takeaways

- Readable code communicates intent.
- Focused units are easier to understand and change.
- Simple control flow reduces mistakes.
- Comments should explain useful context, not restate code.
- Future maintainers are part of the audience.

## Related Reading

- [03 Consistency](03%20Consistency.md)
- [06 Code Review](06%20Code%20Review.md)

---

## Navigation

**Previous**

- [01 Technology Baseline](01%20Technology%20Baseline.md)

**Next**

- [03 Consistency](03%20Consistency.md)

**Book**

- [Engineering Standards](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
