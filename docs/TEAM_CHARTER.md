# T1 — Team Charter and Executive Summary

**Project:** Enterprise IT Ticketing and Bug System  
**Course:** EECE 4081-002 Software Engineering, Fall 2026  
**Date:** September 8, 2026  
**Repository:** https://github.com/treybarrett1/eece4081-teamproject  
**Team:** Charles Barrett, Austin Gross, Caleb Turris, and Doc Aberle  
**Version:** 1.0 — prepared for team review. Names and project topic are user-confirmed; responsibilities, scope, and meeting commitments below are proposed until team adoption is recorded.

## 1. Executive summary

The Enterprise IT Ticketing and Bug System is a web application that gives employees one place to report technology problems and software defects, and gives support staff a shared place to manage the response. An employee can describe a problem, receive a ticket number, and check its progress. Support staff can prioritize the request, assign responsibility, ask questions, and record a resolution. When the problem is a software defect, a developer can document how to reproduce it and link the defect to the original support ticket.

The project addresses a common coordination problem: requests spread across messages, email, and separate lists can lose their owner, history, or next step. The proposed system keeps those details together so requesters can see progress, support staff can avoid duplicate effort, and managers can identify unresolved or aging work. Linking related tickets and bugs should also help developers understand how a defect affects users without requiring employees to file a second report.

The semester deliverable is a working prototype for a single organization's internal workflow. Its central demonstration will follow an employee's report through support triage, a linked bug investigation, resolution, and closure. The prototype will use synthetic records and demonstration accounts. It is intended to demonstrate an understandable, testable workflow; adoption by a real enterprise is outside the semester commitment.

## 2. Scope statement

### In scope

| Capability | Semester boundary |
| --- | --- |
| Accounts and access | Demonstration accounts with requester, support agent, developer, and administrator roles; authorization enforced by the application |
| Ticket intake | Create a support ticket with a unique ID, title, description, category, reported impact, and creation time; requester can view their own tickets |
| Triage and ownership | Support staff set Low, Medium, High, or Critical priority, assign one current owner, and update status |
| Ticket lifecycle | New → Triaged → In Progress → Resolved → Closed; support may resolve a triaged ticket directly with a resolution note; requester may reopen their resolved or closed ticket to Triaged with a reason |
| Bug records | Record description, reproduction steps, expected and actual behavior, severity, owner, and status; link one bug to multiple support tickets and multiple bugs to a ticket |
| Bug lifecycle | Open → In Progress → Fixed → Verified → Closed; failed verification returns the bug to In Progress with an explanation |
| Communication and history | Timestamped requester-visible ticket comments, separately identified staff-only notes, and history of assignment, priority, status, and ticket/bug-link changes |
| Search and filtering | Staff search by ID or title and filter authorized results by status, priority/severity, and owner; requesters search only their own tickets |
| Dashboard | Counts of open tickets by status and priority, unassigned tickets, and ticket age calculated from creation time |
| Persistence and delivery | Data survives an application restart; documented setup, synthetic seed data, tests, and a repeatable end-to-end demonstration |

Requesters can access only their own tickets and public comments. Support agents can manage all support tickets and associate bugs. Developers can manage bug records and view the linked technical context needed for investigation. Administrators can manage application accounts and role assignments. Staff-only notes and bug details are not exposed through requester screens or endpoints. A linked bug's closure does not automatically close support tickets: support verifies the resolution for each affected requester.

### Explicitly out of scope

- Integration with corporate identity providers, single sign-on, directories, email inboxes, Slack, Teams, or commercial ticketing platforms.
- Multi-tenant hosting, billing, customer contracts, native mobile applications, and an external customer portal.
- Production availability guarantees, contractual service-level enforcement, automatic escalation, on-call paging, or 24-hour support.
- Automatic diagnosis, AI-generated resolutions, autonomous remediation, and remote control of employee devices.
- Full asset inventory, configuration management, procurement, change approval, and knowledge-base management.
- File uploads and attachments; users describe the issue and reproduction steps as text in this version.
- A general workflow designer or arbitrary custom fields; the prototype uses the defined roles, fields, and states.
- Migration of real enterprise data, handling of actual confidential tickets, or claims of production security certification.

### Scope-change control

A proposed addition is recorded as an issue with the user benefit, acceptance criteria, estimated effort, and a named owner. The team compares it with the sprint goal and remaining semester work. A strict majority of all team members must approve a change to the committed scope. If it adds work, the decision must identify work removed or explain why available capacity covers it. Record the decision and update this document through a PR before implementation. Instructor requirements take precedence over team scope decisions.

## 3. Stakeholders, roles, and interests

These are intended stakeholder groups, not claims that interviews or organizational commitments have occurred.

