# TStory_Agent

TISTORY GROWTH OS automation, introduced in independently testable slices.

The first tracked slice is a local SQLite save-intent guard, not a live publisher.
It uses Python 3.11+ and the standard library. With pytest already available:

```sh
PYTHONPATH=src pytest -q
```

See [the guard contract](docs/30_save_intent_guard.md) and
[repository delivery policy](docs/31_repository_delivery.md).

Earlier offline MVP code and operational documents remain in the owner's local
workspace pending a separate inspected import. They are not part of this initial
slice. No credentials, browser state, generated articles or runtime databases
belong in this repository.
