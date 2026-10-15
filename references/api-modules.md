# OPERA Cloud REST API Modules and Key Operations

OPERA Cloud REST APIs are organised into functional modules exposed through OHIP. This file maps
the module surface and the most common operations by domain. Endpoint paths, payload schemas, and
field names are defined per release in the OHIP Developer Portal and Oracle's published hospitality
API specifications; treat the spec for the running version as authoritative and do not invent paths.

**Scope:** This is a conceptual map, not a guarantee that a module or operation is licensed,
enabled, or exposed to a particular integration. Oracle's Help Center listed OPERA Cloud
Services 26.4 as the newest release on 2026-10-15. Confirm the actual API contract and entitlement in the
tenant's OHIP documentation and the deployed release before implementation.

## Module map

| Module | Domain |
|--------|--------|
| RSV | Reservations |
| CRM | Profiles / customer relationship (guests, companies, travel agents, sources, contacts) |
| CSH | Cashiering / folios / postings |
| FOF | Front office finance |
| HSK | Housekeeping |
| RTP | Rate plans and rate management |
| INV | Inventory and availability |
| BLK | Block (group) management |
| EVM | Event management, sales and catering |
| Exports | Operational exports (module/API availability is release-specific) |
| ENTCFG | Enterprise configuration |
| Property configuration | Property-level configuration |
| INT / INTCFG | Interfaces and interface configuration |
| Distribution (ARI, ResNotif) | Channel availability, rates, restrictions, reservation notification |
| Reporting / analytics | Report and data retrieval |

Some API operations have asynchronous variants for long-running work. Availability and behavior are
operation- and release-specific; see `async-streaming-events.md` and check the relevant API
specification.

## Reservations (RSV)

Core capabilities:
- Search reservations by criteria such as arrival date, departure date, confirmation number,
  profile, room, or status.
- Retrieve a single reservation by its identifier.
- Create, modify, and cancel reservations.
- Manage attached items: packages, fixed charges, traces, alerts, accompanying guests, routing.
- Check-in and check-out actions where exposed through the API.

Typical patterns:
- Search and detail operations can return different projections; check the response schemas and
  available follow-up operations in the API contract.
- Reservation state is indicated by release-specific status values; read current state and allowed
  transitions before acting.
- Response detail and available state transitions are operation-specific; check the endpoint
  contract before acting.
- Routing instructions can affect folio windows or other accounts when supported and configured.

## Profiles / CRM

Capabilities:
- Profile types: guest, company, travel agent, source, contact, group.
- Create and update profiles; search by name, membership, contact details.
- Manage memberships, preferences, addresses, communication channels, and negotiated rates
  attached to company/agent profiles.
- Profile lookup and de-duplication considerations: matching reduces duplicate guest records.

Data protection: profiles are personal data. Extract and retain only what an integration needs.

## Cashiering (CSH)

Capabilities:
- Post charges and payments to a folio window.
- Retrieve folio and transaction detail.
- Adjust, transfer, and void postings subject to cashiering privileges and OPERA Controls.
- Settlement and folio generation.

Concepts:
- A reservation folio has multiple windows; routing and transfers move charges between them.
- Transaction codes classify each posting (room, food and beverage, tax, payment, and so on) and
  drive reporting and back-office mapping.
- Credit and debit behaviour and sign conventions matter for downstream exports (see
  `backoffice-export.md`).

## Rooms, room status, and housekeeping

Capabilities:
- Read and update room status (for example clean, dirty, inspected, out of order, out of service).
- Manage housekeeping task assignment and room conditions.
- Front office room operations such as room moves and assignment.

Concepts:
- Room condition/status and inventory availability are related but not interchangeable. Verify the
  effect of each status and its availability treatment in the property's configuration and the
  current release documentation before changing it.

## Rate management (RTP)

Capabilities:
- Read rate plans, rate codes, rate details, and rate amounts by date.
- Create and update rate plans and rate detail where exposed.
- Manage rate plan attributes: market segment, room types, packages, derivation.

Concepts:
- Derived rates calculate from a base rate by a formula or adjustment rather than holding their own
  amounts. Check the configured derivation and resulting rate rather than assuming how changes
  propagate.
- Bulk rate operations are good candidates for the asynchronous APIs.
- See `rates-restrictions.md` for rate plan structure and restrictions.

## Inventory and availability (INV)

Capabilities:
- Read availability and inventory counts by date and room type.
- Manage sell limits and inventory controls where exposed.

## Block management (BLK)

Capabilities:
- Create and manage blocks (group allotments): room block grid, pickup, cut-off, rooming list.
- Read block availability and pickup against allocation.

Concepts:
- Block status governs whether inventory is deducted from general availability.
- Verify the configured cut-off and release behavior for the block before relying on unsold rooms
  returning to general inventory.

## Front office finance (FOF)

Capabilities:
- Operational finance actions tied to the front desk: balances, deposits, and related postings,
  depending on what the release exposes.

## Event management / sales and catering (EVM)

Capabilities:
- Manage events, function space bookings, and catering where the property is licensed for sales
  and catering.

## Enterprise and property configuration (ENTCFG / property config)

Capabilities:
- Read and manage configuration entities: room types, rate codes, market segments, source codes,
  transaction codes, packages, and similar reference data.
- Configuration APIs underpin any integration that must keep an external system's code set aligned
  with OPERA.

## Interfaces (INT / INTCFG)

Capabilities:
- Configure and query interface definitions used by OPERA to talk to external systems (payment,
  point of sale, door locks, and others).
- See `interfaces-ifc8.md` for IFC8 and OXI concepts.

## General API conventions

- Pagination: list operations page results; follow the documented paging parameters rather than
  assuming a fixed page size.
- Idempotency: before retrying a create or financial/state-changing operation, determine from its
  contract and response whether the first attempt may have succeeded. Do not assume an idempotency
  key is supported.
- Versioning: APIs are versioned; pin to a known version and review the change log before upgrading
  (see `version-changes.md`).
- Errors: read the Oracle error response body, not just the HTTP status (see `error-handling.md`).

## Authoritative references

- [OPERA Cloud Services documentation](https://docs.oracle.com/en/industries/hospitality/hotels.html)
- [OHIP documentation index](https://docs.oracle.com/en/industries/hospitality/integration-platform/)

Use the release-specific API reference available to the integration in the OHIP Developer Portal
for request paths, schemas, required headers, entitlements, limits, and deprecations.
