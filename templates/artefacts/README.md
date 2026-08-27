# Artefact Templates

This folder contains reusable templates for the standard Nestgrid Engineering workflow artefacts.

Templates include an `eos_version` field. Set it to the canonical EOS version recorded in [`VERSION`](../../VERSION) when completing an artefact, and use `version` for the artefact's own revision.

## Templates

- [Opportunity Decision](Opportunity%20Decision.Template.md)
- [Product Brief](Product%20Brief.Template.md)
- [Architecture Handover](Architecture%20Handover.Template.md)
- [Architecture Recommendation](Architecture%20Recommendation.Template.md)
- [Architecture Pack](Architecture%20Pack.Template.md)
- [Implementation Plan](Implementation%20Plan.Template.md)
- [Implementation Report](Implementation%20Report.Template.md)
- [Engineering Assurance](Engineering%20Assurance.Template.md)
- [Test Strategy](Test%20Strategy.Template.md)
- [Security Assessment](Security%20Assessment.Template.md)
- [Deployment Guide](Deployment%20Guide.Template.md)
- [Operational Readiness Review](Operational%20Readiness%20Review.Template.md)
- [Release Readiness Report](Release%20Readiness%20Report.Template.md)
- [Release Report](Release%20Report.Template.md)
- [Feedback](Feedback.Template.md)
- [Independent Review](Independent%20Review.Template.md)

## Usage

Start from the relevant template when creating a project artefact.

The Opportunity Decision template is optional. Use it when early discovery rationale, evidence or follow-up should endure before a Product Brief exists.

Product-level artefacts should usually live in the product repository under:

```text
docs/artefacts/
  01 Discovery/
  02 Architecture/
  03 Implementation/
  04 Quality/
  05 Security/
  06 Platform/
  07 Release/
```

Initiative-level artefacts should live with the initiative:

```text
docs/initiatives/<yyyy-mm>-<initiative-name>/artefacts/
  01 Discovery/
  02 Architecture/
  03 Implementation/
  04 Quality/
  05 Security/
  06 Platform/
  07 Release/
```

Independent Reviews should live in `docs/reviews/` for product-level reviews or inside the relevant initiative's `reviews/` folder for initiative-specific reviews.

Use one stable, scope-based filename per review series. Update the canonical document for follow-up reviews, increment its version, preserve stable finding IDs and append to its Review History. Do not create competing date-stamped copies for the same scope.

See [Engineering Artefacts](../../books/16%20Engineering%20Artefacts/README.md) for guidance.
