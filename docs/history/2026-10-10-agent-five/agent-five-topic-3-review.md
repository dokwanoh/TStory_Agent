# Independent topic review — article 3

Decision: ACCEPT. Reviewed 2026-10-10. No article, publication, or other contributor file was changed. This evidence-only file is required by the executor evidence contract.

The combined topic has sufficient scope: account selection, tool execution permissions, and model location affect actual use. It differs from article 248 subscription transition and article 249 mobile dot/Codex context continuity. No demand or traffic measurement is claimed.

## Direct observations

1. Weekly release: `curl -L --fail --silent https://github.blog/changelog/2026-10-09-github-copilot-weekly-releases-october-5/`, parsed with Python HTMLParser. Observable: readable October 9 weekly release explicitly lists separate license/repository accounts in Copilot app, local sandbox GA, Ollama model discovery, and VS Code Agents grid. PASS. Initial web.open failed; curl succeeded.
2. Sandbox scope: web.open https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/about-cloud-and-local-sandboxes and https://github.blog/changelog/2026-10-07-local-sandboxing-for-github-copilot-now-generally-available/. Observable: readable documentation says default off; CLI/app settings separate; VS Code announcement limited to Agent Host sessions; built-in file tools honor policy on a best-effort basis; remote MCP is not sandboxed. PASS.
3. Local models: web.open https://github.blog/changelog/2026-10-07-discover-local-models-in-github-copilot-cli/. Observable: CLI 1.0.94-0+, running Ollama and installed tool-calling/streaming model required; discovery needs selection/confirmation; no runtime/model installation; choosing local model does not enable offline mode or disable telemetry. PASS.

## Essential editorial conditions

- Describe October 9 as weekly publication; sandbox and local-model announcements are October 7. Exact publication hour unknown; do not assert trailing24h.
- Separate license account from repository account without implying additional repository rights, organization-policy bypass, or unrestricted private use of an employer's license. Detailed account-switch UI steps were not independently established.
- State sandbox default off and scope/OS dependence. Do not claim complete isolation, automatic activation across clients, or guaranteed security.
- Explain model location separately from tool isolation. Local model selection alone is not offline operation or a zero-network guarantee.
- Keep VS Code grid as a brief aid to result review; human result checks remain necessary.
- Product selection remains outside this review; no product/edition endorsement.

No tests or browser UI actions were performed. The scenarios above are source-reading checks, not feature-execution tests. Captured observations and limitations are recorded in this file.
