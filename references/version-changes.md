# Version Changes and Release Tracking

## Review-date snapshot

On 2026-10-15, Oracle's Hotels documentation index listed OPERA Cloud Services 26.4, OPERA Cloud
Distribution 26.4, and Hotel Property Interface 8.17 as the newest releases of each. Earlier
Services releases stay listed back to 21.5. The OHIP documentation was last recorded at 26.3 on
2026-10-13 and was not re-checked on 2026-10-15. This snapshot records what the public
documentation indexes showed on those dates. It is not a deployment inventory, a guarantee of
feature compatibility, or a claim that every topic in this skill was independently verified against
every manual for those releases.

Oracle controls its release schedule and numbering. Do not promise a fixed cadence or state a
current release from memory. A customer environment may be on a different release, patch, or
configuration.

## How to track changes

1. Identify the exact OPERA Cloud/OHIP release, environment, product modules, and dependent
   interface versions in use.
2. Read the Oracle release readiness guide, release notes, compatibility matrix, and security
   guidance for the target release.
3. Compare each integration operation with the API contract and portal documentation applicable
   to that integration and release.
4. Review configuration/control dependencies and any announced deprecations.
5. Re-test relevant workflows with representative data in an approved non-production environment.
6. Record source links, versions, results, approvals, and rollback arrangements.

OPERA 5 is a distinct product with release- and patch-specific documentation. Do not apply OPERA
Cloud release notes or setup assumptions to OPERA 5.

## Areas to re-check on upgrades

- API operations, required fields, response shapes, enums, authorization, and limits.
- Event payloads, filters, subscription lifecycle, delivery, and reconciliation.
- Property configuration, permissions, OPERA Controls, reports, and templates.
- Distribution mappings, message compatibility, channel behavior, and dependent software.
- Fiscal/accounting schemas, certification requirements, date/sign conventions, and receiver
  validation.
- Supported devices, browsers, operating systems, network requirements, certificates, and security
  advisories.
- Data migration, history/report continuity, and external code mappings.

## Confirm the deployed release

Documentation publication does not establish a property's deployed version. Confirm its release
and maintenance schedule with the customer and Oracle. Behaviour can differ across releases:

- Establish the property's installed release before answering a release-sensitive question.
- State the release each claim is true for, for example "as at 26.4, X; introduced in 26.1".
- If the release is unknown or its notes have not been read, say so. Do not answer from the nearest
  release you do have.
- Do not carry a newer release's behaviour back to an older tenant, or the reverse.

Example of a release boundary. **Documented (26.1, checked 2026-10-15):** Oracle's 26.1 release
readiness guide lists "Auto Check Out Fiscal Folios Added" and "Quick Check Out Updated to Support
Fiscal Workflow for Zero Balance Departures" under Cashiering and Financials. The first lets the
Fiscal Folio Printing and Auto Check Out controls be active together, and the second sends the fiscal
payload to the fiscal partner for zero-balance departures. Source:
[26.1 release readiness guide](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.1/oprnc/c_feature_summary.htm).
**Inference:** this release boundary warrants checking older tenants for workflow limitations.
It does not prove that every earlier fiscal integration lacked automated checkout or that any
transaction went unreported. Verify the actual workflow and fiscal records. The limits and failure behaviour are in `fiscal-compliance.md`.

## 26.4 release-note items verified on 2026-10-15

These are examples of confirmed changes, not a complete release summary. They come from the
[26.4 release readiness guide](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm),
including the Country Specific section.

- **Portugal:** the Advanced Packages OPERA Control is no longer displayed, to avoid issues with the
  `PT_SAFT_104` country export. Oracle's impact note says Advanced Packages functionality is not
  compatible with that export. A Portuguese property where the control is active should set it
  inactive before moving to 26.4, then confirm the Package Allowance fields no longer display and
  regression-test the SAF-T export. Scale SMALL, no enablement needed.
- **Spain:** municipality-code functionality is added for properties with Country Mode ES. It lets
  a property import municipality codes and show them on Profiles, Police Registration Cards, and
  R+A reports. It must be enabled: turn on the Display Municipality Code OPERA Control, choose a
  value for the Municipality Code Region OPERA Control (ESP, BAS, or CAT), and grant the Import
  Municipality Code Account Folio task to the relevant role. Scale SMALL.

- **Leisure Management:** the 26.4 guide describes Leisure Experiences for eligible OPERA Cloud
  Services or OPERA Cloud Central Management Services subscriptions. Setup requires configured
  locations, experience types, resources, pricing, schedules, controls, and role tasks. The guide
  says experience statuses are generally updated manually, No Show is assigned during End of Day,
  and an unconfirmed availability hold expires after 30 minutes. This is product workflow evidence,
  not evidence that a matching OHIP API is available or enabled; verify the API contract separately.

Only selected 26.4 sections were read for this review. Read the full guide before planning an
upgrade.

## 26.3 release-note items verified on 2026-10-13

These are examples of confirmed changes, not a complete release summary:

- **OHIP event streams:** streams with no successful connection for 4 days receive a warning;
  at 7 days streaming is automatically disabled while the configuration/allocation remain; at 30
  days the stream, configuration, and queued events are permanently deleted. Re-enabling the UI
  toggle does not reset the inactivity counter; a successful consumer connection does. See the
  [OHIP 26.3 release notes](https://docs.oracle.com/en/industries/hospitality/integration-platform/axern/c_feature_summary.htm).
- **OPERA Cloud Reservations:** the 26.3 release readiness guide notes changes to the Reservation
  Sales Screen availability flow and allows copying reservations from Future and Past Stays in the
  Find Reservation flow. Check the [26.3 release readiness guide](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.3/oprnc/c_feature_summary.htm)
  for exact scope and workflow details.

Do not assume these features are enabled or behave identically in a customer tenant. Review the
full release notes and configuration/entitlement requirements before deployment.

## Integration upgrade checklist

- [ ] Confirm source and target product/release/environment for every dependency.
- [ ] Review official release notes and compatibility/security documentation.
- [ ] Inventory API calls, events, configurations, and downstream assumptions.
- [ ] Check for schema changes, new/retired values, deprecations, permissions, and controls.
- [ ] Test success, validation failures, authorization, retries, duplicates, and recovery behavior.
- [ ] Validate fiscal and finance exports against the current authoritative receiver schema.
- [ ] Verify mappings and end-to-end distribution/interface flows.
- [ ] Obtain required approval, prepare rollback, and monitor the production cutover.

When answering a release-specific question, identify the release and environment, link the
applicable official source, and say what remains unverified. If the exact release cannot be
established, give a general answer and explain how to check rather than presenting old details as
current.

## Official indexes

- [Oracle Hospitality Hotels documentation index](https://docs.oracle.com/en/industries/hospitality/hotels.html) (all products and releases)
- [OPERA Cloud Services 26.4 release readiness](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm)
- [Oracle Hospitality Integration Platform documentation](https://docs.oracle.com/en/industries/hospitality/integration-platform/)
- [OHIP release notes](https://docs.oracle.com/en/industries/hospitality/integration-platform/axern/c_feature_summary.htm)
- [Oracle Hospitality documentation home](https://docs.oracle.com/en/industries/hospitality/)
