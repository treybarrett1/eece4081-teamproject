# Engineering Playbook v0.1

**Course:** EECE 4081-002 Software Engineering, Fall 2026  
**Prepared:** September 8, 2026  
**Team:** Charles Barrett, Austin Gross, Caleb Turris, and Doc Aberle  
**Status:** Complete working-agreement proposal for team review. Member agreement and meeting availability are not yet confirmed.

## 1. Branching strategy

Use short-lived feature branches from `main`. Name branches `feat/<issue-number>-<description>`, `fix/<issue-number>-<description>`, or `docs/<issue-number>-<description>`. Each branch addresses one issue with written acceptance criteria.

Open a draft pull request within 24 hours of the first branch commit. Merge or close the branch within three calendar days of that commit. If the work cannot fit, split the issue into smaller, independently reviewable changes. Before the three-day limit, the author must record any extension, its reason, and a new deadline in the PR; the assigned reviewer must approve it. Only one extension of up to two calendar days is permitted.

Update the branch from `main` before final validation. Merge through a pull request using squash merge, then delete the source branch. Do not force-push `main`, commit credentials, or bypass review to meet a deadline. Initial repository setup before adoption of this agreement may use direct commits; all changes after adoption, including document changes, require PRs.

## 2. Definition of done

A work item is done only when every applicable check below is satisfied and its evidence is recorded in the PR. A not-applicable check requires a written reason accepted by the reviewer.

### Before merge

- [ ] The PR links an issue with one named owner and measurable acceptance criteria.
- [ ] Every acceptance criterion has a recorded pass result or linked evidence; unmet criteria keep the issue open.
- [ ] Changed behavior has appropriate automated coverage, including relevant invalid inputs or failure paths. Document-only changes receive content, link, and consistency checks.
- [ ] Applicable documented build, test, and lint commands pass. The PR records commands and results; configured required CI checks pass on the latest commit.
- [ ] Relevant user-facing behavior has been manually exercised, with steps and observed results recorded. UI changes include screenshots when helpful.
- [ ] Setup instructions, user documentation, and design notes reflect changed behavior where applicable.
- [ ] The diff contains no credentials, private user data, unexplained generated files, or unrelated changes.
- [ ] Any AI assistance is recorded in `AI_LOG.md`, including affected files and human verification completed or still required. If none was used, the PR says so.
- [ ] A named teammate other than the author has approved the latest substantive changes, and blocking review comments are resolved.

### After merge

- [ ] The PR has merged into `main`, and the source branch has been deleted.
- [ ] The author verifies the merged result with the applicable smoke check, records the outcome, and links the merged PR in the issue before closing it. A failing check triggers a fix or revert and keeps the issue open.

## 3. Sprint length and ceremonies

Use one-week sprints, Monday through Sunday, in America/Chicago time. The times below are proposed until members confirm availability. The first partial week covers setup; the first full sprint begins Monday, September 14, 2026.

| Activity | Cadence | Required repository record |
| --- | --- | --- |
| Planning | Monday, 6:00-6:30 p.m. | Sprint goal, ordered issues, one owner and reviewer per issue, acceptance criteria, and each member's available hours |
| Asynchronous stand-up | Monday-Friday by 8:00 p.m. | Each member posts completed work, next work, and blockers in the sprint tracking issue |
| Midweek check | Wednesday, 6:00-6:15 p.m. | Blockers, overdue reviews, and revised assignments |
| Review/demo | Sunday, 6:00-6:20 p.m. | Demonstrated completed items, acceptance evidence, and unfinished items returned to the backlog |
| Retrospective | Sunday, 6:20-6:35 p.m. | One improvement action with an owner and a deadline in the next sprint |

Charles Barrett is the sprint facilitator; Doc Aberle is the backup, with Austin Gross as second backup. The facilitator posts notes in `docs/meetings/YYYY-MM-DD.md` within 24 hours, including attendance, decisions, and actions with owners and dates. For a moved meeting, the facilitator records the replacement time at least 24 hours ahead unless an emergency prevents notice. Asynchronous participation must still produce the required record.

