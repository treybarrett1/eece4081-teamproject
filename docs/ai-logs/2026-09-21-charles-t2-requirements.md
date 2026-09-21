# AI session — T2 requirements and stakeholder specification

- Date: September 21, 2026; America/Chicago.
- Responsible member: Charles Barrett.
- Tool: OpenAI Codex; exact model version not exposed in the task record.
- Issue: https://github.com/treybarrett1/eece4081-teamproject/issues/5
- Baseline: 5c8b49e2f55925c87e8ec18645b5986370e9bd4a.
- Status: AI draft completed for human audit; human acceptance pending.

## User input and follow-ups

The initial September 21 message supplied two images, `Photo 1.jpg` and `Photo 2.jpg`, with no prose after “My request:”. The assistant interpreted this as continuing the established assignment-preparation workflow.

The images show T2 — Requirements and Stakeholder Specification and request: stakeholder interests/influence/needs; functional requirements; falsifiable non-functional requirements; epics/stories with acceptance criteria; charter-to-requirement-to-story traceability; a member authorship map; and an AI-use appendix. The rubric points are 5, 6, 6, 6, 3, 7, 3, 2, and 2 respectively (40 total).

Exact subsequent user-authored messages, in order:

> No authorship map yet, i think check the repo

> maybe in the playbook

> continue

The assistant checked the current playbook, charter, repository history, and PR #4. No T2 section-writing map was found. Roles and review assignments were treated as responsibilities, not as proof of authored prose.

## Context inspected

- Charter and Playbook v0.2 at the baseline commit.
- README, AI_LOG.md, and existing submission checklist.
- `docs/story-map-photo.jpg` and PR #4's workshop transcription.
- Verified artifact account: WoodlandMoss, commit b80c81caae26565bae59b4e3b107275055280c66; personal identity not assumed.
- Earlier user-confirmed project topic and team roster.
- No stakeholder interviews, actual ticket dataset, or implementation test evidence were supplied.

## Output disposition

Codex drafted the specification, a 20-source/32-requirement/20-story register, six epics, 72 acceptance criteria, 114 traceability combinations, 12 gap/conflict dispositions, a truthful authorship map, CSV, documentation validator, and human audit checklist.

The draft treats numeric bounds and response-time thresholds as proposed elaborations, not established stakeholder evidence. It preserves charter scope and records story-map ideas outside that scope as proposals requiring approval. It does not attribute generated prose to teammates. Human acceptance/rejection of the proposed requirements remains pending.

## Verification

Assistant checks: structural traceability completeness, uniqueness and referential integrity, correspondence of the register with the Markdown/CSV, local links/anchors, and Git whitespace checks. Remote file content is compared to the prepared package after publication. Results are recorded in `docs/t2/VALIDATION.md` and the PR.

These checks do not verify the software or the meaning of every requirement. No application tests, interviews, independent human review, policy adoption, or course submission are claimed.

## Human follow-up

Record actual section-writing contributions, accepted/modified/rejected requirements, reviewed commit, independent checks, and approval in the PR and specification authorship map. Review-only work must remain labeled review.
