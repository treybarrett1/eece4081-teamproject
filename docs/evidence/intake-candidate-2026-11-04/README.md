# Proposed Team1 ticket-intake starter and measured coverage

Created November 4, 2026 at Doc's request. **New implementation candidate, not
historical Sprint 1 work and not yet adopted or merged into Team1.** The prior
class snapshot `ba34d08711ff64aa4cfe484a16013ed2d6971bb4` contained documentation
and verification helpers only. This packet supplies newly written, executable
application code and tests instead of inventing missing coverage results.

## Actual results

40 tests passed, zero failures and zero skips. Aggregate statement coverage:
**127 executable statements, zero missed, 100%**. The same test run with a
proposed `--cov-fail-under=90` threshold also passed. Ruff lint/format, Django
system checks and migration-drift checks passed. Exact transcripts and tool
versions are in `evidence/`. No remote CI or production security audit is claimed.

The scope is the first-party `tickets` package, excluding migrations:

| File | Statements | Missed | Statement coverage |
| --- | ---: | ---: | ---: |
| tickets/__init__.py | 0 | 0 | 100% |
| tickets/models.py | 16 | 0 | 100% |
| tickets/services.py | 49 | 0 | 100% |
| tickets/urls.py | 3 | 0 | 100% |
| tickets/views.py | 59 | 0 | 100% |
| TOTAL | 127 | 0 | 100% |

This is statement coverage, not branch coverage. Settings, project URL wiring,
manage.py, migrations, tests and dependencies are outside the denominator. The
percentage does not establish complete requirements coverage or absence of bugs.
An existing proposal for 60% across the whole application is a different scope;
this smaller report does not establish that broader baseline.

## Implemented slice

The T4 planning document's Sprint 1 goal was sign-in → create → own-ticket detail,
with cross-requester direct-ID denial. This new starter implements a JSON API
for that path. It follows the documented title/description limits and category /
impact values. It is a partial S1/S2 candidate, not the full T4 deliverable.

- Session sign-in/out using Django authentication, with uniform invalid/disabled
  credential errors and CSRF enforcement.
- Shared-service role checks: one current active role; only Requesters create;
  Requesters read only their own tickets; Support reads all; Developer and
  Administrator do not receive implicit ticket access.
- UUID ticket IDs, UTC creation times, New status and no owner/priority at intake.
- Trimmed text validation, invalid choices, missing fields and client-forged
  ownership/state fields rejected before persistence.
- Real database rollback check after an inserted row followed by an injected
  exception; no partial ticket remains.
- HTTP/session/CSRF/database acceptance test plus behavior and boundary tests.

There is no UI, seed command for normal users, triage, assignment, resolution,
reopening, immutable event history, concurrency control, search or deployment
setup. Creation rollback does not prove ticket/history atomicity: history has
not been implemented. This is not all of FR01/FR03/FR05/FR21 or all of S1–S4.
Direct ORM writes and production deployment hardening remain future concerns.

## Reproduce from this source ZIP

Use Python 3.12 or newer in an isolated local environment:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-test.txt
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py makemigrations --check --dry-run
.\.venv\Scripts\python.exe -m pytest -q --cov=tickets --cov-report=term-missing --cov-report=xml:evidence/coverage.xml
```

Tests create a temporary database and synthetic accounts. A fast password
hasher is enabled only in tests; runtime keeps Django's ordinary hashers.
For local API experimentation, migrate a local database and create synthetic
accounts with one of the Requester/Support/Developer/Administrator groups.
There are no registration or role-management endpoints. The server settings
are local-development settings, not a production configuration. Set a stable
private TEAM1_SECRET_KEY for manual sessions; none is supplied in the ZIP.

## For Austin's Amendment 1

Send `evidence/coverage.xml`, `evidence/pytest-coverage.txt`, the source/tests ZIP
and `SOURCE-MANIFEST.json` together. The manifest identifies the exact new source
that produced this report; there is no Team1 implementation commit yet.

Before calling this Team1's application baseline, the team must review/adopt
this source, put it in the designated repository, rerun the tests on that commit,
and link the resulting evidence. Do not claim it was present in Sprint 1.

A possible proposal for **this scope only** is 90% aggregate statement coverage:
the observed baseline is 100%, with ten percentage points of proposed development
headroom. That buffer is a planning judgment, not a percentage selected by the
coverage tool or an agreed team policy. Preserve the role/isolation/CSRF/rollback
tests even if an aggregate percentage passes. Update the CI command and coverage
scope together if the team adopts a floor. Re-evaluate when the runtime expands.

The Sprint 1 incident/date confirmation and the T4 receipt remain separate
requirements. No date, receipt, team vote or adoption has been invented.

## AI assistance

OpenAI Codex generated this new source, tests and evidence packet at Doc's
request, using the existing T2/T4 requirements as context. The recorded tests
were actually executed. Human review, independent reproduction, team adoption,
GitHub publication and course submission remain pending. This packet contains
no private peer-assessment content.
