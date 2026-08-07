# Lifecycle Flow

> Part of the **[Engineering Workflow](README.md)**.

## Purpose

Lifecycle flow defines the normal movement of work from idea to production readiness.

## Guidance

The workflow applies to any engineering initiative, regardless of scope.

The scale and quantity of artefacts should be proportionate to the significance and risk of the initiative.

The workflow should be adapted to the size and risk of the work, but the default flow is:

1. Product discovers what should be built and why.
2. Product captures functional, quality and operational requirements.
3. Architecture defines how the solution should be designed and operationalised.
4. Engineering implements the approved design and operational model.
5. Quality validates behaviour, release confidence and operational scenarios.
6. Security assesses risk, mitigation and operational security.
7. Platform realises the operational package and readiness model.
8. Release records the final release decision, evidence and accepted risks.

### Standard Flow

```text
Product
  -> Architecture
  -> Engineering
  -> Quality
  -> Security
  -> Platform
  -> Release
```

### Feedback Loops

Downstream roles may send feedback upstream when an artefact is incomplete, ambiguous or risky.

Feedback should be captured explicitly rather than handled as silent redesign.

Examples:

- Engineering sends Engineering Feedback to Architecture when a design is impractical.
- Quality sends Quality Feedback to Engineering when test gaps or defects are found.
- Security sends Security Feedback to Architecture or Engineering when risk requires design or code changes.
- Platform sends Operational Feedback when deployment or support concerns are discovered.

### Operationalisation Flow

Operationalisation is the process of making the engineered product deliverable and usable in its intended environment.

It applies to every product type, including libraries, services, APIs, web applications, workers, command-line tools and mobile applications.

The concern flows through the lifecycle:

```text
Product captures operational requirements
  -> Architecture designs the operational model
  -> Engineering implements the packageable, deployable or consumable shape
  -> Quality validates operational scenarios
  -> Security reviews operational security
  -> Platform realises publication, installation, deployment and readiness
```

Platform owns final operationalisation, but should not be discovering the operational strategy for the first time at the end of the lifecycle.

### Release Ownership

Platform prepares the product for release from an operational perspective.

Quality, Security and Platform provide release recommendations from their respective responsibilities.

The Project Sponsor owns final release approval.

The Release stage captures the approval decision, release evidence, known issues, accepted risks, version and outcome.

### Architecture Internal Flow

Architecture should normally move through:

```text
Review
  -> Understand
  -> Assess
  -> Recommend
  -> Execute
```

The Recommend checkpoint should occur before substantial Architecture artefacts are produced.

Once the recommendation is approved, Architecture executes by producing the agreed Architecture artefacts.

### Scale the Workflow

Small changes may use lightweight artefacts.

Large, risky or cross-team changes should use the full set of artefacts and review gates.

The same lifecycle may be applied to:

- Products
- Major features
- Significant enhancements
- Platform initiatives
- Security initiatives
- Migration programmes

Product-level artefacts describe the product as a whole.

Initiative-level artefacts describe a scoped body of work and should be stored with that initiative.

## Key Takeaways

- The default flow moves from product intent to production readiness.
- Operationalisation is a cross-cutting concern from Discovery to Platform.
- Platform recommends operational readiness; the Project Sponsor approves release.
- Architecture uses Review, Understand, Assess, Recommend and Execute internally.
- Feedback loops are expected and should be explicit.
- Workflow depth should match risk and complexity.
- The lifecycle applies to any engineering initiative, not only whole products.
- Silent redesign weakens traceability.

## Related Reading

- [04 Handover Process](04%20Handover%20Process.md)
- [05 Review Gates](05%20Review%20Gates.md)
- [Initiative Artefacts](../16%20Engineering%20Artefacts/07%20Initiative%20Artefacts.md)

---

## Navigation

**Previous**

- [02 Roles and Responsibilities](02%20Roles%20and%20Responsibilities.md)

**Next**

- [04 Handover Process](04%20Handover%20Process.md)

**Book**

- [Engineering Workflow](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
