# Nestgrid Engineering Operating System

Nestgrid Engineering Operating System defines the engineering methodology, standards, agents, templates and lifecycle practices used to design, build and maintain software within the Nestgrid ecosystem.

It captures the complete engineering lifecycle, from understanding a business problem through to designing, implementing, testing, reviewing, deploying and operating production software.

Although developed for Nestgrid products, the methodology is technology-agnostic and may be adopted by any engineering team seeking a structured and consistent approach to software engineering.

## Engineering Lifecycle

The methodology follows a structured engineering lifecycle.

1. [Philosophy](handbook/01%20Philosophy/README.md)
2. [Language](handbook/02%20Language/README.md)
3. [Discovery](handbook/03%20Discovery/README.md)
4. [Domain Modelling](handbook/04%20Domain%20Modelling/README.md)
5. [Architecture](handbook/05%20Architecture/README.md)
6. [Decisions](handbook/06%20Decisions/README.md)
7. [Solution Structure](handbook/07%20Solution%20Structure/README.md)
8. [Engineering Standards](handbook/08%20Engineering%20Standards/README.md)
9. [Testing](handbook/09%20Testing/README.md)
10. [Deployment](handbook/10%20Deployment/README.md)
11. [Operations](handbook/11%20Operations/README.md)
12. [Documentation](handbook/12%20Documentation/README.md)
13. [Templates](handbook/13%20Templates/README.md)
14. [Samples](handbook/14%20Samples/README.md)
15. [Engineering Workflow](handbook/15%20Engineering%20Workflow/README.md)
16. [Engineering Artefacts](handbook/16%20Engineering%20Artefacts/README.md)

See [Engineering Lifecycle](ENGINEERING-LIFECYCLE.md) for an overview.

## Repository Structure

`/agents`

Engineering agents that define lifecycle roles, responsibilities, working practices and handovers.

`/handbook`

Canonical handbook guidance for each stage of the engineering lifecycle.

`/docs/decisions`

Decision records for the Nestgrid Engineering Operating System.

`/docs/initiatives`

Lifecycle initiatives used to evolve the Nestgrid Engineering Operating System.

`/templates`

Reusable documentation and engineering templates.

`/templates/artefacts`

Reusable templates for standard engineering workflow artefacts.

`/samples`

Reference samples demonstrating the methodology in practice.

## Product Repository Convention

Product repositories should separate enduring handbook knowledge from lifecycle artefacts.

Recommended structure:

```text
src/
tests/
docs/
  handbooks/
    01 Philosophy/
    02 Language/
    03 Discovery/
    04 Domain Modelling/
    05 Architecture/
    06 Decisions/
    07 Solution Structure/
    08 Engineering Standards/
    09 Testing/
    10 Deployment/
    11 Operations/
    12 Documentation/
  artefacts/
    01 Discovery/
    02 Architecture/
    03 Implementation/
    04 Quality/
    05 Security/
    06 Platform/
    07 Release/
  decisions/
  reviews/
  initiatives/
samples/        optional
assets/         optional
scripts/        optional
tools/          optional
.github/        optional
```

This is the standard target structure for a product repository.

During pure Discovery and Architecture, a repository may remain documentation-first and omit `src/` and `tests/` until Engineering begins.

`src/` contains production code.

`tests/` contains automated tests.

`docs/handbooks/` contains long-lived product knowledge.

`docs/artefacts/` contains lifecycle outputs produced during engineering work.

`docs/decisions/` contains decision records.

`docs/reviews/` contains independent review artefacts, including Sentinel reviews.

`docs/initiatives/` contains lifecycle artefacts and decisions for scoped engineering initiatives such as major features, enhancements, migrations and platform work.

Artefacts should use the standard templates from `/templates/artefacts`.

Standard artefact flow:

```text
Product Brief
  -> Architecture Handover
  -> Architecture Recommendation
  -> Architecture Pack
  -> Implementation Plan / Implementation Report
  -> Test Strategy
  -> Security Assessment
  -> Deployment Guide / Operational Readiness Review
  -> Release Report
```

Chats are for thinking. Artefacts are for engineering.

## Contributing

Contributions should follow the standards described in this repository.

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance.

## Security

Security issues should be reported responsibly.

See [SECURITY.md](SECURITY.md) for security guidance.

## License

This repository is licensed under the [MIT License](LICENSE).
