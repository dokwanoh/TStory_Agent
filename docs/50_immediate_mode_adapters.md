# Immediate-public input and readback contracts

2026-09-20. Implements the first local increment of docs/49_immediate_publication_mode.md. No live article, existing-post mutation or recurring restart occurred.

## Implemented

- `configure_immediate_publication`: operates only on the normal new-editor URL with an already open, matching publish panel. Requires exact title/category/home-topic/tags, selects the visible public radio and current-time button, and verifies selected current mode. Default dry-run does nothing. Never clicks reservation or final publish. It does not substitute for body/media review or authority.
- `ImmediateTarget` and `ImmediateObservation`: bind numeric saved identity, exact structured content, save start, publication/readback time, visibility and anonymous-public evidence without a scheduled slot. Verification rejects missing/stale/future/naive evidence, wrong identity/content, scheduled/private visibility and absent anonymous-public evidence. Tistory minute precision is allowed only from the minute containing the actual save start.

The observation is a typed input contract, not fabricated evidence. A future adapter must populate it from authenticated saved-content plus independent anonymous-public reads. Setting a boolean in a fixture is not proof of production public access.

## Verification

Both new boundaries were tested failing first: absent current-mode function, absent immediate target contract. GREEN:13immediate-readback unit cases plus6current-panel Chrome cases;46total related cases including existing reservation settings and integrated native save fixtures. All browser traffic was intercepted; no remote write. Changed source/tests type check:0errors/0warnings. Compileall, no-excuse checker and diff check passed. Existing source patterns and dependencies remain unchanged; both edited/new production modules are under200nonblank/noncomment lines.

Full suite:502passed/1pre-existing failure in143.52s. `tests/test_memory_documents.py::test_status_does_not_claim_unearned_completion` still rejects a historical word in STATUS.md. No gate was waived or test removed; full suite is not green.

## Remaining integration, explicitly not certified

The current native CLI still executes the reservation contract and remains stopped. Connect a distinct immediate intent/authority and journal identity, full new-editor preparation, one final save, persisted receipt and real anonymous observation before claiming an independent immediate-public run. Do not fake an08/12/19slot or turn a scheduled receipt into immediate authority. The paused scheduler and runtime STOP remain unchanged. Post93 is not edited, re-created or accelerated.

No library, service, permission or account configuration was changed. No print, Lighthouse, external-ad, narration or excluded image-pixel lane was restored.
