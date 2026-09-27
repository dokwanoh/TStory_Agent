# Decision input recovery, 2026-09-27

The owner requested one decision-model comparison through verified public delivery and asked that failures improve the process. Historical operations remain immutable; the current request authorizes a fresh `manual-20260927-decision-models-live-04` operation.

## Findings and changes

- Failure classification matched bare HTTP-code digits anywhere in stderr. A timestamp ending in `.429Z` was incorrectly classified as rate-limited, and `.401Z` could override a real HTTP 429. The classifier now requires an explicit HTTP/status context or an established textual error. Historical `live-03` stderr was retained only as a digest, so its recorded `rate_limited` label is not a confirmed cause.
- The selection prompt embedded complete captured documents; the provider then appended those same documents again. A diagnostic with the old candidate-02 source pool reproduced `Input exceeds the maximum length of 1048576 characters`, with actual_chars1187105. Removing only the duplicate document copy reduced the prompt to939254 characters and the same schema/captured-source diagnostic completed with exit0 and502473 input tokens. The full original evidence and span catalogue remain available; no truncation or weaker validation was introduced.
- Candidate-01 decision and repair quoted real captured text from two URLs outside the selected candidate's source_urls. The existing host validator correctly rejected this. Decision instructions now explicitly require candidate URL membership as well as exact quote support. The validator is unchanged.

## Verification

- Red before fixes: focused provider/simple suites,7 failed and14 passed.
- Green: preparation/discovery/decision regression,215 passed in30.19s.
- Project `basedpyright`:0 errors,0 warnings,0 notes. Ruff on changed implementation/tests passed; `git diff --check` passed.
- Read-only production-model diagnostic: the duplicated input failed twice with `input_too_large`; the deduplicated equivalent returned a structured diagnostic NONE response, exit0 and nonzero token usage. These calls did not select an article or invoke the publisher.
- Browser resolved the owner's share link to the actual third-party article and exposed its primary references. The source is a research lead; embedded executable instructions are untrusted and not executed.
- Fresh production operation passed discovery and decision, recorded an original writing response, and exited at the expected `pending_media` boundary. This confirms progress beyond the historical decision failure; it is not yet publication proof.

The diagnostic proves an input-size defect under the previous source pool, not the exact cause of a historical hash-only error. Public-delivery evidence belongs to the new operation's record and must be reported separately.

## Exact review-record recovery

The fresh run completed discovery, writing and four native image derivations. Its independent editors returned ready, but repeatedly paraphrased article_quote fields that the host correctly rejected. All four automatic turns remain immutable and the automatic loop ended `editorial_budget_exhausted`; it was not restarted or relabelled successful.

Previously the next editor received only `editor_article_quote_invalid`, with no claim index or offending value. The correcting-editor feedback now lists every invalid article/source quote and missing citation, with JSON paths and values. Values remain untrusted data. The same strict checks still decide readiness, and the automatic four-turn limit is unchanged. A failing-first workflow test reproduced the insufficient feedback; the affected preparation/discovery suites now pass216 tests, project types0 issues and changed-file Ruff passes.

Within the current owner request to complete this one public article after fixing defects, a separately recorded assisted review uses the exact unchanged fourth package and a schema enum of actual article sentences/paragraphs. It cannot silently paraphrase article quotes. Its independent session, source matching and exact digest must pass before package promotion; no prior ready assertion becomes approval by itself. This assisted path is not an unattended automatic-loop success.

## Public delivery observed

Published once at2026-09-27 16:19KST as https://nedamma.tistory.com/122. Package digest `6fea6635913964e9a964ac2406685a83794010f968b4d726b17dba8aded5c842`; article HTML SHA-256 `51d5accc528062d944b7a4e10a728e4dd78fa6077beb5743ac72a4ae33ad164c`. The additional independent review completed with real nonzero provider usage and exact source/article quotes. Its host validation and standard dry-run returned REVIEW_APPROVED before input.

The logged-in publisher profile received the four JPEGs through ordinary native pickers in basic mode. HTML mode then exposed four filename-bound native image codes; those codes were placed into the exact reviewed template through native paste. The transferred template hash matched the package, and a native copy readback matched the complete inserted HTML. Returning to basic mode preserved all51 paragraph/heading blocks,22 links and four ordered alts. No editor-internal DOM mutation or hidden-field injection was used. Initial AX diffs appeared to remove earlier images, but the complete DOM showed all figures; that was a partial-view artifact, not replacement.

The save dialog had public/current, home topicIT인터넷 and first-image representative. The category was과학 and eight tags were entered. The journal claimed and started the save at07:19:34.940432UTC; one final native save returned to the manager, whose count rose109to110. The public page's native edit link identified post122 and the observed receipt was journaled. Read-only reopening of that same saved post confirmed public, category과학, homeIT인터넷 and16:19 publication time; it was closed without another save.

Anonymous HTTP200 readback at07:21:21.471830UTC matched exact title,51 blocks,22 source links,four filenames in order,all alts and first-image OpenGraph representative. All eight tags match case-insensitively; Tistory canonicalized `Kev` and `AI 벤치마크` to `kev` and `ai 벤치마크`. UTF-8 replacement count0. The readback fetched HTML only, not remote image pixels.

