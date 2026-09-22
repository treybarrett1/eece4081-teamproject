# T2 — Requirements and Stakeholder Specification

**Enterprise IT Ticketing and Bug System**

EECE 4081-002 Software Engineering, Fall 2026

Charles Barrett · Austin Gross · Caleb Turris · Doc Aberle

Version 1.0 · September 21, 2026 · Prepared for team audit

**Status:** AI-assisted specification with review clarifications incorporated. Caleb Turris completed a scoped permissions/ownership review; overall final-revision approval, individual human section writing, stakeholder interviews, implementation, and product test results are not asserted. The authorship map in section 9 states what is known. This document is the T2 deliverable; its supporting files make the traceability and audit reproducible.

## Navigation

1. [Baseline and scope](#baseline)
2. [Definitions, permissions, and lifecycle rules](#rules)
3. [Stakeholder analysis](#stakeholders)
4. [Functional requirements](#functional)
5. [Non-functional requirements](#quality)
6. [Epics and user stories](#epics)
7. [Traceability in both directions](#traceability)
8. [Gaps, conflicts, and resolutions](#gaps)
9. [Authorship map](#authorship)
10. [AI-use disclosure](#disclosure)

<a id="baseline"></a>
## 1. Baseline and scope

This specification elaborates the [team charter at commit 5c8b49e2f55925c87e8ec18645b5986370e9bd4a](https://github.com/treybarrett1/eece4081-teamproject/blob/5c8b49e2f55925c87e8ec18645b5986370e9bd4a/docs/TEAM_CHARTER.md). The [merged story-map transcription in PR #4](https://github.com/treybarrett1/eece4081-teamproject/pull/4), submitted by GitHub account `WoodlandMoss`, was also reviewed. The same baseline contains the [team's story-map photo](https://github.com/treybarrett1/eece4081-teamproject/blob/5c8b49e2f55925c87e8ec18645b5986370e9bd4a/docs/story-map-photo.jpg) and Playbook v0.2. Source IDs below are reference labels for existing charter rows, not retroactive edits to that charter.

The product is a single-organization demonstration web application connecting employee IT requests with support work and related software defects. The semester commitment is the charter's positive scope: accounts/access, ticket intake/triage/lifecycle, bug records/lifecycle/links, communication/history, search, dashboard, and persistent, reproducible demonstration delivery.

All requirements below are **Must** for this proposed baseline. Requirements refine the charter without asserting they have already been implemented. Explicit numeric field limits, permission decisions, and the response-time target are proposed acceptance refinements requiring team review; they are not reported stakeholder quotations. The charter's scope-change rule still governs additions.

### Exclusions and boundaries

Corporate integrations/SSO/email ingestion, multiple tenants, billing, native mobile apps, external customer portals, contractual SLAs/on-call service, AI diagnosis/remediation, remote device control, asset/procurement/change-management suites, real enterprise-data migration, and production certification remain outside the positive scope.

The latest charter removed earlier explicit exclusions for attachments and customizable workflows, but added no positive requirement for either. This T2 therefore makes no commitment to either; a proposed addition needs an approved scope change. Likewise, story-map ideas without a charter basis are dispositioned in section 8, not silently included.

### Charter source register

| Source | Exact charter locator | Commitment represented | Type |
| --- | --- | --- | --- |
| <a id="c00"></a>C00 | §1 — Executive summary | Single-organization prototype; requester-to-support-to-developer workflow using synthetic records. | product |
| <a id="c01"></a>C01 | §2 / Accounts and access | Four demonstration roles and application-enforced authorization. | product |
| <a id="c02"></a>C02 | §2 / Ticket intake | Unique ID, title, description, category, impact, creation time, and own-ticket viewing. | product |
| <a id="c03"></a>C03 | §2 / Triage and ownership | Four priorities, one current owner, and staff status updates. | product |
| <a id="c04"></a>C04 | §2 / Ticket lifecycle | Defined ticket transitions, direct triaged resolution, and requester reopening with reason. | product |
| <a id="c05"></a>C05 | §2 / Bug records | Reproduction details, expected/actual behavior, severity, owner, and many-to-many ticket links. | product |
| <a id="c06"></a>C06 | §2 / Bug lifecycle | Open, In Progress, Fixed, Verified, Closed; failed verification returns to In Progress. | product |
| <a id="c07"></a>C07 | §2 / Communication and history | Public comments, private staff notes, and actor/time history of material changes. | product |
| <a id="c08"></a>C08 | §2 / Search and filtering | Authorized ID/title searches with status, priority/severity, and owner filters. | product |
| <a id="c09"></a>C09 | §2 / Dashboard | Open counts, unassigned tickets, and age from creation time. | product |
| <a id="c10"></a>C10 | §2 / Persistence and delivery | Restart persistence, documented setup, synthetic seed data, tests, and repeatable demo. | product |
| <a id="g01"></a>G01 | §5 / Complete support workflow | End-to-end ticket/linked-bug resolution, closure, and reopening. | outcome |
| <a id="g02"></a>G02 | §5 / Reliable bug workflow | Valid fields, one bug linked to two tickets, failed verification, and independent ticket closure. | outcome |
| <a id="g03"></a>G03 | §5 / Correct access boundaries | Own-ticket isolation, staff-note isolation, and role checks on screens and endpoints. | outcome |
| <a id="g04"></a>G04 | §5 / Consistent data and lifecycle | Reject invalid transitions, record actor/time, and preserve data after restart. | outcome |
| <a id="g05"></a>G05 | §5 / Accurate queue visibility | At least 100 tickets and 20 bugs; filters/counts equal independent expectations. | outcome |
| <a id="g06"></a>G06 | §5 / Usable requester experience | At least four of five evaluators submit and find status within five minutes without coaching. | outcome |
| <a id="g07"></a>G07 | §5 / Repeatable delivery | A teammate other than the setup author initializes a fresh checkout and runs the demo. | outcome |
| <a id="g08"></a>G08 | §5 / Delivery quality | Acceptance criteria pass; zero open access, data-loss, or core-workflow-blocking defects. | outcome |
| <a id="g09"></a>G09 | §5 / Team accountability | Post-adoption PR issue/review/evidence records and sprint review/retro notes. | process |

G09 is a team-process commitment, so its requirement and story are explicitly process evidence rather than an invented application feature.

<a id="rules"></a>
## 2. Definitions, permissions, and lifecycle rules

### Data and validation vocabulary

- A **ticket** is a request for IT support. A **bug** is a software defect with reproduction information. They have separate IDs, owners, and states.
- Each account has one active role in this prototype. A support manager uses the Support role; there is no fifth Manager role. An Administrator has account-management permissions, not implicit access to operational records.
- Ticket category: Hardware, Software, Network, Access, or Other. Reported impact: One user, Multiple users, or Organization-wide. Priority/severity: Low, Medium, High, Critical. Category captures problem type; impact records reported breadth; Support sets priority without an automatic VIP rule.
- Proposed text bounds, after trimming: title 1–120 characters; ticket/bug description 1–4,000; reproduction steps, expected result, and actual result each 1–4,000; public comment/staff note/resolution/fix/verification/reopening reason each 1–2,000. Empty or whitespace-only values fail. Counts use Unicode code points. Text is displayed as text, not executable markup.
- Usernames are unique case-insensitively and use 3–40 ASCII letters, digits, periods, underscores, or hyphens. Local demonstration credentials are supplied through setup/admin flows, never placed in audit events or returned in application responses.
- All record times are stored in UTC and displayed with a time-zone label. Creation times and IDs are immutable. History is ordered by timestamp, then event ID. No hard deletion of tickets, bugs, comments, or history is required by this baseline.
- **Open ticket for dashboard purposes** means New, Triaged, or In Progress. A ticket awaiting triage has priority **Not triaged**, not an invented fifth priority. Resolved and Closed remain searchable but are excluded from the open queue.
- All normative guard/permission rules in this section are included in FR01–FR21 and their linked stories; this section is not an untraced feature list.

### Role/action matrix

“Deny” applies to the role by itself. The same rules must hold in the UI and on direct requests.

| Action | Requester | Support | Developer | Administrator |
| --- | --- | --- | --- | --- |
| Authenticate/sign out | Own account | Own account | Own account | Own account |
| Create/manage accounts and roles | Deny | Deny | Deny | Allow |
| Create support ticket | Own ticket | Deny in this baseline | Deny in this baseline | Deny |
| Read ticket public details | Own only | All | Technical projection for tickets linked to own bugs | Deny |
| Edit triage/priority/owner; begin/resolve ticket | Deny | Allow under lifecycle guards | Deny | Deny |
| Confirm closure or reopen | Own only | Deny | Deny | Deny |
| Add/read public comments | Own, non-Closed to add | All, non-Closed to add | Read technical projection only; no public commenting | Deny |
| Add/read staff notes | Deny | All | Tickets linked to own bugs only | Deny |
| Create/read/search bugs | Deny | Allow | Allow | Deny |
| Claim/update bug technical fields | Deny | Reassign owner; not developer technical edits | Claim unassigned Open; edit owned Open/In Progress | Deny |
| Mark bug Fixed | Deny | Deny | Assigned Developer only | Deny |
| Verify/fail verification/close bug | Deny | Allow under lifecycle guards | Deny | Deny |
| Add/remove ticket–bug links | Deny | Allow | Deny | Deny |
| Ticket search/filter | Own only | All | Linked to own bugs only, technical projection | Deny |
| Dashboard | Deny | Allow | Deny | Deny |
| View change history | Own public ticket events only | Operational history | Bug history; linked-ticket technical events for own bugs | Account-change history only |

The Developer technical projection includes ticket ID, title, description, category, reported impact, status, priority, public troubleshooting comments, and authorized staff notes; it omits requester identity and unrelated ticket records. If a link/ownership change removes eligibility, subsequent access must be denied. FR03 and NFR01 enforce this boundary.

### Ticket lifecycle

| From → To | Actor | Required guard/effect |
| --- | --- | --- |
| New → Triaged | Support | Valid priority and category |
| Triaged → In Progress | Support | One active Support owner |
| Triaged → Resolved | Support | Public resolution note; permits a direct answer without starting work |
| In Progress → Resolved | Support | Public resolution note |
| Resolved → Closed | Owning requester | Explicit confirmation |
| Resolved → Triaged | Owning requester | Nonblank reopening reason; retain priority/owner/history |
| Closed → Triaged | Owning requester | Nonblank reopening reason; retain priority/owner/history |

All unlisted transitions are rejected. “Pending” from the story-map photo is represented by current status and explanatory notes; it does not add a state. FR07 guards account disabling/role changes that would orphan In Progress work.

### Bug lifecycle

| From → To | Actor | Required guard/effect |
| --- | --- | --- |
| Open → In Progress | Assigned Developer | Active Developer owner |
| In Progress → Fixed | Assigned Developer | Nonblank fix note |
| Fixed → Verified | Support | Nonblank successful-verification evidence |
| Fixed → In Progress | Support | Nonblank failed-verification explanation |
| Verified → Closed | Support | Preserve recorded verification |
| Verified → In Progress | Support | Nonblank failed-verification explanation |

All unlisted transitions are rejected. Closing a bug never changes a linked ticket's state. These are refinements of C06; reopening a Closed bug is not included because the charter does not promise that action.

<a id="stakeholders"></a>
## 3. Stakeholder analysis

**Interest** means the stakeholder's stake in the outcome. **Influence** means their ability to change requirements, acceptance, or use. Ratings are proposed analysis, not interview results. All needs below are inferred from the charter and story map; no named interview participant or approval is invented.

| ID / stakeholder | Interest and why | Influence and why | Concrete need | Requirement coverage | Engagement/validation plan |
| --- | --- | --- | --- | --- | --- |
| S01 Employee/requester | High: a blocked task and uncertain progress affect daily work | Medium: usability feedback drives changes; does not control scope | Submit once, locate owner/status, obtain an understandable resolution, protect own records | FR01, FR03–FR05, FR09–FR10; NFR01, NFR03 | Austin observes the five-user task in NFR03 and records actual feedback |
| S02 IT support agent | High: owns the queue and resolution workload | High: workflow expert whose acceptance determines operational usefulness | Actionable reports, priorities, single ownership, public/private communication, reusable bug links | FR06–FR12, FR15, FR17, FR19 | Austin reviews the lifecycle and core demo with an available support representative; otherwise retain assumptions |
| S03 Developer/maintainer | High: needs enough evidence to reproduce defects | High: technical feasibility constrains implementation; does not set course scope alone | Reproduction detail, expected/actual result, bounded access to ticket context, clear verification | FR11, FR13–FR16, FR18; NFR02 | Caleb reviews technical scenarios and permission boundaries; external developer input only if actually obtained |
| S04 IT support manager | High: accountable for neglected and unassigned work | High over prioritization; no separate system role is implied | Accurate open/unassigned counts and age rather than an unverified SLA claim | FR17, FR19; NFR04–NFR05 | Demonstrate the independent expected-count fixture and ask which queue decisions it supports |
| S05 System administrator | Medium: setup and account operations are periodic | High: controls access and environment | Predictable setup, current account permissions, preserved attribution when accounts change | FR01–FR03, FR20, FR22; NFR01, NFR06, NFR08 | Caleb and Doc review disable/reassignment cases and fresh-checkout evidence |
| S06 Student team | High: shared delivery and course grade | High: owns scope proposals, implementation, and evidence | Feasible baseline, traceable work, honest contribution records, reproducible validation | FR22; NFR06–NFR10 | Charles coordinates a review of this diff and records actual authorship/adoption |
| S07 Instructor/evaluator | High: must evaluate the course outcomes | High: sets rubric and judges the artifact | Complete bidirectional traceability, falsifiable requirements, explicit authorship and AI disclosure | NFR07, NFR09; sections 7–10 | Use the supplied rubric and address feedback; do not claim instructor approval |

If future stakeholder feedback conflicts with this baseline, record the feedback, affected IDs, and an approved change rather than silently rewriting a requirement or its source.

<a id="functional"></a>
## 4. Functional requirements

Requirements use immutable IDs for review and traceability. Verification references planned checks, not passing results.

<a id="fr01"></a>
### FR01 — Demonstration sign-in

The system shall authenticate an active seeded or administrator-created demonstration account, establish its current role, reject invalid/disabled credentials without revealing which field failed, and invalidate the session on sign-out.

**Priority:** Must. **Charter:** [C01](#c01), [G03](#g03). **Stories:** [US01](#us01).

**Verification:** Credential and sign-out scenarios in US01.

<a id="fr02"></a>
### FR02 — Manage demonstration accounts

An administrator shall create a local demonstration account, assign exactly one of Requester, Support, Developer, or Administrator, and enable/disable accounts. Duplicate usernames and unknown roles shall be rejected. A role or active-status change shall affect the next authorized request; it shall not delete historical attribution.

**Priority:** Must. **Charter:** [C01](#c01), [G03](#g03). **Stories:** [US02](#us02).

**Verification:** US02 account/role cases, including an already signed-in disabled user.

<a id="fr03"></a>
### FR03 — Enforce the role matrix

The system shall enforce the matrix in section 2 on every read and write, including detail IDs, searches, counts, and direct endpoint requests. Unauthorized access shall disclose neither protected fields nor the existence/count of another requester's tickets.

**Priority:** Must. **Charter:** [C01](#c01), [G03](#g03). **Stories:** [US03](#us03).

**Verification:** Positive and negative matrix cases; cross-requester and direct-ID probes.

<a id="fr04"></a>
### FR04 — Create a support ticket

A requester shall create a ticket with title, description, category, and reported impact. On success the system shall generate a unique immutable ticket ID, set the requester to the authenticated account, stamp UTC creation time, and set status New with no assignee or priority until triage.

**Priority:** Must. **Charter:** [C02](#c02), [C03](#c03). **Stories:** [US04](#us04).

**Verification:** US04 valid creation, duplicate-title distinction, forged-requester rejection.

<a id="fr05"></a>
### FR05 — View own ticket progress

A requester shall list and read their own tickets, showing ID, title, category, reported impact, status, assigned support display name or Unassigned, priority or Not triaged, creation time, public comments, and any resolution note. Staff notes and bug details shall be excluded.

**Priority:** Must. **Charter:** [C02](#c02), [C07](#c07), [G01](#g01), [G03](#g03). **Stories:** [US05](#us05).

**Verification:** US05 visibility and status after resolution/reopening.

<a id="fr06"></a>
### FR06 — Triage and prioritize

Support shall review a New ticket, confirm/correct its category while retaining reported impact, and assign exactly one priority: Low, Medium, High, or Critical. Moving to Triaged requires a selected priority. Later priority changes shall be permitted to Support and recorded in history.

**Priority:** Must. **Charter:** [C03](#c03), [C04](#c04). **Stories:** [US06](#us06).

**Verification:** US06 four priorities, invalid value, missing priority, history.

<a id="fr07"></a>
### FR07 — Assign one current ticket owner

Support shall assign or reassign a ticket to one active Support account. Reassignment shall replace the current owner and preserve prior assignment history. New and Triaged tickets may be unassigned; entering or remaining In Progress requires an active owner. Disabling an owner or removing their Support role shall be rejected until their In Progress tickets are reassigned.

**Priority:** Must. **Charter:** [C03](#c03), [G04](#g04). **Stories:** [US07](#us07).

**Verification:** US07 reassign, wrong-role assignee, and disable-owner guard.

<a id="fr08"></a>
### FR08 — Enforce ticket lifecycle

The system shall allow only the ticket transitions and actor/guard combinations in section 2. Support may begin work only from Triaged, and no role may skip directly from New to Closed or set an arbitrary status. Rejected transitions shall leave data and history unchanged.

**Priority:** Must. **Charter:** [C04](#c04), [G01](#g01), [G04](#g04). **Stories:** [US08](#us08).

**Verification:** Every allowed edge and a rejected edge for each state in US08.

<a id="fr09"></a>
### FR09 — Resolve, close, and reopen

Support shall supply a nonblank public resolution note for Triaged or In Progress → Resolved. The owning requester may confirm Resolved → Closed. The owning requester may reopen Resolved or Closed → Triaged with a nonblank reason; retain priority/owner and all earlier history. Reopening by a different requester shall fail.

**Priority:** Must. **Charter:** [C04](#c04), [G01](#g01). **Stories:** [US09](#us09).

**Verification:** US09 note/reason validation, direct resolution, closure, two reopening routes.

<a id="fr10"></a>
### FR10 — Public ticket conversation

The owning requester and Support shall append nonblank public comments to a ticket in New, Triaged, In Progress, or Resolved. Comments shall record author/time and become visible to that requester and Support. Closed tickets require reopening before further comments. Existing comments cannot be edited or deleted in this baseline.

**Priority:** Must. **Charter:** [C07](#c07), [G01](#g01). **Stories:** [US10](#us10).

**Verification:** Public comment round-trip, invalid text, closed-ticket rejection.

<a id="fr11"></a>
### FR11 — Staff-only technical notes

Support shall append staff-only notes; Developers may append notes only to tickets linked to a bug they own. Support can read all staff notes; a Developer can read notes only on tickets linked to a bug they own. Requester views, endpoint responses, and search results shall never expose them.

**Priority:** Must. **Charter:** [C07](#c07), [C01](#c01), [G03](#g03). **Stories:** [US10](#us10), [US03](#us03).

**Verification:** Public/private paired records and unlinked-developer access checks.

<a id="fr12"></a>
### FR12 — Change history

The system shall append an immutable actor/time event with old and new values for ticket owner, priority, category, status, bug owner/status/severity, and ticket–bug link additions/removals. Account changes shall record actor/time and changed role/active status, never credentials. Requesters see only public ticket status/priority/owner history; technical events follow the role matrix.

**Priority:** Must. **Charter:** [C07](#c07), [G04](#g04), [G03](#g03). **Stories:** [US07](#us07), [US09](#us09), [US13](#us13), [US17](#us17).

**Verification:** History content/order/access checks, including failed writes leaving no event.

<a id="fr13"></a>
### FR13 — Record reproducible bugs

Support or Developer shall create a bug with immutable unique ID, title, description, reproduction steps, expected result, actual result, and severity Low/Medium/High/Critical. New bugs start Open; required missing fields or unknown severity shall be rejected.

**Priority:** Must. **Charter:** [C05](#c05), [G02](#g02). **Stories:** [US11](#us11).

**Verification:** US11 required-field matrix and unique ID.

<a id="fr14"></a>
### FR14 — Bug ownership and technical updates

Support may assign/reassign any non-Closed bug to one active Developer without changing its state. A Developer may claim an unassigned Open bug, then edit its technical fields while Open or In Progress. A different Developer cannot edit it. In Progress requires an active owner; disabling that owner or removing their Developer role requires reassignment first.

**Priority:** Must. **Charter:** [C05](#c05), [G02](#g02). **Stories:** [US12](#us12).

**Verification:** Claim, reassign, unauthorized edit, and disable-owner checks.

<a id="fr15"></a>
### FR15 — Link tickets and bugs without coupling closure

Support shall add/remove many-to-many links between existing tickets and bugs, reject duplicate/nonexistent links, and record link history. A single bug may have two tickets and one ticket two bugs. Closing a bug shall never change a linked ticket's status; Support must resolve each ticket separately.

**Priority:** Must. **Charter:** [C05](#c05), [G02](#g02), [G01](#g01). **Stories:** [US13](#us13).

**Verification:** Two-by-two link fixture, removal, duplicates, and independent closure.

<a id="fr16"></a>
### FR16 — Fix and verify bugs

The assigned Developer shall move Open → In Progress and In Progress → Fixed with a nonblank fix note. Support shall move Fixed → Verified with verification evidence, or Fixed → In Progress with a failed-verification explanation. Support shall close Verified bugs or return Verified → In Progress with a failed-verification explanation. Every transition into In Progress requires an active Developer owner; Support must reassign an inactive owner before recording failed verification. Other transitions are rejected.

**Priority:** Must. **Charter:** [C06](#c06), [G02](#g02), [G04](#g04). **Stories:** [US14](#us14).

**Verification:** All allowed edges, rejected Open → Closed, and failed verification.

<a id="fr17"></a>
### FR17 — Search and filter tickets

Authorized users shall search ticket ID exactly or title by case-insensitive substring and combine applicable status, priority, and owner filters with AND. Requesters are constrained to their own tickets; Developers to the technical projection of tickets linked to their owned bugs. Unassigned and Not triaged are explicit filter values; results are ordered by creation time descending, then ID.

**Priority:** Must. **Charter:** [C08](#c08), [G05](#g05), [G03](#g03). **Stories:** [US15](#us15).

**Verification:** US15 independent fixture queries and cross-user leak tests.

<a id="fr18"></a>
### FR18 — Search and filter bugs

Support and Developer shall search bug ID exactly or title by case-insensitive substring, AND-filter by status, severity, and Developer owner including Unassigned, and receive deterministic creation-time/ID ordering. Requesters and accounts with only Administrator role cannot access bug searches.

**Priority:** Must. **Charter:** [C08](#c08), [G05](#g05), [G03](#g03). **Stories:** [US15](#us15).

**Verification:** US15 bug queries, no-results case, and forbidden roles.

<a id="fr19"></a>
### FR19 — Queue dashboard

Support shall see counts of open tickets by status and priority, a total open count, an unassigned-open count, and age per open ticket. Open means New, Triaged, or In Progress; Resolved/Closed are excluded. Untriaged New tickets are counted under Not triaged. Age is floor((current UTC time − creation UTC time)/86400) nonnegative whole days.

**Priority:** Must. **Charter:** [C09](#c09), [G05](#g05). **Stories:** [US16](#us16).

**Verification:** US16 independent counts and frozen-clock age boundaries.

<a id="fr20"></a>
### FR20 — Synthetic seed dataset

The delivery shall provide a repeatable seed procedure with at least 100 synthetic tickets, 20 bugs, two Requesters, two Support users, two Developers, and one Administrator. Include every lifecycle state, priorities/severities, unassigned cases, public/private comments, and many-to-many links. Loading a fresh dataset shall produce documented expected dashboard counts.

**Priority:** Must. **Charter:** [C10](#c10), [G05](#g05), [G07](#g07). **Stories:** [US18](#us18).

**Verification:** Fresh database seed twice with the same seed; compare expected IDs/counts.

<a id="fr21"></a>
### FR21 — Validate input without partial changes

All create/update endpoints shall enforce the field rules in section 2 regardless of UI validation. Missing/invalid inputs shall return a field-specific error and perform no partial record, link, or history update. User-authored ticket, comment, note, and bug text shall render as text rather than executable markup.

**Priority:** Must. **Charter:** [C02](#c02), [C05](#c05), [G02](#g02), [G04](#g04), [G08](#g08). **Stories:** [US04](#us04), [US11](#us11), [US17](#us17).

**Verification:** Boundary values, malformed status/IDs, script-like text, and atomic-write failure cases.

<a id="fr22"></a>
### FR22 — Repeatable demonstration package

The repository shall provide setup instructions, prerequisites, seed command, test command(s), and an end-to-end script covering report → triage → assignment → linked bug → fix/verification → individual ticket resolution → requester closure/reopening. The script shall identify accounts, expected states, and evidence to capture.

**Priority:** Must. **Charter:** [C00](#c00), [C10](#c10), [G01](#g01), [G07](#g07). **Stories:** [US18](#us18), [US19](#us19).

**Verification:** A non-author follows the committed instructions on a fresh checkout.

<a id="quality"></a>
## 5. Non-functional and process requirements

Detailed procedures for NFR02, NFR05, NFR09, and NFR10 are part of this specification in [Review resolutions and verification procedures](t2/REVIEW_RESOLUTIONS.md).

Each statement identifies a threshold or a named failure condition. These are acceptance targets. No measurements or successful tests are claimed. NFR09 is explicitly a team-process requirement so the charter's accountability promise is not omitted.

<a id="nfr01"></a>
### NFR01 — Authorization completeness

For each permitted and denied role/action pair in section 2, the acceptance suite shall include at least one success or rejection test as appropriate. All cases must pass; two requesters must be used for ownership tests. A disabled account or revoked role must lose access on its next request.

**Priority:** Must. **Charter:** [C01](#c01), [G03](#g03), [G08](#g08). **Stories:** [US03](#us03).

**Pass/fail method:** Run the complete matrix suite; one unauthorized disclosure or mutation fails the requirement.

<a id="nfr02"></a>
### NFR02 — Persistence and atomicity

After ten scripted workflows and a normal application/database restart without reseeding, all acknowledged tickets, bugs, comments, links, and history shall match the pre-restart snapshot. Inject a failure between data and history writes in one test: either both persist or neither persists. No partial result is permitted.

**Priority:** Must. **Charter:** [C10](#c10), [G04](#g04). **Stories:** [US17](#us17).

**Pass/fail method:** Execute W01–W10 and the separate atomicity-injection case in the review-resolution procedures; compare canonical pre/post-restart snapshots with zero mismatches.

<a id="nfr03"></a>
### NFR03 — Requester usability

At least four of five volunteer evaluators unfamiliar with the implementation shall submit a valid ticket and find its status within five minutes total using only the provided instructions and no live coaching. Each successful result must refer to the evaluator's newly created ticket.

**Priority:** Must. **Charter:** [G06](#g06), [C02](#c02). **Stories:** [US05](#us05).

**Pass/fail method:** Record anonymous task results and elapsed times from first instruction to correct status.

<a id="nfr04"></a>
### NFR04 — Queue accuracy

On the FR20 dataset, every dashboard count and the result set of the US15 filter queries shall equal independently calculated expected values. At frozen ages 0, 23h59m, 24h, and 48h, display 0, 0, 1, and 2 days respectively. Required mismatch count is zero.

**Priority:** Must. **Charter:** [G05](#g05), [C08](#c08), [C09](#c09). **Stories:** [US15](#us15), [US16](#us16).

**Pass/fail method:** Expected results computed directly from seed records, not copied from UI output.

<a id="nfr05"></a>
### NFR05 — Interactive response time

On the documented reference environment (4 logical CPU cores, 8 GB RAM, local app/database), with the FR20 dataset and five simultaneous authenticated sessions, at least 95 of 100 measured requests for each of ticket list, ticket detail, and dashboard shall finish within 2 seconds, measured at the client after five warm-up requests per operation; no HTTP 5xx is permitted.

**Priority:** Must. **Charter:** [G06](#g06), [C09](#c09). **Stories:** [US16](#us16).

**Pass/fail method:** Execute the review-resolution protocol: five independent Support sessions, three operation phases, five warm-ups per phase, then 20 synchronized rounds of five requests. Retain raw measurements; this is a proposed target, not an achieved benchmark.

<a id="nfr06"></a>
### NFR06 — Fresh-checkout reproducibility

One teammate other than the setup-guide author shall install, seed, and execute the demonstration from a fresh checkout using only documented prerequisites and steps, with no undocumented correction or live coaching. Record the tested commit and environment. Any missing step that blocks completion fails.

**Priority:** Must. **Charter:** [C10](#c10), [G07](#g07). **Stories:** [US18](#us18).

**Pass/fail method:** Observed independent setup run; no installation-time promise is invented.

<a id="nfr07"></a>
### NFR07 — Release acceptance

Before the final demonstration, 100% of the committed story acceptance criteria shall pass and zero open defects may allow unauthorized access, lose acknowledged records, or block the FR22 core workflow. Other known defects shall list impact and workaround.

**Priority:** Must. **Charter:** [G08](#g08), [C10](#c10). **Stories:** [US19](#us19).

**Pass/fail method:** Commit-specific acceptance report and open-defect review; unmet criteria cannot be marked done.

<a id="nfr08"></a>
### NFR08 — Auditable change records

Every successful mutation covered by FR12 shall produce exactly one attributable event per changed field/link, with an ISO 8601 UTC timestamp, actor ID, record ID, and applicable old/new values; order ties by event ID. History-edit/delete attempts through the application shall fail. Audit payloads must contain zero passwords, tokens, or session identifiers.

**Priority:** Must. **Charter:** [C07](#c07), [G04](#g04), [G03](#g03). **Stories:** [US17](#us17).

**Pass/fail method:** Enumerate expected events for scripted changes, test immutability, and inspect payloads.

<a id="nfr09"></a>
### NFR09 — Team delivery evidence

Every post-adoption merged PR shall link an issue, identify a non-author human approval covering the final substantive revision, and record validation; each completed sprint shall have review and retrospective notes. AI-assisted work shall link its prompt record under the adopted playbook. The final evidence audit shall find zero missing records.

**Priority:** Must. **Charter:** [G09](#g09). **Stories:** [US20](#us20).

**Pass/fail method:** Use an actual dated team-adoption record to set the post-adoption audit interval; inspect PRs and sprint notes. PR #2's merge proves publication only. Adoption is currently unverified and this process requirement is not assessed/passed.

<a id="nfr10"></a>
### NFR10 — Prototype data boundary

The committed seed/demo assets and acceptance evidence shall contain zero real employee ticket records, live credentials, or confidential organization data. Use synthetic display names and clearly labeled demonstration accounts; prompt and audit logs must also respect this boundary.

**Priority:** Must. **Charter:** [C00](#c00), [C10](#c10), [G08](#g08). **Stories:** [US18](#us18), [US20](#us20).

**Pass/fail method:** Create the complete artifact manifest and content-inspection record defined in the review-resolution procedures; every delivered seed/demo/evidence artifact must be accounted for and show zero real private records or live credentials.

<a id="epics"></a>
## 6. Epics and user stories

The delivery order follows the requester journey: establish access → report/triage → own/resolve → investigate linked defects → inspect evidence → demonstrate delivery. Six epics make the hierarchy explicit. Acceptance criteria below are planned tests; none are marked passed.

| Epic | Outcome | Stories |
| --- | --- | --- |
| [E01 — Establish accountable access](#e01) | Only authorized people can access the records needed for their job. | [US01](#us01), [US02](#us02), [US03](#us03) |
| [E02 — Report and understand the problem](#e02) | Employees submit actionable reports and understand their progress. | [US04](#us04), [US05](#us05), [US06](#us06) |
| [E03 — Own and resolve the support request](#e03) | Support has accountable ownership, conversation, and explicit completion. | [US07](#us07), [US08](#us08), [US09](#us09), [US10](#us10) |
| [E04 — Investigate linked software defects](#e04) | Developers reproduce defects; support verifies fixes for affected tickets. | [US11](#us11), [US12](#us12), [US13](#us13), [US14](#us14) |
| [E05 — Inspect the queue and evidence](#e05) | Staff find work and trust the dashboard and history. | [US15](#us15), [US16](#us16), [US17](#us17) |
| [E06 — Demonstrate and govern the prototype](#e06) | A teammate can reproduce delivery and the team can show acceptance evidence. | [US18](#us18), [US19](#us19), [US20](#us20) |

<a id="e01"></a>
### E01 — Establish accountable access

**Outcome:** Only authorized people can access the records needed for their job.

**Epic acceptance:** All acceptance criteria of [US01](#us01), [US02](#us02), [US03](#us03) pass at the same release baseline, with linked evidence and no unresolved blocking defect. E06 includes process evidence as well as the product demonstration.

<a id="us01"></a>
#### US01 — Sign in and end a session

As a demonstration user, I want to sign in and out so that access is tied to my identity.

**Requirements:** [FR01](#fr01).

1. **US01-AC1:** Given an active account and correct credentials, signing in shows that account's permitted workspace; an incorrect password and a disabled account both fail with the same non-specific sign-in error.
2. **US01-AC2:** Given a signed-in user, after sign-out the old session cannot read ticket data; the next protected request is rejected.
3. **US01-AC3:** Given a role change or disable action during a session, the next request uses the new permissions or rejects the disabled account.

<a id="us02"></a>
#### US02 — Manage accounts

As an administrator, I want to manage demonstration accounts so that only assigned participants can act in each role.

**Requirements:** [FR02](#fr02).

1. **US02-AC1:** Given an unused valid username and valid credentials/role, creating the account succeeds; duplicate username and an unknown role fail without creating a partial account.
2. **US02-AC2:** Given an existing account, changing its role or enabled state affects its next protected request and creates an attributable account-change event without credentials.
3. **US02-AC3:** Given a Support or Developer who owns In Progress work, disabling or changing them out of that role is blocked until the affected work is reassigned; historical actor IDs remain resolvable.

<a id="us03"></a>
#### US03 — Protect records across roles

As a requester, I want my requests and staff's private work separated so that other users cannot inspect my problem history.

**Requirements:** [FR03](#fr03), [FR11](#fr11), [NFR01](#nfr01).

1. **US03-AC1:** Given Requesters A and B, A cannot read or mutate B's ticket through URL guessing, a forged requester ID, direct endpoints, search, or counts; the response contains no protected record data.
2. **US03-AC2:** Given public and staff-only text on A's ticket, A receives public text only. Developers see technical projection/notes only for tickets linked to bugs they own.
3. **US03-AC3:** Given each role/action pair in the role matrix, allowed and denied requests match that matrix; the stored credential and session secret never appear in application response payloads.
4. **US03-AC4:** Given every NFR01 matrix case, all pass before access-boundary acceptance is recorded.

<a id="e02"></a>
### E02 — Report and understand the problem

**Outcome:** Employees submit actionable reports and understand their progress.

**Epic acceptance:** All acceptance criteria of [US04](#us04), [US05](#us05), [US06](#us06) pass at the same release baseline, with linked evidence and no unresolved blocking defect. E06 includes process evidence as well as the product demonstration.

<a id="us04"></a>
#### US04 — Submit a ticket

As an employee requester, I want to describe a problem once so that support receives an actionable request.

**Requirements:** [FR04](#fr04), [FR21](#fr21).

1. **US04-AC1:** Given valid title, description, category, and impact, submission returns one immutable ID, UTC creation time, status New, requester identity from the session, and Unassigned/Not triaged values.
2. **US04-AC2:** Given two valid submissions with the same title, each has a different ID; a submitted requester identity different from the session is rejected.
3. **US04-AC3:** Given a missing required field, an over-limit title, or an unknown category, a field-specific error appears and no ticket/history fragment is persisted.
4. **US04-AC4:** Given markup-like description text, it is displayed as text and does not execute.

<a id="us05"></a>
#### US05 — Find my status

As a requester, I want to see my ticket's owner and progress so that I know what happens next.

**Requirements:** [FR05](#fr05), [NFR03](#nfr03).

1. **US05-AC1:** Given a newly created ticket, its requester can find it in their list and read every public field required by FR05, including explicit Unassigned and Not triaged values.
2. **US05-AC2:** Given a support status change or resolution note, reloading the ticket shows the new public state and note without exposing internal notes or bug details.
3. **US05-AC3:** Given five unfamiliar volunteer evaluators and the provided instructions, at least four create a valid ticket and locate that ticket's status within five minutes without live coaching; capture anonymous timing/results.

<a id="us06"></a>
#### US06 — Triage by impact

As a support agent, I want to classify and prioritize new tickets so that important work is visible.

**Requirements:** [FR06](#fr06).

1. **US06-AC1:** Given a New ticket, Support can confirm/correct category and set each supported priority value; reported impact remains intact.
2. **US06-AC2:** Given no selected priority, New → Triaged is rejected; selecting a valid priority permits it.
3. **US06-AC3:** Given a later priority/category change, the old/new values, actor, and timestamp appear in the authorized history; Requesters cannot perform the update.

<a id="e03"></a>
### E03 — Own and resolve the support request

**Outcome:** Support has accountable ownership, conversation, and explicit completion.

**Epic acceptance:** All acceptance criteria of [US07](#us07), [US08](#us08), [US09](#us09), [US10](#us10) pass at the same release baseline, with linked evidence and no unresolved blocking defect. E06 includes process evidence as well as the product demonstration.

<a id="us07"></a>
#### US07 — Assign accountable ownership

As a support agent, I want one current ticket owner so that the next action has a responsible person.

**Requirements:** [FR07](#fr07), [FR12](#fr12).

1. **US07-AC1:** Given a New or Triaged ticket, Support assigns active Support A, then reassigns to Support B; only B is current and both changes remain in history.
2. **US07-AC2:** Given an inactive or non-Support target, assignment fails; Triaged → In Progress fails until an active Support owner is selected.
3. **US07-AC3:** Given an In Progress ticket, clearing its owner or disabling/removing that owner's Support role is rejected until the ticket is reassigned.

<a id="us08"></a>
#### US08 — Move work through valid states

As a support agent, I want predictable ticket states so that progress cannot skip required work.

**Requirements:** [FR08](#fr08).

1. **US08-AC1:** Given valid priority and an active owner, New → Triaged → In Progress succeeds with authorized events.
2. **US08-AC2:** Given each allowed ticket transition in section 2, the specified actor and guard succeed; test at least one disallowed target from every state.
3. **US08-AC3:** Given New → Closed or an arbitrary state string, the update fails and both ticket state and change-history count remain unchanged.

<a id="us09"></a>
#### US09 — Resolve, confirm, and reopen

As a requester, I want to confirm a solution or reopen my ticket so that closure reflects whether my problem was addressed.

**Requirements:** [FR09](#fr09), [FR12](#fr12).

1. **US09-AC1:** Given a Triaged or In Progress ticket, Support can resolve it only with a nonblank public resolution note; both routes are tested.
2. **US09-AC2:** Given my Resolved ticket, I can confirm Closed; another requester and a Developer cannot close it.
3. **US09-AC3:** Given my Resolved or Closed ticket, a nonblank reopening reason returns it to Triaged while retaining priority/owner and previous resolution/history; a blank reason fails.
4. **US09-AC4:** Given a linked bug closes, my ticket's state does not change until Support performs its own resolution action.

<a id="us10"></a>
#### US10 — Separate public conversation from internal notes

As a support agent, I want public replies and staff-only notes so that useful internal investigation does not leak to requesters.

**Requirements:** [FR10](#fr10), [FR11](#fr11).

1. **US10-AC1:** Given a non-Closed ticket, Support and the owning requester append public comments with author/time; whitespace-only and over-limit text fail.
2. **US10-AC2:** Given a staff-only note, Support and the owner of a linked bug can read it, while the requester and an unlinked Developer cannot; only Support and the owning linked Developer may add staff notes.
3. **US10-AC3:** Given a Closed ticket, new public comments are rejected until reopening. Staff notes may still record technical follow-up without changing ticket status.
4. **US10-AC4:** Given existing public comments or notes, edit/delete attempts are rejected in this baseline.

<a id="e04"></a>
### E04 — Investigate linked software defects

**Outcome:** Developers reproduce defects; support verifies fixes for affected tickets.

**Epic acceptance:** All acceptance criteria of [US11](#us11), [US12](#us12), [US13](#us13), [US14](#us14) pass at the same release baseline, with linked evidence and no unresolved blocking defect. E06 includes process evidence as well as the product demonstration.

<a id="us11"></a>
#### US11 — Describe a reproducible defect

As a developer, I want reproduction steps and expected versus actual results so that I can investigate a software problem.

**Requirements:** [FR13](#fr13), [FR21](#fr21).

1. **US11-AC1:** Given all required bug fields and a valid severity, Support or Developer creates an Open bug with unique immutable ID and UTC time.
2. **US11-AC2:** Given each missing required field, an unknown severity, or over-limit field, creation fails with a specific error and no partial bug.
3. **US11-AC3:** Given two bugs with the same title, IDs differ; markup-like field content displays inertly.

<a id="us12"></a>
#### US12 — Own a bug investigation

As a developer, I want to claim or receive a bug so that investigation has one accountable owner.

**Requirements:** [FR14](#fr14).

1. **US12-AC1:** Given an unassigned Open bug, a Developer can claim it; claiming a bug already owned by another Developer fails.
2. **US12-AC2:** Given an Open, In Progress, Fixed, or Verified bug, Support can reassign it to an active Developer without changing status, and the prior assignment remains in history.
3. **US12-AC3:** Given the current owner, technical edits are allowed only in Open/In Progress; another Developer, an inactive user, or a requester is denied.
4. **US12-AC4:** Given an In Progress bug, its owner cannot be disabled or lose the Developer role until reassignment; it cannot be left ownerless.

<a id="us13"></a>
#### US13 — Connect related work

As a support agent, I want ticket–bug links so that one investigation can serve multiple reported problems.

**Requirements:** [FR12](#fr12), [FR15](#fr15).

1. **US13-AC1:** Given tickets T1 and T2 and bugs B1 and B2, create links T1–B1, T2–B1, and T1–B2; authorized views expose the same relationships in either direction.
2. **US13-AC2:** Given an existing link, a duplicate attempt fails without a duplicate row; a nonexistent record ID fails; removing a link leaves both original records intact and records the removal.
3. **US13-AC3:** Given B1 closes, T1 and T2 retain their previous statuses and Support resolves each separately after checking its public resolution.
4. **US13-AC4:** Given T1's requester, bug IDs/details and link history are not exposed through requester responses.

<a id="us14"></a>
#### US14 — Verify a fix

As a support agent, I want to verify a developer's fix so that a bug is not closed merely because code changed.

**Requirements:** [FR16](#fr16).

1. **US14-AC1:** Given the assigned active Developer, Open → In Progress succeeds and In Progress → Fixed requires a nonblank fix note.
2. **US14-AC2:** Given a Fixed bug, Support can record successful verification evidence and move it to Verified, then Closed.
3. **US14-AC3:** Given failed verification of a Fixed or Verified bug, Support records a nonblank explanation and returns it to In Progress; retain an active owner, or require reassignment first if the owner is inactive or no longer a Developer.
4. **US14-AC4:** Given Open → Closed, an unassigned start, a missing note, or a Developer attempting the Support verification action, the request fails without a state/history change.

<a id="e05"></a>
### E05 — Inspect the queue and evidence

**Outcome:** Staff find work and trust the dashboard and history.

**Epic acceptance:** All acceptance criteria of [US15](#us15), [US16](#us16), [US17](#us17) pass at the same release baseline, with linked evidence and no unresolved blocking defect. E06 includes process evidence as well as the product demonstration.

<a id="us15"></a>
#### US15 — Find authorized work

As a support agent or developer, I want precise filters so that I can locate relevant work without scanning every record.

**Requirements:** [FR17](#fr17), [FR18](#fr18), [NFR04](#nfr04).

1. **US15-AC1:** Given the documented seed, compare independently expected sets for exact-ID search, mixed-case title substring, each status, each priority/severity, and each owner including Unassigned.
2. **US15-AC2:** Given combined status plus priority/severity plus owner filters, the result is their intersection in creation-time-descending/ID order; a query with no matches returns an empty list.
3. **US15-AC3:** Given a requester, ticket results contain only their own records and bug search is denied; a Developer's ticket searches return only the technical projection for tickets linked to their own bugs; an Administrator-only account cannot search operational records.
4. **US15-AC4:** Given NFR04's expected query results, every actual result set equals the independently calculated set.

<a id="us16"></a>
#### US16 — Inspect queue size and age

As a support manager using a Support account, I want accurate queue counts and age so that I can identify neglected work.

**Requirements:** [FR19](#fr19), [NFR04](#nfr04), [NFR05](#nfr05).

1. **US16-AC1:** Given the seed dataset, open counts include only New/Triaged/In Progress; counts grouped by status/priority sum to the total, and Not triaged remains visible for untriaged tickets.
2. **US16-AC2:** Given both assigned and unassigned open/closed records, unassigned-open count excludes Resolved and Closed records.
3. **US16-AC3:** Given a frozen clock, ticket ages at 0, 23h59m, 24h, and 48h are 0, 0, 1, and 2 whole days; do not use last-update time.
4. **US16-AC4:** Given the NFR05 workload/environment, each measured operation meets its 95-of-100 response threshold and zero-server-error condition; retain raw measurements.

<a id="us17"></a>
#### US17 — Trust persisted records and history

As a maintainer, I want durable, attributable changes so that progress can be reconstructed after a restart.

**Requirements:** [FR12](#fr12), [FR21](#fr21), [NFR02](#nfr02), [NFR08](#nfr08).

1. **US17-AC1:** Given ten completed scripted workflows, snapshot tickets, bugs, comments, links, and history, restart without reseeding, and compare: zero acknowledged records or values are missing or changed.
2. **US17-AC2:** Given a forced failure between a record mutation and its event write, either both persist or neither persists; no partial update is allowed.
3. **US17-AC3:** Given every FR12 mutation, NFR08's actor/time/old-new fields and event count are correct and no credential/session secret appears.
4. **US17-AC4:** Given attempted history editing/deletion or an invalid transition, the history remains unchanged.

<a id="e06"></a>
### E06 — Demonstrate and govern the prototype

**Outcome:** A teammate can reproduce delivery and the team can show acceptance evidence.

**Epic acceptance:** All acceptance criteria of [US18](#us18), [US19](#us19), [US20](#us20) pass at the same release baseline, with linked evidence and no unresolved blocking defect. E06 includes process evidence as well as the product demonstration.

<a id="us18"></a>
#### US18 — Reproduce the prototype

As a teammate who did not write the setup guide, I want a fresh-checkout path and synthetic dataset so that I can independently run the demonstration.

**Requirements:** [FR20](#fr20), [FR22](#fr22), [NFR06](#nfr06), [NFR10](#nfr10).

1. **US18-AC1:** Given only documented prerequisites and instructions, the teammate installs, seeds, and runs the demo without undocumented correction or live coaching, recording commit/environment.
2. **US18-AC2:** Given a fresh database, the seed creates at least 100 tickets, 20 bugs, all four roles and required edge cases; repeat on another fresh database with the same seed and compare expected values.
3. **US18-AC3:** Given the demo assets and acceptance evidence, inspection finds no actual employee ticket content, live credentials, or confidential organization data.
4. **US18-AC4:** Given the repository, the setup, seed/test commands, demo accounts, and expected steps are all documented; missing instructions fail acceptance.

<a id="us19"></a>
#### US19 — Prove the core workflow

As the course evaluator, I want reproducible acceptance evidence so that the delivered behavior can be checked against the specification.

**Requirements:** [FR22](#fr22), [NFR07](#nfr07).

1. **US19-AC1:** Given the FR22 script, demonstrate ticket reporting through a linked bug fix, verification, independent ticket resolution, requester closure, and reopening; record actual outcomes at a named commit.
2. **US19-AC2:** Given the final story checklist, every committed criterion has a pass result; any failure keeps delivery acceptance open.
3. **US19-AC3:** Given the defect list, no unresolved unauthorized-access, acknowledged-data-loss, or core-workflow-blocking issue remains; other issues state impact/workaround.

<a id="us20"></a>
#### US20 — Audit team evidence

As a team member, I want traceable reviews and AI disclosures so that contribution and acceptance claims can be verified.

**Requirements:** [NFR09](#nfr09), [NFR10](#nfr10).

1. **US20-AC1:** Given the actual adoption record, inspect every later merged PR: each links an issue, has a non-author human approval covering its final substantive revision, and records validation.
2. **US20-AC2:** Given each completed sprint, review and retrospective notes exist; AI-assisted PRs link prompt records under the adopted playbook.
3. **US20-AC3:** Given no recorded adoption or no human authorship evidence, mark those facts unverified rather than inventing dates, approvals, or contribution claims.
4. **US20-AC4:** Given the release evidence and logs, synthetic-data/privacy inspection finds no prohibited real records or live credentials.

<a id="traceability"></a>
## 7. Traceability in both directions

The following tables are generated from the same [machine-readable register](t2/requirements-register.json). The [CSV export](t2/traceability.csv) contains one row per requirement–charter-source–story combination; links do not imply that a test has passed. Sources are frozen to the baseline above.

### 7.1 Every requirement → charter → story

| Requirement | Charter sources | Story/epic | Check |
| --- | --- | --- | --- |
| [FR01](#fr01) | [C01](#c01), [G03](#g03) | [US01](#us01) / E01 | Credential and sign-out scenarios in US01. |
| [FR02](#fr02) | [C01](#c01), [G03](#g03) | [US02](#us02) / E01 | US02 account/role cases, including an already signed-in disabled user. |
| [FR03](#fr03) | [C01](#c01), [G03](#g03) | [US03](#us03) / E01 | Positive and negative matrix cases; cross-requester and direct-ID probes. |
| [FR04](#fr04) | [C02](#c02), [C03](#c03) | [US04](#us04) / E02 | US04 valid creation, duplicate-title distinction, forged-requester rejection. |
| [FR05](#fr05) | [C02](#c02), [C07](#c07), [G01](#g01), [G03](#g03) | [US05](#us05) / E02 | US05 visibility and status after resolution/reopening. |
| [FR06](#fr06) | [C03](#c03), [C04](#c04) | [US06](#us06) / E02 | US06 four priorities, invalid value, missing priority, history. |
| [FR07](#fr07) | [C03](#c03), [G04](#g04) | [US07](#us07) / E03 | US07 reassign, wrong-role assignee, and disable-owner guard. |
| [FR08](#fr08) | [C04](#c04), [G01](#g01), [G04](#g04) | [US08](#us08) / E03 | Every allowed edge and a rejected edge for each state in US08. |
| [FR09](#fr09) | [C04](#c04), [G01](#g01) | [US09](#us09) / E03 | US09 note/reason validation, direct resolution, closure, two reopening routes. |
| [FR10](#fr10) | [C07](#c07), [G01](#g01) | [US10](#us10) / E03 | Public comment round-trip, invalid text, closed-ticket rejection. |
| [FR11](#fr11) | [C07](#c07), [C01](#c01), [G03](#g03) | [US10](#us10) / E03, [US03](#us03) / E01 | Public/private paired records and unlinked-developer access checks. |
| [FR12](#fr12) | [C07](#c07), [G04](#g04), [G03](#g03) | [US07](#us07) / E03, [US09](#us09) / E03, [US13](#us13) / E04, [US17](#us17) / E05 | History content/order/access checks, including failed writes leaving no event. |
| [FR13](#fr13) | [C05](#c05), [G02](#g02) | [US11](#us11) / E04 | US11 required-field matrix and unique ID. |
| [FR14](#fr14) | [C05](#c05), [G02](#g02) | [US12](#us12) / E04 | Claim, reassign, unauthorized edit, and disable-owner checks. |
| [FR15](#fr15) | [C05](#c05), [G02](#g02), [G01](#g01) | [US13](#us13) / E04 | Two-by-two link fixture, removal, duplicates, and independent closure. |
| [FR16](#fr16) | [C06](#c06), [G02](#g02), [G04](#g04) | [US14](#us14) / E04 | All allowed edges, rejected Open → Closed, and failed verification. |
| [FR17](#fr17) | [C08](#c08), [G05](#g05), [G03](#g03) | [US15](#us15) / E05 | US15 independent fixture queries and cross-user leak tests. |
| [FR18](#fr18) | [C08](#c08), [G05](#g05), [G03](#g03) | [US15](#us15) / E05 | US15 bug queries, no-results case, and forbidden roles. |
| [FR19](#fr19) | [C09](#c09), [G05](#g05) | [US16](#us16) / E05 | US16 independent counts and frozen-clock age boundaries. |
| [FR20](#fr20) | [C10](#c10), [G05](#g05), [G07](#g07) | [US18](#us18) / E06 | Fresh database seed twice with the same seed; compare expected IDs/counts. |
| [FR21](#fr21) | [C02](#c02), [C05](#c05), [G02](#g02), [G04](#g04), [G08](#g08) | [US04](#us04) / E02, [US11](#us11) / E04, [US17](#us17) / E05 | Boundary values, malformed status/IDs, script-like text, and atomic-write failure cases. |
| [FR22](#fr22) | [C00](#c00), [C10](#c10), [G01](#g01), [G07](#g07) | [US18](#us18) / E06, [US19](#us19) / E06 | A non-author follows the committed instructions on a fresh checkout. |
| [NFR01](#nfr01) | [C01](#c01), [G03](#g03), [G08](#g08) | [US03](#us03) / E01 | Run the complete matrix suite; one unauthorized disclosure or mutation fails the requirement. |
| [NFR02](#nfr02) | [C10](#c10), [G04](#g04) | [US17](#us17) / E05 | Execute W01–W10 and the separate atomicity-injection case in the review-resolution procedures; compare canonical pre/post-restart snapshots with zero mismatches. |
| [NFR03](#nfr03) | [G06](#g06), [C02](#c02) | [US05](#us05) / E02 | Record anonymous task results and elapsed times from first instruction to correct status. |
| [NFR04](#nfr04) | [G05](#g05), [C08](#c08), [C09](#c09) | [US15](#us15) / E05, [US16](#us16) / E05 | Expected results computed directly from seed records, not copied from UI output. |
| [NFR05](#nfr05) | [G06](#g06), [C09](#c09) | [US16](#us16) / E05 | Execute the review-resolution protocol: five independent Support sessions, three operation phases, five warm-ups per phase, then 20 synchronized rounds of five requests. Retain raw measurements; this is a proposed target, not an achieved benchmark. |
| [NFR06](#nfr06) | [C10](#c10), [G07](#g07) | [US18](#us18) / E06 | Observed independent setup run; no installation-time promise is invented. |
| [NFR07](#nfr07) | [G08](#g08), [C10](#c10) | [US19](#us19) / E06 | Commit-specific acceptance report and open-defect review; unmet criteria cannot be marked done. |
| [NFR08](#nfr08) | [C07](#c07), [G04](#g04), [G03](#g03) | [US17](#us17) / E05 | Enumerate expected events for scripted changes, test immutability, and inspect payloads. |
| [NFR09](#nfr09) | [G09](#g09) | [US20](#us20) / E06 | Use an actual dated team-adoption record to set the post-adoption audit interval; inspect PRs and sprint notes. PR #2's merge proves publication only. Adoption is currently unverified and this process requirement is not assessed/passed. |
| [NFR10](#nfr10) | [C00](#c00), [C10](#c10), [G08](#g08) | [US18](#us18) / E06, [US20](#us20) / E06 | Create the complete artifact manifest and content-inspection record defined in the review-resolution procedures; every delivered seed/demo/evidence artifact must be accounted for and show zero real private records or live credentials. |

### 7.2 Every charter commitment → requirements → stories

| Charter source | Requirements that serve it | Story coverage |
| --- | --- | --- |
| [C00](#c00) | [FR22](#fr22), [NFR10](#nfr10) | [US18](#us18), [US19](#us19), [US20](#us20) |
| [C01](#c01) | [FR01](#fr01), [FR02](#fr02), [FR03](#fr03), [FR11](#fr11), [NFR01](#nfr01) | [US01](#us01), [US02](#us02), [US03](#us03), [US10](#us10) |
| [C02](#c02) | [FR04](#fr04), [FR05](#fr05), [FR21](#fr21), [NFR03](#nfr03) | [US04](#us04), [US05](#us05), [US11](#us11), [US17](#us17) |
| [C03](#c03) | [FR04](#fr04), [FR06](#fr06), [FR07](#fr07) | [US04](#us04), [US06](#us06), [US07](#us07) |
| [C04](#c04) | [FR06](#fr06), [FR08](#fr08), [FR09](#fr09) | [US06](#us06), [US08](#us08), [US09](#us09) |
| [C05](#c05) | [FR13](#fr13), [FR14](#fr14), [FR15](#fr15), [FR21](#fr21) | [US11](#us11), [US12](#us12), [US13](#us13), [US04](#us04), [US17](#us17) |
| [C06](#c06) | [FR16](#fr16) | [US14](#us14) |
| [C07](#c07) | [FR05](#fr05), [FR10](#fr10), [FR11](#fr11), [FR12](#fr12), [NFR08](#nfr08) | [US05](#us05), [US10](#us10), [US03](#us03), [US07](#us07), [US09](#us09), [US13](#us13), [US17](#us17) |
| [C08](#c08) | [FR17](#fr17), [FR18](#fr18), [NFR04](#nfr04) | [US15](#us15), [US16](#us16) |
| [C09](#c09) | [FR19](#fr19), [NFR04](#nfr04), [NFR05](#nfr05) | [US16](#us16), [US15](#us15) |
| [C10](#c10) | [FR20](#fr20), [FR22](#fr22), [NFR02](#nfr02), [NFR06](#nfr06), [NFR07](#nfr07), [NFR10](#nfr10) | [US18](#us18), [US19](#us19), [US17](#us17), [US20](#us20) |
| [G01](#g01) | [FR05](#fr05), [FR08](#fr08), [FR09](#fr09), [FR10](#fr10), [FR15](#fr15), [FR22](#fr22) | [US05](#us05), [US08](#us08), [US09](#us09), [US10](#us10), [US13](#us13), [US18](#us18), [US19](#us19) |
| [G02](#g02) | [FR13](#fr13), [FR14](#fr14), [FR15](#fr15), [FR16](#fr16), [FR21](#fr21) | [US11](#us11), [US12](#us12), [US13](#us13), [US14](#us14), [US04](#us04), [US17](#us17) |
| [G03](#g03) | [FR01](#fr01), [FR02](#fr02), [FR03](#fr03), [FR05](#fr05), [FR11](#fr11), [FR12](#fr12), [FR17](#fr17), [FR18](#fr18), [NFR01](#nfr01), [NFR08](#nfr08) | [US01](#us01), [US02](#us02), [US03](#us03), [US05](#us05), [US10](#us10), [US07](#us07), [US09](#us09), [US13](#us13), [US17](#us17), [US15](#us15) |
| [G04](#g04) | [FR07](#fr07), [FR08](#fr08), [FR12](#fr12), [FR16](#fr16), [FR21](#fr21), [NFR02](#nfr02), [NFR08](#nfr08) | [US07](#us07), [US08](#us08), [US09](#us09), [US13](#us13), [US17](#us17), [US14](#us14), [US04](#us04), [US11](#us11) |
| [G05](#g05) | [FR17](#fr17), [FR18](#fr18), [FR19](#fr19), [FR20](#fr20), [NFR04](#nfr04) | [US15](#us15), [US16](#us16), [US18](#us18) |
| [G06](#g06) | [NFR03](#nfr03), [NFR05](#nfr05) | [US05](#us05), [US16](#us16) |
| [G07](#g07) | [FR20](#fr20), [FR22](#fr22), [NFR06](#nfr06) | [US18](#us18), [US19](#us19) |
| [G08](#g08) | [FR21](#fr21), [NFR01](#nfr01), [NFR07](#nfr07), [NFR10](#nfr10) | [US04](#us04), [US11](#us11), [US17](#us17), [US03](#us03), [US19](#us19), [US18](#us18), [US20](#us20) |
| [G09](#g09) | [NFR09](#nfr09) | [US20](#us20) |

### 7.3 Every story → requirements → charter

| Story | Epic | Requirements | Charter sources |
| --- | --- | --- | --- |
| [US01](#us01) | E01 | [FR01](#fr01) | [C01](#c01), [G03](#g03) |
| [US02](#us02) | E01 | [FR02](#fr02) | [C01](#c01), [G03](#g03) |
| [US03](#us03) | E01 | [FR03](#fr03), [FR11](#fr11), [NFR01](#nfr01) | [C01](#c01), [G03](#g03), [C07](#c07), [G08](#g08) |
| [US04](#us04) | E02 | [FR04](#fr04), [FR21](#fr21) | [C02](#c02), [C03](#c03), [C05](#c05), [G02](#g02), [G04](#g04), [G08](#g08) |
| [US05](#us05) | E02 | [FR05](#fr05), [NFR03](#nfr03) | [C02](#c02), [C07](#c07), [G01](#g01), [G03](#g03), [G06](#g06) |
| [US06](#us06) | E02 | [FR06](#fr06) | [C03](#c03), [C04](#c04) |
| [US07](#us07) | E03 | [FR07](#fr07), [FR12](#fr12) | [C03](#c03), [G04](#g04), [C07](#c07), [G03](#g03) |
| [US08](#us08) | E03 | [FR08](#fr08) | [C04](#c04), [G01](#g01), [G04](#g04) |
| [US09](#us09) | E03 | [FR09](#fr09), [FR12](#fr12) | [C04](#c04), [G01](#g01), [C07](#c07), [G04](#g04), [G03](#g03) |
| [US10](#us10) | E03 | [FR10](#fr10), [FR11](#fr11) | [C07](#c07), [G01](#g01), [C01](#c01), [G03](#g03) |
| [US11](#us11) | E04 | [FR13](#fr13), [FR21](#fr21) | [C05](#c05), [G02](#g02), [C02](#c02), [G04](#g04), [G08](#g08) |
| [US12](#us12) | E04 | [FR14](#fr14) | [C05](#c05), [G02](#g02) |
| [US13](#us13) | E04 | [FR12](#fr12), [FR15](#fr15) | [C07](#c07), [G04](#g04), [G03](#g03), [C05](#c05), [G02](#g02), [G01](#g01) |
| [US14](#us14) | E04 | [FR16](#fr16) | [C06](#c06), [G02](#g02), [G04](#g04) |
| [US15](#us15) | E05 | [FR17](#fr17), [FR18](#fr18), [NFR04](#nfr04) | [C08](#c08), [G05](#g05), [G03](#g03), [C09](#c09) |
| [US16](#us16) | E05 | [FR19](#fr19), [NFR04](#nfr04), [NFR05](#nfr05) | [C09](#c09), [G05](#g05), [C08](#c08), [G06](#g06) |
| [US17](#us17) | E05 | [FR12](#fr12), [FR21](#fr21), [NFR02](#nfr02), [NFR08](#nfr08) | [C07](#c07), [G04](#g04), [G03](#g03), [C02](#c02), [C05](#c05), [G02](#g02), [G08](#g08), [C10](#c10) |
| [US18](#us18) | E06 | [FR20](#fr20), [FR22](#fr22), [NFR06](#nfr06), [NFR10](#nfr10) | [C10](#c10), [G05](#g05), [G07](#g07), [C00](#c00), [G01](#g01), [G08](#g08) |
| [US19](#us19) | E06 | [FR22](#fr22), [NFR07](#nfr07) | [C00](#c00), [C10](#c10), [G01](#g01), [G07](#g07), [G08](#g08) |
| [US20](#us20) | E06 | [NFR09](#nfr09), [NFR10](#nfr10) | [G09](#g09), [C00](#c00), [C10](#c10), [G08](#g08) |

**Coverage rule:** Every FR/NFR has at least one valid charter source and one defined story; every positive capability/success criterion has a requirement; every story belongs to exactly one epic and has requirements and acceptance criteria. Exclusions are not silently turned into features. A structural check cannot prove that a semantic link is justified; human reviewers must inspect the source-to-requirement rationale and section 8.

<a id="gaps"></a>
## 8. Gaps, conflicts, and resolutions from tracing

These are explicit dispositions in this proposed specification. “Resolved in draft” means the draft has an actionable baseline decision; it does not claim the team voted for it.

| ID / discovery | Resolution in this draft | Requirement/story effect | Approval impact |
| --- | --- | --- | --- |
| D01 Story map says VIP/regular and tiered workers; charter defines four roles and priority by support | Do not add VIP routing, employee tiers, or escalation tiers. Treat them as backlog ideas requiring a scope-change proposal | FR06–FR07 / US06–US07 implement charter priority and ownership | New tiers require charter change |
| D02 Story map says service time and pending status; charter promises age but no contractual SLA or Pending state | Use creation-based age and current lifecycle; explanatory notes communicate waiting. No SLA timer or new status | FR08, FR19 / US08, US16 | Baseline clarification; team reviews |
| D03 Story map says leadership review and approve/deny work; no management approval gate exists in charter | Use Support verification of a bug fix and requester confirmation of resolution. Do not add a management gate or fifth role | FR09, FR16 / US09, US14 | Any separate leadership gate needs scope change |
| D04 Story map says archive, feedback, category/summary/survey | Closed records remain searchable, resolution is public, and category identifies type. No separate archive subsystem, email feedback, or survey | FR05, FR09, FR17 / US05, US09, US15 | Surveys/email require positive scope decision |
| D05 Charter removed attachment/customization exclusions without adding positive capabilities | Neither is committed here. Removal from an exclusion list is not evidence of a feature promise | No unsupported FR created | Team may propose additions under scope control |
| D06 “Staff” and manager visibility were underspecified | Four-role matrix gives manager Support permissions; Developers get bounded technical projection; Administrator only manages accounts | FR03, FR11, NFR01 / US03, US10 | Proposed permission refinement |
| D07 Open-count and untriaged priority semantics were ambiguous | Define open as New/Triaged/In Progress and give untriaged tickets an explicit Not triaged bucket | FR19, NFR04 / US16 | Proposed counting definition |
| D08 Ticket/bug closure could incorrectly cascade | Bug closure never closes tickets; each affected requester has a separate support resolution and confirmation | FR15 / US13 and US09 | Directly preserves charter G02 |
| D09 Account disabling could leave active work ownerless | Require reassignment before disabling/removing an owner's necessary role; retain historical actors | FR02, FR07, FR14 / US02, US07, US12 | Proposed guard, no new business capability |
| D10 A functional-only trace would omit usability, setup, quality, and accountability goals | Add explicit NFR03, NFR06–NFR09 and delivery/process stories, not fictional application features | G06–G09 → US05, US18–US20 | Covers all nine outcomes |
| D11 Numeric limits and response time were absent | Label field bounds and NFR05's 2-second workload as proposed measurable refinements. Preserve the charter's existing 4-of-5 usability target exactly | FR21, NFR03, NFR05 / US04, US05, US11, US16 | Team must accept or revise targets before baseline approval |
| D12 No individual section-writing or interview evidence was supplied | Attribute the draft to Codex; record Charles's supplied context and separately propose human review ownership. Do not claim teammates wrote text or stakeholders were interviewed | Sections 3, 9, 10 and prompt record | Factual human contribution entries must be completed from evidence |

<a id="authorship"></a>
## 9. Authorship map

This is a factual contribution map, not a division of credit based on role titles. Git commit identity alone does not prove who wrote a section. No new human prose for T2 or completed interview transcript has been supplied in this conversation.

| Person/tool | Actual contribution verified for this draft | Sections authored in this draft | Proposed human review responsibility |
| --- | --- | --- | --- |
| Charles Barrett | Supplied the assignment screenshots, project topic and roster in the conversation, and clarified the AI-tool preference | Source/context contribution; no claim of personally writing the generated T2 prose | Confirm scope, decisions, authorship, and final submission |
| Austin Gross | No individual T2 writing contribution supplied or verified | None claimed | Stakeholder analysis; epics/stories; non-author review |
| Caleb Turris (`WoodlandMoss`) | Submitted the story-map artifact/transcription in PR #4; signed a scoped review of permissions, technical projection, and ownership guards on September 21 at commit d780614e8617a1f782f6da34c4334689c2990ae4 | No T2 section-writing claimed; reviewer explicitly states review only | Overall approval was deferred to the primary reviewer |
| Doc Aberle | No individual T2 writing contribution supplied or verified | None claimed | Non-functional thresholds, acceptance methods, traceability checks |
| OpenAI Codex | Generated this draft from the supplied screenshots and current repository artifacts | Sections 1–10, register, CSV, verification tooling, and audit materials | Cannot perform or certify the team's human audit |

The repository story-map photo and transcription were contributed through merged [PR #4](https://github.com/treybarrett1/eece4081-teamproject/pull/4) by GitHub account `WoodlandMoss` (commit `b80c81caae26565bae59b4e3b107275055280c66`). The signed [Caleb Turris review](https://github.com/treybarrett1/eece4081-teamproject/pull/6#pullrequestreview-5273284958) identifies that account as Caleb. Individual workshop-note authorship remains unverified. The playbook supplies review responsibilities, not a T2 section-authorship record. Charles explicitly confirmed that no authorship map exists yet. To finalize the graded human-authorship map, each person must identify actual sections they wrote or substantively revised and link the corresponding edit/PR evidence. Review-only contributions should be labeled review, not writing. Until that evidence is added, this remains an honest AI-assisted draft rather than a claim of four-person authorship.

<a id="disclosure"></a>
## 10. AI-use disclosure appendix

**Review follow-through:** The [review-resolution record](t2/REVIEW_RESOLUTIONS.md) records Caleb's scoped human review and the separate explicitly AI-assisted review submitted through `docasbarton-gif`. Its four requests for more concrete verification procedures are addressed as specification clarifications. No overall human approval or executed product tests are implied.

**Tool:** OpenAI Codex, used for course-document assistance under the repository's v0.2 tool policy. No Claude Code or ChatGPT drafting is claimed for this artifact merely because those are the team's preferred tools for other work.

**Inputs:** The two September 21 T2 assignment screenshots; the charter, playbook, README, AI log, and story-map photo at baseline 5c8b49e2f55925c87e8ec18645b5986370e9bd4a; and prior project/roster context from the user.

**Assistance:** Drafted the analysis, requirement statements, permission/lifecycle refinements, epics and acceptance criteria, traceability tables/register/CSV, conflict dispositions, authorship disclosure, and audit support. The helper validator checks document structure, not product behavior.

**Verification limits:** Assistant checks can establish ID coverage, link consistency, source preservation, and successful repository publication. They cannot establish stakeholder agreement, actual usability/response-time results, product correctness, personal authorship, team adoption, or course submission. Those remain human tasks.

**Prompt and disposition record:** [September 21 session log](ai-logs/2026-09-21-charles-t2-requirements.md). [Human audit checklist](t2/AUDIT.md). Team members must record their own revisions and approvals without attributing AI output to themselves as unassisted writing.
