# Amendment 1 review materials

Published at Austin's request on November 4, 2026. These are proposals and supplied evidence, not adopted team policy or historical Sprint 1 implementation results.

## Documents

- [Diff against v0.3](Amendment1-against-v0.3.diff): primary proposed assignment artifact; rationales A1–A4 are embedded.
- [Readable proposed playbook](PLAYBOOK-Amendment1-PROPOSED.md): relative links adjusted for this folder; substantive policy matches the original proposal.
- [Original review packet ZIP](original-review-packet.zip): preserves the original guide, playbook, diff, disclosure and verification exactly. Its local paths and pre-intake evidence assessment are historical context.
- [Original patch validation](VALIDATION.txt): patch applied cleanly to the saved Team1 v0.3 baseline. This is an assistant check, not a human approval.
- [New intake candidate and measured reports](../evidence/intake-candidate-2026-11-04/README.md), [source-and-tests ZIP](../evidence/intake-candidate-2026-11-04/intake-candidate-source-and-tests.zip), [coverage table](../evidence/intake-candidate-2026-11-04/evidence/pytest-coverage.txt), [coverage XML](../evidence/intake-candidate-2026-11-04/evidence/coverage.xml) and [source manifest](../evidence/intake-candidate-2026-11-04/SOURCE-MANIFEST.json).
- [Publication AI record](../ai-logs/2026-11-04-austin-amendment1-publication.md).

## What the new candidate changes

The original amendment proposed 60% aggregate statement coverage over the full first-party application runtime without an actual baseline. The newly supplied packet reports 40 passing tests and 100% coverage over 127 statements in the narrower tickets package, excluding migrations. It includes a separate 90% proposal for that narrower scope. Neither percentage is adopted by this publication. The narrow report cannot establish the broad proposal's baseline, and this newly created source cannot establish historical Sprint 1 coverage. Original documents are preserved rather than silently rewritten to imply otherwise.

The source is archived for reproducible review, not installed as the repository's runtime application. The supplied reports are preserved results, not test runs performed during publication. Every manifest-listed source hash and the metadata's manifest hash were verified, and ZIP contents were compared byte for byte with the supplied folder.

## Remaining decisions before course submission

1. Confirm the professor's v0.3 baseline and whether the T4 confirmation-gap incident belongs to the course-defined Sprint 1; substitute a genuine in-sprint incident if needed.
2. Review the candidate and decide which codebase and coverage scope the team is committing to. Reproduce its tests on the eventual implementation commit before calling it an adopted Team1 baseline.
3. Reconcile the broad 60% and narrow 90% proposals explicitly, using the corresponding real report; update the final diff and CI together if adopting a floor.
4. Record the existing required team vote and non-author review, then submit the final diff and retain a sanitized portal receipt.

The canonical playbook remains [docs/PLAYBOOK.md](../PLAYBOOK.md). This documentation publication does not change policy, activate candidate code, configure a threshold or claim instructor receipt.
