# TStory_Agent

TISTORY GROWTH OS automation, introduced in independently testable slices.

The first tracked slice is a local SQLite save-intent guard, not a live publisher.
It uses Python 3.11+ and the standard library. With pytest already available:

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
