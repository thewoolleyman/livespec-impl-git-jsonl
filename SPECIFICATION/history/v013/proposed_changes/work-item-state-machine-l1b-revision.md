---
proposal: work-item-state-machine-l1b.md
decision: accept
revised_at: 2026-06-29T14:16:43Z
author_human: thewoolleyman <chad@thewoolleyman.com>
author_llm: claude-opus-4-8-l1b
---

## Decision and Rationale

Ratify the L1b schema migration: 7-state status enum, +rank (sole ordering authority, sentinel-on-read for legacy lines), -priority, terminal closed->done, and the forced downstream reconciliation (next ranking by rank, list/capture/implement prose). Pins to livespec-runtime v0.5.0's WorkItemStatus + BOTTOM_SENTINEL; the shared validator requires lockstep. No H2 heading changes -> no heading-coverage co-edit. Auto-ratified per the locked design (decisions 1-46); the maintainer-owned gate is delegated under the autonomous wrap-up mandate.

## Resulting Changes

- contracts.md
