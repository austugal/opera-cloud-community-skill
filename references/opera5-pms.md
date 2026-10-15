# OPERA 5 Property Management System

OPERA 5 is distinct from OPERA Cloud. Product generations, licensed modules, patch levels,
deployment models, interfaces, and configuration paths vary. This reference is a topic map and
troubleshooting aid, not a universal click-by-click procedure. Verify every menu path, parameter,
task name, version prerequisite, and operational effect in the manual matching the installed
release.

## Configuration areas

OPERA 5 deployments commonly organize configuration and operations around areas such as:

- Reservations and reservation rules.
- Profiles and memberships.
- Rate management and packages.
- Cashiering, transaction codes, payment methods, and folios.
- Rooms, housekeeping, and room status.
- Blocks, events, and other licensed functions.
- Users, roles, workstations, printers, and interfaces.

Names, menu placement, availability, and behavior differ among OPERA 5 versions and licensed
modules. Search the exact-version help library rather than copying a path from another release.

## Workstations and print tasks

Workstation records, printers, and print-task assignment are OPERA 5 configuration topics. For the
target version, confirm:

- How the workstation is identified and associated with a property.
- Whether the workstation is registered automatically or must be configured.
- Where printers and print tasks are defined, assigned, inherited, and tested.
- Which feature, license, parameter, and user permissions are prerequisites.
- Whether multiple assignments can create duplicate output.

Test using a non-sensitive document in a controlled environment. Do not rely on historical task
names or parameter values without checking the exact manual and property configuration.

## Interfaces and payments

OPERA 5 interface products and payment integrations have separate compatibility matrices,
installation guides, security requirements, and release dependencies. For OPI, IFC8, OXI, or
another integration, identify the exact product version and OPERA 5 patch, then follow the matching
Oracle/vendor deployment guide. Do not reuse obsolete server specifications, installer options,
ports, cipher/key formats, credentials, or minimum versions from this generic guide.

Payment deployments must follow the merchant/acquirer and applicable PCI/security requirements.
Never send card data, secrets, or unredacted logs through ordinary support channels.

## Business events and operations

OPERA 5 installations may include configured business-event or queue processing. Verify event
definitions, conditions, retention/purge behavior, module availability, and processing ownership in
the version-specific manual. Do not assume event names, queue retention periods, cache operations,
or server placement are consistent across releases.

Other configuration topics to verify include cashiering, reservation deposits/cancellations,
transaction codes, tax setup, reports, and local regulatory interfaces. Their availability and
legal effect depend on release, license, country, and property configuration.

## Safe troubleshooting

1. Record the OPERA 5 release/patch, hosted/on-premises model, property, module, workstation, exact
   sanitized error, time, impact scope, and recent changes.
2. Check the matching release manual, Oracle release notes, customer runbook, and supported
   interface documentation.
3. Compare affected and known-good workstations/users without exposing guest or payment data.
4. Collect approved OPERA/interface/OS diagnostics and correlate timestamps across systems.
5. Avoid direct database edits, guessed log paths, unapproved restarts, firewall changes, or
   configuration changes. Escalate through the customer's support process when needed.

## Oracle documentation

- [Oracle Help Center](https://docs.oracle.com/en/industries/hospitality/)
- [OPERA Property Management 5.0.04 legacy documentation library](https://docs.oracle.com/cd/E53547_01/index.html)

The legacy library is release-specific and may not cover the installed version. Locate the exact
OPERA 5.6 or patch-level manual from Oracle Help Center when that is the deployed release.
