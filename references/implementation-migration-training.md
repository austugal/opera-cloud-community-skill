# Implementation, migration and user training

Reviewed 2026-10-15. Selected import documentation is for OPERA Cloud 26.2; Enterprise Management is a separate documented configuration route. No migration or tenant test was executed.

## Documented import boundaries

Oracle's OPERA Cloud Data Import uses supplied templates for a configured target property. Retrieve the templates from the target environment; do not build a universal CSV from remembered columns. The 26.2 guide separates upload, validation, error correction and importing validated data. It documents a 14-day import-cycle window after the first successful upload and a maximum 10 MB per data file. Reconfirm these limits for the installed release.

Important dependencies and exclusions include profiles/reservations before ledger imports, and block exclusions such as packages, attachments and master/sub-blocks. This selected list is not a complete migration scope. Read the entity table and file requirements before agreeing a migration contract.

Oracle Hospitality Enterprise Management separately supports seeding an unconfigured Enterprise Template from an OPERA Cloud property in OPERA mode, and selective CSV configuration imports. The documented property import excludes OPERA Controls. Its CSV limit is 2 MB per file. Do not confuse this with transactional Data Import or promise a complete clone of a property.

## Recommended delivery framework (author guidance)

1. Discover product/releases, countries, environments, subscriptions, property structure, integrations and accountable owners. Create a configuration inventory and exclusions list.
2. Agree rooms, rates, transaction/tax codes, payment methods, profiles and mapping ownership. Establish a signed source-to-target mapping and source extraction authority.
3. Prepare and clean data outside the target using approved handling. Check keys, required fields, lengths, dates, duplicates and referential links against downloaded templates.
4. Run trial uploads and validation in a permitted test environment. Reconcile counts, ledger totals, reservations, inventory and rejected records. Define acceptance criteria before a cutover date.
5. Rehearse cutover: freeze/extract boundaries, interface pause/restart ownership, final reconciliation, communication and fallback decision. Do not promise that an import has a one-click reversal.
6. Train by role with synthetic scenarios, then conduct UAT, controlled go-live and hypercare. Record evidence of acceptance and unresolved defects.

## Role and shift training plan (author guidance)

| Role | Practice scenarios and observable acceptance |
|---|---|
| Front office AM | Arrivals, room readiness, reservation/rate review and check-in exceptions; explain each discrepancy before changing it |
| Front office PM | Departures, traces, routing/payment review and shift handover; identify unresolved balances and ownership |
| Night audit | Pre-audit exceptions, business date and ledger checks; follow the property's approved end-of-day sequence |
| Housekeeping | Room status, discrepancies, tasks and maintenance handover; distinguish availability from cleaning status |
| Reservations/revenue | Daily rates, fixed-rate decisions, restrictions and channel mapping; preserve approved overrides unless a deliberate change is authorised |
| Finance | Folio/AR/deposit/adjustment and fiscal-output reconciliation; explain differences without blind reposting |
| Administrators/integration support | Roles, environment scope, message failures, retries and escalation; demonstrate safe diagnosis |

These are curriculum topics, not claimed Oracle menu sequences or a substitute for the property's SOP. Teach the effect of each action and exceptions as well as button clicks. Never prescribe refreshing/repricing every booking: establish the intended rate and override before changing it. Link the exact deployed-release procedure when producing a detailed SOP.

## Primary sources

- [OPERA Cloud 26.2 About Data Import](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.2/ocsuh/c_system_setup-importing_data.htm), selected requirements and exclusions.
- [Enterprise Management: Using Data Import](https://docs.oracle.com/en/industries/hospitality/enterprise-management/ecmug/ch_manage_imports.htm).
- [Oracle Hospitality Hotels documentation](https://docs.oracle.com/en/industries/hospitality/hotels.html), select the deployed-release User Guide for role-specific procedures.
