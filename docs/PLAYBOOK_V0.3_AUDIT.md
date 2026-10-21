# Engineering Playbook v0.3 — Rubric and CI audit

**Course:** EECE 4081-002, Fall 2026  
**Audit date:** October 21, 2026 (America/Chicago)  
**Status:** Rubric text reviewed; documentation-only CI verified previously. This is not a teammate's independent approval or a course submission.  
**Change under review:** [Pull request #17](https://github.com/treybarrett1/eece4081-teamproject/pull/17), branch `docs/playbook-v0.3-quality-gates`.

## Rubric coverage

| Criterion | Pts | Evidence in proposed v0.3 |
| --- | ---: | --- |
| Every gate names a concrete tool | 4 | `docs/PLAYBOOK.md` §8 specifies `python -m pytest`/`pytest-django`, `python -m ruff check .`, `python -m ruff format --check .`, `python manage.py check`, `python manage.py makemigrations --check --dry-run`, `pytest-cov`, and `python tools/docs/validate_t2.py` |
| Each gate states where it runs and what failure blocks | 4 | §8 quality-gate table gives local vs GitHub Actions operation and a failed gate's PR approval/merge consequence |
| Gates are enforceable with current CI | 3 | `.github/workflows/quality-gates.yml` runs on push and pull request. Ruff lint, Ruff formatting, and T2 document validation already ran successfully in GitHub Actions. pytest, coverage, and Django checks activate once application code exists. **GitHub branch protection requiring the status check is not independently verified**; until then, non-author review enforces the documented process rule |
| Coverage floor explicitly deferred | 2 | §8 states no numeric floor and no `--cov-fail-under` in v0.3; team will read its own coverage report before setting a value in Amendment 1 at Session 15 |
| Version marked and committed to repository | 2 | `docs/PLAYBOOK.md` title, updated date, §8 heading, and version record explicitly say **v0.3**. The work is committed to the review branch of `treybarrett1/eece4081-teamproject`, **not yet merged**, and the designated `eece-4081-fall-2026/Team1` organization repository was inaccessible to the current GitHub connection |

**Audit assessment:** The rubric's substantive document elements are covered; **do not claim final repository/submission points or guaranteed GitHub merge blocking** before the team's review, publication to the designated repository, and required-check setup.

## Observed automated CI evidence

For the documentation-only project before the October 21 audit edits:

- [Passing pull request workflow run](https://github.com/treybarrett1/eece4081-teamproject/actions/runs/39688731937)
- [Passing push workflow run](https://github.com/treybarrett1/eece4081-teamproject/actions/runs/39688722092)

Those GitHub Actions runs verified dependency installation, Ruff lint/format, and T2 documentation validation. The pytest and Django steps appeared successful as shell steps but explicitly **skipped their substantive tests** because application code/`manage.py` was absent. Uploading a coverage artifact was similarly optional, not proof that a coverage report exists. New commits require new current-head CI evidence before merge.

## Additional consistency and implementation notes

- `README.md` must link this audit file, the existing v0.2 audit, and the current v0.3 playbook accurately.
- AI disclosure remains linked from `AI_LOG.md`; its verification claims must distinguish passing documentation CI from never-run Django application tests.
- `pytest-django` requires real Django settings/application requirements when the app is committed. Do not call its conditional step passed for real behavior until then.
- The requirements document validator `tools/docs/validate_t2.py` is a legacy documentation script, not a Django application. Its formatting changed to satisfy the new Ruff gate without intentionally changing validation logic.
- The `quality-gates` job is a *configured* GitHub Actions check, not proof that `main` rejects failing merges. A repo administrator must require that check in branch protection / rulesets.
- AI tool use and new rules require the existing human review/adoption process; no assistant-generated team approval is implied.

## Human and submission checklist

- [ ] Team member independently reviews PR #17's full diff and applicable evidence, and records their own approval.
- [ ] Team policy-adoption requirements in `docs/PLAYBOOK.md` are met.
- [ ] The latest PR `quality-gates` CI run succeeds after all edits.
- [ ] A repository admin confirms or configures `quality-gates` as a required status check, if technically available; avoid falsely claiming GitHub mechanically blocks a merge otherwise.
- [ ] PR #17 merges after non-author approval; `main` shows v0.3.
- [ ] The designated team repository `eece-4081-fall-2026/Team1` has the updated playbook, or the instructor confirms an alternate authorized team repository.
- [ ] Exactly one team submission to the course portal; retain its receipt.

## Human audit record

- Reviewer/date: Pending
- Reviewed commit: Pending
- Findings/dispositions: Pending
- Independent approval: Pending
- Team adoption record: Pending
- Team repo publication: Pending
- Course submission receipt: Pending
