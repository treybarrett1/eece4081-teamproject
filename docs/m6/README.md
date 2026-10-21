# M6 — thin-slice test plan and evidence

The linked Team1 repository is not accessible to this GitHub connection.
This proposed runnable ticket-intake starter is on a review branch of
`treybarrett1/eece4081-teamproject`. It should not be presented as existing
M5 code from Team1. Full S1–S4 ticket lifecycle remains unfinished.

## Actual acceptance boundary

`tests/test_acceptance.py` uses Django's CSRF-enforcing HTTP client to
establish a session, submit a ticket, read back a database-persisted ticket,
prove another requester cannot see it, and verify Support can. It checks
forged owner rejection, wrong-role denial, and logout.

`tests/test_unit.py` validates observable behavior: 120/4,000 inclusive
length limits, trimmed content, category/impact enumerations, duplicates,
invalid-write nonpersistence, and role/disable enforcement.

## Commands

```bash
python -m pip install -r requirements-quality.txt
python -m pytest -q --cov=tickets --cov-report=term-missing --cov-report=xml:coverage.xml
python manage.py check
python manage.py makemigrations --check --dry-run
```

## Injected-fault recipe (do not invent the result)

Change this single business-rule line in `tickets/services.py`:

```diff
-        if not value or len(value) > limit:
+        if not value or len(value) >= limit:
```

The changed boundary incorrectly rejects valid titles of exactly 120
characters and descriptions of exactly 4,000 characters. The acceptance
test and the unit test explicitly cover these lengths.

Save (1) the fault commit/diff, (2) the observed failing test run, and
(3) a restoring commit with observed green output. Include a real coverage
report and a prompt-and-diff log. Never claim runtime results without CI
or local execution records.
