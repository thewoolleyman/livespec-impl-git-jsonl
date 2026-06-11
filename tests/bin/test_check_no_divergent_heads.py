"""Per-wrapper coverage test for bin/check_no_divergent_heads.py."""

from collections.abc import Callable


def test_check_no_divergent_heads_wrapper_threads_exit_code(
    wrapper_runner: Callable[[str, str, int], None],
) -> None:
    wrapper_runner(
        "check_no_divergent_heads.py",
        "livespec_impl_git_jsonl.checks.no_divergent_heads",
        1,
    )
