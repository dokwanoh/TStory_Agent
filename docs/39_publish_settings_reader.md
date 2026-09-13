# Existing publication settings reader

Checked 2026-09-13. `delivery/playwright_publish_settings.py` reads an already open normal publish dialog on the exact HTTPS nedamma numeric editor identity. It returns the title, selected visibility setting, home topic, existing date/time in Asia/Seoul and URL slug. It performs no clicks, navigation, input, upload or save.

The observed existing-date control is `.btn_date.on` with a full timestamp. A selected 현재/예약 label, malformed date, unknown visibility, absent/ambiguous fields, wrong ID/origin or unsafe slug returns None. This deliberately does not read proposed reservation inputs or infer stored state from default values. SDK exceptions propagate.

## Evidence

- Failing-first test: module absent before implementation.
- Synthetic real-Chrome tests:13passed in12.32s. All fixture network requests fulfilled locally; the reader issued no writes.
- Actual79: PUBLIC setting, home스포츠일반, existing2026-09-13T12:00+09:00 and expected title/slug. Cancel panel, explicit reload and reopen produced an equal snapshot. No final save or field changes.
- basedpyright:0errors/0warnings; compileall exit0; programming checker no violations in2files.
- Dedicated browser closed normally after inspection; profile preserved. No scheduler changes.

## Limits and next integration

This snapshot is not proof of future reservation or anonymous release, nor an atomic transaction. The caller must open a fresh saved editor without intervening edits, bind it to native content/media, category, tags and representative identity, and compare the intended release. Current79 is already public; it is not a new reservation test. Signed media references must not be included in diagnostic markup dumps; this reader selects only the required text/input fields and does not inspect thumbnail CSS.

Remaining: tags/representative binding; reviewed body/media input; reservation-input state; one-shot save; full independent readback. Keep existing scheduler as sole writer until separately verified/approved cutover. No fresh article was created in this slice.
