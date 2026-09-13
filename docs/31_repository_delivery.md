# Standing repository delivery authorization

Owner decision: 2026-09-13, "항시 커밋하고 푸시하고 오토머지까지 해줘."

For dokwanoh/TStory_Agent, commit scoped work and push feature branches without
asking again for each ordinary delivery. Proceed through a reviewed PR and enable
auto-merge only after the exact commit's required tests and review gates pass.
Recheck the remote merge state before reporting completion. This authorization
does not waive quality failures, secrets checks, required reviews or branch rules.
Never force-push, use admin bypass, make the repository public, purchase a plan,
or alter unrelated repository permissions under this authorization.

Current platform observation: repository is private; REST branch-protection read
returned HTTP 403 with a GitHub Pro/public-repository requirement. Updating
allow_auto_merge=true returned allow_auto_merge=false. Therefore native auto-merge
is not enabled; do not claim a requested setting was applied. Preserve privacy.
Do not replace this with direct main pushes or an unreviewed manual merge.

## Initial import scope

The first feature branch includes only the reviewed local save-intent module,
its tests, minimal package metadata, ignore rules and these introductory docs.
The wider local workspace has an existing failing status-document wording test
(226 tests passed, one failed in the prior complete local run). It is not silently
waived or deleted: the wider import remains separate and unmerged. Passing this
small slice does not certify the earlier workspace, browser adapter or publisher.

Final LLM selection targets the lowest total accepted-article cost among models
passing unchanged task evaluations. Include retries and image/research costs;
no automatic premium fallback or weaker acceptance thresholds.
