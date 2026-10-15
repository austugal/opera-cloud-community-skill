---
name: opera-integration-assessment
description: >-
  Assess Oracle Hospitality OPERA Cloud, OPERA 5, OHIP, and partner integrations.
  Use for vendor compatibility claims, interface design, data-flow questions,
  implementation discovery, and integration troubleshooting.
---

# OPERA integration assessment

Use this specialist module with the root `SKILL.md` and the relevant API/interface references.
It provides a repeatable integration-analysis workflow; it does not connect to hotel systems.

## Workflow

1. Identify the vendor and exact product/edition/version on both sides. Distinguish OPERA Cloud, OPERA 5, OHIP, Distribution, IFC8, OXI, OPI, and other named services rather than treating them as interchangeable.
2. Rank evidence: deployed-release Oracle API/interface documentation and the vendor's technical specification first; current vendor compatibility statements next; partner directories and marketing pages as discovery evidence only. Record source date and scope. A listing is not an interface contract, certification, or proof that a particular release is supported.
3. Map each business flow separately: source and destination, data objects/fields, create/update direction, trigger, latency model (synchronous API, asynchronous job, business event/stream, polling, or batch), and ownership of transformations and mappings.
4. Confirm access and runtime behavior: authentication, property/chain and role scope, entitlements, rate limits, pagination, idempotency, duplicate handling, retry safety, error reporting, event recovery, and reconciliation. Verify every endpoint, schema, permission, and limit in the actual release specification.
5. Define a non-production validation plan using synthetic or approved data. Include positive, negative, duplicate, delayed/out-of-order, unavailable-service, and reconciliation cases; set cutover, monitoring, rollback, and support ownership before production.
6. Report confirmed facts separately from vendor claims, observations, inferences, and unknowns. Give the exact source links and list what each party still needs to confirm.

## Vendor-claim checklist

For partner-list entries, capture the vendor, product named in the listing, exact displayed integration wording, source URL, and review date. Do not silently upgrade a generic “Opera” claim to “OPERA Cloud,” “OPERA 5,” “OHIP,” or “Oracle-certified.” When the public page omits a technical specification, say that the interface details are unverified and provide the confirmation questions in `references/partner-integrations.md`.

## Safety boundaries

- Never request or publish credentials, private endpoints, real guest/payment data, or restricted support material.
- Do not recommend direct database access, unverified endpoint paths, blind retries, or production changes without customer approval.
- Do not promise compatibility, data completeness, real-time delivery, or reversibility unless the applicable primary sources establish it.