| Stakeholder | Role in the system or project | Actual interest |
| --- | --- | --- |
| Employee/requester | Reports problems and checks their own requests | Fast submission, a clear owner and next status, understandable resolution notes, and privacy from other requesters |
| IT support agent | Triages, assigns, investigates, and resolves tickets | One reliable queue, enough context to act, fewer duplicate requests, and a visible history of ownership and troubleshooting |
| Software developer/maintainer | Investigates and fixes linked bugs | Reproducible reports, expected versus actual behavior, severity, and links to affected support requests |
| IT support manager | Monitors the queue and balances assignments | Visibility into unassigned, high-priority, and aging work; consistent status definitions and dashboard counts that match underlying records |
| System administrator | Manages application accounts and roles | Predictable setup, correct access boundaries, and an auditable record of important changes |
| Student development team | Designs, builds, tests, and documents the prototype | A semester-sized commitment, clear responsibilities, reviewable work, and enough time for integration and validation |
| Course instructor/evaluator | Evaluates course deliverables and the final demonstration | Traceable requirements, concrete team practices, evidence supporting success claims, and honest AI-use disclosure |

Before finalizing detailed requirements, the team will seek feedback from potential requesters and support/developer representatives available through class or personal contacts. The requirements owner records the participant's role, questions, findings, and resulting decisions without placing private identifying details in the public repository. If a role cannot be reached, label its needs as assumptions.

## 4. Team charter

### Named responsibilities

The confirmed roster is Charles Barrett, Austin Gross, Caleb Turris, and Doc Aberle. Charles owns the repository through `treybarrett1`. The following assignments give each responsibility one accountable person and are proposed for team adoption.

| Responsibility | Named owner | Required work and evidence |
| --- | --- | --- |
| Team coordinator and scope owner | Charles Barrett | Maintains sprint goals and scope decisions; posts meeting notes; coordinates missed-commitment follow-up and instructor escalation |
| Requirements and user-experience owner | Austin Gross | Maintains stakeholder findings, acceptance criteria, and requester/staff workflow designs; checks delivered behavior against requirements |
| Application and data owner | Caleb Turris | Maintains ticket/bug data relationships, lifecycle rules, persistence, and server-side access controls; documents key design decisions |
| Quality and integration owner | Doc Aberle | Maintains acceptance scenarios, permissions checks, defect tracking, and release evidence; verifies a clean setup and final demonstration |
| Repository maintainer | Charles Barrett (`treybarrett1`) | Maintains repository access and document organization, checks contribution records, and verifies published submission links |
| Technical decision owner | Caleb Turris | Breaks a documented technical tie within the rule below; when involved in the dispute, Austin Gross acts as decision owner |
| Facilitator backup | Doc Aberle | Runs meetings and coordinates follow-up when Charles is absent or involved in the dispute; Austin Gross is second backup if both are involved |

Every member implements assigned work, reviews another member's work, records progress and blockers, and updates documentation affected by their changes. A responsibility owner coordinates a result; they are not expected to perform every task in that area alone. Nobody may approve their own PR.

### Meetings and availability

Use the one-week sprint and proposed ceremony schedule in [Playbook v0.1](PLAYBOOK.md): Monday planning at 6:00 p.m., Wednesday check-in at 6:00 p.m., and Sunday review and retrospective at 6:00 p.m., America/Chicago time. Weekday asynchronous updates are due by 8:00 p.m.

The proposed baseline is four hours per member per week, including ceremonies, with work scheduled around each person's classes and other obligations. Each person confirms or revises this baseline and the meeting times before adoption; the document does not claim personal availability has been verified. At each planning meeting, members report that week's exceptions and accept only work that fits their stated capacity. Planned absences require advance notice and an asynchronous update. Weekday work requests receive an acknowledgement within 24 hours.

GitHub issues and PRs are the record of work, decisions, and reviews. Private discussions that change a commitment must be summarized in the relevant issue without exposing personal information. Meeting notes record attendance and actions within 24 hours.

### Decision-making

1. An issue identifies the decision, its owner, options, and acceptance constraints.
2. The team discusses it for up to 20 minutes. If evidence is missing, agree on a measurable comparison and an experiment lasting no more than one working day.
3. Seek agreement first; otherwise use a strict majority of all team members. Asynchronous votes close 24 hours after the coordinator posts the options. Silence is not approval.
4. If the vote ties or no majority is reached, the named decision owner chooses a reversible technical option, explains the rationale, and sets a review date no later than the next sprint review.
5. Scope changes require the separate majority rule above. A tie-break cannot waive course requirements, approve someone's own PR, or change another person's availability. Escalate unresolved course-policy questions to the instructor.

### Conflict resolution: two reasonable technical approaches

Each participant writes a short account of their preferred approach, evidence, and tradeoffs in the issue. The facilitator restates the shared acceptance criteria and applies the decision process above. If the facilitator is involved in the dispute, the recorded backup facilitates. Debate addresses the proposal and evidence, not the person's motives. The final record includes the selected option, reason, owner, and revisit date so the same disagreement does not silently restart.

### Conflict resolution: two consecutive missed meetings

A meeting is missed when a member does not attend and has not arranged the asynchronous alternative in advance. An unforeseen emergency is handled privately and does not require disclosure of sensitive details.

