# M6 evidence package — automated tests, coverage, deliberate fault

**Project:** EECE 4081 Enterprise IT Ticketing and Bug System
**Date:** October 21, 2026 (America/Chicago)
**Prepared by:** Charles Barrett, with disclosed AI implementation assistance
**Status:** Reproducible, CI-verified provisional ticket-intake slice on a
personal repository review branch. **Not** claimed merged or submitted to
`eece-4081-fall-2026/Team1`, which is inaccessible through this connection.
The user's existing Team1 M5 implementation could not be inspected.

## Scoring checklist (20 points offered by assignment)

| Rubric item | Evidence | Observed result |
| --- | --- | --- |
| Acceptance test at real boundary (4) | [tests/test_acceptance.py](../../tests/test_acceptance.py) | CSRF-enforcing Django HTTP Client, login, POST ticket, DB assertion, GET detail/list, second requester denied, Support allowed, logout rejected |
| Behavioral unit tests (4) | [tests/test_unit.py](../../tests/test_unit.py) | Inclusive limits, invalid fields, valid choices, duplicate IDs, service role/disabled-account denial |
| Coverage report (2) | [text output](evidence/02-coverage-report.txt), [XML artifact](https://github.com/treybarrett1/eece4081-teamproject/actions/runs/39691153398/artifacts/12388298593) | `tickets` statement coverage 89% (132 statements, 15 missed) |
| Subtle injected fault (4) | [fault commit](https://github.com/treybarrett1/eece4081-teamproject/commit/c67c39d5f7b6f8422a5b4277776ac38e8b462f99), [fault diff](evidence/03-fault.diff) | Single `>` to `>=` change rejects allowed exact limits |
| Fault, failure, fix (4) | [fault diff](evidence/03-fault.diff), [failing CI output](evidence/04-fault-test-output.txt), [fix diff](evidence/05-fix.diff), [restored passing CI output](evidence/06-restored-test-output.txt) | 31 passed -> 2 failed / 29 passed -> 31 passed |
| Prompt-and-diff log (2) | [session record](../ai-logs/2026-10-21-charles-m6-bug-injection.md) | Actual prompts, scope, files and verification documented |

## Exact workflow sequence

1. **Green baseline** `7274b202`:
   [CI run 39691153398](https://github.com/treybarrett1/eece4081-teamproject/actions/runs/39691153398),
   [test output](evidence/01-baseline-test-output.txt) and
   [coverage report](evidence/02-coverage-report.txt). 31 passed; 89%.
2. **Injected wrong branch condition** `c67c39d5`:
   [one-line diff](evidence/03-fault.diff),
   [failing CI run 39691243098](https://github.com/treybarrett1/eece4081-teamproject/actions/runs/39691243098).
   Two existing tests caught it: one HTTP acceptance test and one validator unit test.
3. **Revert** `d18875ac`:
   [fix diff](evidence/05-fix.diff),
   [successful CI run 39691411338](https://github.com/treybarrett1/eece4081-teamproject/actions/runs/39691411338),
   [restored test output](evidence/06-restored-test-output.txt). 31 passed; 89%.

## Interpretation and outstanding boundaries

- These numbers describe only the **new starter ticket-intake implementation**
  in this personal repository branch, not the absent team's M5 system.
- Django browser UI, seeded-account CLI, triage, ownership transitions,
  history/events, and the full S1–S4 promise are not implemented by this work.
- The accepted slice has a **real HTTP/session/CSRF/persistence boundary** and
  demonstrates that behavioral tests catch a subtle user-visible defect.
- A teammate must review this branch and adapt/re-run these same tests
  against the **actual team M5 code**, then submit to the team repository.
- The playbook's existing approved AI coding tools may differ from the tool used
  here; obtain the team's human approval of this disclosed use before adoption.

## Local rerun

```bash
python -m pip install -r requirements-quality.txt
python -m pytest -q --cov=tickets --cov-report=term-missing --cov-report=xml:coverage.xml
python manage.py check
python manage.py makemigrations --check --dry-run
```
