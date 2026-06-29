# Handoff — work-item-state-machine (L1b, livespec-orchestrator-git-jsonl) — ✅ DONE

> # ✅ L1b COMPLETE — released as **v0.3.0** (tag `4fd3c124`).
> Epic `bd-gj-45liqm` is **CLOSED**; both children shipped. The whole L1b
> slice landed: spec ratified to **v013** (PR #148), the atomic code
> migration to the v0.5.0 lifecycle schema (PR #150), and the release
> (PR #151). Nothing further is required on this thread; it is kept for
> provenance (L0-precedent style). Detail in "State as of this handoff".

**Thread:** `plan/work-item-state-machine/` · **Ledger anchor:** epic
`bd-gj-45liqm` (`livespec-orchestrator-git-jsonl` beads tenant; **CLOSED**) ·
**Fleet anchor (prose ref):** `livespec-35s3zo` (livespec core tenant).

> Status is **derived from the ledger**, never stored here. To read it:
> ```bash
> with-livespec-env.sh bd show bd-gj-45liqm
> with-livespec-env.sh bd children bd-gj-45liqm --json   # the groomed slices
> ```
> (`with-livespec-env.sh` injects the tenant password; run from this repo
> root so `bd` resolves `.beads/config.yaml`.)

## Autonomy posture

Maintainer ASLEEP; full autonomous wrap-up authorized; design LOCKED
(decisions 1–46). **AUTO-PROCEED through `revise` + `groom` per the
locked design** — do NOT pause for approval. Halt + report ONLY on a
genuine blocker or a new decision the design does not resolve. Report at
each milestone.

## Read-first chain (cold-start)

1. `research/00-l1b-overview.md` — the slice, the anchor, the reframe,
   the autonomy posture, and the full read-first chain (incl. the
   cross-repo design of record + the L0 worked example).
2. `research/01-spec-delta.md` — the drafted `contracts.md` delta (the
   propose-change payload, human-readable).

## State as of this handoff

- ✅ Epic `bd-gj-45liqm` anchored (prose-linked to `livespec-35s3zo`; no
  typed cross-tenant `depends_on`), now **CLOSED**.
- ✅ Thread created; `00-l1b-overview.md` + `01-spec-delta.md` + this
  handoff committed (PR #147).
- ✅ **Spec gate** — `SPECIFICATION/contracts.md` ratified to **v013**
  (propose-change → revise; PR #148): schema 16→**17** keys (`+rank`,
  `−priority`), the 7-state `status` enum, terminal `closed→done`, `next`
  ranks by `rank`. All `doctor-static` checks pass.
- ✅ **Groom** — epic cut into 2 `ready` children: `bd-gj-ol5hmu` (code
  migration) → `bd-gj-af4nsa` (release). Both **CLOSED** with
  merge-evidence.
- ✅ **Code** — re-vendor `livespec_runtime` v0.4.0 → **v0.5.0**
  (`.vendor.jsonc` + `pyproject.toml` `[tool.uv.sources]` + `uv.lock`) +
  the consumer migration, landed atomically (PR #150, merge `4f911c58`):
  `store.py` 17 required-keys + `rank` + `BOTTOM_SENTINEL` adapter;
  `commands/next.py` `_sort_key → (rank, id)`; the forced collateral
  (`is_item_ready` `open→ready`; dep `done`; `list`/merge-evidence/
  `beads_to_jsonl` `closed→done`); tests + fixtures re-authored. Committed
  via the **green-verified leg** (`TDD-Suite-Green-*`); `just check` green
  (50 targets, 100% coverage).
- ✅ **Release** — **v0.3.0** cut (release-please PR #151; tag
  `4fd3c1245da0bf5f5d4cacd8600c4b50e81cea4e`; GitHub Release published;
  master green post-release). The artifact the L2 tenant migration
  consumes.

## Next action — NONE. ✅ L1b is COMPLETE.

All steps (spec → code → release) shipped; epic `bd-gj-45liqm` is CLOSED;
**v0.3.0** is released. Nothing remains on this thread.

**Downstream (NOT this thread):** the L2 migration (all 9 beads tenants +
the OpenBrain adopter) consumes this release; the fleet exit gate (delete
`.claude/skills/overseer/` once dogfooded) lives on the core anchor
`livespec-35s3zo`. The coordinator drives those.

## Discipline (non-negotiable)

- Every change via **worktree → PR → rebase-merge**; `mise exec -- git …`;
  **never `--no-verify`**; halt + report on any hook failure.
- Product `.py` follows this repo's **red-green-replay** ritual.
- Co-edit `tests/heading-coverage.json` for any `## `-heading change
  (this slice changes NO H2 heading, so no co-edit is required).
- Operate only in worktrees you create.
