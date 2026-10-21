# Enterprise IT Ticketing and Bug System

Team project for **EECE 4081-002 Software Engineering, Fall 2026**.

A proposed web application for employees to report IT problems, support staff to triage and assign tickets, and developers to investigate linked software bugs. The semester scope includes role-based access, ticket and bug lifecycles, comments, change history, search, and queue reporting using synthetic data.

## Team

| Member | Proposed primary responsibility |
| --- | --- |
| Charles Barrett | Coordination, scope, and repository maintenance |
| Austin Gross | Requirements and user experience |
| Caleb Turris | Application, data, and technical decisions |
| Doc Aberle | Quality, integration, and facilitator backup |

Names and project topic are confirmed by the repository owner. Roles and meeting commitments are proposed for team adoption.

## Assignment documents

- [T2 — Requirements and Stakeholder Specification](docs/T2_REQUIREMENTS.md): 32 requirements, six epics, 20 stories, bidirectional traceability, and transparent authorship.
- [T2 audit checklist](docs/t2/AUDIT.md), [traceability CSV](docs/t2/traceability.csv), and [validation evidence](docs/t2/VALIDATION.md).

- [T1 — Team Charter and Executive Summary](docs/TEAM_CHARTER.md): executive summary, scope inclusions and exclusions, stakeholders and interests, named responsibilities, conflict procedures, measurable success criteria, and AI disclosure.
- [Engineering Playbook v0.3 — Quality Gates](docs/PLAYBOOK.md): retains v0.1/v0.2 rules and adds concrete Python/Django quality gates, their local and GitHub Actions commands, failure consequences, and the Session 15 coverage-floor deferral.
- [v0.3 rubric and CI audit](docs/PLAYBOOK_V0.3_AUDIT.md): exact rubric coverage, observed CI evidence, and outstanding human/submission steps.
- [v0.2 human-audit checklist](docs/PLAYBOOK_V0.2_AUDIT.md).
- [v0.2 prompt record](docs/ai-logs/2026-09-16-charles-playbook-v0.2.md).
- [AI-use log](AI_LOG.md).
- [Rubric and submission checklist](docs/SUBMISSION_CHECKLIST.md).

- [T4 — Scope Agreement](docs/T4_SCOPE_AGREEMENT.md): proposed two-sprint ticket workflow, T2 dispositions, capacity assumptions, and ordered cuts; team agreement pending.
- [T3/T4 submission handoff](docs/T3_T4_SUBMISSION_HANDOFF.md): Doc Aberle is Charles's selected submitter; acknowledgement and completion pending.

## Current state

This repository is currently a documentation package. A Python/Django quality-check workflow is implemented on the v0.3 review branch, with successful lint, formatting, and documentation CI checks. No Django application, Django test run, numeric coverage floor, verified required-status-check configuration, team adoption, or course-portal submission is claimed.

Before submission, each member reviews their responsibilities and availability, and Charles records adoption. Use the document links above or the course portal's permitted upload format.

## Proposed contribution workflow

Work is tracked in issues and short-lived branches. After team adoption, changes require a PR with a non-author approval and validation evidence. See the playbook for the named review rotation, deadlines, and merge checklist. The PR template supports those rules; CI validation runs on pushes and pull requests, but required-status-check merge protection is not verified.
