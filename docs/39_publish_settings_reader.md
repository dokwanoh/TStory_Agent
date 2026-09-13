# Existing publication settings reader

Checked 2026-09-13. `delivery/playwright_publish_settings.py` reads an already open normal publish dialog on the exact HTTPS nedamma numeric editor identity. It returns the title, selected visibility setting, home topic, existing date/time in Asia/Seoul and URL slug. It performs no clicks, navigation, input, upload or save.

The observed existing-date control is `.btn_date.on` with a full timestamp. That produces `existing_at` and `scheduled_at=None`. A selected 예약 label now requires unique visible `button.btn_reserve`, `input#dateHour[type=number]` and `input#dateMinute[type=number]`: strict calendar date and hour/minute produce `scheduled_at` with `existing_at=None`. 현재, malformed dates, unknown visibility, absent/ambiguous fields, wrong ID/origin or unsafe slug return None. These are form observations, not inferred stored state from default values. SDK exceptions propagate.

## Reservation-form extension, 2026-09-13

Actual80 normal panel exposes selected 예약, date button2026-09-13, hour19/minute00. Added8fixture cases: valid, missing hour, impossible date, invalid hour/minute, hidden/duplicate controls and current-mode rejection. RED1failed/20passed in17.82s; manager/settings39passed in34.33s after implementation. basedpyright0errors, compileall exit0, programming checker clean2files. Full offline278pass/1pre-existing status-substring failure in16.00s remains.

Actual SDK80 returned scheduled2026-09-13T19:00+09:00, PUBLIC setting, 스포츠일반, expected title/slug, existing_at=None. Cancel/reload/reopen comparison: `reload_equal True; manager_time_equal True; wrong_id_rejected True`. Independently read manager80 reservation time agrees. No field changes, final save, uploads or scheduler mutation. Dedicated browser closed normally. This is observation of the previously saved80 reservation, not a newly scheduled article or proof of public release at19:00.

## Evidence

- Failing-first test: module absent before implementation.
- Synthetic real-Chrome tests:13passed in12.32s. All fixture network requests fulfilled locally; the reader issued no writes.
- Actual79: PUBLIC setting, home스포츠일반, existing2026-09-13T12:00+09:00 and expected title/slug. Cancel panel, explicit reload and reopen produced an equal snapshot. No final save or field changes.
- basedpyright:0errors/0warnings; compileall exit0; programming checker no violations in2files.
- Dedicated browser closed normally after inspection; profile preserved. No scheduler changes.

## Limits and next integration

This snapshot is not proof of future reservation or anonymous release, nor an atomic transaction. The caller must open a fresh saved editor without intervening edits, bind it to native content/media, category, tags and representative identity, and compare the intended release. Current79 is already public; it is not a new reservation test. Signed media references must not be included in diagnostic markup dumps; this reader selects only the required text/input fields and does not inspect thumbnail CSS.

Remaining: combined tags/representative/content binding; reviewed body/media input; one-shot save; full independent readback. The reservation-form reader above does not perform input or scheduling. Keep existing scheduler as sole writer until separately verified/approved cutover. No fresh article was created in this slice.
