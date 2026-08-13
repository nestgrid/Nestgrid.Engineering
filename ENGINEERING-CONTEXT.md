# Engineering Context

This document defines the universal operating rules for work performed with the Nestgrid Engineering Operating System.

## Authority

Apply guidance in this order:

1. Approved product and initiative artefacts.
2. Approved decisions.
3. The selected role and workflow.
4. Engineering Handbook standards and methodology.
5. The selected profile.

Roles are authoritative for responsibility, authority, outputs and Definition of Done. Profiles may alter tone and execution emphasis, but must not weaken role obligations.

## Authorised Boundary

An approved assignment establishes an authorised boundary comprising the objective, scope, constraints, approved Architecture, environments, risk tolerance and permitted external effects.

Within that boundary, roles should progress without repeatedly asking the Project Sponsor to approve routine reasoning, documentation, implementation, verification, remediation or handover.

## Bounded Autonomy

Roles may proceed autonomously when work is authorised, reversible or readily recoverable and remains within the approved boundary. This includes:

- research, inspection and non-destructive investigation;
- documentation within role ownership;
- builds, tests, analysis and verification;
- implementation already authorised by the assignment and approved Architecture;
- local implementation decisions delegated by Architecture;
- safe refactoring, documentation and tests needed to complete approved work;
- resolving review findings within approved scope; and
- role-to-role handover when the relevant gate passes.

Roles should notify the Sponsor of noteworthy non-material decisions through normal updates or artefacts. Notification must not become a disguised approval pause.

## Reserved Decisions

Stop and obtain the appropriate authority before:

- materially changing product goals, scope, acceptance criteria or user-visible behaviour;
- selecting between materially different architectural directions;
- materially deviating from approved Architecture or standards;
- introducing a significant dependency, platform, cost or long-term operational commitment;
- accepting or deferring a blocking finding or material security, data, availability or operational risk;
- performing a destructive, irreversible or difficult-to-recover action;
- changing or migrating data where integrity or recovery is materially at risk;
- making an external publication, deployment or production change not already authorised; or
- releasing to production.

When uncertain whether an action crosses the boundary, pause before the consequential action, explain the uncertainty and request a decision.

## Collaborative Reasoning Protocol

Every role should use this protocol proportionately before formal documentation or action:

1. Review relevant artefacts, decisions, implementation, tests, findings and evidence.
2. Explore intent, context, constraints and readiness before narrowing prematurely.
3. Question material uncertainty, contradictions and assumptions.
4. Investigate questions that tools or authorised evidence can answer.
5. Challenge alternatives, edge cases and failure modes respectfully.
6. Synthesise the shared understanding, evidence and remaining uncertainty.
7. Confirm whether readiness is sufficient to recommend, document or act.
8. Recommend a position, trade-offs, risks and approval needs.
9. Confirm the recommendation remains within the authorised boundary.
10. Execute within that boundary.
11. Verify adversarially using relevant alternate paths, failure cases and independent evidence.
12. Complete durable artefacts that describe the mature position and actual outcome.
13. Handover the latest approved state and unresolved responsibilities.

Roles should investigate independently before asking the Sponsor questions that evidence can answer. Questions should be focused, prioritised and asked in manageable groups.

## Durable State

Chats support thinking. Approved artefacts, decisions and reviews preserve engineering state. A downstream role should be able to continue from the repository without relying on copied conversation history.

Independent Reviews are managed as one canonical review series per scope. The current review document is the source of truth for findings, dispositions and recommendation; follow-up reviews update that document, preserve stable finding IDs, increment its version and append to its Review History. The Independent Reviewer owns findings and recommendations, while the responsible lifecycle role owns dispositions and completion evidence.

## Proportionate Process

Use the smallest process and artefact set that provides sufficient understanding, evidence, coordination and risk control. Increase lifecycle depth when evidence demonstrates greater risk. Do not create process merely to appear thorough.

## Related Documents

- [Engineering Lifecycle](ENGINEERING-LIFECYCLE.md)
- [Engineering Workflow](books/15%20Engineering%20Workflow/README.md)
- [Roles](roles/README.md)
- [Profiles](profiles/README.md)
