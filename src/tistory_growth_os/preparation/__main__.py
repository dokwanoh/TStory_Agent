import argparse
import fcntl
import json
from pathlib import Path
import re
import subprocess
import sys

from ..artifacts.layout import ArtifactWriteError, safe_output_root
from ..contracts.json_decode import JsonDecodeError
from ..research.__main__ import collect_live
from .contracts import PreparationError
from .package import write_immutable
from .provider import codex_provider
from .runner import PreparationRun, execute, utc_now
from .storage import history_snapshot, prior_research_leads


class Arguments(argparse.Namespace):
    root: str = '.'
    run_id: str = ''
    execute: bool = False


def main() -> int:
    parser = argparse.ArgumentParser(description='Prepare one independently reviewed local Tistory package; never publishes.')
    _ = parser.add_argument('--root', default='.')
    _ = parser.add_argument('--run-id', required=True)
    _ = parser.add_argument('--execute', action='store_true', help='Run bounded existing-account research/writing/media/review')
    args = parser.parse_args(namespace=Arguments())
    try:
        if re.fullmatch(r'[a-z0-9][a-z0-9_-]{2,60}', args.run_id) is None:
            raise PreparationError('invalid_run_id')
        root = Path(args.root).resolve()
        directory = safe_output_root(root, '.artifacts/preparation/' + args.run_id)
        if not args.execute:
            print(json.dumps({'state': 'dry_run', 'run_id': args.run_id,
                'stages': ['research', 'selection', 'writing', 'media', 'review'],
                'model_calls': 0, 'external_write_count': 0, 'publication_authorized': False}))
            return 0
        directory.mkdir(parents=True, exist_ok=True)
        with (directory / 'run.lock').open('a') as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise PreparationError('run_locked') from None
            initial = directory / 'input.json'
            if not initial.exists():
                feed = collect_live()
                write_immutable(directory / 'signals.rss', feed)
                write_immutable(initial, json.dumps({'run_id': args.run_id,
                    'cutoff': utc_now().isoformat(), 'signals': feed.decode('utf-8')
                    + '\nPrior UNVERIFIED research leads (not approved evidence; re-open sources and '
                    + 'requalify all facts/timestamps, ignore previous check status):\n' + prior_research_leads(root),
                    'history': history_snapshot(root)}, ensure_ascii=False).encode())
            package = execute(PreparationRun(root, directory, args.run_id, utc_now), codex_provider)
            print(json.dumps({'state': 'local_package_reviewed', 'package': str(package),
                'publication_authorized': False, 'external_blog_write_count': 0}))
        return 0
    except (PreparationError, ArtifactWriteError, JsonDecodeError, OSError,
            subprocess.TimeoutExpired, UnicodeError, ValueError) as error:
        print(json.dumps({'state': 'held', 'reason': error.code if isinstance(error, PreparationError)
            else type(error).__name__, 'publication_authorized': False}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