Members acknowledge direct work requests within 24 hours on weekdays. A blocked member records the blocker as soon as it becomes known, and no later than the next stand-up. Each member gives notice of a planned absence before the meeting and supplies an asynchronous update.

## 4. Pull requests and review rules

### Responsibility and approval

Use the following default review rotation. Charles Barrett records the reviewer names in each issue at planning and maps them to GitHub handles when members join the repository. The author requests the primary's review in the PR. No member may review or approve their own work.

| PR author | Primary reviewer | Backup reviewer |
| --- | --- | --- |
| Charles Barrett | Austin Gross | Doc Aberle |
| Austin Gross | Caleb Turris | Charles Barrett |
| Caleb Turris | Doc Aberle | Austin Gross |
| Doc Aberle | Charles Barrett | Caleb Turris |

Charles may record a reassignment to another available non-author when expertise or availability requires it; the replacement must acknowledge the assignment in the issue. No item enters implementation without a named primary reviewer.

The author requests review after adding the change description, linked issue, validation evidence, and known limitations. Keep PRs focused. For more than 400 non-generated changed lines, explain why splitting would prevent meaningful review or split the change.

One approval from a teammate other than the author is required. The reviewer checks acceptance criteria, correctness, error handling, appropriate tests, readability, documentation, and accidental exposure of credentials or private data. The reviewer runs relevant validation or records which evidence was inspected and why it was sufficient. Document reviews check rubric coverage, specific responsibilities, and consistency with the charter.

### Review deadlines and stalls

The primary reviewer acknowledges the request within 24 hours and provides approval or actionable comments within 48 hours of the request. If either deadline is missed, the author records it and requests the backup, who must provide a review within 24 hours of reassignment.

If there is no eligible available backup, or the backup misses the deadline, the facilitator records the blocker and arranges a review session within the next 24 hours. The PR stays unmerged until an eligible reviewer approves. The team reduces or reschedules the affected sprint work when review capacity is unavailable; a deadline never permits self-approval.

### Comments, disagreements, and merging

Label comments blocking or nonblocking. A blocking comment identifies a failing acceptance criterion, defect, or violated rule and describes a verifiable resolution. The author addresses it or explains an alternative with evidence. Substantive commits after approval require another review.

For two reasonable approaches in dispute, participants record the options and tradeoffs in the issue. Time-box discussion to 20 minutes. If evidence is missing, agree on a comparison criterion and run an experiment of at most one working day. Then use a strict-majority team vote. If tied, Caleb Turris selects a reversible technical option and records the reason and a date to revisit it no later than the next sprint review. If Caleb is involved in the dispute, Austin Gross acts as decision owner. This tie-breaking rule cannot override course requirements, definition-of-done checks, or an individual's agreed availability.

The author may merge when all before-merge checks pass, then completes the after-merge checks. Scope changes follow the charter's scope-change procedure.

## Adoption and revision

Before adoption, Charles Barrett opens an adoption issue linking the charter and this playbook. All four members confirm their responsibilities, the review rotation, the proposed meeting schedule, and their weekly capacity in that issue. Each member records their own agreement; this proposal does not substitute for it.

Policy changes use a PR identifying the old rule, replacement, and reason. Approval requires a strict majority of team members and at least one non-author review. Changing an individual's availability requires that person's explicit agreement. Preserve previous versions in Git history.

These are written team rules; repository settings and automated enforcement have not been configured or verified.

## AI-use disclosure

OpenAI Codex drafted this agreement from the assignment screenshots, user-confirmed project topic and roster, and the user's request on September 8, 2026. The process rules and meeting times are proposed recommendations. Member consent, availability, and actual compliance have not been verified. The team must review the text and record adoption. No meetings, approvals, or passing project tests are claimed. See [AI_LOG.md](../AI_LOG.md).
