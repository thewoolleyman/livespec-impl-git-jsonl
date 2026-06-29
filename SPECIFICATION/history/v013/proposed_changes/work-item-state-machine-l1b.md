---
topic: work-item-state-machine-l1b
author: claude-opus-4-8-l1b
created_at: 2026-06-29T14:15:43Z
---

## Proposal: Migrate the work-items JSONL schema to the lifecycle state machine (L1b)

### Target specification files

- contracts.md

### Summary

L1b slice of the fleet work-item-lifecycle epic (anchor `bd-gj-45liqm`,
prose-linked to fleet anchor `livespec-35s3zo`). Migrate this plugin's
`## Work-items JSONL record schema` to the shared lifecycle model that
livespec-runtime v0.5.0 ships: the seven-state `status` enum replaces the
legacy five values, `rank` (a fractional/lexicographic key) becomes the
sole ordering authority, and `priority` is removed.

### Motivation

livespec-runtime **v0.5.0** (the artifact this plugin vendors) lands the
deterministic work-item state machine: a 7-state `WorkItemStatus`
(`backlog · pending-approval · ready · active · acceptance · blocked ·
done`), a required non-null `rank: str` (replacing `priority`), and the
shared `BOTTOM_SENTINEL` constant. Because this plugin validates `status`
against the vendored `WorkItemStatus` Literal and carries a closed-key
JSONL record schema in this `contracts.md`, the schema must move in
lockstep with the runtime bump (the standing "required-key schema change
is a cross-repo epic" rule; the shared validator otherwise renders the
store unreadable). Authority: the cross-repo design of record
(`livespec/plan/work-item-state-machine/research/02-design.md` §2/§5/§6
"Backend mapping" git-jsonl column + consequence (d); `03-decision-log.md`
decisions 24/32/36/39/44; `04-slice-plan.md` "L1b").

### Proposed Changes

Under `## Work-items JSONL record schema` (no `## ` heading added,
changed, or removed — so `tests/heading-coverage.json` needs no co-edit;
the shared check tracks H2 only):

1. **Key count + categories** — the canonical schema is **seventeen**
   keys. Fourteen (`id`, `type`, `status`, `title`, `description`,
   `origin`, `gap_id`, `assignee`, `depends_on`, `captured_at`,
   `resolution`, `reason`, `audit`, `superseded_by`) are
   required-on-write AND required-on-read; `rank` is required-on-write
   but optional-on-read (sentinel-substituted for legacy lines);
   `spec_commitment_hint` and `supersedes` stay optional-on-read.
   (Corrects the prior prose's "sixteen"/"first fourteen" undercount —
   the section enumerated 17 bullets.)
2. **`status`** — the seven livespec lifecycle states (was
   `open/in_progress/blocked/closed/deferred`), validated against the
   vendored `WorkItemStatus` Literal. `blocked` is a name-matched reuse;
   `done` is the terminal closure state (was `closed`).
3. **`+ rank`** — new key (after `gap_id`): the fractional/lexicographic
   ordering key, the sole ordering authority; required non-null on write;
   a legacy record lacking it reads back as
   `livespec_runtime.work_items.rank.BOTTOM_SENTINEL` via the store
   adapter; every live head MUST carry a real non-sentinel rank
   (doctor-checkable).
4. **`− priority`** — removed (two order sources = two conflicting
   truths; decision 39).
5. The three abstract `WorkItem` policy fields the runtime adds
   (`admission_policy`/`acceptance_policy`/`blocked_reason`) are NOT
   persisted by this realization (Dispatcher/admission concerns this
   plugin does not run); they default to `null` on read.
6. **Terminal-state rename `closed → done`** wherever the schema and its
   sibling sections reference closure: the `resolution`/`#### implement`
   closing records (`status: done`), the `### Materialized view`
   terminal clause, and the `### work_item_merge_evidence` static check.
7. **`#### next` ranking** — order by `rank` then `id` (the
   `priority → gap-tied → captured_at` heuristic is retired); ready =
   `status: ready` with deps empty/all-`done`; `urgency` becomes a
   uniform advisory `medium` (priority-tier derivation retired —
   `urgency` is an impl-specific advisory field the cross-plugin contract
   does not prescribe); candidates emit `rank` not `priority`.
8. **`#### list-work-items` filters** — `--filter=ready` = `status:
   ready` + deps empty/all-`done`; `--filter=closed` matches the terminal
   `status: done` (the CLI token stays `closed`); `--filter=blocked`
   unchanged.
9. **`#### capture-work-item`** — drop the `priority` input; freeform
   records file with a fresh `rank` (create position).
