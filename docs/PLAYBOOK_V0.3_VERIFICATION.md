# Playbook v0.3 verification and follow-up record

Date: October 21, 2026, America/Chicago. Working repository:
`treybarrett1/eece4081-teamproject`, open PR #17. This document records checks;
it does not claim team adoption, a policy vote, or course submission.

## Acceptance and evidence

| Playbook section 8 gate | Current repository verification | Controlled fixture verification |
| --- | --- | --- |
| Ruff lint | `python -m ruff check .` | Clean source passes; unused import exits 1 |
| Ruff format | `python -m ruff format --check .` | Formatted source passes; bad formatting exits 1 |
| T2 integrity | `python tools/docs/validate_t2.py` | Valid documents pass; broken link and CSV trace drift each exit 1 |
| pytest | Not applicable to the product until tracked application/test source exists | Passing test exits 0; failed test exits 1; source without tests exits 5 |
| pytest-django | No ticketing Django application exists | A disposable Django model test verifies plugin setup and exits 0 |
| Coverage evidence | No product coverage is claimed; no numeric floor | Fixture pytest generates parseable XML; real product pytest must produce nonempty `coverage.xml` |
| Django system check | Not applicable until a tracked `manage.py` exists | Valid fixture passes; invalid model exits 1 |
| Migration drift | Not applicable until a tracked `manage.py` exists | Missing migration and changed model each exit 1; matching migration exits 0 |

`python tools/docs/verify_quality_gates.py --output gate-evidence/fixtures.json`
runs those actual commands against disposable fixtures. Its JSON records the
revision, UTC time, installed tool versions, expected and actual exit codes, and
captured output. Fixture success means the gate catches known failures; it is
not evidence of implemented ticket transitions, permissions, or business tests.

CI runs the same fixtures and uploads `quality-gate-evidence`, including the
tested revision, environment, tracked-source inventory, raw command transcripts,
fixture JSON and any actual product coverage XML. Each run is tied to its own
workflow SHA; a green earlier commit is not evidence for a later edit.

## Scope detection and failure behavior

`tools/docs/gate_scope.py` detects every tracked `.py` path outside `tools/docs/`,
including nested `src/`, `services/` and test directories. Any such source
activates pytest. All tracked application `manage.py` paths are checked from
their own directories, including nested projects. A Git inventory error fails
the step rather than being reported as an absent application. Documentation
helpers and fixture verification remain under the excluded `tools/docs/` path.

CI uses Bash pipefail: storing transcripts with `tee` does not hide a failed
check. Zero collected product tests fail; missing product coverage fails.
There is no `--cov-fail-under`: the floor remains deferred to Amendment 1 at
Session 15, based on an actual product coverage report.

## Review findings and dispositions

| Finding | Resolution / evidence |
| --- | --- |
| Stale claims that CI was never verified | Trey's follow-up commits updated current wording; earlier historical records are retained. New evidence is recorded separately for this follow-up. |
| Fixed app paths could bypass tests | Tracked-source selection and arbitrary nested manage.py detection are shared by CI and the fixture verifier. |
| Referenced v0.3 audit file was missing | Trey added the linked rubric audit concurrently. His document is preserved; this separate record supplies executable verification. T2 validation must pass. |
| Main lacks mechanical merge protection | GitHub reports `protected: false`. Current account has push but no admin/maintain permission. An administrator must perform the settings change below. No enabled protection is claimed. |
| Organization repository destination | Team1 is now accessible but empty. Doc instructed this work to remain in the repository containing the project information and left organization publication to Trey. No organization repository was changed. |

## Administrator handoff: branch protection

A repository administrator must configure a ruleset or branch protection for
`main`, require pull requests and at least one non-author approval, dismiss
stale approvals after substantive updates, require `quality-gates`, require the
branch to be up to date, and restrict bypasses. Retain the playbook's separate
strict-majority adoption requirement for policy changes.

Verify with GitHub's branch/ruleset APIs and a controlled PR with a failing
required check: its merge must be blocked. Merely creating this workflow or
observing a green run is insufficient. The current account cannot complete or
test this admin-only action, and no course-portal receipt is claimed.

## Review responsibility

These edits follow the earlier approval of `dbf3f6e`; that approval does not
cover this newer substantive change. A non-author teammate must review the new
head. Source/workflow changes and their verification are kept together because
the fixture checks exercise the same gate selection used by CI. Human
acceptance, independent human testing and majority adoption remain pending.

## Observed local verification

The isolated declared-tool environment completed 26 fixture assertions with all
expected outcomes, plus repository Ruff lint, Ruff format and T2 validation.
The T2 validator observed 20 charter sources, 32 requirements, 20 stories,
6 epics, 72 acceptance criteria and 114 traceability rows.

[Machine-readable local record](evidence/playbook-v0.3-local.json) retains
commands, tool versions, stdout/stderr and expected/actual exits. It identifies
its starting revision and modified working tree; file hashes identify the
verified gate implementations. This local record is not falsely labelled as a
clean later commit. Exact-head CI evidence follows in the PR and CI artifact.

Commands used from the repository root, with Python from a separate environment
installed from `requirements-quality.txt`:

```text
python -m ruff check .
python -m ruff format --check .
python tools/docs/validate_t2.py
python tools/docs/verify_quality_gates.py --output gate-evidence/fixtures.json
```
