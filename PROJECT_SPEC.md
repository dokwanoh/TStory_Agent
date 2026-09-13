# TISTORY GROWTH OS — project specification

## Purpose

Current validation scope (ADR-037, owner-approved2026-09-09): actual screen-reader/VoiceOver/narration testing is excluded from the entire loop and Definition of Done, not deferred or passed. Other accessibility/content/policy/print/delivery requirements and the initial MVP objective remain. Older screen-reader obligations are historical and cannot block current completion.

Restore a long-inactive Tistory content operation as a sustainable, evidence-led system that improves reader value and search performance without deceptive scaling, policy evasion, or unreviewed external actions.

## Starting variables

| Variable | Value | Confidence |
| --- | --- | --- |
| `project_name` | `TISTORY_GROWTH_OS` | confirmed |
| `owner` | `DK` | confirmed |
| `primary_language` | `ko-KR` | confirmed |
| `timezone` | `Asia/Seoul` | confirmed |
| `historical_inactivity` | `6+ years` | confirmed owner statement |
| `blog_url` | `https://nedamma.tistory.com` | confirmed owner-provided, 2026-09-07 |
| `monetization_model` | `UNKNOWN` | OWNER_DECISION_REQUIRED / ODR-003 |
| `budget_limit` | `UNKNOWN` | OWNER_DECISION_REQUIRED / ODR-003 |
| `initial_execution_scope` | `discovery_to_offline_mvp` | confirmed |
| `initial_publish_mode` | `approval_required` | confirmed |
| `target_publish_mode` | `policy_compliant_auto_publish` | future aspiration, not authorized |
| `risk_tolerance` | `conservative` | confirmed |

## Goals

- Recover an evidence-backed picture of the existing blog and its operating process when the owner authorizes access.
- Define a traceable AS-IS → BDW → ERASK+C → TO-BE operating model.
- Build a local, deterministic content path from structured topic through evidence, brief, draft, quality report, and editor-ready Tistory package.
- Make publication, claims, source freshness, experience evidence, policy controls, package identity, and later learning changes auditable.
- Establish measurement contracts before setting numeric performance targets.

## Non-goals for the Offline MVP

- Remote delivery, Tistory login, Open API use, undocumented API use, browser-write automation, media upload, post change, deletion, or scheduling.
- Live analytics collection, advertising or affiliate integration, payment configuration, or any new paid service.
- A claim that higher rankings, traffic, indexing, revenue, or automatic publishing is guaranteed.
- Open-ended generative writing without a structured evidence and quality contract.
- Requiring an owner-expertise interview before researching or selecting a topic. The agent discovers audience demand and independently learns and explains subjects; experience and credentials must not be fabricated.
- Legal, medical, financial, or privacy determinations made by the system.

## Public operating contracts

The data-contract inventory covers `TopicCandidate`, `ContentOpportunity`, `SourceEvidence`, `Claim`, `ContentBrief`, `ArticleDraft`, `QualityReport`, `PublishManifest`, `PublishedPost`, `PostMetrics`, `Experiment`, and `EvolutionProposal`.

The Offline MVP’s success terminal is `READY_FOR_APPROVAL`, with `publish_mode=approval_required`, a local `ready_for_approval` state, and `external_write_count=0`. It does not make a remote post reachable.

## Constraints

- Use a Python 3.11, standard-library runtime and checked-in JSON contracts unless an approved decision replaces it.
- Use the owner-provided blog only for read-only public asset, SEO, technical, freshness, and risk auditing. Do not learn, imitate, or treat its historical writing style as a constraint on the future strategy.
- Treat policy records as dated evidence. Recheck live-policy facts before a future external action.
- Maintain Korean-first editorial output, accessible semantic HTML, non-deceptive media placeholders, valid links, and source attribution.
- Keep all secret material out of source, logs, fixtures, and chat.
- Preserve idempotency, dry-run safety, diagnostics-only failure output, auditability, and rollback materials.

## Deliverables

1. Durable Phase 0 memory, risk, metric, plan, and owner-decision records.
2. Evidence-based process-redesign documents and machine-readable traceability.
3. Dated policy/owner catalogs and executable domain contracts.
4. Tested local vertical slice and its reviewable package artifacts.
5. Captured verification, browser-surface, and independent-review evidence.

## Definition of done

The safe initial delivery is done only when the requested memory and process artifacts exist, the local vertical slice follows its executable contracts, deterministic quality/policy failures fail closed, dry-run external_write_count=0 is proven, replay identity is stable, rendered output is manually inspected, and evidence paths are recorded. External delivery remains out of scope until an owner explicitly authorizes it after a current policy review.