After the first unexplained absence, the coordinator contacts the member within 24 hours, records the missed attendance, and requests a status update. After two consecutive unexplained absences, the coordinator contacts the member privately within 24 hours and asks for a response within the following 24 hours. The coordinator and member then agree on a written recovery plan within 48 hours of contact, listing outstanding work, revised dates, and a feasible meeting/update arrangement.

If the member does not respond by the deadline, or misses the recovery plan's first commitment without notice, the coordinator reassigns time-critical work and contacts the instructor with factual dates, attempted contacts, and outstanding work. Share only necessary information; do not publish personal circumstances. The team cannot impose grading penalties or remove a member without the instructor's direction.

### Missed work and interpersonal concerns

A member who expects to miss an issue deadline records the blocker before the deadline and proposes a revised date or reduced task. If a deadline passes without notice, the coordinator requests an update within 24 hours and revises assignments at the next check-in. Two unexplained missed commitments in a sprint trigger the same documented recovery process used for repeated absences.

For interpersonal conflict, first request a private conversation when appropriate. If it remains unresolved after 48 hours, ask the coordinator or uninvolved backup to mediate and record concrete future actions. Serious misconduct, or a conflict that cannot safely be handled directly, may go immediately to the instructor. Public records contain actions and decisions, not personal accusations.

### Adoption

Before submission, each member reviews the assigned responsibilities and confirms individual availability. Charles creates the charter-adoption issue, and Charles Barrett, Austin Gross, Caleb Turris, and Doc Aberle each record their own agreement. Later changes require a PR and a strict-majority vote; changes to a person's availability require that person's explicit agreement. No signatures or consent have been fabricated in this draft.

## 5. Success criteria

The following are end-of-semester targets, not results already achieved. The quality owner records evidence against each criterion and the tested commit.

| Criterion | Checkable target | Evidence |
| --- | --- | --- |
| Complete support workflow | A requester submits a ticket; support triages and assigns it, creates a linked bug, records progress, resolves it, and the requester verifies/ closes it. A reopened issue returns to the queue with a reason. | Repeatable demo script and pass/fail record |
| Reliable bug workflow | Required bug fields are validated; a bug can link to two tickets; a failed verification returns it to In Progress; closing it leaves support tickets unchanged until individually resolved. | Integration scenarios and recorded results |
| Correct access boundaries | Requesters cannot read or change another requester's tickets, see staff-only notes, or access staff endpoints by changing an ID or URL. Support/developer/admin permissions match the documented role matrix. | Allow/deny tests for every role, including direct endpoint requests |
| Consistent data and lifecycle | Invalid status transitions are rejected; assignment, priority, status, and link changes record actor and time; tickets, bugs, comments, and links survive a restart. | Automated tests plus restart verification |
| Accurate queue visibility | With at least 100 seeded tickets and 20 bugs, filters and dashboard counts match independently calculated expected results. | Seed data and comparison results |
| Usable requester experience | At least four of five volunteer evaluators can submit a ticket and find its status within five minutes using the provided instructions and no live coaching. | Anonymous task results, timing, and recorded usability defects |
| Repeatable delivery | A teammate who did not write the setup guide can initialize a fresh checkout, load synthetic data, and run the demo using the guide. | Setup checklist, environment details, and tested commit |
| Delivery quality | All committed acceptance criteria pass; there are no open defects causing unauthorized access, data loss, or a blocked core workflow. Other known issues are listed with impact and workarounds. | Acceptance report and final issue list |
| Team accountability | Every post-adoption merged PR links an issue and records independent approval and validation; all sprint reviews and retrospectives have notes. | Repository history and meeting records |

If a target cannot be met, document the failed result, impact, and any agreed scope revision rather than marking it complete without evidence.

## 6. Appendix: AI-use disclosure

**Tool:** OpenAI Codex.  
**Date:** September 8, 2026.  
**Inputs:** Four user-supplied screenshots containing the T1 and EP 0.1 instructions/rubrics; the request to prepare a team repository and assignments; the user's project description, “enterprise it ticketing and bug system”; and the user-confirmed roster of Austin Gross, Charles Barrett, Caleb Turris, and Doc Aberle.

**Assistance:** Codex drafted the executive summary, proposed scope and exclusions, stakeholder-interest analysis, operating rules, acceptance targets, and companion engineering playbook. It also prepared the repository documentation and published the assignment files through the GitHub connection.

**Limits and review status:** The user supplied the project topic and all four team members' names. Detailed requirements, stakeholder access, acceptance of the proposed role assignments, meeting availability, and team adoption have not been confirmed. The drafts do not report completed interviews, implemented software, passing tests, member consent, or assignment submission.

**Human responsibility:** Team members must correct assumptions, accept or revise their named responsibilities, review the documents against the assignment rubrics, and record their adoption. Actual future validation and edits belong in [AI_LOG.md](../AI_LOG.md); they must not be backdated or invented.
