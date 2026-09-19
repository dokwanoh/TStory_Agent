from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import re
import shutil
import sys
from collections.abc import Generator


class RunBlocked(Exception):
    pass


class Arguments(argparse.Namespace):
    action: str = "status"
    session: str = ""
    run: str = ""
    idle_confirmed: bool = False


def identifier(value: str) -> str:
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,100}", value) is None:
        raise RunBlocked("INVALID_ID")
    return value


def count_at(path: Path) -> int:
    safe_path(path)
    match = re.fullmatch(r'\s*\{\s*"count"\s*:\s*(0|[1-9][0-9]*)\s*\}\s*', path.read_text())
    if match is None:
        raise RunBlocked("INVALID_COUNTER")
    return int(match[1])


def atomic_write(path: Path, value: str) -> None:
    safe_path(path)
    temporary = path.with_name(path.name + ".new")
    with temporary.open("x") as stream:
        _ = stream.write(value)
        stream.flush()
        os.fsync(stream.fileno())
    _ = temporary.replace(path)


@contextmanager
def locked(path: Path) -> Generator[None, None, None]:
    safe_path(path)
    with path.open("a") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RunBlocked("LIFECYCLE_BUSY") from error
        yield


def safe_path(path: Path) -> None:
    current = Path.cwd()
    for part in path.relative_to(current).parts:
        current /= part
        if current.is_symlink():
            raise RunBlocked("SYMLINK_REJECTED")


def operate(args: Arguments) -> str:
    session = Path.cwd() / ".omo" / "ulw-loop" / identifier(args.session)
    _ = identifier(args.run)
    safe_path(session)
    counter = session / "spawn-count.json"
    if not (session / "goals.json").is_file() or counter.is_symlink() or session.is_symlink():
        raise RunBlocked("SESSION_STATE_UNAVAILABLE")
    runs = session / "spawn-runs"
    safe_path(runs)
    runs.mkdir(exist_ok=True)
    with locked(runs / "lock"):
        return operate_locked(args, runs, counter)


def operate_locked(args: Arguments, runs: Path, counter: Path) -> str:
    count = count_at(counter)
    run = runs / args.run
    latest = runs / "latest"
    pending = runs / "pending"
    for path in (run, latest, pending):
        safe_path(path)
    if pending.exists():
        raise RunBlocked("INCOMPLETE_ROTATION: reconcile archived state; never blindly reset")
    active = identifier(latest.read_text().strip()) if latest.exists() else None
    if args.action == "status":
        return json.dumps({"run_id": active, "count": count, "run_requested": args.run})
    if not args.idle_confirmed:
        raise RunBlocked("FRESH_NO_LIVE_CHILDREN_CHECK_REQUIRED")
    if args.action == "close":
        if active != args.run:
            raise RunBlocked("RUN_ID_MISMATCH")
        closed = run / "closed.json"
        if closed.exists():
            if count_at(closed) != count:
                raise RunBlocked("COUNTER_DRIFT")
        else:
            atomic_write(closed, counter.read_text())
        return json.dumps({"run_id": args.run, "status": "closed", "count": count})
    if active == args.run:
        if (run / "closed.json").exists():
            raise RunBlocked("CLOSED_RUN_CANNOT_REOPEN")
        return json.dumps({"run_id": args.run, "status": "resumed", "count": count})
    if run.exists():
        raise RunBlocked("RUN_ID_ALREADY_USED")
    if active is not None:
        closed = runs / active / "closed.json"
        if not closed.exists():
            raise RunBlocked("ACTIVE_RUN: finish existing operation before starting another")
        if count_at(closed) != count:
            raise RunBlocked("COUNTER_DRIFT: untracked spawn after close")
    if args.action == "adopt" and active is not None:
        raise RunBlocked("ADOPT_IS_BOOTSTRAP_ONLY")
    if args.action == "begin" and active is None:
        raise RunBlocked("BOOTSTRAP_ADOPT_REQUIRED")
    atomic_write(pending, args.run)
    run.mkdir()
    _ = shutil.copy2(counter, run / "before.json")
    atomic_write(run / "started.txt", datetime.now(timezone.utc).isoformat())
    if args.action == "begin":
        atomic_write(counter, '{"count":0}\n')
        count = 0
    atomic_write(latest, args.run)
    pending.unlink()
    return json.dumps({"run_id": args.run, "status": args.action, "count": count})


def main() -> int:
    parser = argparse.ArgumentParser(description="Project-controlled OMO operation budget lifecycle")
    _ = parser.add_argument("action", choices=("adopt", "begin", "close", "status"))
    _ = parser.add_argument("--session", required=True)
    _ = parser.add_argument("--run", required=True)
    _ = parser.add_argument("--idle-confirmed", action="store_true",
                            help="Attest a fresh native agent inventory contains no running children")
    args = parser.parse_args(namespace=Arguments())
    try:
        print(operate(args))
    except (RunBlocked, OSError) as error:
        print(json.dumps({"status": "blocked", "reason": str(error)}), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
