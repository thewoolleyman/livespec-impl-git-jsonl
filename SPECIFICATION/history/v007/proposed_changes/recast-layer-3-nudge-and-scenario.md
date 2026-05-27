---
topic: recast-layer-3-nudge-and-scenario
author: claude-opus-4-7
created_at: 2026-05-27T08:13:31Z
---

## Proposal: drop-layer-3-discoverability-nudge-subsection-from-next-skill

### Target specification files

- SPECIFICATION/contracts.md

### Summary

Remove the §Layer 3 discoverability nudge subsection from contracts.md §next per the upstream v089 recast. Under the recast, impl-plugin `next` skills no longer carry the parallel-and-symmetric nudge contract because impl-plugin repos no longer carry a Layer 3 driver — a nudge from impl-plaintext's `next` has no in-repo Layer 3 surface to point at.

### Motivation

Coordinates with livespec PR #304's v089 recast (Layer 3 is livespec-resident only). The upstream contracts.md no longer mandates the impl-plugin `next` nudge; this sub-spec MUST follow suit to stay in sync. The cross-side composition discipline continues to apply to /livespec:next (which IS colocated with the resident Layer 3 driver in livespec) but does NOT apply to impl-plugin `next` skills under the recast.

### Proposed Changes

Remove the entire §Layer 3 discoverability nudge subsection from `SPECIFICATION/contracts.md` (currently nested under §next, lines ~321-367). The wrapper-stays-thin-transport sentence MUST be preserved as a standalone sentence at the end of the parent §next bullet ('The wrapper at `.claude-plugin/scripts/bin/next.py` MUST remain a pure thin-transport pass-through.'). Replace the subsection with a single short paragraph stating: 'Under the v089 upstream recast (livespec/SPECIFICATION/spec.md §"Three-layer orchestration architecture" → "Layer 3 — Cross-repo orchestration (livespec-resident)"), the Layer 3 discoverability nudge applies only to /livespec:next; impl-plugin `next` skills do NOT carry the parallel-and-symmetric nudge contract because impl-plugin repos do NOT carry their own Layer 3 driver.'

## Proposal: recast-scenario-6-to-livespec-resident-driver

### Target specification files

- SPECIFICATION/scenarios.md

### Summary

Recast §Scenario 6 — Project-local Layer 3 loop driver to reflect that the Layer 3 driver lives in livespec (resident), not in the consumer project. The driver scenario MUST continue to describe how /livespec:next + /livespec-impl-plaintext:next are composed, but the surface that composes them is livespec's own .claude/skills/loop/SKILL.md, not 'the consumer project's' loop skill.

### Motivation

Coordinates with livespec PR #304's v089 recast. The Scenario 6 prose still says 'the consumer project's `.claude/skills/loop/SKILL.md` is the hand-tuned orchestration driver', which is now incorrect under the recast. The driver is livespec's resident driver.

### Proposed Changes

In `SPECIFICATION/scenarios.md` §"Scenario 6 — Project-local Layer 3 loop driver", rename the heading to §"Scenario 6 — Cross-repo Layer 3 loop driver (livespec-resident)". In the body, change 'The consumer project's `.claude/skills/loop/SKILL.md` is the hand-tuned orchestration driver.' to 'livespec's `.claude/skills/loop/SKILL.md` is the livespec-resident cross-repo orchestration driver.' Preserve the rest of the scenario (the 4-step iteration sequence + empty-queue handoff + memo/gap/drift invocation framing) intact — those describe orchestration mechanics that remain correct under the recast.
