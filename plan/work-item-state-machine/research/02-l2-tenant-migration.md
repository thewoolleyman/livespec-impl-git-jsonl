# L2 — tenant migration (livespec-orchestrator-git-jsonl beads tenant)

The L2 step of the fleet 9-tenant lockstep migration, for THIS repo's own
beads tenant (`livespec-orchestrator-git-jsonl`). It carries no product
code/spec change (the schema + tooling shipped in L1b/L1a) — only the data
migration of the tenant, captured here in history per
`livespec/plan/work-item-state-machine/research/04-slice-plan.md` "L2" and
`03-decision-log.md` decisions 36 + 39.

**Done — the tenant is migrated.** Verified: all live heads carry a real,
non-sentinel `rank`; the 5 custom lifecycle statuses are registered.

## What was applied

1. **Custom-status registration** (decision 36 consequence (a)). The 5
   livespec lifecycle states that map to beads CUSTOM statuses were
   registered on the tenant:

   ```bash
   bd config set status.custom "backlog,pending-approval,ready:active,active:wip,acceptance:wip"
   ```

   (`blocked` is a name-matched built-in reuse; `done → closed` is the
   native-closure built-in reuse — neither is a custom status, so the set
   is exactly 5.)

2. **`rank` backfill** (decision 39) via the beads-fabro
   `rebalance-ranks` **legacy-seed** primitive — `legacy_seed(rows)`:
   order the pre-migration rows by the legacy `priority → captured_at →
   id` key and assign evenly-spaced fractional keys
   (`livespec_runtime.work_items.rank.n_keys_between`), then write each
   `rank` in place via `update_work_item_rank` (`metadata.rank`),
   preserving every item's audit/status/edges. Result (4 items):

   | seed order (`priority → captured_at → id`) | id | rank |
   |---|---|---|
   | 1 | `bd-gj-45liqm` (epic; P1) | `a0` |
   | 2 | `bd-gj-ol5hmu` (code; P1) | `a1` |
   | 3 | `bd-gj-clk` (test; P2) | `a2` |
   | 4 | `bd-gj-af4nsa` (release; P2) | `a3` |

   Every live head now reads back a real `rank` (no `BOTTOM_SENTINEL`
   `~`); the sentinel only ever surfaces for superseded historical lines.

3. **Conformance cleanup.** The one remaining pre-migration `open` item
   `bd-gj-clk` (a disposable "TEST: verify filing works (safe to delete)"
   filing-test row) was closed administratively, so the tenant holds only
   conformant lifecycle states (all four items are `done`/`closed`).

## Notes

- **Tooling source.** The `rebalance-ranks` legacy-seed primitive ships in
  the **L1a** `livespec-orchestrator-beads-fabro` build that re-vendored
  `livespec_runtime` v0.5.0 (the build carrying
  `commands/rebalance_ranks.py` + `store.update_work_item_rank`). It was
  driven directly against this tenant under the family env wrapper
  (`with-livespec-env.sh`); no change to this repo's
  `.livespec.jsonc`/orchestrator pin was required for the migration (the
  "bump the orchestrator pin if needed" caveat did not apply — the tooling
  ran from the L1a build directly).
- **Secrets** were probe-only (the bare `BEADS_DOLT_PASSWORD` injected by
  the wrapper); never echoed, never committed.
- **Downstream (NOT this repo):** the other 8 tenants (the 7 remaining
  fleet tenants + the OpenBrain adopter) migrate in the same lockstep, and
  the fleet exit gate (delete `.claude/skills/overseer/`) lives on the core
  anchor `livespec-35s3zo`. The coordinator drives those.
