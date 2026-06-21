#!/usr/bin/env python3
"""Shebang wrapper for check-no-divergent-heads. No logic; see livespec_orchestrator_git_jsonl.checks.no_divergent_heads."""

from _bootstrap import bootstrap

bootstrap()

from livespec_orchestrator_git_jsonl.checks.no_divergent_heads import main

raise SystemExit(main())
