# Integrated saved-reservation observation

`read_saved_reservation(page, manager, tags)` composes existing typed readers into
one `SavedReservationSnapshot`. It performs no clicks, navigation, edits or saves.

Required caller sequence: freshly observe the exact manager row; open its saved
editor; read tags before opening the publish dialog; open the dialog without edits;
call this reader. The modal hides tag links from accessibility queries, so a same-ID
pre-dialog tag snapshot is required. Caller freshness and no-intervening-edit rules
are not cryptographically authenticated by this value object.

The reader requires manager reservation marker with unknown list visibility,
PUBLIC in the editor, equal scheduled time, matching title and numeric/slug URL,
four editor images/alts, same-ID tags, and one visible representative thumbnail.
The observed `img1.daumcdn.net/thumb/C170x170/` thumbnail contains exactly one fname
whose full decoded URL must equal exactly one body image source. No pixel checks,
downloads, URL rewriting or signature removal. Unknown formats return None.
Repeated content/settings/thumbnail reads detect changes within the sampling window;
the observation is sequential, not an atomic platform transaction.

## Evidence, 2026-09-13

- First requested-module absence produced RED collection error.
- Initial fixture had a zero-size empty thumbnail span; actual thumbnail includes a
  delete control. Initial live composition found body/settings but no tags after
  opening the modal. Corrected fixture shape and pre-dialog tag sampling, not gates.
- New11browser cases pass in11.22s: identity/time/title/slug disagreement,
  nonreservation, absent/foreign/unknown thumbnail, duplicate fname and missing tags.
- Types0errors, compilation exit0, programming checker clean2files.
- Combined integrated/editor/tags/settings/manager Chrome regression:73passed in63.23s.
- Full offline278pass/1pre-existing STATUS substring failure in11.96s. Not waived.
- Actual80: scheduled2026-09-13T19:00+09:00, 스포츠/스포츠일반,4media,4tags,
  representative_index0. Complete second snapshot after cancel/reload/reopen equals
  the first, with freshly sampled tags.
- Native body SHA256: df111eebf2400176b4ad14a3f32f4beb5a755edac9038e75a555a556fbe62ae6.
- No final save/upload/editor content change/scheduler mutation. Profile closed
  normally; no signed image references or debug artifacts committed.

## Remaining boundary

This is coherent saved-state observation, not proof of source rights, reviewed
package equivalence, authenticated approval, future public release, freshness of
caller-supplied snapshots or a complete ReservationObservation for the executor.
Local asset IDs must be bound to uploaded sources and expected editor bytes before
using the result to verify a new delivery. Actual prepare/upload/save adapter and
one-program E2E remain unfinished. No scheduler cutover or new article in this step.
