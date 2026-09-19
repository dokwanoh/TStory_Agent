from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("spawn_run.py")


class SpawnRunTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sandbox = tempfile.TemporaryDirectory()
        self.addCleanup(self.sandbox.cleanup)
        self.root = Path(self.sandbox.name)
        self.session = self.root / ".omo/ulw-loop/test-session"
        self.session.mkdir(parents=True)
        self.counter = self.session / "spawn-count.json"
        self.counter.write_text('{"count":78}')
        (self.session / "goals.json").write_text('{"goals":[]}')
        self.assertEqual(self.invoke("adopt", "legacy").returncode, 0)
        self.assertEqual(self.invoke("close", "legacy").returncode, 0)

    def invoke(self, action: str, run: str = "20260920-0800-prepare") -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), action, "--session", "test-session",
             "--run", run, "--idle-confirmed"],
            cwd=self.root, text=True, capture_output=True, check=False,
        )

    def test_new_run_archives_old_count_and_resets_live_counter(self) -> None:
        result = self.invoke("begin")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(self.counter.read_text()), {"count": 0})
        backups = list(self.session.glob("spawn-runs/*/before.json"))
        self.assertEqual(len(backups), 2)
        self.assertEqual(backups[0].read_text(), '{"count":78}')

    def test_same_run_resume_preserves_exhausted_budget(self) -> None:
        self.assertEqual(self.invoke("begin").returncode, 0)
        self.counter.write_text('{"count":60}')
        result = self.invoke("begin")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"count": 60', result.stdout)
        self.assertEqual(json.loads(self.counter.read_text()), {"count": 60})

    def test_another_run_cannot_erase_active_budget(self) -> None:
        self.assertEqual(self.invoke("begin").returncode, 0)
        result = self.invoke("begin", "20260920-1200-prepare")
        self.assertEqual(result.returncode, 2)
        self.assertIn("ACTIVE_RUN", result.stderr)

    def test_closed_run_cannot_reopen_but_next_run_can_begin(self) -> None:
        self.assertEqual(self.invoke("begin").returncode, 0)
        self.counter.write_text('{"count":3}')
        self.assertEqual(self.invoke("close").returncode, 0)
        self.assertEqual(self.invoke("begin").returncode, 2)
        self.assertEqual(self.invoke("begin", "20260920-1200-prepare").returncode, 0)
        self.assertEqual(json.loads(self.counter.read_text()), {"count": 0})

    def test_unknown_counter_blocks_without_reset(self) -> None:
        self.counter.write_text("broken")
        result = self.invoke("begin")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(self.counter.read_text(), "broken")

    def test_post_close_untracked_spawn_blocks_next_run(self) -> None:
        self.assertEqual(self.invoke("begin").returncode, 0)
        self.assertEqual(self.invoke("close").returncode, 0)
        self.counter.write_text('{"count":1}')
        result = self.invoke("begin", "20260920-1200-prepare")
        self.assertEqual(result.returncode, 2)
        self.assertIn("COUNTER_DRIFT", result.stderr)

    def test_interrupted_rotation_blocks_replay(self) -> None:
        runs = self.session / "spawn-runs"
        (runs / "pending").write_text("interrupted")
        result = self.invoke("begin")
        self.assertEqual(result.returncode, 2)
        self.assertIn("INCOMPLETE_ROTATION", result.stderr)

    def test_missing_idle_evidence_blocks_mutation(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "begin", "--session", "test-session",
             "--run", "20260920-0800-prepare"],
            cwd=self.root, text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 2)
        self.assertEqual(self.counter.read_text(), '{"count":78}')

    def test_missing_ledger_requires_adopt_without_reset(self) -> None:
        (self.session / "spawn-runs/latest").unlink()
        result = self.invoke("begin")
        self.assertEqual(result.returncode, 2)
        self.assertIn("BOOTSTRAP_ADOPT_REQUIRED", result.stderr)
        self.assertEqual(self.counter.read_text(), '{"count":78}')

    def test_symlinked_run_storage_is_rejected(self) -> None:
        runs = self.session / "spawn-runs"
        moved = self.root / "moved"
        runs.rename(moved)
        runs.symlink_to(moved, target_is_directory=True)
        result = self.invoke("begin")
        self.assertEqual(result.returncode, 2)
        self.assertIn("SYMLINK_REJECTED", result.stderr)

    def test_real_stock_hook_keeps_cap_across_resume_and_rotates_next_run(self) -> None:
        cli = os.environ.get("TISTORY_TEST_OMO_CLI")
        if cli is None:
            self.skipTest("Installed OMO integration requires TISTORY_TEST_OMO_CLI")
        self.assertEqual(self.invoke("begin").returncode, 0)
        self.counter.write_text('{"count":60}')
        self.assertEqual(self.invoke("begin").returncode, 0)
        payload = json.dumps({
            "cwd": str(self.root), "hook_event_name": "PreToolUse",
            "model": "test", "permission_mode": "default", "session_id": "test-session",
            "tool_input": {"message": "bounded scan"}, "tool_name": "collaboration.spawn_agent",
            "tool_use_id": "test-one", "transcript_path": None, "turn_id": "test-turn",
        })
        denied = subprocess.run(["node", cli, "hook", "pre-tool-use-spawn"],
                                input=payload, text=True, capture_output=True, check=True)
        self.assertIn("61/60", denied.stdout)
        self.assertEqual(self.invoke("close").returncode, 0)
        self.assertEqual(self.invoke("begin", "20260920-1200-prepare").returncode, 0)
        allowed = subprocess.run(["node", cli, "hook", "pre-tool-use-spawn"],
                                 input=payload, text=True, capture_output=True, check=True)
        self.assertEqual(allowed.stdout, "")
        self.assertEqual(json.loads(self.counter.read_text()), {"count": 1})


if __name__ == "__main__":
    unittest.main()
