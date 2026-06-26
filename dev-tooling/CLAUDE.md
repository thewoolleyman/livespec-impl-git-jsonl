# dev-tooling/

Standalone git-hook + worktree-discipline shell scripts installed by
`just bootstrap` (the commit-refuse hook via `just
install-commit-refuse-hooks`) into `.git/hooks/`. Unlike the `livespec`
repo, this plugin does NOT host its own Python enforcement checks here
— the shared checks live in the vendored `livespec_dev_tooling`
package and are invoked through the `mise exec -- just check-*` targets
in the `justfile`.

- `git-hook-wrapper.sh` — the structural commit-refuse hook installed
  at `.git/hooks/pre-commit`, `.git/hooks/pre-push`, AND
  `.git/hooks/commit-msg`. It refuses commits/pushes at the primary
  checkout STRUCTURALLY (when `git rev-parse --git-dir` equals `git
  rev-parse --git-common-dir`) — armed on install, with no
  `livespec.primaryPath` arming step and so no fail-open window — then
  delegates to mise-managed lefthook at secondary worktrees (and in
  declared-exempt Fabro sandboxes that set `git config
  livespec.sandboxExempt true`) via `mise exec -- lefthook run
  --no-auto-install "$HOOK_NAME"`. The basename of `$0` selects which
  hook's command list fires from `lefthook.yml`. The doctor invariant
  `primary-checkout-commit-refuse-hook-installed` recognizes its
  fingerprint — the marker comment `# livespec commit-refuse hook` + a
  `git rev-parse --git-common-dir` invocation + an `exit 1` branch —
  via substring match.
- `worktree-lib.sh` / `worktree-hydrate.sh` / `branch-protection.sh` —
  the Worktree Discipline Pack: the portable, pure-git worktree
  lifecycle core (create / hydrate / land / reap + primary-vs-linked
  detection), the ecosystem-specific hydrate hook stamped from the
  copier `ecosystem` answer, and the server-side branch-protection
  Installer/Verifier. Driven by the `just worktree-*` and `just
  protect-default-branch` / `just check-branch-protection` recipes.

Rules an agent editing this tree must follow:

- `--no-auto-install` on every `lefthook run` invocation is
  load-bearing: omitting it lets lefthook auto-sync `.git/hooks/`
  against its own standard wrapper, clobbering these custom scripts
  to `<name>.old` and silently disabling the gate. Never remove it.
- Keep these portable `#!/bin/sh` scripts; do NOT add bashisms or
  hard-code interpreter paths other than the mise/git invocations
  shown.
- Do NOT weaken the refuse-at-primary branch in `git-hook-wrapper.sh`
  — its marker comment, the `git-dir` == `git-common-dir` comparison,
  and the `exit 1` branch together form the fingerprint the doctor
  invariant matches.
- The task runner (`justfile`) is the single source of truth for
  dev-tooling invocations; hooks delegate via `lefthook` →
  `just <target>`, never by calling tools directly.
