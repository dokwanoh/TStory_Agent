import argparse
import fcntl
import json
from hashlib import sha256
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
from .publication import PublicationGrant
from .enrichment import REWORK_NEEDED
from .source_capture import capture_sources


class Arguments(argparse.Namespace):
    root: str = '.'
    run_id: str = ''
    execute: bool = False
    publish_grant: str = ''


def main() -> int:
    parser = argparse.ArgumentParser(description='Prepare one reviewed Tistory package; optionally hand off an explicitly authorized immediate publication.')
    _ = parser.add_argument('--root', default='.')
    _ = parser.add_argument('--run-id', required=True)
    _ = parser.add_argument('--execute', action='store_true', help='Run bounded existing-account research/writing/media/review')
    _ = parser.add_argument('--publish-grant', default='', help='Project-relative one-run owner publication grant; never removes STOP')
    args = parser.parse_args(namespace=Arguments())
    try:
        if re.fullmatch(r'[a-z0-9][a-z0-9_-]{2,60}', args.run_id) is None:
            raise PreparationError('invalid_run_id')
        root = Path(args.root).resolve()
        directory = safe_output_root(root, '.artifacts/preparation/' + args.run_id)
        if not args.execute:
            print(json.dumps({'state': 'dry_run', 'run_id': args.run_id,
                'stages': ['research', 'opportunity', 'evidence', 'selection', 'writing', 'text_review', 'media', 'review'],
                'model_calls': 0, 'external_write_count': 0, 'publication_authorized': False}))
            return 0
        run = PreparationRun(root, directory, args.run_id, utc_now)
        grant = PublicationGrant.read(run, safe_output_root(root, args.publish_grant)) if args.publish_grant else None
        directory.mkdir(parents=True, exist_ok=True)
        with (directory / 'run.lock').open('a') as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise PreparationError('run_locked') from None
            initial = directory / 'input.json'
            if not initial.exists():
                pool = capture_sources(directory, utc_now())
                feed = collect_live()
                write_immutable(directory / 'signals.rss', feed)
                write_immutable(initial, json.dumps({'run_id': args.run_id,
                    'cutoff': utc_now().isoformat(), 'signals': feed.decode('utf-8')
                    + '\nPrior UNVERIFIED research leads (not approved evidence; re-open sources and '
                    + 'requalify all facts/timestamps, ignore previous check status):\n' + prior_research_leads(root),
                    'history': history_snapshot(root), 'source_pool_sha256': sha256(pool.encode()).hexdigest()}, ensure_ascii=False).encode())
            package = execute(run, codex_provider)
            if grant is not None:
                return grant.publish(package)
            print(json.dumps({'state': 'local_package_reviewed', 'package': str(package),
                'publication_authorized': False, 'external_blog_write_count': 0}))
        return 0
    except (PreparationError, ArtifactWriteError, JsonDecodeError, OSError, ImportError,
            subprocess.TimeoutExpired, UnicodeError, ValueError) as error:
        reason = error.code if isinstance(error, PreparationError) else type(error).__name__
        state = 'needs_enrichment' if reason in REWORK_NEEDED else 'held'
        print(json.dumps({'state': state, 'reason': reason, 'retry_safe': False,
            'next_action': 'preserve checkpoints; remedy the recorded defect before fresh review'
            if state == 'needs_enrichment' else 'reconcile authority, runtime or checkpoint integrity',
            'publication_eligible': False}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
