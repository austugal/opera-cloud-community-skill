# Italy: fiscal, guest reporting and city-tax research

Use for Italian OPERA Cloud questions about guest reporting, custom charges, folios, e-invoicing,
fiscal devices and reporting. First establish the municipality/region, deployed OPERA release,
OFIS deployment/version, fiscal partner, required output and receiving system.

## Guide-based topic coverage

The supplied Oracle Italy guide (DOC1887, portal version 62, published 2026-10-07) covers the
following distinct workstreams. Do not treat one export or partner connection as satisfying all of them.

| Workstream | What to investigate and validate |
|---|---|
| Additional addressee | Identify the intended recipient separately from the staying guest; check accompanying-profile selection, reservation, folio-history and transaction-research behaviour. |
| Alloggiati guest reporting | Establish arrival-day versus previous-day processing, day-use scope, accompanying guests, group/family relationships, identification fields and required municipality/country mappings. Check the control report before export. |
| Guest-type/UDF configuration | Verify the deployed guide's group-leader field, permitted values and customization scope; do not infer the complete mapping from screenshots alone. |
| Statistical reporting | Select the actual regional receiver and template. The supplied guide discusses ASTAT and regional ISTAT variants; a template for one region is not a national substitute. Reconcile guests, arrivals, departures and overnight stays separately. |
| Custom charges | Confirm municipal rule, rate base, per-person treatment, limits, posting rhythm, exclusions and effective dates. Distinguish reservation/property/accompanying-guest exemptions and subsequent adjustments. |
| Reporting | Reconcile the Custom Charge and Redemption Summary, exemptions and adjustments with generated export totals. |
| Folios and credit bills | Distinguish Ricevuta, Fattura, deposits and their credit bills. Validate original-document association, VAT breakdown, folio numbering and payment handling with approved test cases. |
| E-invoice data | Review payee identifiers, recipient delivery data, public-administration fields, order/contract references, and applicable mappings. Do not assume a visible profile field alone proves successful delivery. |
| VAT offset and deposits | Establish the relevant accounting scenario and trace the offset through payment, deposit and final folio; reconcile amounts without double counting. |
| Fiscal devices/OFIS | Separate configuration of partners, terminals, print tasks and commands from actual device acknowledgement. Validate resend, void, credit bill and end-of-day behaviour for the selected integration. |
| Electronic receipts | Verify supported terminal/device capability, destination choice, required collection fields and delivery outcome. Do not reuse printer firmware settings from an older example. |
| R&A | Identify the supported report/template, property access, schedule, date basis and secure destination. A scheduled job is not proof the receiver accepted the output. |

## Publicly verified product anchors

Oracle's [26.4 Custom Charges documentation](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/t_configuring_custom_charges.htm)
describes per-person charges, stay/date exemptions, posting rhythms, exclusions, rate-per-person
ranges and percentage-with-limit calculations. Read the actual rule exposed by the deployment;
do not manufacture a formula from its name.

Oracle's [R&A release note](https://docs.oracle.com/en/industries/hospitality/opera-reporting-analytics/rnora/t_added_custom_charge_export_for_italy.htm)
identifies `ITA-Tracciati.xml` in `/Shared Folders/Templates/Fiscal/Italy` for city-tax export.
It sends readers to the country guide for full configuration. This is separate from Alloggiati,
regional statistics and invoice transmission.

## Acceptance workflow (original)

1. Define one scenario per receiver, with expected record count, amount, date and acknowledgement.
2. Test individual, family/group, accompanying guest, day use, changed dates and missing identification.
3. For city tax, test an exempt guest, a partially exempt stay, cap boundary, package exclusion,
   adjustment and stay spanning an effective-date change.
4. For fiscal documents, test deposit, settlement, credit bill and a failed-delivery recovery.
   Check original acceptance before resending to prevent duplicate fiscal documents.
5. Reconcile PMS postings, report totals, export payload and receiver response. Record unresolved
   differences rather than declaring compliance from successful file creation.

Source locator: [Oracle Italy fiscal reference guide](https://iccp.custhelp.com/app/answers/answer_view/a_id/1002186)
(access may require an Oracle entitlement). Exact export layouts, formulas and device settings are
not bundled here; verify them from the applicable Oracle source.

## Evidence and use boundary

Reviewed 2026-10-19. This is an original research and acceptance-test aid, not a copy of the
Oracle guide or an installation manual. **Guide-based** means the topic is present in the
user-supplied Oracle country guide; it does not mean its exact settings were independently
verified in public documentation or against a live property. Obtain the applicable Oracle
revision and deployed-release documentation before implementing those settings. Publicly
verified items are identified separately. Do not reproduce support attachments, screenshots,
sample guest records, signed download links, or credentials in answers or deliverables.

Separate product configuration from current legal requirements. Never apply example tax rates,
thresholds, retention periods or historical forms as current law. Use synthetic test records.
