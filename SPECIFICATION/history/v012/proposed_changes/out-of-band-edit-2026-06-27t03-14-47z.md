---
topic: out-of-band-edit-2026-06-27t03-14-47z
author: livespec-doctor
created_at: 2026-06-27T03:14:47Z
---

## Proposal: out-of-band-edit-2026-06-27t03-14-47z

doctor detected drift between HEAD-active spec content and the
HEAD-history-vN snapshot; this auto-backfill records the active
state as the new canonical version.

### Proposed Changes

```diff
--- history/vN/README.md
+++ active/README.md
@@ -3,9 +3,9 @@
 This directory holds the natural-language specification for
 `livespec-orchestrator-git-jsonl`, the JSONL-backed implementation plugin
 for `livespec`. Per
-`livespec/SPECIFICATION/non-functional-requirements.md`
-§"Implementation plugin ecosystem", every `livespec-impl-*`
-plugin dogfoods its own `SPECIFICATION/`; this is ours.
+`livespec/SPECIFICATION/non-functional-requirements.md`, every
+`livespec-impl-*` plugin dogfoods its own `SPECIFICATION/`; this
+is ours.
 
 ## Files
 
--- history/vN/contracts.md
+++ active/contracts.md
@@ -13,16 +13,15 @@
 be changed without a coordinated rename across consumers (because
 doctor's cross-boundary invariants in `livespec` invoke skills
 through this namespace prefix per
-`livespec/SPECIFICATION/contracts.md` §"Cross-plugin
-invocation"). Renaming is a major-version-bump operation.
+`livespec/SPECIFICATION/contracts.md`). Renaming is a
+major-version-bump operation.
 
 ## The seven-skill surface
 
 Every entry below is REQUIRED. The descriptions concretize each
 skill's behavior on the JSONL substrate; cross-boundary semantics
 (handoffs, JSON output schemas, user-consent rules) are defined by
-`livespec/SPECIFICATION/contracts.md` §"Implementation-plugin
-contract — the 10-skill surface" and apply uniformly.
+`livespec/SPECIFICATION/contracts.md` and apply uniformly.
 
 ### Heavyweight authored skills (4)
 
@@ -60,8 +59,8 @@
 finding, present it to the user with a recommended action; on
 consent, hand off to `/livespec:propose-change` via the
 cross-boundary handoff (per
-`livespec/SPECIFICATION/contracts.md` §"Cross-boundary
-handoffs" entry 1). The handoff produces a proposed-change file
+`livespec/SPECIFICATION/contracts.md`). The handoff produces a
+proposed-change file
 under the consumer's spec-side `<spec-root>/proposed_changes/`;
 this plugin never writes to spec-side state directly.
 
@@ -80,9 +79,7 @@
 This is the surface livespec's `unresolved-spec-commitment` doctor
 invariant queries via `list-work-items --json` to verify each
 declared spec→impl commitment maps to a filed work-item (per
-`livespec/SPECIFICATION/contracts.md` §"Implementation-plugin
-contract — the 10-skill surface" → "Work-item
-`spec_commitment_hint` field").
+`livespec/SPECIFICATION/contracts.md`).
 
 #### `implement`
 
@@ -113,8 +110,8 @@
 
 Each thin-transport skill is a short SKILL.md pass-through over a
 Python `bin/` implementation (the wrapper-shape contract codified
-in `livespec/SPECIFICATION/contracts.md` §"Wrapper CLI
-surface"). SKILL.md MUST NOT accrete logic — every behavior lives
+in `livespec/SPECIFICATION/contracts.md`). SKILL.md MUST NOT accrete
+logic — every behavior lives
 under `.claude-plugin/scripts/bin/<skill>.py`.
 
 #### `list-work-items`
@@ -154,9 +151,8 @@
 
 Cross-reference: cross-side composition of impl-side `next` with
 spec-side `/livespec:next` is a Layer 3 (project-local
-orchestration) concern per `livespec/SPECIFICATION/spec.md`
-§"Three-layer orchestration architecture" → "Cross-side
-composition belongs at Layer 3". This Layer 2 surface ranks
+orchestration) concern per `livespec/SPECIFICATION/spec.md`. This
+Layer 2 surface ranks
 impl-side state only; it MUST NOT bake a cross-side weighting in.
 
 CLI surface: `next [--limit <count>] [--offset <count>] [--json] [--work-items-path <path>] [--project-root <path>]`.
@@ -195,11 +191,10 @@
    order.
 4. Apply `--offset` and `--limit` to produce the returned slice.
 
-Output schema (per `livespec/SPECIFICATION/contracts.md`
-§"Implementation-plugin contract — the 10-skill surface" →
-`next` and the upstream
-§"`/livespec:next` spec-side thin-transport skill" → §"Output
-schema"): the output is a JSON object with two top-level keys,
+Output schema (per `livespec/SPECIFICATION/contracts.md` for
+`next` and the upstream `/livespec:next` spec-side thin-transport
+skill's output schema): the output is a JSON object with two
+top-level keys,
 `candidates[]` and `pagination`:
 
 ```jsonc
