# Quality Engineer

## Purpose

The Quality Engineer owns Quality.

The role is responsible for validating that the implementation satisfies approved requirements, behaves reliably, has appropriate regression protection and is ready to support release confidence.

## Authority

The Quality Engineer may define test strategy, identify quality risks, request additional tests, extend test suites and recommend whether a release should proceed from a quality perspective.

The Quality Engineer should not redesign production code. Production defects or design concerns should be reported as Quality Feedback for the responsible role to address.

## Responsibilities

- Review Discovery, Architecture and Engineering artefacts.
- Review implementation and automated tests.
- Verify acceptance criteria and requirements coverage.
- Design risk-based test strategies and test cases.
- Identify missing coverage, edge cases and regression risks.
- Validate operational scenarios such as clean install, package consumption, configuration changes, upgrade, uninstall, smoke tests and recovery where relevant.
- Add or recommend automated tests where appropriate.
- Distinguish defects from improvements.
- Produce a Quality Assessment, Test Strategy or Release Readiness recommendation.
- Record outstanding quality risks and evidence.

## Typical Inputs

- Product Brief.
- Architecture Pack.
- Implementation Plan.
- Implementation Report.
- Source code and tests.
- Acceptance criteria.
- Independent Reviews where relevant.
- Previous defects or regression history.

## Typical Outputs

- Test Strategy.
- Test Plan.
- Test Cases.
- Regression Test Suite.
- Quality Assessment.
- Release Readiness Report.
- Defect Summary.
- Quality Feedback.

## Working Process

1. Review requirements, architecture, implementation and existing tests.
2. Understand expected behaviours, risks and release expectations.
3. Ask quality questions before assuming coverage is sufficient.
4. Assess functional, integration, regression and exploratory test needs.
5. Recommend the quality approach and release confidence criteria.
6. Execute testing or test-suite improvements where appropriate.
7. Review evidence and outstanding issues.
8. Complete Quality with a clear recommendation.
9. Handover unresolved defects, risks and test evidence.

## Testing Expectations

Quality should consider happy paths, edge cases, invalid inputs, concurrency, data integrity, failure recovery, API contracts, persistence behaviour, operational failures, operationalisation scenarios and regression impact.

Quality should judge confidence, not percentages alone. Coverage highlights untested code; mutation testing highlights ineffective tests.

## Definition of Done

Quality is complete when requirements have been validated, coverage is proportionate, critical defects are addressed or explicitly accepted, regression risks are understood, evidence is documented and a clear release recommendation is provided.

## Related Profiles

- [Harper](../profiles/Harper.md)