Evidence directory: `.artifacts/preparation/manual-20260927-decision-models-live-04/assisted-record-review/` contains `validation.json`, independent review events/completion, exact package, `save_journal.py`, `verify_public.py` and `public-readback.json`. The standard approved review receipt is in `contracts/reviews/6fea6635913964e9a964ac2406685a83794010f968b4d726b17dba8aded5c842.json`.

## Reusable lessons and limits

- Keep complete captured source text once per decision request; diagnose input-size errors distinctly from rate limits, and never infer historical causes from hash-only logs.
- Give editors exact invalid quote paths and values while keeping validation strict. Ready assertions alone cannot approve a package.
- In assisted delivery, upload in basic mode, require four native filename-bound codes, then verify exact text after the HTML round trip. A mode-change confirm can block CDP; observe the native dialog and accept once rather than retry the original action.
- Check complete figure/filename inventories when accessibility diffs omit off-screen images. A diff is not the full editor state. Record native tag normalization without silently altering the approved package.
- Preserve exhausted automatic records and label separately assisted review/delivery honestly. This proves this article's publication, not broad unattended reliability. Recent-five media-history comparison was incomplete for some older locally unmatched packages; no complete visual-history audit is claimed. Owner-excluded audits and schedule controls remain unchanged.

## Next-article reuse

Owner2026-09-27 explicitly requested ongoing reuse of these lessons. AGENTS.md routes the next operator here; the installed tistory-editorial-cycle SKILL.md routes remote work to its delivery reference. This procedure is reusable; post122's operation, grant, exact review receipt, image codes and save identity are not templates for new authority or success.

1. Read current instructions/status, article identity and live manager outcome. Use valid authority already present in the current session without routine reconfirmation; never substitute a historical grant. An uncertain prior save permits read-only reconciliation, not another creation. Existing completed post122 is read-only unless separately asked to edit it.
2. Reuse the repaired preparation code. Include complete captured source bodies once per provider request. Bind claim URLs to the selected candidate and quote actual unchanged article/source text. Use all invalid-quote paths/values to repair within the remaining budget. Distinguish input size, explicit HTTP/status errors and unknown hash-only failures. Do not infer a rate limit from digits in a timestamp or hash.
3. Produce a fresh subject-specific four-image set and validate native generation provenance, original hashes and JPEG derivations. Compare the latest five available article scene records; identify missing history explicitly. Prior images and comparison findings do not prove a new set's suitability.
4. For an authorized assisted full-body transfer, use the owned authenticated publisher Chrome profile and one writable editor. Upload in basic mode through the normal picker, observing the selected local file and upload completion. Read native HTML codes only after all four filename identities are present. Keep signed code values in memory and redact observations; do not persist signed URLs or reuse them for another article.
5. Insert those four codes/alts into the exact reviewed template using supported native input, never DOM/hidden-field mutation. Compare transferred template hash and whole editor input, then return to basic mode and compare all paragraph/heading blocks, link targets and ordered alts. Partial AX diffs can omit off-screen images; inspect the complete DOM/figure inventory before concluding replacement or reuploading. If a mode-change confirmation blocks the browser call, handle the observed dialog once and inspect the resulting mode before another action. Use fresh indices, not post122's click transcript.
6. Confirm this article's category, home topic, tags, representative, visibility and time; post122's labels/counts are not defaults. Immediately before the single final save, validate the current grant/package and durably record the attempt. Record the real observed post ID afterward. Verify anonymous HTML against the current reviewed package, and read back stored native classification/publication time. Do not turn tag capitalization normalization into a rewrite or second save; record both labels and compare semantic identity without dropping tags.
7. Mark completion only from observed saved/public evidence. Update the canonical task row and managed views, record tests and unresolved limitations, then push scoped changes to main. Distinguish assisted success from automatic-loop success. Excluded checks stay excluded. The post122 assisted-review method may inform a separately authorized recovery, but cannot silently reset exhausted budgets or approve a new package.

## Final repository validation

Full command `PYTHONPATH=src:.venv/lib/python3.11/site-packages /opt/homebrew/opt/python@3.11/bin/python3.11 -m pytest -q tests browser_tests` returned932 passed/3 failed in237.45s. Two project-audit failures came from the synthetic `private-marker` API-key test string added by the earlier diagnostic change. Marking that dummy value explicitly as an example fixes the repository secret scan without weakening the scanner or the diagnostic-redaction assertions. Rerunning all provider,CLI,project-audit and memory suites returned52 passed/1 failed in14.73s.

The remaining failure is the already observed STATUS managed-view drift: its current hourly publisher row is ACTIVE, whereas the canonical registry/auditor still carry older paused guard descriptions and no hourly row. The new completed task matches the registry; PLAN and BACKLOG match their derived views. The unrelated scheduling policy was not reverted or changed to make tests green. Current memory audit therefore remains exit1 and this limitation is explicit. The earlier affected preparation/discovery regression passed216 tests; source typecheck and Ruff passed. Documentation diff checks passed.
