# TStory_Agent

TISTORY GROWTH OS automation, introduced in independently testable slices.

## Install for Codex

Give Codex this repository and ask:

> Install the Tistory Growth OS skill from `dokwanoh/TStory_Agent`, path `skills/tistory-growth-os`.

Codex can install the skill with its built-in skill installer. It becomes available
on the next Codex turn. For an even shorter request after sharing this repository,
say: **“Install this repository's Codex skill.”** The root `AGENTS.md` contains
the project-wide rules when Codex is working in a checkout.

The Python command-line package is separate from the Codex skill. To install it
from a checkout:

```sh
python3 -m pip install .
tistory-growth-os --help
```

To install directly from GitHub:

```sh
python3 -m pip install "git+https://github.com/dokwanoh/TStory_Agent.git"
tistory-growth-os --help
```

The skill provides the repository workflow and safeguards; installing it does
not transfer a publisher login, Chrome profile, API keys, or permission to
publish. The current Python package provides local/offline commands and does
not itself sign in to Tistory or publish articles.

The project uses Python 3.11+ and the standard library. With pytest already available:

```sh
PYTHONPATH=src pytest -q
```

See [the guard contract](docs/30_save_intent_guard.md) and
[repository delivery policy](docs/31_repository_delivery.md).

The feature branch also preserves the earlier offline MVP, contracts, tests and
project memory. This is an unmerged import: a legacy status-document test still
fails because it rejects the word `published` even in a negative diagnostic.
Do not interpret that known failure as waived or this branch as merge-ready.
No credentials, browser state, generated articles or runtime databases belong
in this repository. Local account labels and home paths are redacted.

## Latest editorial instructions and records

The [2026-10-10 session archive](docs/history/2026-10-10-session-preservation/README.md) preserves the current goal, post223 editorial layout, native-editor success/recovery paths and final publication ledger through post244. Coding Agent goal240–244 is complete; Tistory app confirmation remains unverified. Generated article/media bytes stay local; the archive includes sanitized records and a media hash manifest.
