# Handover Commands

> Part of the **[Engineering Workflow](README.md)**.

## Purpose

Handover commands provide concise prompts that help a role produce the right artefact for the next lifecycle stage.

## Guidance

Commands should be short, explicit and role-oriented.

They should ask for an artefact, not a transcript summary.

### Product to Architecture

Use when discovery is complete.

```text
Produce a Product Brief for Architecture using the standard Nestgrid Engineering artefact template. Include goals, non-goals, scope, requirements, constraints, assumptions, risks, acceptance criteria and open questions.
```

### Architecture to Engineering

Use when solution design is complete.

```text
Produce an Architecture Pack for Engineering using the standard Nestgrid Engineering artefact template. Include context, architectural decisions, boundaries, domain model, API strategy, data strategy, operational considerations, risks and open questions.
```

### Engineering to Quality

Use when implementation is ready for validation.

```text
Produce an Implementation Report for Quality using the standard Nestgrid Engineering artefact template. Include scope, completed work, implementation decisions, tests written, known limitations, risks and outstanding work.
```

### Engineering to Security

Use when implementation is ready for security review.

```text
Produce an Implementation Report for Security using the standard Nestgrid Engineering artefact template. Highlight authentication, authorisation, data handling, validation, dependencies, configuration and known security-sensitive decisions.
```

### Quality to Release

Use when testing has been completed.

```text
Produce a Release Readiness Report using the standard Nestgrid Engineering artefact template. Include coverage, executed tests, defects, regression risks, outstanding issues, evidence and release recommendation.
```

### Security to Release

Use when security review has been completed.

```text
Produce a Security Assessment using the standard Nestgrid Engineering artefact template. Include scope, findings, severity, impact, mitigations, accepted risks and release recommendation.
```

### Platform to Operations

Use when deployment and production readiness have been assessed.

```text
Produce an Operational Readiness Review using the standard Nestgrid Engineering artefact template. Include deployment process, configuration, observability, health checks, rollback, recovery, operational risks and production recommendation.
```

## Key Takeaways

- Ask for artefacts, not conversation summaries.
- Handover commands should be concise and specific.
- Each command should name the target consumer.
- Commands should use the standard artefact templates.

## Related Reading

- [04 Handover Process](04%20Handover%20Process.md)
- [Engineering Artefacts](../16%20Engineering%20Artefacts/README.md)

---

## Navigation

**Previous**

- [05 Review Gates](05%20Review%20Gates.md)

**Next**

- [Engineering Artefacts](../16%20Engineering%20Artefacts/README.md)

**Book**

- [Engineering Workflow](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
