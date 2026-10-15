# OPERA PMS Support and Troubleshooting

Use this guide to structure investigation, not to replace the OPERA release manual, Oracle Support
instructions, the property's runbook, or the interface vendor's procedure. OPERA Cloud and OPERA 5
have different architectures and diagnostics. Avoid fixed ports, log paths, latency limits, repair
steps, response times, and recovery objectives unless verified for the actual environment.

## 1. Establish the facts

Collect the minimum information needed to reproduce and route the problem:

- Product and exact release/patch; hosted or on-premises model where applicable.
- Environment and property, affected module/workflow, user role, client/device, and interface.
- Start time and time zone, exact sanitized error/code, frequency, reproducibility, and scope.
- Recent configuration, release, credential, network, device, or integration changes.
- Expected versus actual result and a safe reproduction sequence.

Do not request passwords, tokens, full payment-card information, or unnecessary guest data.

## 2. Isolate the scope

Determine whether the issue follows one user, device, property, environment, function, date range,
transaction, network, or external integration. Compare with a known-good case only when that is
authorized and does not duplicate a financial or guest-facing action. For an API, preserve method,
documented operation, sanitized request/response, status, and correlation ID. For interfaces,
compare sender and receiver timestamps, message identifiers, and processing status.

## 3. Investigate with evidence

- **Access:** verify account status, role/privileges, property assignment, integration entitlement,
  and current authentication requirements.
- **Configuration:** compare the relevant documented setting/control with an approved known-good
  configuration; confirm release and license dependencies.
- **Data/workflow:** inspect the affected reservation, posting, room, rate, report, or event using
  approved product tools and minimum necessary access.
- **API/integration:** check contract, environment/property context, credentials without exposing
  them, mapping, delivery/acknowledgement, service status, and both sides' sanitized logs.
- **Network/device:** follow Oracle's current compatibility and network guidance; test only
  documented endpoints and approved paths.
- **Time/date:** distinguish system time, business date, property time zone, and API/report date
  semantics; do not infer which one controls an operation.

Use official release notes, product documentation, support advisories, and customer runbooks.
Symptoms alone do not establish root cause.

## 4. Apply a controlled correction

Before a change, document the hypothesis, evidence, expected result, risk, approval, and rollback.
Prefer reversible, least-impact changes and use an approved non-production environment when
representative. Avoid:

- Blindly restarting services, clients, interfaces, or devices.
- Direct database queries/edits or undocumented repair tools.
- Repeating a state-changing or financial request before determining whether it already succeeded.
- Disabling controls, security checks, certificates, or firewall rules to bypass an error.
- Restoring backups or changing fiscal/accounting data without the accountable owner's process.

Validate the original reproduction and check for side effects; monitor according to the customer's
runbook.

## 5. Escalation and evidence

Escalate through the hotel's support owner, authorized integration/vendor team, or Oracle Support
using the applicable support contract. Provide:

- Product/release, environment, property, module, time zone, and business impact.
- Reproduction steps, sanitized request/response or message IDs, and correlation identifiers.
- Relevant logs/diagnostics collected using the supported tool and handling policy.
- Recent changes, checks performed, and whether the issue is ongoing or intermittent.

Redact tokens, secrets, personal data, and payment information. Use Oracle's supported diagnostic
bundle and service-request process; do not guess file locations or attach raw logs without review.

## Common symptom routing

| Symptom | Start with |
|---|---|
| Login or authorization failure | Identity, role, property entitlement, token/client setup, and exact sanitized error |
| Reservation not found or unexpected status | Property, date/business-date semantics, search filters, status, and audit trail |
| Folio or balance discrepancy | Transaction detail, posting date, transaction codes, taxes, routing, and authorized reconciliation |
| Rate/availability differs by channel | Effective property values, dates, restrictions, code mapping, message delivery, and channel-side interpretation |
| Event not received | Subscription/event configuration, filters, connection/consumer health, delivery status, and reconciliation |
| Export rejected | OPERA release/configuration, exact receiver schema, sanitized validation error, and reconciled sample |
| Night audit/end-of-day blocked | Current stage, documented prerequisites, property business date, job status, and dependency errors |
| Printing/device issue | Supported OS/client/device, assignment, user permission, queue/service status, and controlled test |

## Official references

- [Oracle Hospitality documentation home](https://docs.oracle.com/en/industries/hospitality/)
- [OPERA Cloud Services documentation](https://docs.oracle.com/en/industries/hospitality/hotels.html)
- [OHIP documentation index](https://docs.oracle.com/en/industries/hospitality/integration-platform/)