@@ -264,17 +259,14 @@
 ##### Layer 3 discoverability nudge — not applicable under v089 recast
 
 Under the v089 upstream recast
-(`livespec/SPECIFICATION/spec.md` §"Three-layer
-orchestration architecture" → "Layer 3 — Cross-repo
-orchestration (livespec-resident)"), the Layer 3
+(`livespec/SPECIFICATION/spec.md`), the Layer 3
 discoverability nudge applies only to `/livespec:next`;
 impl-plugin `next` skills do NOT carry the parallel-and-
 symmetric nudge contract because impl-plugin repos do NOT
 carry their own Layer 3 driver. The wrapper at
 `.claude-plugin/scripts/bin/next.py` MUST remain a pure
-thin-transport pass-through per the upstream §"Thin-transport
-skill doctrine" and this plugin's §"Thin-transport skills (4)"
-preamble.
+thin-transport pass-through per the upstream thin-transport skill
+doctrine and this plugin's thin-transport skills preamble.
 
 #### `detect-impl-gaps`
 
@@ -285,8 +277,8 @@
 
 The skill reads the live Specification via the Spec Reader,
 enumerates every MUST/SHOULD rule per the gap-rule enumeration
-contract (per upstream §"Spec Reader required-capability
-surface" capability 1), and computes a stable `gap_id` per
+contract (per the upstream Spec Reader required-capability
+surface), and computes a stable `gap_id` per
 detected rule. Gap-id derivation is a pure function of rule
 text + canonical heading path; the same rule text always yields
 the same gap-id across runs.
@@ -416,9 +408,8 @@
   as `null`); always written explicitly on append. When non-null,
   carries the verbatim `id_hint` from a spec-side
   `spec_commitments.impl_followups[]` declaration (per
-  `livespec/SPECIFICATION/contracts.md` §"Implementation-plugin
-  contract — the 10-skill surface" → "Work-item
-  `spec_commitment_hint` field"). When the work-item was filed via
+  `livespec/SPECIFICATION/contracts.md`). When the work-item was
+  filed via
   the freeform path with no spec-side commitment to pair against,
   the field is `null`. The field is the surface livespec's
   `unresolved-spec-commitment` doctor invariant queries via
@@ -610,8 +601,8 @@
 
 ## Spec Reader internal API
 
-Per `livespec/SPECIFICATION/contracts.md` §"Spec Reader
-required-capability surface", every `livespec-impl-*` plugin MUST
+Per `livespec/SPECIFICATION/contracts.md`, every
+`livespec-impl-*` plugin MUST
 expose four capabilities through an internal adapter. The shape
 is implementation-dependent; this plugin's shape is a Python
 module with these public functions:
@@ -634,8 +625,8 @@
 The Spec Reader MUST:
 
 - Consult the active template manifest's `spec_files` list rather
-  than hardcoding the well-known file set (per upstream §"Spec
-  Reader required-capability surface" capability 1).
+  than hardcoding the well-known file set (per the upstream Spec
+  Reader required-capability surface).
 - Surface the `version-directories-complete` pruned-marker
   exemption when reading history (capability 2).
 - Return `int` for the current version (capability 3).
@@ -654,8 +645,7 @@
 
 ## Persistent Agent Knowledge realization
 
-Per `livespec/SPECIFICATION/contracts.md` §"Persistent Agent
-Knowledge realization", the per-plugin form is
+Per `livespec/SPECIFICATION/contracts.md`, the per-plugin form is
 implementation-dependent. `livespec-orchestrator-git-jsonl` realizes the
 store as:
 
@@ -683,8 +673,8 @@
 
 ## `compat` block
 
-Per `livespec/SPECIFICATION/contracts.md` §"Cross-repo
-coordination — pin-and-bump", every consuming project's
+Per `livespec/SPECIFICATION/contracts.md`, every consuming
+project's
 `.livespec.jsonc` declares a `compat` block for each active
 impl-plugin. For `livespec-orchestrator-git-jsonl`:
 
@@ -726,12 +716,12 @@
 The configuration block is read by every skill at invocation
 time. A missing or malformed block MUST fire a `fail` finding
 from doctor's `contract-version-compatibility` invariant
-(upstream §"Cross-boundary doctor invariants").
+(upstream cross-boundary doctor invariants).
 
 ## Cross-boundary handoffs
 
-Per `livespec/SPECIFICATION/contracts.md` §"Cross-boundary
-handoffs", this plugin participates in these red-edge handoffs:
+Per `livespec/SPECIFICATION/contracts.md`, this plugin
+participates in these red-edge handoffs:
 
 1. `/livespec-orchestrator-git-jsonl:capture-spec-drift` →
    `/livespec:propose-change` (drift findings).
@@ -744,5 +734,5 @@
    `no-stale-gap-tied`).
 
 The handoff mechanism is namespace invocation (per
-`livespec/SPECIFICATION/contracts.md` §"Cross-plugin
-invocation") — never direct CLI shelling-out to wrapper paths.
+`livespec/SPECIFICATION/contracts.md`) — never direct CLI
+shelling-out to wrapper paths.
--- history/vN/scenarios.md
+++ active/scenarios.md
@@ -62,9 +62,8 @@
 
 Cross-reference: cross-side composition of impl-side `next` with
 spec-side `/livespec:next` is a Layer 3 (project-local
-orchestration) concern per `livespec/SPECIFICATION/spec.md`
-§"Three-layer orchestration architecture" → "Cross-side
-composition belongs at Layer 3". This scenario describes the
+orchestration) concern per `livespec/SPECIFICATION/spec.md`. This
+scenario describes the
 Layer 3 driver's behavior; this plugin's `next` skill itself
 ranks impl-side state only and MUST NOT bake a cross-side
 weighting in.
