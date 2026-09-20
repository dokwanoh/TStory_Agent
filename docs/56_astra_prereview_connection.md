# Astra pre-review connection: implemented, live execution held

2026-09-20. This increment connects the captured-feed experiment to installed Codex CLI and parses completed-turn usage. It does **not** establish a successful live model review or measured savings.

## Scope and execution

`research.prereview_cli` offers raw-feed and compact-packet variants against an identical cutoff, model `gpt-6-astra`, rubric `signal-prereview-v1`, and SHA256 binding of original feed plus cutoff. Existing ChatGPT authentication is used normally. No credentials are read/copied, no new paid API is configured, no packages or global settings are changed. No model fallback is attempted.

```sh
PYTHONPATH=src python3 -m tistory_growth_os.research.prereview_cli \
  --feed .artifacts/topic-intake-20260920-replayable.rss \
  --as-of 2026-09-20T14:19:15.412230+00:00 \
  --variant compact --output .artifacts/prereview-new.json
```

Default is dry-run, zero calls. `--execute` is an explicit, manual existing-account invocation; never wire it into unattended production before live certification. A pre-call attempt journal prevents replay of the same output identity even when the process fails. Different filenames are not authority to bypass an uncertain result or repeatedly consume usage. Current two experiment identities are consumed and remain held.

The child CLI uses ephemeral execution, read-only sandbox, one explicit model and output schema, with a 240-second timeout and no wrapper retry. No hook-trust bypass, ignored configuration/rules or permission relaxation is used. The prompt forbids tool use; the parser rejects tool-using results. This is an output acceptance rule, not a claim that read-only shell sandboxing disables every inherited MCP capability. No unattended live certification follows.

## Response and metering boundaries

- Candidate queries must be unique and present in the eligible input; maximum five.
- Each needs a reader question, rationale and missing-evidence statement.
- `publication_eligible` and every `event_verified` must remain false.
- Signal-only pre-review never replaces the independent-source/event/rights investigation or final highest-model editorial gate.
- Completed-turn input/cached-input/output usage is recorded once. Reasoning output is not added twice.
- A structured response passes only structural checks; `quality_passed=false` until separate semantic evaluation. The economic comparison therefore refuses to claim savings automatically.
- API-equivalent prices are not ChatGPT subscription invoices. Actual cash savings remain unknown.

## Observed live attempts

Installed `codex-cli 0.145.0`; `codex login status` reported `Logged in using ChatGPT`. That does not prove model execution readiness.

1. Compact variant `.artifacts/prereview-20260920-compact.attempt.json`: CLI nonzero; no successful completion/usage receipt. Initial adapter did not retain stderr diagnostics. Do not report zero tokens.
2. Raw variant `.artifacts/prereview-20260920-raw.attempt.json` and `.json`: provider exit1, adapter exit2/held. Sanitized stderr keyword flags `hook`, `model`; stderr hash and byte count retained, raw text not stored. These words do **not** establish a hook trust error, model denial or quota problem.
3. One direct startup diagnostic was attempted after these variants; its text-prefix output filter returned no matching lines. It does not provide root-cause or usage evidence. No further provider calls were made.

A missing-schema local startup probe reported the expected file-not-found before model work. A bounded local Codex session finder returned no matching current-day records; ephemeral executions cannot be reconstructed from that result. No session/counter reset or child-agent creation was performed.

The root cause of live execution failure is still **UNKNOWN**. The concrete local observability limitation is confirmed: the first adapter discarded stderr, and the later keyword-only summary is insufficient to diagnose the provider. Do not call this a model quota failure or a fixed connection. A future diagnostic must capture structured provider errors with secret-safe filtering before another paid/usage-consuming comparison; do not repeat the blind calls.

## Verification

- Absent-module RED reproduced before implementation.
- Ten focused tests pass: completion usage, failed/incomplete/tool-using runs, candidate invention, false publication/freshness claims, actual CLI subprocess using an isolated fixture executable, and consumed-attempt replay prevention.
- Source and scoped-test typechecks: zero errors/warnings. No-excuse rules: no violations in two source files.
- Actual CLI help, dry-run and consumed-identity refusal executed. Fixture CLI success is not real Astra success.
- Full regression:581passed/164.62s. Source/scoped-test types, compilation and diff checks pass. Implementation commit `e702d30`. No claim of live success or merge readiness.

Source: [official Codex non-interactive execution documentation](https://learn.chatgpt.com/docs/non-interactive-mode), checked2026-09-20, plus installed `codex exec --help`. Documentation describes JSON event/usage and output-schema interfaces; only a future successful local invocation can certify this account/environment path.

STOP and automation3PAUSED remain unchanged. No article, reservation or external blog write occurred.
