# Quick Reference Cheatsheet

Generic concepts only; this is not a request-ready API contract. No live endpoints, property
codes, or credentials are included. Oracle's Help Center listed OPERA Cloud Services 26.4 as the newest release on 2026-10-15, but a
property runs the release Oracle scheduled for it, often an older one. Confirm the exact tenant
release, entitlements, API contract, and configuration.

## Authentication (concept)

1. Register the integration using the applicable OHIP process and protect its credentials.
2. Request a token using the grant and endpoint documented for that integration.
3. Send the token and the API's required application/property context using the documented
   authorization header.

Never use real credentials in examples or logs.

## Common operation patterns

- **Reservations:** search, retrieve, create, modify, or cancel only through operations documented
  for the integration; check current reservation state before acting.
- **Cashiering:** inspect folio windows, postings, and operation permissions before any financial
  action; reconcile the response with the folio.
- **Rooms / housekeeping:** distinguish room condition from inventory availability; verify the
  effect of any status change before applying it.
- **Rates / inventory:** inspect effective values, restrictions, room/rate mappings, and delivery
  status for the relevant dates and channel.
- **Blocks:** check block status, allocation, pickup, and release/cut-off rules in the property's
  setup before changing inventory.

## Asynchronous operations and events

- If the API contract provides asynchronous processing, follow its documented submit, status,
  completion, timeout, and error behavior.
- For Business Events, verify subscription status, filters, delivery path, consumer processing, and
  the documented replay/reconciliation behavior.
- Design state-changing consumers to tolerate duplicates and delayed delivery; do not assume
  ordering or delivery guarantees not stated by Oracle for that interface.

## HTTP response handling

- `2xx`: inspect the response and operation contract; `202` commonly indicates accepted work, not
  completed work.
- `400`, `401`, `403`, `404`, `409`, `422`: inspect the response and correct request, identity,
  entitlement, resource, state, or business-rule issues as applicable.
- `429` and `5xx`: follow documented retry guidance. Reconcile state before repeating any operation
  that may have succeeded or have non-idempotent effects.

## Decision shortcuts

- Bulk/long-running operation: check whether the specific operation has an asynchronous variant.
- Near-real-time notification: check whether a suitable Business Event and supported delivery
  mechanism exist.
- Channel availability, rates, or restrictions: identify the actual Distribution/channel product
  and message direction.
- An action is unavailable: check entitlement, role, license, property configuration, and relevant
  control in the current release.
- A rate differs: compare rate plan, room type, occupancy, dates, restrictions, and channel mapping.
- An export is rejected: validate the actual output against the current receiver/authority schema.

## Operational safeguards

- Follow customer change control and test non-production changes in a representative environment.
- Never log or commit tokens, secrets, full authorization headers, or unnecessary personal data.
- Treat guest, reservation, and folio details as sensitive.
- State release/environment assumptions and verify version-specific details with the official
  documentation and customer-approved procedures.

## Official documentation

- [OPERA Cloud Services documentation](https://docs.oracle.com/en/industries/hospitality/hotels.html)
- [OHIP documentation index](https://docs.oracle.com/en/industries/hospitality/integration-platform/)