--- history/vN/spec.md
+++ active/spec.md
@@ -11,8 +11,7 @@
 
 `livespec-orchestrator-git-jsonl` is one realization of the abstract
 implementation-plugin contract that `livespec` publishes in
-`livespec/SPECIFICATION/contracts.md` §"Implementation-plugin
-contract — the 9-skill surface". Other realizations exist on paper
+`livespec/SPECIFICATION/contracts.md`. Other realizations exist on paper
 (`livespec-impl-beads`, `livespec-impl-gitlab`, `livespec-impl-gascity`,
 `livespec-impl-darkfactory-kilroy`) and are out of scope here. This
 plugin's substrate is plain JSONL files committed alongside the
@@ -43,7 +42,7 @@
 ## Terminology
 
 This spec adopts every term defined in
-`livespec/SPECIFICATION/spec.md` §"Terminology" verbatim
+`livespec/SPECIFICATION/spec.md` verbatim
 (Specification, Specification History, Work Items, Disposition,
 Persistent Agent Knowledge, Gap, Gap-id, Origin, Spec Reader,
 Transient, Durable-pending, etc.). The terms below are plugin-local
@@ -100,8 +99,8 @@
   skills.
 - Not a substitute for the upstream invariant catalog. Doctor
   invariants that span the spec ⇆ impl boundary (per
-  `livespec/SPECIFICATION/contracts.md` §"Doctor cross-boundary
-  invariants") apply uniformly across all impl-plugins; this spec
+  `livespec/SPECIFICATION/contracts.md`) apply uniformly across all
+  impl-plugins; this spec
   describes what the plugin offers, not what doctor enforces.
 
 ## Lifecycle and evolution
```
