# Distribution APIs and Channel Manager Migration

Distribution capabilities, API contracts, product names, and message behavior are release- and
configuration-dependent. Oracle's Help Center listed OPERA Cloud Distribution 26.4 as the newest release on 2026-10-15.
Check the customer's actual release and enabled products before applying this overview.

## Distribution APIs

Oracle Hospitality Distribution provides documented capabilities for channel connectivity.
Confirm which Distribution APIs or interface products are in scope for the property; do not
assume every channel connection uses the same product or message flow.

### ARI push (Availability, Rates, Inventory)

ARI refers to availability, rates, and inventory/rate restrictions. The direction, triggering,
timing, and acknowledgment of updates depend on the configured integration and contract. Do not
promise immediate propagation; verify monitoring and reconciliation behavior.

- Availability: how many rooms are sellable by room type and date.
- Rates: rate amounts by rate plan and date.
- Restrictions: open/close, minimum/maximum length of stay, closed to arrival/departure, and
  similar controls (see `rates-restrictions.md`).

### Reservation notification (ResNotif)

Reservation notification is one pattern used for inbound channel reservation messages. Confirm
which create, change, cancel, and error flows are supported by the actual channel integration.

### Design notes

- Do not assume distribution flows are synchronous or near real time; design monitoring and
  reconciliation around the documented delivery objectives.
- Code mapping between OPERA and the channel is the heart of a reliable integration: room types,
  rate plans, and restrictions must map cleanly in both directions.
- Confirm the exact module set and behaviour against the Distribution API documentation for the
  running release; distribution capability changes across versions.

## Channel manager migration

Migration behavior depends on the source/target products, mappings, contract, and cutover plan.
Treat the checklist below as questions to resolve, not guaranteed Oracle behavior.

### Core principle

Determine which external and OPERA codes are retained or remapped. OXI is a distinct integration
product and is not a generic synonym for OHIP or every OPERA Cloud distribution integration.

### What changes versus what stays the same

| Component | Changes? | Notes |
|-----------|----------|-------|
| Channel external rate codes | Confirm | Retain or remap based on the channel and migration design |
| Interface / distribution mappings | Confirm | Identify the actual product and mapping configuration |
| Channel extranet rate plan links | Verify | Confirm links and eligibility with the channel manager |
| OPERA internal rate codes | Confirm | Depends on configuration and any rate restructure |

### Extranet rate plan links

Channel extranet rate plan links are not always covered by the external-code preservation rule.
Treat them as an exception:
1. Document them pre-migration (export or screenshot all active extranet links).
2. Verify post-migration that they still resolve correctly.
3. Reconfigure if the underlying OPERA rate code changed.

### Reporting structural break

Assess whether code, configuration, or data changes affect reporting continuity. Before cutover,
document the relevant old-to-new mappings and agree how historical reports and comparisons will
handle them with the report owners.

### Guest profile and reservation impact

Determine whether profile and historical reservation data is transformed, retained, or remapped.
Validate representative historical and new records, and document the effect on downstream
segmentation and revenue analysis.

### Interface sequencing at go-live

Plan and test the exact source/target cutover:
1. Identify all systems, channels, properties, credentials, and code mappings in scope.
2. Test representative new, modified, and cancelled reservations and ARI updates end to end.
3. Define how in-flight messages and bookings are reconciled during cutover.
4. Agree monitoring, rollback criteria, ownership, and the production change window.

## Authoritative references

- [OPERA Cloud Services documentation](https://docs.oracle.com/en/industries/hospitality/hotels.html)
- [OHIP documentation index](https://docs.oracle.com/en/industries/hospitality/integration-platform/)

Use the documentation for the actual Distribution product and channel contract for detailed
message schemas and operating procedures.
