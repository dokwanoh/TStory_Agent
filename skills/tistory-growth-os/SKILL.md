---
name: tistory-growth-os
description: Use this repository's Tistory Growth OS workflow, policies, and local tools. Activate when the user asks to install this repository, prepare or audit Tistory content, or work on the TStory_Agent project.
---

# Tistory Growth OS

Use the canonical project repository at https://github.com/dokwanoh/TStory_Agent.
When the user asks to install this project and a checkout is not present, clone it
to a user-selected or normal project directory, then install this skill from
`skills/tistory-growth-os` into the active Codex home with the built-in
`skill-installer`. Do not copy repository-wide `AGENTS.md` into global memory;
it includes account-owner preferences that may not apply to another person.

For a checkout-based setup, run `python3 -m pip install .` from its root. This
registers the `tistory-growth-os` command. Check its available local commands
with `tistory-growth-os --help`. The package currently provides local and
offline workflows; it does not authenticate to Tistory or publish articles.

## Project context

When operating inside a checkout, read its root `AGENTS.md` first, then the
relevant current project status and linked documents. Treat owner-specific
account, topic, publishing, schedule, media, and browser instructions as scoped
to that repository owner; never silently impose them on a different blog.

Prefer the repository's typed contracts, audit commands, and documented CLI.
Keep secrets, browser profiles, generated article media, and runtime databases
out of Git. Do not claim a live article was published based on a local package,
test, mock, or CLI output.

Installing this skill adds workflow instructions to Codex. It does not include
the owner's authenticated browser session, credentials, API access, or blanket
authorization for external actions. Use only an account and publication scope
that the current user explicitly authorizes.
