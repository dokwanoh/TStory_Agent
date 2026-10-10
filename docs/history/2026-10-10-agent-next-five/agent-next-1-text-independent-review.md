# Independent text review — additional five, article 1

Decision: PASS / READY. No essential factual or readability repair.
Reviewed exact file: outputs/agent-next-1-article.md
SHA256: `ab7b6f606cde2b167b7222c13c667aff346c7b1cf1c69f8e939ef14f02836c76`
Review date: 2026-10-10 (Asia/Seoul)

## Scenario and invocation

Read the entire title, lead, summary and three sections using exec_command `cat outputs/agent-next-1-article.md`. Compare directly with the source bodies inspected during the topic review and today's independent official homepage/updating fetches. No tests or product execution.

Read-only Python invocation measured SHA256 and removed URL strings with regex `https?://\S+` for the character count. Observable: 3542 characters including whitespace and Markdown syntax after URLs are removed; three numbered main sections; three bold spans, one per section. Two-column summary has four data rows. Count is a measured size, not a claim of exactly3000 rendered characters.

## Findings

- Title and summary accurately frame Store distribution. No first-ever Windows support or new core capability claim.
- The announcement date is October9 with timezone uncertainty expressly retained. No within24h, today-launch or popularity metric claim. Official X independently returned403 during topic review; announcement text/date rely on the assigned captured official post body. This limitation remains in this evidence.
- Windows10 source support and Windows11 22H2+ MSIX support are correctly separated. The article explicitly says regional listing/install UI was not checked.
- Store updates are correctly distinct from source updates. The October8 v0.21.6 passage states Store/desktop packages retained their existing build, avoiding attribution of code patches to the Store version.
- Provider/model connection and software installation are separate. Local app location is not treated as proof that inference/data processing stay local. No unsupported free-service or universal availability promise.
- The official homepage newly checked here directly describes Hermes as free open source under MIT, with model providers and optional hosted services priced separately. The draft reflects that scope without copying marketing capability guarantees.
- Excel merge is labeled hypothetical and not executed. It specifies preserved originals, separate output, duplicate policy and row/column checks; copies are explicitly not enforced isolation. Asking to explain and approve desired steps is presented as a user approach, not a guaranteed product-wide approval mechanism.
- Short paragraphs and explanations of agent, MSIX, model and Python suit beginners. Three section arguments remain focused. The manuscript does not advertise or overclaim the optional book.

## Independent official sources and binary observations

1. https://hermes-agent.nousresearch.com/docs/user-guide/windows-native
Invocation: web.open during topic review. Observable: official body returned; MSIX/AppInstaller/Store section expressly provides Windows11 22H2 requirement and separate source/Store mechanisms. PASS.
2. https://github.com/NousResearch/hermes-agent/releases/tag/v0.21.6
Invocation: web.open during topic review. Observable: official release body returned; October8 code/Docker patch retains Store and desktop package builds. PASS.
3. https://hermes-agent.nousresearch.com/docs/getting-started/quickstart/
Invocation: web.open and web.find during topic review. Observable: official body returned; installation, provider choice and working-chat verification are separate steps. PASS. This is general documentation, not proof of every current Store build feature.
4. https://hermes-agent.nousresearch.com/
Invocation: web.open in this text review. Observable: FAQ How does pricing work, lines110–115, gives free/MIT software, separate model/hosted-service pricing and connecting a model before conversation. PASS. Homepage download banner is broad Windows10/11; article correctly uses the dedicated MSIX conditions instead of transferring that banner to Store requirements.
5. https://hermes-agent.nousresearch.com/docs/getting-started/updating/
Invocation: web.open in this text review. Observable: update table lists Microsoft Store updates; package-owned files are not rewritten by hermes update. PASS.
6. https://x.com/NousResearch/status/2108231536772596193
Invocation: web.open during topic review. Observable:403, not independently live-verified; captured official text in work/agent-next-1-sources.md is the limited announcement evidence. No exact timezone or24h certification.

## Limits and integrity

This is the independent text/fact gate only. No Store installation, regional availability, actual Excel output, archive-wide uniqueness, live internal-link operation, image layout, editor save or publication is certified. No manuscript or browser changes. Only this requested evidence artifact was written.

Input source hashes:
- work/agent-next-1-topic.md: `8587fb426eef4145a440d0d2a4ee014e11a45befe0ec231ca4501d9d7bbb9cb7`
- work/agent-next-1-sources.md: `be1e44e2e3cce210c1eb300c1b690eb05b818e914f9ed70328b6babab44603d3`
- work/agent-next-1-hermes-release.md: `daddd588bb4da14e5cc9d8e9017c645e95dce1a45bbfbe5f6cdde624943249a0`
