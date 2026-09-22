# T4 — Scope Agreement

- **Project:** Enterprise IT Ticketing and Bug System
- **Course:** EECE 4081-002 Software Engineering, Fall 2026
- **Version/date:** 0.1 proposal / September 22, 2026
- **Status:** Pending team scope approval, capacity confirmation, and review; not the accepted grading baseline yet.
- **Work item:** [Issue #9](https://github.com/treybarrett1/eece4081-teamproject/issues/9)
- **T2 baseline:** [Reviewed specification at bba8b22](https://github.com/treybarrett1/eece4081-teamproject/blob/bba8b22a8c976b54ba4e93f53a091cb3004bd26e/docs/T2_REQUIREMENTS.md)
- **Submission lead:** Doc Aberle, selected by Charles; Doc's acknowledgement and portal access are pending. See the [T3/T4 handoff](T3_T4_SUBMISSION_HANDOFF.md).

## 1. Delivery commitment and boundary

**Proposed commitment for session 26: a working support-ticket application in which a requester signs in, submits and follows their own ticket, and Support triages, assigns, and resolves it. The requester can close or reopen it. Required changes have persistent, attributable history.** The team will demonstrate the four items below from a fresh checkout using synthetic accounts and records.

We deliberately defer software-bug management and reporting to make one complete support workflow the delivery target. This reduces the original product vision; it is not a claim that ticket-only delivery satisfies all of T2. Session 26 is the demonstration milestone given by the assignment. Its calendar date and the two course sprint dates must be copied from the course schedule before acceptance; this document does not invent them or assume the playbook's weekly cadence equals those course milestones.

### Reconciliation with T2 and the charter

T2 labels all 32 requirements Must. This T4 proposes a **scope amendment**, with the exact retained/deferred portions in section 3. The T2 document and register remain the historical requirements baseline; omitted work cannot be reported as implemented or passed. This amendment reduces charter commitments C05–C09 and the bug-related portions of G01–G02, plus the specific deferred targets below.

Before acceptance, at least three of the four members must approve this scope change under the charter, each member must confirm their own hours/assignments, and a non-author must review the final revision. Doc will confirm that the proposed reduction complies with course instructions and resolve any conflict with the instructor before submission. The submission is the agreed T4 grading baseline; retaining a requirement in the T2 register does not silently restore a deferred delivery promise.

No contingency cut automatically changes an accepted or submitted baseline. Section 5 explains the change procedure. T3's architecture proposal remains a separate decision: shared workflow services can support the retained ticket slice, but its examples involving bugs do not make those deferred features committed. Revisit that ADR's context during team review if this reduction is accepted.

## 2. Specific committed items and demonstration criteria

All items are mandatory if this proposal is accepted. Each numbered criterion is pass/fail; no completed application or passing product test is claimed. Proposed owners coordinate work and remain subject to their acknowledgement.

### S1 — Seeded sign-in and protected ticket access

**Proposed owner:** Caleb Turris. **Reviewer:** Doc Aberle. **Estimate:** 4 person-hours including implementation checks and review.

**T2 trace:** [FR01](T2_REQUIREMENTS.md#fr01), [FR03](T2_REQUIREMENTS.md#fr03), [NFR01](T2_REQUIREMENTS.md#nfr01); seeded delivery portion of [FR20](T2_REQUIREMENTS.md#fr20).

1. Seed two Requesters, two Support users, one Developer, and one Administrator with synthetic identities. Demonstration credentials are provided through setup, never committed as live credentials.
2. An active seeded account signs in and signs out. Invalid/disabled credentials fail without revealing which field failed; a signed-out or disabled session cannot access protected ticket data on its next request. Use a controlled test fixture to disable an account; an account-management screen is deferred.
3. Requester A cannot read, list, or mutate Requester B's tickets, including direct ID requests. Support may access both. Developer and Administrator accounts cannot perform ticket operations in this slice; they do not inherit Support rights.
4. No client-submitted requester ID or role can give additional access. Every exposed role/action combination has a positive or negative test, including two-requester isolation.

### S2 — Ticket submission and progress views

**Proposed owner:** Austin Gross. **Reviewer:** Caleb Turris. **Estimate:** 5 person-hours including tests and review.

**T2 trace:** [FR04](T2_REQUIREMENTS.md#fr04), retained fields of [FR05](T2_REQUIREMENTS.md#fr05), input rules of [FR21](T2_REQUIREMENTS.md#fr21).

1. A Requester creates a ticket with title, description, category, and impact using the T2 allowed values and text limits. The server sets unique immutable ID, authenticated requester, UTC creation time, New state, no owner, and no priority.
2. Blank/overlong values, unknown category/impact, and forged ownership fail without partial data. Identical titles still create distinct IDs. User text renders as text rather than executable markup.
3. A Requester can list their own tickets and open a detail page showing the FR05 fields that exist in this slice: ID, title, category, impact, state, owner or Unassigned, priority or Not triaged, timestamp, and resolution note when present. Support has an all-ticket list and detail view.
4. Refresh after an authorized update shows the current state/owner/priority. General comment threads, search, filters, and dashboard counts are deferred; plain lists are not claimed as FR17 search.

### S3 — Complete ticket lifecycle with attributable history

**Proposed owner:** Caleb Turris; Charles Barrett contributes workflow/history work before or after his unavailable date. **Reviewer:** Austin Gross. **Estimate:** 8 person-hours including tests and review.

**T2 trace:** [FR06](T2_REQUIREMENTS.md#fr06), ticket-assignment portion of [FR07](T2_REQUIREMENTS.md#fr07), [FR08](T2_REQUIREMENTS.md#fr08), [FR09](T2_REQUIREMENTS.md#fr09), ticket-history portion of [FR12](T2_REQUIREMENTS.md#fr12), [FR21](T2_REQUIREMENTS.md#fr21), [NFR08](T2_REQUIREMENTS.md#nfr08).

1. Support confirms/corrects category, preserves reported impact, and selects Low, Medium, High, or Critical priority to move New → Triaged. Later priority changes are recorded.
2. Support assigns/reassigns one active Support owner. Triaged → In Progress requires that owner. An inactive or wrong-role assignee fails. Runtime account role/disable management is deferred; setup/test changes must not be used as a user-facing bypass of owner invariants.
3. Support resolves a Triaged or In Progress ticket only with a nonblank public resolution note. Only the owning Requester may confirm Resolved → Closed or reopen Resolved/Closed → Triaged with a nonblank reason. Reopening preserves priority, owner, and earlier history.
4. Every allowed transition is demonstrated/tested; at least one unlisted transition from each state and wrong-actor transitions are rejected without modifying data or history.
5. Ticket category, priority, owner, and status changes produce exactly one immutable event per changed field with actor ID, record ID, UTC time, and old/new values. History sorts by timestamp then event ID. Support sees ticket history; Requesters see only their own public status/priority/owner history. Credentials and staff-only content never appear in those responses.

### S4 — Reproducible, persistent demonstration with acceptance evidence

**Proposed owner:** Doc Aberle, with Charles maintaining the setup/demo instructions. **Reviewer:** Austin Gross. **Estimate:** 5 person-hours including integration, review, and evidence capture.

**T2 trace:** retained delivery portions of [FR20](T2_REQUIREMENTS.md#fr20), [FR22](T2_REQUIREMENTS.md#fr22), [NFR02](T2_REQUIREMENTS.md#nfr02), [NFR06](T2_REQUIREMENTS.md#nfr06), [NFR07](T2_REQUIREMENTS.md#nfr07), [NFR10](T2_REQUIREMENTS.md#nfr10).

1. Commit prerequisites, setup/seed/test commands, and a scripted demo using the S1 accounts and at least four synthetic tickets split between the two Requesters. Seed loading on a fresh database is repeatable; roles remain fixed for the ordinary demo.
2. A teammate other than the setup-guide author completes a fresh checkout, seed, and demo without undocumented corrections or live coaching. Record the tested commit, environment, person, and result.
3. The script executes S1–S3, including direct resolution, the In Progress route, closure, both reopening routes, and unauthorized access rejection. Capture each criterion's pass/fail result. Rejected operations must leave history unchanged.
4. Snapshot the tickets, required notes/reasons, owners, priorities, and history; restart the app/database without reseeding; compare with zero mismatches. Inject a failure between one ticket update and its history write: both persist or neither persists, with no partial result. This is the narrowed ticket-only protocol, not a claim to have run T2's ten workflows including bugs.
5. Before demonstration, all retained criteria must pass and no open defect may expose unauthorized data, lose acknowledged records, or block the committed workflow. Record other defects and workarounds. Inventory the delivered seed/demo/evidence artifacts and verify zero real employee tickets, confidential records, or live credentials.

## 3. Explicit deferrals and T2 disposition

**Deferred** means outside the session-26 delivery commitment, not a hidden stretch promise. **Retained subset** names a deliberate reduction; it does not mark the original whole requirement satisfied. No deferred feature is added back merely because spare time appears: finish the committed slice first and use the scope-change procedure for additions.

| T2 requirement | T4 disposition and exact boundary |
| --- | --- |
| [FR01](T2_REQUIREMENTS.md#fr01) | Retain sign-in, disabled-account rejection, and sign-out for seeded accounts (S1); administrator-created accounts are deferred with FR02. |
| [FR02](T2_REQUIREMENTS.md#fr02) | Defer account creation, role editing, and enable/disable UI/endpoints. Controlled test setup is not this feature. |
| [FR03](T2_REQUIREMENTS.md#fr03) | Retain all permissions for exposed S1–S3 paths; deny unavailable operations. Full bug/account/search/dashboard matrix deferred with those features. |
| [FR04](T2_REQUIREMENTS.md#fr04) | Retain ticket intake (S2). |
| [FR05](T2_REQUIREMENTS.md#fr05) | Retain own-ticket progress and resolution fields (S2); general comment display deferred with FR10. |
| [FR06](T2_REQUIREMENTS.md#fr06) | Retain triage and priority updates (S3). |
| [FR07](T2_REQUIREMENTS.md#fr07) | Retain assignment/reassignment and active-owner entry guard (S3); account-administration disable/role-change workflow deferred with FR02. |
| [FR08](T2_REQUIREMENTS.md#fr08) | Retain full ticket transition/actor guards (S3). |
| [FR09](T2_REQUIREMENTS.md#fr09) | Retain resolution, requester closure, and both reopening routes (S3). |
| [FR10](T2_REQUIREMENTS.md#fr10) | Defer general public comment threads; required resolution/reopening notes remain in S3. |
| [FR11](T2_REQUIREMENTS.md#fr11) | Defer staff-note creation/display and developer technical context; no private-note feature is exposed. |
| [FR12](T2_REQUIREMENTS.md#fr12) | Retain ticket category/owner/priority/status history (S3); bug/link/account-change history deferred with those mutations. |
| [FR13](T2_REQUIREMENTS.md#fr13) | Defer bug creation and reproduction fields. |
| [FR14](T2_REQUIREMENTS.md#fr14) | Defer bug ownership, claiming, reassignment, and technical edits. |
| [FR15](T2_REQUIREMENTS.md#fr15) | Defer all ticket–bug links and linked-bug demonstrations. |
| [FR16](T2_REQUIREMENTS.md#fr16) | Defer fixing/verifying/closing bugs and failed-verification loops. |
| [FR17](T2_REQUIREMENTS.md#fr17) | Defer ticket text/ID search and combinable filters; retain only S2's plain authorized lists/details. |
| [FR18](T2_REQUIREMENTS.md#fr18) | Defer bug searches/filters. |
| [FR19](T2_REQUIREMENTS.md#fr19) | Defer queue dashboard, aggregated counts, and age calculations. |
| [FR20](T2_REQUIREMENTS.md#fr20) | Retain reproducible synthetic seed setup (S4), reduced to six accounts and at least four tickets. Defer 100-ticket/20-bug fixture and dashboard expectations. |
| [FR21](T2_REQUIREMENTS.md#fr21) | Retain all input validation, safe text display, and no-partial-write rules for S1–S3; deferred features introduce no endpoints. |
| [FR22](T2_REQUIREMENTS.md#fr22) | Retain fresh setup and ticket-only end-to-end demo (S4); bug/link/fix/verification stages are explicitly removed. |
| [NFR01](T2_REQUIREMENTS.md#nfr01) | Retain complete allow/deny coverage for the exposed slice, including revoked/disabled-session fixtures (S1); broader matrix deferred. |
| [NFR02](T2_REQUIREMENTS.md#nfr02) | Retain ticket restart comparison and fault-injected atomicity (S4); original W01–W10 including bug/link/comment workflows deferred. |
| [NFR03](T2_REQUIREMENTS.md#nfr03) | Defer formal five-volunteer usability study and its 4-of-5/five-minute target. No equivalent result claimed. |
| [NFR04](T2_REQUIREMENTS.md#nfr04) | Defer dashboard/filter accuracy study with those features. |
| [NFR05](T2_REQUIREMENTS.md#nfr05) | Defer five-session response-time benchmark and 95-of-100/two-second target; no performance guarantee substituted. |
| [NFR06](T2_REQUIREMENTS.md#nfr06) | Retain independent fresh-checkout reproduction for the committed demo (S4). |
| [NFR07](T2_REQUIREMENTS.md#nfr07) | Amend release gate to 100% of this accepted T4's retained criteria, not all 72 T2 criteria. Preserve zero critical access/data-loss/core-workflow defects (S4). |
| [NFR08](T2_REQUIREMENTS.md#nfr08) | Retain required ticket audit events, immutability, ordering, and payload exclusions (S3); other domains deferred. |
| [NFR09](T2_REQUIREMENTS.md#nfr09) | Retain issue/review/AI evidence and sprint records as team obligations. Original playbook adoption remains separately unverified; T4 approval does not backdate it. |
| [NFR10](T2_REQUIREMENTS.md#nfr10) | Retain synthetic-only data and artifact inspection for all delivered assets (S4). |

Original exclusions remain: corporate SSO/email/chat integrations, billing/multiple tenants, native mobile app, production SLAs/on-call, AI remediation, asset/procurement management, and real enterprise-data migration. Attachments and customizable workflows have no positive commitment and remain outside this delivery.

## 4. Two-sprint plan and capacity

**Planning assumption, not confirmed availability:** four members × four hours/week × two one-week delivery sprints = 32 person-hours. This uses the charter's tentative baseline. Confirm the course sprint/session dates and each person's actual capacity before accepting it. Charles's absence on the assignment due date does not establish his availability for either implementation sprint; his hours below need separate confirmation.

Budget **22 hours of item work including tests/review**, **4 hours of coordination**, and **6 hours of contingency**. This is a rough planning estimate, not measured velocity. Required ceremonies and asynchronous updates must fit the coordination allowance or the team must revise capacity/commitments before acceptance; the budget does not waive the playbook. Basic server-rendered forms/lists are assumed; custom visual polish is deferred.

| Delivery sprint | Sequence and exit evidence | Item hours | Coordination | Reserve |
| --- | --- | --- | --- | --- |
| Sprint 1 | S1 access (4h), S2 intake/read (5h), S4 initial setup/fixtures (2h). Fresh seed → sign-in → create → own detail works; cross-requester direct-ID test denies access. | 11 | 2 | 3 |
| Sprint 2 | S3 lifecycle/history (8h), S4 independent setup/restart/fault-injection/demo evidence (3h). All S1–S4 criteria and release gates have results. | 11 | 2 | 3 |
| **Total** | Session-26 demo uses the tested commit. | **22** | **4** | **6** |

Proposed distribution makes the individual capacity assumption visible:

| Member | Item work allocation | Work | Coordination | Reserve | Total / confirmation |
| --- | --- | --- | --- | --- | --- |
| Charles Barrett | S2 assistance 1h; S3 workflow/history 3h; S4 instructions 2h | 6 | 1 | 1 | 8h / pending |
| Austin Gross | S2 UI/validation 4h; S3 acceptance/review 2h | 6 | 1 | 1 | 8h / pending |
| Caleb Turris | S1 access 4h; S3 lifecycle/integration 3h | 7 | 1 | 0 | 8h / pending |
| Doc Aberle | S4 setup/verification/evidence 3h | 3 | 1 | 4 | 8h / pending |

Owner/reviewer participation must be included in these allocations; they are not extra unpaid capacity. Doc's reserve is shared integration/defect capacity, not four hours of additional committed features. If estimates or ceremony costs do not fit confirmed hours, reduce scope before accepting the baseline. A reviewer must challenge these estimates against the actual starting code and skills; the repository currently supplies documentation, not an implemented application.

Dependencies: agree the minimal implementation approach; establish setup/seed/access before intake; land intake before lifecycle; add history with mutations, not at the last minute. Record actual course sprint dates, session-26 date, and the tested implementation baseline in the issue when confirmed.

## 5. Delivery risks and stated cut order

| Risk / trigger | Proposed mitigation owner and response | First scope action if mitigation fails |
| --- | --- | --- |
| Capacity lower than 32h, or member hours unconfirmed at scope review | Doc collects actual availability, including Charles's implementation availability; re-estimate before acceptance. | Apply candidate cut C1 first, then C2 if required; do not accept a baseline with unfunded work. |
| Fresh seed/sign-in/intake/own-detail path fails at Sprint 1 exit | Caleb integrates one working path; Doc spends reserve reproducing setup/access defects. | Freeze additions and propose C1. |
| Lifecycle/history work exceeds its 8h estimate or uses more than half the total reserve | Caleb and Austin isolate failing transitions; keep successful guarded paths and their tests together. | C1, then C2, then C3, in that order. |
| Unauthorized access, lost history, or partial writes in any rehearsal | Doc records a blocking defect; Caleb fixes it before cosmetic work. | Cut optional workflow breadth before safeguards; if the remaining core is unsafe, report it as incomplete. |
| Charles unavailable and Doc cannot submit/access the portal | Doc acknowledges and checks access early; Austin is the proposed backup, subject to acknowledgement. Record reassignment in issue #9. | No feature cut fixes this risk: arrange an eligible submitter or contact the instructor before the deadline. |

The **candidate contingency cuts** are ranked and precise:

1. **C1 — Defer both requester reopening routes.** Remove S3.3's Resolved/Closed → Triaged actions and related demo cases; retain resolution and requester closure. Affects FR08/FR09 and S4 coverage. Save an estimated 1–2 hours; team must validate that estimate.
2. **C2 — Defer assignment/reassignment and the In Progress path.** Retain New → Triaged → Resolved → Closed with a required resolution note; show Unassigned consistently. Remove S3.2 and the In Progress route/tests, while preserving retained category/priority/status history. Affects FR05/FR07/FR08/FR09/FR12 and S4. Estimated additional 2–3 hours, unverified.
3. **C3 — Defer priority changes after triage.** Retain required initial priority and its history; reject later edits. Affects FR06 and S3.1/S4. Estimated additional 0.5–1 hour, unverified.

Never cut authorization, server-side validation, retained-operation audit/atomicity, persistence, independent setup, or truthful acceptance evidence to show more features. Deferred bugs/search/dashboard are already removed; they cannot be counted again as contingency savings. If C1–C3 are insufficient, renegotiate explicitly rather than claim a broken workflow is done.

**Before submission:** adopt any needed cut through the charter's scope vote and revise the exact criteria, trace table, plan, and estimates. **After submission:** preserve the submitted version/commit, raise a change request with impact and team votes, and obtain any course-required instructor acceptance before treating a smaller scope as the grading baseline. Unless that change is accepted, the original commitment remains and missed items are reported as unmet. A risk table is not permission to move the target unilaterally.

## 6. Agreement and submission readiness

| Member | Scope vote and reasoning | Accepted assignment/hours | Evidence/date/commit |
| --- | --- | --- | --- |
| Charles Barrett | Pending | Pending | Pending |
| Austin Gross | Pending | Pending | Pending |
| Caleb Turris | Pending | Pending | Pending |
| Doc Aberle | Pending | Pending; T3/T4 submission acknowledgement also needed | Pending |

- [ ] At least three affirmative scope-change votes are linked, with all four members' own workload confirmations.
- [ ] Course sprint dates and session-26 date are verified; estimates include actual required coordination and review.
- [ ] Team explicitly accepts or revises the ticket-only reduction and every retained-subset/deferred T2 disposition.
- [ ] Final non-author review covers the submitted revision; blocking comments resolved.
- [ ] Status updated to Accepted with real evidence/date; final PR merged and main-branch content verified.
- [ ] Doc completes the separate T3 and T4 portal submissions and records confirmation under the [handoff checklist](T3_T4_SUBMISSION_HANDOFF.md).

**Agreement date:** Pending. **Session 26 calendar date:** Pending course-schedule confirmation. **Implementation results:** Not yet demonstrated. **Course submission:** Pending.

## 7. AI-use disclosure

OpenAI Codex drafted this proposed scope, estimates, deferrals, traceability, risks, and handoff from the T4 screenshots and current T2/charter/playbook. Charles requested a separate PR and selected Doc as submitter. The ticket-only reduction, hours, owners/reviewers, and cut estimates are assistant proposals awaiting human agreement, not measured delivery capacity or completed work. See the [session record](ai-logs/2026-09-22-charles-t4-scope.md).
