# Engineering Playbook v0.2 — AI Tooling Guidelines

**Course:** EECE 4081-002 Software Engineering, Fall 2026  
**Prepared:** September 8, 2026  
**Updated:** September 16, 2026 — v0.2

**Team:** Charles Barrett, Austin Gross, Caleb Turris, and Doc Aberle  
**Status:** Complete working-agreement proposal for team review. Member agreement and meeting availability are not yet confirmed.

## 1. Branching strategy

Use short-lived feature branches from `main`. This is a feature-branch workflow. Branches are created per issue rather than committing directly to main, but are kept intentionally short-lived to minimize divergence. Name branches `feat/<issue-number>-<description>`, `fix/<issue-number>-<description>`, or `docs/<issue-number>-<description>`. Each branch addresses one issue with written acceptance criteria.

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
- [ ] Any AI assistance has a session entry in `docs/ai-logs/` linked from `AI_LOG.md`, with prompts, output disposition, and actual validation evidence. AI review findings are resolved or explained. If none was used, the PR says so.
- [ ] A named teammate other than the author has approved the latest substantive changes, and blocking review comments are resolved.

### After merge

- [ ] The PR has merged into `main`, and the source branch has been deleted.
- [ ] The author verifies the merged result with the applicable smoke check, records the outcome, and links the merged PR in the issue before closing it. A failing check triggers a fix or revert and keeps the issue open.

## 3. Sprint length and ceremonies

Use one-week sprints, Monday through Sunday, in America/Chicago time. The first partial week covers setup; the first full sprint begins Monday, September 14, 2026.

| Activity | Cadence | Required repository record |
| --- | --- | --- |
| Planning | Monday, 4:45-5:15 p.m. | Sprint goal, ordered issues, one owner and reviewer per issue, acceptance criteria, and each member's available hours |
| Asynchronous stand-up | Monday-Friday by 8:00 p.m. | Each member posts completed work, next work, and blockers in the sprint tracking issue |
| Midweek check | Wednesday, 5:00-5:15 p.m. | Blockers, overdue reviews, and revised assignments |
| Review/demo | Sunday, 4:55-5:15 p.m. | Demonstrated completed items, acceptance evidence, and unfinished items returned to the backlog |
| Retrospective | Sunday, 5:00-5:15 p.m. | One improvement action with an owner and a deadline in the next sprint |

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

## 5. Approved AI tools and permitted uses — v0.2

Charles reports that most members expect to use Claude Code for coding and ChatGPT for brainstorming. The proposed primary tools below reflect that preference; they do not require every member to use AI or claim unanimous team adoption. OpenAI Codex is additionally permitted for preparing and revising these course documents, as disclosed in the logs. An unlisted tool or additional use requires a policy-change PR and the adoption procedure below.

| Tool | Permitted uses | Limits |
| --- | --- | --- |
| Anthropic Claude Code — primary coding tool | Draft and revise application code, tests, bug fixes, and refactorings; explain code and provide advisory code-review findings | Work on a task branch; log prompts and affected files; verify generated changes with appropriate tests and human review. No self-approval, policy adoption, or autonomous merge into main. |
| OpenAI ChatGPT — primary brainstorming tool | Brainstorm requirements, user stories, acceptance criteria, design alternatives, and project plans; explain concepts and help organize ideas | Treat ideas as proposals until the team checks them. Brainstorming output is not an approved requirement or implementation. Coding and code-review uses are outside this approval. Do not invent interviews, approvals, sources, test results, or user needs. |
| OpenAI Codex — course-document assistance | Prepare and revise the playbook, assignment documentation, and associated prompt records | Disclose actual use and retain human audit. This limited permission does not authorize project coding or replace the team's primary tools. No self-approval, policy adoption, or autonomous merge into main. |

Approval is for these purposes only. No listed tool may decide grades, impersonate teammates, fabricate evidence, or send messages or take operational actions for real IT users. Generated code has the same acceptance criteria and review obligations as human-written code.

Use repository code that is authorized for sharing and synthetic ticket/bug records. Never put credentials, tokens, personal information, real internal ticket contents, staff-only notes, or confidential enterprise code into an AI prompt. Public-repository logs must also exclude those data. Sanitize first; do not assume a tool's privacy settings make restricted input acceptable. If a secret is accidentally shared, stop using the session and privately notify Charles immediately so access can be revoked or rotated; record only a sanitized incident summary.

Charles Barrett maintains the tool list. Caleb Turris evaluates proposed coding-tool changes and technical risks; Doc Aberle checks how their outputs can be tested. These responsibilities do not replace the team's policy-change vote. Reconsider the list at retrospectives when a tool, use case, or risk changes.

## 6. Prompt-log policy — v0.2

### What must be recorded

Log every project-related AI session used to generate, edit, explain, evaluate, or review requirements, code, tests, designs, or assignment documents, including sessions whose substantive recommendations are rejected. Routine commands that do not invoke AI need no prompt entry.

Each entry contains:

1. A stable ID, date and time zone, responsible member, tool/product, and model/version if displayed. Write "not exposed" when it is unavailable; do not guess.
2. The task, issue/PR link, base commit, and files or sanitized context supplied.
3. The exact user-authored prompts and material follow-up prompts in order. Record attachment names and a sanitized transcript or description of the relevant input. Do not disclose hidden system instructions, private chain-of-thought, or credentials.
4. The output used: a relevant excerpt or concise response summary plus the resulting diff/commit. Record material accepted, modified, and rejected suggestions and the reasons. Do not paste every generated file when the committed diff already preserves it.
5. Actual verification: commands or review steps, observed results, limitations, and the verifying person's name. Label assistant checks separately from human checks. Planned checks remain pending.
6. For AI-assisted review, the reviewed commit, every actionable finding, severity, disposition, and linked fix or reason for rejection.

