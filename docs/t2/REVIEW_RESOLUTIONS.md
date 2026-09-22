# T2 review resolutions and verification procedures

Date: September 21, 2026 (America/Chicago).
Reviewed baseline: `d780614e8617a1f782f6da34c4334689c2990ae4`.

## Review evidence and disposition

| Evidence | Verified contribution | Disposition |
| --- | --- | --- |
| [Caleb Turris / WoodlandMoss review](https://github.com/treybarrett1/eece4081-teamproject/pull/6#pullrequestreview-5273284958) | Human review of permissions, technical projection, and ownership guards. Caleb explicitly states “None — review only” for writing credit and defers overall approval to the primary reviewer. | Record scoped approval; do not label it overall approval or section authorship. |
| [Review submitted through docasbarton-gif](https://github.com/treybarrett1/eece4081-teamproject/pull/6#pullrequestreview-5272957143) | Explicitly identifies OpenAI Codex as the reviewer and gives no human approval. Requests concrete procedures for NFR02, NFR05, NFR09, and NFR10. | Treat as advisory AI findings. The four procedures below address the findings in the specification, not as claims of executed product tests. |

No inline review threads were present when checked. These clarifications do not change the reviewed role matrix or ownership guards. Overall non-author human approval of the final revision remains separate from Caleb's scoped review.

## NFR02 — Ten named persistence workflows

Use the FR20 synthetic dataset. Bind the named Requester A/B, Support A/B, Developer A/B, and Administrator aliases to the actual seeded account IDs in the test record. Use fresh uniquely titled test records in each workflow to avoid dependence on an existing seeded record's state. Record every created ticket/bug ID.

| Workflow | Actions to execute | Acknowledged state included in the snapshot |
| --- | --- | --- |
| W01 Standard ticket closure | Requester A creates a ticket; Support A triages, assigns Support A, starts and resolves it; Requester A closes it | Closed ticket, public resolution, owner/priority and full transition history |
| W02 Direct resolution | Requester B creates a ticket; Support B triages it and resolves directly from Triaged; Requester B closes it | Closed ticket with no In Progress transition and a resolution note |
| W03 Reopen resolved work | Create, triage, and resolve a ticket for A; A reopens from Resolved with a reason | Triaged ticket, retained priority/owner and prior resolution, reopening reason/history |
| W04 Reopen closed work | Create and close a ticket for B; B reopens from Closed | Triaged ticket with original closure and reopening history preserved |
| W05 Reassign a ticket | Create/triage a ticket, assign Support A, start it, then reassign to Support B | In Progress ticket owned only by B; both assignments attributable |
| W06 Public/private conversation | Create a ticket, add public comments from its requester and Support, and a staff-only note from Support | Comment and note text, visibility classification, author and time |
| W07 Bug fix and closure | Create a complete bug, assign Developer A, start/fix with a note; Support verifies with evidence and closes | Closed bug with reproduction fields, fix/verification notes and lifecycle history |
| W08 Failed bug verification | Create/assign/start/fix a bug owned by Developer B; Support rejects the fix with an explanation | In Progress bug with preserved owner, fix note, and failed-verification explanation |
| W09 Many-to-many relationship change | Create tickets T1/T2 and bugs B1/B2; add T1–B1, T2–B1, T1–B2, then remove T1–B2 | Remaining links, intact records, and link addition/removal history |
| W10 Linked closure without ticket cascade | Create an active ticket linked to a bug; fix, verify, and close the bug while leaving the ticket unresolved | Closed bug and unchanged active ticket, with link and independent histories |

After **all ten** workflows receive success acknowledgements, export a canonical pre-restart snapshot of their ticket, bug, public-comment, staff-note, link, and event records. Sort by immutable IDs and exclude derived current age, session data, and other volatile display fields; retain all stored business values and timestamps. Stop and restart the application and database normally without reseeding. Export the same records and compare for exact equality. Retain the workflow-to-ID map, both snapshots, tested commit, commands, and zero-mismatch comparison.

The atomicity injection is a separate case, not a substitute for one of the ten: force failure after a proposed ticket status mutation but before its required event write. After restart, inspect both the ticket and event store. Both committed together or neither committed passes; a partial result fails. The implementation's chosen injection mechanism must be described in the test evidence before running it.

## NFR05 — Exact five-session workload

1. Use the NFR05 reference environment and FR20 seed; record CPU count, available RAM, OS, runtime/database versions, application commit, and seed identity. Stop unrelated test traffic.
2. Authenticate five independent Support sessions (S1–S5); the seeded Support accounts may be reused across sessions. Session tokens are not part of retained evidence.
3. Run three separate phases: ticket list, ticket detail for one existing seeded ticket, then dashboard. Use the same valid operation/input within each phase.
4. Before each phase, send one warm-up request from each session: **five warm-up requests per operation**, excluded from timing statistics.
5. Run 20 measured rounds per phase. At each round's start, release one request in each of S1–S5 concurrently, then wait for all five to finish before the next round. This produces **100 measured requests per operation** and **300 total**, with up to five requests in flight. Do not add other traffic.
6. Measure elapsed time at the client from dispatch until the full response is received, using a monotonic clock. Record phase, round, non-secret session alias, HTTP status, elapsed milliseconds, timeout/error, and whether the response contains the expected authorized content.
7. For each phase, at least 95 of its 100 requests must finish within 2,000 ms with a successful expected response. An incorrect/error response does not count as a timely success. Any HTTP 5xx fails the phase. A timeout counts as a failure; retain it in the denominator. Evaluate each phase independently, not only a pooled percentile.
8. Retain raw timings and the per-phase success/threshold/error counts. These are future product measurements; this document reports no measured performance.

## NFR09 — Adoption evidence boundary

Playbook v0.2 was merged in [PR #2](https://github.com/treybarrett1/eece4081-teamproject/pull/2), merge commit `86dcf02e494be9d58aab611fd59ecaaed1987347`. This is evidence of repository publication, **not proof of the team adoption vote**.

No dated adoption vote/record was found in the inspected playbook or PR #2 discussion. Adoption is therefore **unverified**, and NFR09 is **not assessed/passed**. Before the semester evidence audit, Charles must identify the actual adoption issue/minutes, each required member's recorded agreement, and the effective date/commit. Do not invent or backdate the record. Audit only the appropriate post-adoption PR interval and explicitly list any earlier records outside that interval. If no adoption evidence can be produced, report that limitation and leave NFR09 unsatisfied.

## NFR10 — Artifact inventory and inspection evidence

Before each release/demo, build a manifest of the exact evidence being distributed. Inspect actual content, not just filenames.

| Inventory field | Required value |
| --- | --- |
| Artifact | Repository-relative path or separately delivered filename |
| Identity | Commit and SHA-256 digest; for a generated archive, also list its contents |
| Category | Seed fixture, demo account configuration, screenshot, export/snapshot, measurement output, prompt log, audit record, or other delivery evidence |
| Provenance | Synthetic-data source or why the artifact has no user data |
| Inspector/date | Actual person and inspection date |
| Checks/outcome | Synthetic identities confirmed; no real tickets/private organization content/live credentials; pass/fail and finding location |

The inventory must cover all FR20 seed inputs, demonstration account/config files (without exposing secret values), setup/demo instructions, generated screenshots, persistence snapshots, workload logs, prompt records, and audit/acceptance reports. List excluded non-deliverable temporary artifacts explicitly. An empty or partial inventory does not pass.

A human inspector checks the text and visible image/export content for real employee names/contact details, actual internal ticket narratives, confidential company material, and live secrets. Automated pattern scans may assist but do not replace content review. Record what was checked, findings, and remediation; then re-inventory and re-inspect changed artifacts. Store only sanitized evidence in the public repository.

Pass requires all delivered artifacts accounted for and inspected with zero prohibited records or live credentials. There is no claim that the future product/dataset has passed this inspection. The current deliverable is a requirements document specifying this procedure.
