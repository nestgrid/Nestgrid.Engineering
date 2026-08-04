# Sentinel Review Artefacts

This initiative formalises Sentinel Reviews as recognised engineering review artefacts.

## Context

Sentinel is positioned as an independent reviewer across the Nestgrid Engineering Lifecycle.

Reviews should not remain trapped in chat history. Downstream Engineering Agents should be able to continue from Sentinel findings by reading durable repository artefacts.

## Scope

This initiative updates the Engineering Handbook, templates and Engineering Agent documents to make Sentinel Reviews durable, discoverable and reusable.

## Changes

- Added the Sentinel Review artefact template.
- Added `docs/reviews/` as the product-level review location.
- Added initiative-level `reviews/` guidance.
- Updated handover and review gate guidance to include Sentinel findings.
- Updated Engineering Agents so their Review step includes relevant Sentinel reviews and finding dispositions.
- Updated reusable prompts so agents read Sentinel review folders where they exist.

## Artefacts

- [Implementation Report](artefacts/03%20Implementation/Implementation%20Report.md)

## Decisions

No decision record was required for this initiative.

Sentinel Reviews are recognised but optional review artefacts. They do not add a mandatory lifecycle stage.
