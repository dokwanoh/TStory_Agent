# Reservation automation slice B

Implemented local library: `delivery/reservation_readback.py`.

## Machine-owned decisions

- Generate three canonical daily slot identities for nedamma.tistory.com:08:00,12:00,19:00Asia/Seoul; preparation is three hours earlier.
- Reject a naive timezone, extra daily release time or seconds hidden behind the same minute key.
- Compare expected and observed post ID, URL, release instant, scheduled visibility, title, body SHA-256, four ordered asset identities/alts, representative, category, home topic and tags.
- Missing readback, future observation time, observation age of five minutes or more, or an elapsed release deadline returns UNKNOWN. Exactly matching future reservation returns VERIFIED; mismatches return MISMATCH with field names.
- This VERIFIED means only reservation-record equivalence, never public release or overall editorial approval. The five-minute TTL is a conservative initial local hypothesis; real adapter latency is unmeasured.

## Trust and integration boundary

No network, browser, model call, paid service or scheduler registration occurs.
These are typed internal records, not an untrusted JSON parser or an authenticated
review receipt. The future normal-editor adapter must independently read saved
fields, map uploaded asset IDs to the reviewed local assets and provide the
same canonical body representation used for the expected SHA-256. It must never
populate observations by copying expected fields. Partial/unavailable reads must
be held, not padded with defaults. Media identity checks do not restore the
owner-excluded pixel/lightbox/print tests.

The caller still owns package review binding, 24-hour event freshness at release,
rights/policy checks, save-intent recording before editor autosave, persistent
observations, the runtime clock, kill switch and single-writer coordination.
Category=None represents an explicitly chosen absence, not permission to skip a
required classification. No such authority is created by constructing a record.

## Executed local rehearsal

`PYTHONPATH=src pytest -q tests/test_reservation_readback.py tests/test_save_intents.py`
returned40passed. Three additional invalid-slot tests failed before the slot
constructor guard was added, then passed. basedpyright returned0errors/0warnings.

A direct library driver used the synthetic noon slot, four synthetic media IDs
and a temporary real SQLite journal. Matching observation → VERIFIED; changed
body → MISMATCH/body_digest; lost readback → UNKNOWN/missing_readback; reopening
the journal rejected retry. external_write_count=0, model_calls=0. This is a
local library/database scenario, not Tistory E2E certification.

Next: approved Python Playwright environment and independent saved-editor reader,
then durable observation/reconciliation integration and a bounded live rehearsal.
No automatic installation, personal-profile reuse or scheduler cutover.
