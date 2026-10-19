# Germany: city tax, audit exports, fiscalisation and statistics

Use alongside [fiscal compliance](fiscal-compliance.md) for the publicly verified OPERA/OFIS 26.3
ESTATISTIK details. Establish city, OPERA/OFIS release, fiscal partner, TSE arrangement, invoice
receiver and the particular output being requested.

## Guide-based topic coverage

The supplied Germany guide is DOC2090, portal version 65, published 2026-10-15. Distinguish these
workstreams rather than using “German fiscal integration” as a single configuration instruction.

| Workstream | What the agent must establish |
|---|---|
| Country and controls | Property scope, appropriate control prerequisites and role tasks. Do not enable a guide's entire controls table without reviewing existing configuration. |
| City-tax packages | Municipal rule, purpose-of-stay matching/default, net/gross basis, adult/child treatment, included/excluded packages, discounts, posting nights, caps and effective dates. |
| City-specific calculations | Select the applicable city's current rule and supported function; do not substitute another city's formula or a legacy illustrative rate. |
| GoBD | Identify the required audit dataset, responsible system and date range. The presence of a PMS export is not proof that it is the legally required or complete accounting dataset. |
| Fiscalisation/TSE | Distinguish OPERA document creation, OFIS/partner processing and TSE signing. Investigate missing signatures and acknowledgements before retrying or voiding. |
| Fiscal-device interruption | Capture sanitised status and timestamps, establish whether the document was accepted, and follow the partner's documented recovery procedure. Do not fabricate a signature or edit historical output. |
| E-invoicing/XRechnung | Review payee identifiers, recipient/address data, order references and required invoice fields separately from TSE processing. Fiscal signing and invoice delivery have separate results. |
| ESTATISTIK | Identify the reporting month, property and statistical-country mappings; reconcile accommodation totals and validate receipt independently of invoice processing. |

## Publicly verified ESTATISTIK anchor

Oracle's [OFIS 26.3 configuration guidance](https://docs.oracle.com/en/industries/hospitality/opera-fiscal-integration-solution/26.3/ofrrg/c_germany_ofis_cloud_configuration_for_estatistik.htm)
and [OPERA Cloud 26.3 readiness](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.3/oprnc/c_feature_summary.htm)
are the public anchors for the configuration notes already in fiscal-compliance.md. Verify the
applicable release's fiscal partner, DATA MANAGEMENT capability, `ESTATISTIK_STATS` command,
terminal and mapping requirements. Do not conflate statistics delivery with the primary fiscal
invoice delivery. Retain the documented `ESTATISTIK_COUNTRY`/`MC_ESTATISTIK` distinction.

## Acceptance workflow (original)

- City tax: test taxable/exempt purpose, missing purpose, mixed occupants, discounted rates,
  included breakfast, maximum-night boundary and a stay crossing a rate-change date.
- Audit output: reconcile source ledgers, reporting period and record counts; identify exclusions
  explicitly and check which accounting/partner system owns the required audit submission.
- Fiscalisation: test successful processing and a controlled unavailable-device case, then check
  accepted/signature status before recovery. Preserve a trace from original folio to acknowledgement.
- E-invoice: test valid and incomplete recipient data, rejection and corrected re-delivery without
  assuming that TSE success implies invoice acceptance.
- Statistics: compare the monthly result with the property statistics, including unmapped country
  codes and corrections. Confirm receiver acceptance before marking the task complete.

Exact DSFinV-K, TSE and XRechnung schemas, partner credentials, installation settings and legal
certification claims are outside this reference. Obtain their applicable Oracle/partner contracts;
never infer them from an old screenshot or an example export.

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
