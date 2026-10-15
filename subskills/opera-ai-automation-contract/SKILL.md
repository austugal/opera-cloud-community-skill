---
name: opera-ai-automation-contract
description: >-
  Design safe, version-aware AI workflow automation around Oracle Hospitality OPERA Cloud and OHIP.
  Use when turning an operations request into a documented, testable automation contract with
  explicit evidence, access, human approvals, recovery, and rollout boundaries.
---

# OPERA/OHIP AI automation contract

Use this playbook with the root `SKILL.md` and `references/api-modules.md`,
`references/async-streaming-events.md`, `references/architecture-and-auth.md`, and
`references/error-handling.md`. It converts an operations request into a version-aware design.
It is a recommendation and review workflow, not a deployed integration, an Oracle feature, or an
autonomous hotel agent. Do not imply this playbook can connect to or operate a property.

## Contract workflow

1. **Define the request and boundary.** Record the property/business scope, deployed OPERA release,
   business owner, requested outcome, allowed records and fields, exclusions, and what must remain
   a human decision. Define the trigger only after identifying its documented source and timing.
2. **Classify capability and evidence.** Classify each proposed capability as Oracle-native,
   documented partner, customer-built/custom, or proposed. For each material claim, record the
   primary source, exact release, access/entitlement prerequisites, and whether it is documented,
   observed, inferred, or unknown. Do not turn a roadmap, marketing statement, or an AI answer into
   a product/API capability.
3. **Prove the interface and authority.** For every needed read or write, find the exact
   release-specific API contract, operation, schema, required role/permission, property scope,
   entitlement, and response behavior. Check OAuth/client scope and least privilege. If the exact
   read, write, permission, or field is not documented and authorized, mark it **unknown** and stop
   that part of the design; never guess an endpoint or infer write access from an assistant.
4. **Choose a documented trigger and delivery model.** Use an event/stream, polling subscription,
   timed read, asynchronous job, batch input, or manual request only when the relevant release and
   interface document that behavior. Record cursor/acknowledgement, latency, retention, replay, and
   failure semantics where applicable. If none is verified, mark the trigger **unknown**; do not
   quietly substitute polling or assume real-time events.
5. **Specify state and safe processing.** Draw allowed state transitions, preconditions, invariants,
   and terminal states from the product source. Define duplicate detection, idempotency, retry and
   timeout behavior from the specific contract. If a write's first outcome is ambiguous, read back
   and reconcile with OPERA before retrying. Never assume a universal idempotency key or retry limit.
6. **Set approval boundaries.** Separate recommendations, read-only actions, and writes. Name who
   approves each consequential action, including changes to reservations, guest data, inventory,
   money, or end-of-day state. Require explicit human confirmation for any action whose authority,
   impact, or safe reversal is not established; do not let model confidence bypass the gate.
7. **Define postconditions, audit, and stop/recovery.** Specify an authoritative read-back that
   proves the intended result and detects partial or duplicate effects. Log decision and outcome
   identifiers, source/version, approval, timestamps, and redacted errors without tokens or
   unnecessary guest data. Provide an operator-accessible kill switch that stops new triggers and
   writes, alerting/escalation, a reconciliation procedure, and a documented compensating action.
   Do not promise rollback unless the specific operation supports it; otherwise use human-approved
   recovery.
8. **Validate and graduate cautiously.** Test with synthetic or approved nonproduction data,
   including normal, boundary, duplicate, delayed/out-of-order, timeout/unknown-result, permission,
   partial-failure, and reconciliation cases. Shadow-run on read-only data first: compare proposed
   decisions with the authoritative OPERA state and let staff review without executing actions.
   Advance only through explicitly approved stages (shadow, read-only, narrowly scoped low-risk
   action, then any broader scope) with an owner, acceptance criteria, monitoring, and a way to
   halt. A successful test is not production authorization.

## Reusable blank contract

```text
Request and business outcome:
Property / OPERA product and deployed release:
Owner / approver / operational scope:
In scope / explicitly out of scope:
Capability classification (native / partner / custom / proposed) and evidence:
Documented read API, fields, role and entitlement:
Documented write API, fields, role and entitlement (or UNKNOWN):
Documented trigger and delivery semantics (or UNKNOWN):
Allowed state transitions / preconditions / invariants:
Deduplication, idempotency, retry and reconciliation:
Human approval gates:
Postconditions and authoritative read-back:
Audit fields / data minimization / retention:
Kill switch / escalation / rollback or compensating action:
Synthetic nonproduction test cases and acceptance criteria:
Shadow-run comparison / duration / reviewer:
Graduation stage, monitoring owner, and stop criteria:
Unresolved questions / sources and review date:
```

## Illustrative candidate: Leisure Management pre-EOD review

**Documented product facts (OPERA Cloud 26.4):** Oracle's feature summary says Leisure Experience
status updates are manual; it describes an On Hold status, a 30-minute automated availability hold
that expires if the experience is not scheduled and confirmed, and marking a guest No Show during
the End of the Day process. It also describes Scheduled, Checked In, Checked Out, and Cancelled
statuses. These are facts about the documented OPERA workflow, not proof of an external automation
interface. See Oracle's [OPERA Cloud Services 26.4 feature summary](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm),
section **Leisure Experience Status Lifecycle**. [Ask Oracle AI Agent](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/c_getting_started_ask_oracle.htm)
is documented as providing contextual product guidance; that guide does not establish a
transactional agent or leisure-status write capability.

**Conceptual proposal (not a product feature):** Before a property's End of Day, a staff member
could request a read-only review checklist of experiences needing human attention. Staff would
confirm the actual state in OPERA and perform any status change through the approved product
workflow. The review must never infer No Show solely from lack of an observed check-in, change an
experience status, or interfere with OPERA's own 30-minute hold expiry.

**Automation contract status: blocked pending evidence.** A matching OHIP leisure read/write API,
status fields and permissions, Leisure-specific Business Event, event/stream delivery, and any
supported polling or batch behavior are **unknown** from the sources reviewed here. Do not
implement an automated trigger, data read, status write, timer, or EOD action unless the current
release's primary documentation proves the exact capability and authorization. Start with the
manual OPERA workspace and approved procedures; if later verified, test any narrowly scoped
read-only candidate with synthetic/nonproduction data and shadow-run it before considering
human-approved use.

For interface discovery, consult this repository's [OHIP API module map](../../references/api-modules.md)
and [async, Business Events, and streaming notes](../../references/async-streaming-events.md), then
verify exact operations and delivery semantics in the applicable OHIP Developer Portal contract.
Those references are navigation aids, not evidence that a Leisure Management API or event exists.
