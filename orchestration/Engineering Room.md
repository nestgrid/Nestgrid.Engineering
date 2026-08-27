# Engineering Room

## Purpose

The Engineering Room is a persistent product-level conversation where the Project Sponsor may collaborate with one or more explicitly activated Role/Profile participants.

It is an orchestration model, not a lifecycle stage. It does not replace Roles, Profiles, Workflows, approval gates, artefacts or handovers.

## Operating Models

The Engineering Operating System supports two complementary models:

- **Isolated conversation:** one Role/Profile performs a focused assignment in its own conversation.
- **Engineering Room:** multiple Role/Profile participants collaborate in one persistent product or initiative conversation.

Both models follow the same authority, lifecycle, artefact and approval rules.

## Explicit Activation

Activate a participant with `@Profile` syntax:

```text
@Mason: Review the implementation plan and identify engineering concerns.
```

Every explicit `@Profile` invocation is a **fresh activation**, even when that Profile is already active.

On every explicit activation, the participant must:

1. Resolve the named Profile to its canonical Role.
2. Re-read the current Role document.
3. Re-read the current Profile document.
4. Reconcile the request with the current authoritative repository state, approved artefacts, decisions, reviews and workflow.
5. Respond from the refreshed Role/Profile perspective.

Natural follow-up messages without another explicit `@Profile` invocation may continue under the existing Active Profile. The participant heading must make the active Profile and Role evident:

```text
## Mason - Software Engineer
```

Do not add a separate repetitive status block after each activation.

If no Active Profile exists and a message does not identify a participant, ask which Role/Profile should respond.

## Multiple Participants

Multiple participants may be activated for the same request:

```text
@Gideon @Morgan: Review the proposed identity design from Architecture and Security perspectives.
```

Each substantive contribution must be visibly attributed with its Profile and Role. Participants should provide separate perspectives rather than blending into an unlabelled generic response.

When multiple Profiles are activated without an explicitly named owner, the first named Profile remains the Active Profile for natural follow-up. The other participants contribute to that request only; they do not become owners by appearing in the same activation.

Agreement and disagreement should be explicit. Each participant should distinguish facts, assumptions, recommendations, decisions and unresolved concerns.

Participant agreement is not Project Sponsor approval and does not satisfy a lifecycle gate.

## Consultation

Consultation does not transfer ownership. The owning Profile remains explicit:

```text
@Mason: Consult Morgan on the security implications of this design, then continue your Engineering assessment.
```

In this example:

- Mason remains the Active Profile and task owner.
- Morgan is temporarily activated using the normal fresh-activation rules.
- Morgan's contribution is visibly attributed.
- Ownership and lifecycle state do not transfer.
- Mason resumes the assessment using Morgan's input.

## Authority and Isolation

Each participant must preserve the authority and decision rights of its Role. A Profile must not use the Room to:

- perform another Role's responsibilities without explicit consultation;
- silently change lifecycle ownership or stage;
- weaken an approval gate;
- turn a recommendation into an approval;
- override approved artefacts or decisions with conversational preference; or
- blend conflicting perspectives into an untraceable consensus.

When Roles disagree, identify the disagreement, its impact and the Role or Project Sponsor responsible for resolution. Reserved decisions remain subject to the [Engineering Context](../ENGINEERING-CONTEXT.md).

## Lifecycle and Handover

The Room may be used during any lifecycle stage and may move between participants arbitrarily. Profile activation or consultation never constitutes a lifecycle transition or handover.

Lifecycle movement still depends on the applicable workflow, approved artefacts and approval gates. A Role may recommend progression, but may not bypass its gate.

Handover remains explicit and artefact-based. The latest approved artefact, decision or review is authoritative over Room conversation history.

Participants should create or update the normal durable artefacts when the work requires them, including Product Briefs, Architecture Packs, Implementation Plans, Security Assessments and Independent Reviews.

Do not create a Room transcript merely to preserve routine conversation. Preserve durable state through the established artefacts, decisions and reviews.

## Independent Review

Sentinel may participate in the Room when contextual consultation is useful. Formal assurance should use the canonical Independent Review model and may use a separate Review conversation when stronger contextual independence is appropriate.

Sentinel owns findings and recommendations. The responsible Role owns dispositions and completion evidence. Room participation must not weaken Sentinel's independence or replace the canonical review artefact.

## Key Takeaways

- The Engineering Room is orchestration, not a lifecycle stage.
- Every explicit activation refreshes the current Role and Profile.
- Natural follow-ups may continue under the Active Profile.
- Participant headings provide visible Profile and Role attribution.
- Consultation does not transfer ownership.
- Agreement is not approval.
- Artefacts, decisions and reviews remain authoritative over conversation history.
- Isolated Role/Profile conversations remain fully supported.

## Related Reading

- [Engineering Context](../ENGINEERING-CONTEXT.md)
- [Workflow Purpose](../books/15%20Engineering%20Workflow/01%20Workflow%20Purpose.md)
- [Handover Process](../books/15%20Engineering%20Workflow/04%20Handover%20Process.md)
- [Profiles](../profiles/README.md)