For inline completions without a typed prompt, write "inline completion; no typed prompt," describe the surrounding context, and group related completions by issue and working session. Identify affected files and accepted behavior. A broad "AI helped" statement is insufficient. Exploratory conversations that materially influence the design must be logged even when no generated text is copied.

### Where and when

Store entries in `docs/ai-logs/YYYY-MM-DD-member-topic.md`, using [the prompt-log template](ai-logs/TEMPLATE.md). Add a dated summary and link in root `AI_LOG.md`. Commit the entry with the assisted change, before marking its PR ready for human review. Update the record before re-review when further AI assistance changes the work. Rejected explorations with no implementation are still logged on the issue's documentation branch before the issue closes.

Keep logs in Git history for the semester and retain them with the repository afterward. Correct mistakes with a dated amendment; do not erase earlier entries to hide assistance. If redaction is necessary, mark `[REDACTED: reason]` and retain the surrounding meaning without committing the sensitive original. Missing older transcripts must be labeled retrospective/incomplete; never reconstruct them as verbatim.

### Who is responsible

The member invoking the tool owns the entry and its accuracy, even if an AI drafts it. Charles Barrett maintains the index and checks log coverage at sprint review. Doc Aberle performs a weekly completeness check against AI-disclosed PRs and records gaps in the sprint issue. The assigned human PR reviewer checks the entry, output disposition, and verification evidence before approval. A missing required entry is a blocking review finding. If no AI was used, the author explicitly says so in the PR.

For this assignment, Charles owns the AI-assisted submission; the assistant prepared [the actual session record](ai-logs/2026-09-16-charles-playbook-v0.2.md). Human verification remains for the team.

## 7. AI-assisted code review — v0.2

**Decision: AI review is advisory only. It does not count, even partially, toward the one non-author teammate approval required by section 4.** A bot approval, generated "LGTM," or the author's review of their own AI-generated work supplies zero required approvals. This applies to all PRs, including small fixes and documentation changes.

**Why:** A tool can help identify suspicious code or missing cases, but its conclusions may be incorrect or miss project context. The team needs a named person accountable for checking acceptance criteria, access controls, and evidence. A human reviewer may use AI as an aid, but the human must independently inspect and validate the change and submit their own decision. Accountability cannot be delegated to a tool.

Follow this procedure:

1. The author completes the applicable checks and supplies the diff and acceptance criteria. If AI review is used, record the exact reviewed commit in the prompt log.
2. The author triages each actionable AI finding. For a claimed defect, reproduce it or perform a relevant inspection/test. Record accepted findings and fixes, and rejected findings with a reason. A suspected unauthorized-access or data-loss defect remains blocking until a human resolves it.
3. The assigned teammate from section 4 reads the actual diff and linked issue, checks the prompt log and finding dispositions, and runs relevant checks or explains why inspected evidence is sufficient. The reviewer does not merely copy the AI's verdict.
4. For this ticketing system, changes to permissions or visibility require checks for cross-requester access, staff-only notes, and direct endpoint/ID access. Ticket/bug changes require appropriate lifecycle and persistence checks.
5. Only the teammate's recorded approval satisfies section 4. Substantive changes after approval require re-review of the new commit. AI approval cannot override failing checks or an unresolved blocking finding.
6. If review stalls, use section 4's primary/backup reviewer deadlines. Tool availability does not shorten or bypass those rules. Disagreements about AI findings use the existing evidence-based conflict procedure.

Log "AI review not used" when it was not used; AI review is optional. Human review is mandatory. Record the reviewed commit and human reviewer identity in the PR. Do not mark an assignment audit complete based on the assistant's self-checks.

## Version record

- **v0.1:** Original working agreement, including later team edits preserved in sections 1–4.
- **v0.2 — September 16, 2026:** Adds the named AI-tool list, prompt-log policy, and advisory-only AI-review rule. Extends the definition of done and PR template to capture prompt-log evidence. Prepared for human audit; adoption and course submission are not claimed.

## Adoption and revision

Before adoption, Charles Barrett opens an adoption issue linking the charter and this playbook. All four members confirm their responsibilities, the review rotation, the proposed meeting schedule, and their weekly capacity in that issue. Each member records their own agreement; this proposal does not substitute for it.

Policy changes use a PR identifying the old rule, replacement, and reason. Approval requires a strict majority of team members and at least one non-author review. Changing an individual's availability requires that person's explicit agreement. Preserve previous versions in Git history.

These are written team rules; repository settings and automated enforcement have not been configured or verified.

## AI-use disclosure

OpenAI Codex drafted this agreement from the assignment screenshots, user-confirmed project topic and roster, and the user's request on September 8, 2026. The process rules and meeting times are proposed recommendations. Member consent, availability, and actual compliance have not been verified. The team must review the text and record adoption. No meetings, approvals, or passing project tests are claimed. See [AI_LOG.md](../AI_LOG.md).

**v0.2 disclosure:** OpenAI Codex prepared the September 16 additions using the supplied assignment screenshot and current repository files. Tool permissions are proposed policy, not a claim that all tools were used. The team will audit this work; no human approval, policy vote, or course submission is claimed. See the [session record](ai-logs/2026-09-16-charles-playbook-v0.2.md) and [audit checklist](PLAYBOOK_V0.2_AUDIT.md).
