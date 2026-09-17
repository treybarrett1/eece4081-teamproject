# AI session: Playbook v0.2

- ID: 2026-09-16-charles-playbook-v0.2
- Date/time zone: September 16, 2026; America/Chicago.
- Responsible member: Charles Barrett.
- Tool: OpenAI Codex; exact model version not exposed in the task record.
- Issue: https://github.com/treybarrett1/eece4081-teamproject/issues/1
- Base commit: `487c2039c91335dc189b4aefe63e4094c228dc89`.
- Human audit status: pending. This entry was drafted by the assistant and awaits Charles's verification.

## Exact user-authored prompt

> please do the assignment and let me know when its done so we audit you.

No additional user-authored substantive follow-up prompt had been received when this entry was prepared. Environment/tool permission interactions are not project-design prompts.

## Supplied context

The user attached `Photo 1.jpg`, a screenshot of **Playbook v0.2 — AI Tooling Guidelines** for EECE 4081-002. Relevant instructions visible in that image:

1. Approved tools: name the tools and permitted purposes, which can be limited by use.
2. Prompt-log policy: state what gets logged, where the record lives, and who is responsible.
3. AI-assisted code review: explicitly decide whether tool review satisfies, partially satisfies, or does not satisfy the v0.1 review requirement, and explain why.
4. Submission: commit the updated playbook to the team repository, clearly marked v0.2; one submission per team.

Visible rubric rows allocate 3 points to named tools/permitted uses, 2 to prompt-log what/where/who, and 3 to a clear position on AI review. The assignment total is 10 points; the remaining rubric rows are outside the supplied image. No unseen wording is inferred. The sidebar shows a September 16 deadline at 11:59 p.m.

The assistant read the current playbook, README, AI log, PR template, and submission checklist. Existing team edits were preserved. The original roster and project context came from earlier user messages in this same conversation. No real IT tickets, credentials, or confidential organizational data were supplied as drafting context.

## Output and disposition

The assistant drafted:

- Playbook v0.2 sections 5–7: OpenAI Codex, OpenAI ChatGPT, and GitHub Copilot permitted-use policy; prompt-record ownership and location; advisory-only AI review with a rationale and operational procedure.
- A definition-of-done update requiring traceable prompt records.
- A reusable prompt-log template and this actual session record.
- An uncompleted human-audit checklist mapping the visible rubric and submission requirement.
- README and PR-template references, plus a root AI-log index entry.

The repository diff preserves the exact proposed output. These are proposed changes, not team-accepted recommendations. No human accepted/rejected disposition is recorded yet. The assistant selected the advisory-only option to preserve v0.1's non-author approval requirement; it did not adopt that choice on the team's behalf.

## Verification record

Assistant checks are limited to document consistency, preservation of the existing workflow and team edits, required-section coverage, local relative links, whitespace, and remote publication/content read-back. Actual results are reported in the PR. No application tests are appropriate to this documentation-only assignment, and none are claimed.

Human verification is pending. Austin Gross is the primary reviewer and Doc Aberle the backup under the existing Charles-authored-work rotation; this does not claim either person has accepted or completed the review.

## Limitations and audit attention

- Tool permissions and process additions require team adoption.
- The existing Sunday review/demo (4:55–5:15 p.m.) and retrospective (5:00–5:15 p.m.) overlap. The assistant retained those team-edited times; the team should decide whether the overlap is intentional.
- The screenshot's rubric is cropped below the third visible criterion.
- No independent AI reviewer or human reviewer has audited this work.
- Nothing has been submitted in the course portal.

## Human audit — leave blank until performed

- Reviewer and date:
- Reviewed commit:
- Accepted recommendations and rationale:
- Modified/rejected recommendations and rationale:
- Checks performed and observed results:
- Remaining issues:
- Approval/adoption decision:

## September 16 amendment — team tool preference

Subsequent user prompts, in order:

> im confused on what the assignment is asking us to do

> i guess it will be claude code for coding and chatgpt for brainstorming for majority of the members.

The assistant explained the three required policy decisions, then revised section 5 to name Anthropic Claude Code as the primary coding tool and OpenAI ChatGPT as the primary brainstorming tool. GitHub Copilot was removed from the proposed list. OpenAI Codex remains permitted only for course-document assistance and remains disclosed as the tool actually used here. The initial output description above is retained as history, not the current tool list.

Disposition: the user's clarification supersedes the assistant's original suggested primary tools. It expresses expected majority usage, not unanimous adoption. Prompt logging and the proposed human-approval requirement remain unchanged. Assistant checks for this amendment compare the updated remote text with the prepared changes; no human audit or application test run is claimed.
