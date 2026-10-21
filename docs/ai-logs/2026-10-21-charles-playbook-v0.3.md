# AI session record — Playbook v0.3 quality gates

- ID: 2026-10-21-charles-playbook-v0.3
- Date/time zone: October 21, 2026, America/Chicago (exact clock time not recorded)
- Responsible member: Charles Barrett
- Tool/product: OpenAI ChatGPT
- Model/version: GPT-6
- Issue/PR: v0.3 playbook quality-gates proposal (link to the review PR after creation)
- Base/reviewed commit: original repository default branch `main`; exact base SHA not recorded
- Affected files: `docs/PLAYBOOK.md`, `.github/workflows/quality-gates.yml`, `requirements-quality.txt`, `README.md`, `.github/pull_request_template.md`, `AI_LOG.md`, `tools/docs/validate_t2.py`, and this record

## Inputs

The user's EECE 4081 assignment requirements and rubric; the existing `docs/PLAYBOOK.md` v0.2; existing `README.md`, PR template, AI log, and available GitHub repository directory listings. The user previously designated `https://github.com/eece-4081-fall-2026/Team1` as the organization team repo. The linked GitHub App returned 404 for that repository, so the assistant used the accessible `treybarrett1/eece4081-teamproject` as a **proposal branch**, not a claimed submission to Team1. No secrets or project-private user ticket data were supplied.

## Prompts in order (verbatim user-authored text)

> Name the quality gates your code must pass, and name the concrete tools that enforce them.
>
> Required content
>
> For each gate: what it checks, which tool runs it, where it runs (locally, in CI, or both), and what happens when it fails. Your stack is Python/Django, so these should be real tool names — a test runner, a linter, a formatter, whatever static analysis you adopt.
>
> “We will maintain code quality” scores nothing. “pytest runs on every push; ruff runs in CI and a failure blocks merge” is a gate.
>
> Note on the coverage floor
>
> You are not setting a numeric coverage target in this version. That moves to Amendment 1 at session 15, deliberately: by then you will have produced and read an actual coverage report for your own code, and you will pick a number that means something instead of guessing at one now. State in v0.3 that the floor is deferred, and that you will set it in amendment 1.
>
> Submission
>
> Updated playbook committed to the team repository, v0.3 marked. One submission per team.
>
> Rubric
>
> Criterion
>
> Pts
>
> Every gate names a concrete tool rather than a category of tool
>
> 4
>
> Each gate states where it runs and what a failure blocks
>
> 4
>
> Gates are actually enforceable given the team’s current CI setup
>
> 3
>
> Coverage floor explicitly deferred to amendment 1
>
> 2
>
> Version marked; committed to the repository
>
> 2

## Outputs and disposition

- Proposed `docs/PLAYBOOK.md` v0.3: specific tools (`pytest`, `pytest-django`, `Ruff`, `Django manage.py`, and `pytest-cov`), exact local/CI commands, execution scope, failure behavior, and distinction between team rule and GitHub-required status check.
- Proposed `.github/workflows/quality-gates.yml`: `quality-gates` job triggered on push and pull request; checks lint, format, pytest and coverage when Python code exists, and Django system/migration checks when `manage.py` exists.
- Proposed `requirements-quality.txt`: named dependencies to install in CI and locally.
- Updated README, PR template, and AI log for v0.3 traceability.
- **Modified/rejected suggestions:** No invented numeric coverage threshold. No claim that branch protection is enabled. No attempt to commit directly into an inaccessible organization repository or bypass v0.2 review rules.
- **Human acceptance:** Pending. The v0.2 approved tool list authorized ChatGPT for brainstorming and Codex for course documents; this AI-assisted documentation and CI workflow proposal needs human review/policy adoption before being treated as a team-approved exception or new permitted use.

## AI review findings

AI review not used. The assistant drafted these changes; a non-author human must review.

## Verification actually performed

Assistant-side checks:
- Queried the linked GitHub App; confirmed that the designated `eece-4081-fall-2026/Team1` repository returns 404 to the linked account (access unavailable).
- Fetched existing playbook and project files from accessible `treybarrett1/eece4081-teamproject`; confirmed it is documentation-only and does not contain a GitHub Actions workflows directory before this update.
- Created a new branch rather than merging directly into `main`, preserving the v0.2 non-author review policy.
- Read the v0.2 policy and documented the missing branch-protection setting as a **pending configuration**, not an already-enforced prohibition.
- Code/CI execution results: **not yet verified here**. No passing tests or successful workflow run claimed.

Human checks still pending:
- Confirm these tool versions and commands are compatible with the codebase once a Django application is committed.
- Review each proposed quality gate and local/CI failure semantics.
- Inspect `quality-gates` workflow runs and configure GitHub branch/ruleset protection to require the check before merging.
- Obtain non-author reviewer approval and team policy-adoption decision, then publish/transfer to the designated Team1 repository if required.
- Make one course-portal submission per team and verify its receipt.

## Human review

- Reviewer: Pending
- Reviewed commit: Pending
- Independent checks and results: Pending
- Decision and date: Pending

## Amendments

### October 21, 2026 — CI verification and legacy script cleanup

The first `quality-gates` CI runs failed because the existing (non-application) Python helper `tools/docs/validate_t2.py` contained a shebang despite not being executable and did not meet Ruff formatting rules. The assistant removed the unused shebang and applied Ruff's suggested formatting diff; no validator logic was intentionally changed. Pytest invocation was scoped to when the Django application entry point or a test directory appears (not the existing documentation helper). The pre-existing documentation validator was additionally added as a required process gate.

**Observed evidence:** `quality-gates` succeeded for the October 21, 2026 commit `e9116b56689ae458cd825cfdc063056a656e4e3b`:
- [Push workflow successful](https://github.com/treybarrett1/eece4081-teamproject/actions/runs/39688610593).
- [PR workflow successful](https://github.com/treybarrett1/eece4081-teamproject/actions/runs/39688616557).

This verifies that the workflow actually executes and passes Ruff lint, Ruff format, and the T2 documentation validator with the current **documentation-only** repository. It does **not** show Django tests, coverage report output, or Django checks passing: those are intentionally conditional and no application has been committed. Branch protection is not confirmed, and the organization Team1 repo remains inaccessible to this connection. Human review, team adoption, and course submission are still pending.

