# API Usage Guides

> Part of the **[Documentation](README.md)**.

## Purpose

An API Usage Guide explains how consumers use an API to complete meaningful workflows.

It complements the generated OpenAPI contract and interactive development reference. OpenAPI describes the available interface; the usage guide explains the normal journey through it.

## When to Create One

Create an API Usage Guide when an API has meaningful workflow sequencing, prerequisites, context or consumer guidance that cannot be understood from individual endpoint descriptions alone.

It is especially useful for:

- Public or partner-facing APIs.
- APIs consumed by more than one application.
- Domain-heavy APIs such as Finance, Identity or Events.
- APIs where one response provides identifiers required by later operations.
- APIs that need development, demonstration or Quality validation workflows.

Do not create one for a trivial API when accurate OpenAPI documentation is sufficient.

## Ownership

The Software Engineer should produce the initial implementation-focused guide, including endpoint sequence, prerequisites, examples and response identifiers.

Quality Engineering should validate the documented workflows against the implementation and test evidence.

The Product Owner, Technical Writer or equivalent role may refine the guide for external or user-facing audiences when appropriate.

Security and Platform Engineering should contribute authentication, environment, deployment and operational guidance within their areas of responsibility.

## Required Content

The depth should be proportionate to the API and its consumers. Where applicable, include:

- Purpose and scope.
- Prerequisites and configuration.
- Authentication, authorisation and request context.
- A workflow overview.
- Important workflow sequences.
- Example requests and responses.
- Response identifiers required by later operations.
- Common failures and client handling.
- Development usage and OpenAPI/Scalar links.
- Version and compatibility expectations.

Use representative values and avoid secrets or sensitive production data.

## Relationship to OpenAPI

The guide must not become a second, manually maintained endpoint reference.

Keep endpoint names, tags, summaries, descriptions, request models, response metadata and status codes in the API's OpenAPI metadata. Link to that reference from the guide.

The guide should focus on workflow, context and consumer decisions that endpoint-level documentation cannot express well.

## Relationship to Lifecycle Artefacts

An API Usage Guide is durable product documentation, not a mandatory lifecycle artefact.

It may be drafted during Engineering, validated during Quality and refined during Platform or Release preparation. It should be stored under the product's `docs/guides/` directory and linked from appropriate README entry points.

## Maintenance

Update the guide when workflow order, prerequisites, response identifiers, authorisation, compatibility or failure behaviour changes.

Documentation changes should be included with the implementation change where practical.

Use the reusable [API Usage Guide template](../../templates/guides/API%20Usage%20Guide.Template.md) when creating a new guide.

## Key Takeaways

- OpenAPI describes the contract; an API Usage Guide describes meaningful consumer workflows.
- The guide is optional and should be proportionate to complexity.
- Engineering owns the first technical version; downstream roles validate or refine it.
- The guide belongs in `docs/guides/`, not `docs/artefacts/`.
- Keep it linked to, rather than duplicating, OpenAPI and Scalar.

## Related Reading

- [API Contracts](../08%20Engineering%20Standards/11%20API%20Contracts.md)
- [Documentation Principles](01%20Documentation%20Principles.md)
- [Structure and Navigation](02%20Structure%20and%20Navigation.md)
- [Guide Templates](../../templates/guides/README.md)

---

## Navigation

**Previous**

- [05 Documentation Review](05%20Documentation%20Review.md)

**Next**

- [Templates](../13%20Templates/README.md)

**Book**

- [Documentation](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)

