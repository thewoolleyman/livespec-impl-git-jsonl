---
topic: codex-support-constraints
author: codex-gpt-5
created_at: 2026-06-19T17:47:03Z
---

## Proposal: Codex adapter and hook support constraints

### Target specification files

- SPECIFICATION/constraints.md

### Summary

State how Codex support applies to the git-jsonl implementation plugin without copying Claude-specific skill bodies.

### Motivation

The family-wide Codex audit found that impl-plugin specs mention AGENTS.md/Codex only in persistent-knowledge loading, but do not state the required Codex adapter boundary or hook/manual-verification expectations.

### Proposed Changes

In `SPECIFICATION/constraints.md`, add a bullet under the existing `## Skill orchestration constraints` section. The text should state that Codex support is required as a first-class agent-runtime consideration, that Codex adapters must be thin runtime bindings over the same wrapper CLIs / store semantics rather than copies of Claude SKILL.md bodies, that thin-transport behavior remains zero-orchestration, that Claude-only hooks are not assumed to run under Codex, and that any Codex adapter or hook replacement must be manually verified before support is claimed.
