# M6 — verified testing evidence

The [M6 submission index](SUBMISSION.md) maps every rubric item to committed
source and real GitHub Actions evidence.

- **Green baseline:** [31 passing tests, 89% application-package coverage](https://github.com/treybarrett1/eece4081-teamproject/actions/runs/39691153398).
- **Deliberate fault:** [2 failed, 29 passed](https://github.com/treybarrett1/eece4081-teamproject/actions/runs/39691243098).
- **Fault removed:** [31 passing tests, all quality gates green](https://github.com/treybarrett1/eece4081-teamproject/actions/runs/39691411338).
- **Evidence files:** [baseline, coverage, fault diff, failing output, fix diff, restored output](evidence/).
- **Prompt and diff log:** [full disclosure](../ai-logs/2026-10-21-charles-m6-bug-injection.md).

This code is a *provisional Django ticket-intake walking skeleton* written in
the accessible personal repository. It cannot be represented as a test of the
inaccessible `eece-4081-fall-2026/Team1` M5 implementation. See the submission
index for remaining review and transfer steps.
