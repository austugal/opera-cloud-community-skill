# Fiscal and Regulatory Exports

This guide provides a framework for investigating fiscal and regulatory output. It is not tax or
legal advice and does not establish that a particular OPERA feature is certified or suitable for a
jurisdiction. Requirements change by country, region, taxpayer category, transaction, and reporting
period. Confirm obligations with the competent authority and the customer's tax adviser, then check
the feature and certification for the deployed OPERA release.

## What to establish first

Before troubleshooting or changing an export, identify:

- Country/territory, legal entity, taxpayer status, and applicable tax regime.
- Transaction/document type and reporting period.
- Required format/schema version, channel of submission, and filing deadline from the authority.
- OPERA product, release, licensed fiscal functionality, integration/partner, and configured output.
- The receiver's validation response and the exact generated file, handled under data-protection
  policy.

Do not infer a legal obligation or deadline from another property or an old reference document.

## SAF-T and national implementations

SAF-T (Standard Audit File for Tax) is an OECD-based family of accounting/tax data specifications;
national implementations define their own scope, schema, versioning, and submission obligations.
The acronym alone does not define a compliant file.

For Portugal, consult the current SAF-T (PT) technical materials, schema, and submission guidance
from Autoridade Tributária e Aduaneira (AT). Confirm which schema and reporting period apply.

Spain has multiple tax reporting and electronic invoicing obligations, including SII for taxpayers
within its scope. Coverage, territories, deadlines, formats, and other obligations may change.
Confirm the taxpayer's regime and territory with Agencia Estatal de Administración Tributaria
(AEAT) and any other competent authority.

Other jurisdictions may require national SAF-T variants, e-invoicing, certified devices, real-time
reporting, or other controls. Treat each jurisdiction as a separate legal and technical
specification.

## Portugal and Spain: what to check first

Evidence labels used here: **Documented** (an Oracle or authority source that was read, linked),
**Recorded** (taken from a secondary source or the author's reference library and not confirmed
against a primary source), **Inference** (reasoning, not a source). Nothing below replaces the
authority's current text or Oracle's country guide for the deployed release. Oracle's country Fiscal
Reference Guides sit behind a My Oracle Support login and were not read for this section.

### Portugal

- **Documented (26.4):** the Advanced Packages OPERA Control is no longer displayed for Portuguese
  properties, because Advanced Packages functionality is not compatible with the `PT_SAFT_104`
  country export. Set it inactive before upgrading to 26.4 and regression-test the SAF-T export.
  Source: [26.4 release readiness guide](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm),
  Country Specific.
- **Documented (checked 2026-10-15):** Lei n.º 73-A/2025, article 95, paragraph 3,
  accepts PDF invoices as electronic invoices for fiscal-law purposes through 31 December 2026.
  Source: [Diário da República](https://diariodarepublica.pt/dr/detalhe/lei/73-a-2025-993270096).
  This provision alone does not establish the rules from 1 January 2027, mandate CIUS-PT,
  or remove other invoicing obligations. Verify the legislation effective on the invoice date.

### Spain

- **Recorded:** the VERI*FACTU announcement does not by itself change SII operation or show an
  OPERA configuration change. Keep SII running and test any VERI*FACTU path against the
  property's exact legal scope, OPERA release, and Oracle's guidance.
- **Documented (AEAT, read 2026-10-15):** under Real Decreto-ley 15/2025, de 2 de diciembre,
  Corporate Income Tax filers must have invoicing systems adapted before 1 January 2027 and the
  remaining covered taxpayers before 1 July 2027. Source:
  [AEAT note](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html).
- **Documented, not in force (Ministry of Finance, 5 October 2026):** the Ministry announced a
  planned postponement of the pending Real Decreto 1007/2023 obligations to October 2028, aligned
  with mandatory e-invoicing for businesses with turnover up to EUR 8 million. The note describes a
  forecast change that still needs approval. Source:
  [Ministry note](https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf).
  Keep the 2027 dates as the planning baseline until an amending measure is published in the BOE.
  Do not defer an implementation on the press notice alone. Re-check before any Spanish
  go-live in 2027.
- **Documented (26.4):** municipality-code functionality is added for Country Mode ES and must be
  enabled (Display Municipality Code and Municipality Code Region controls, plus the Import
  Municipality Code Account Folio task for the role).
- **Recorded:** Spanish properties may also carry police registration exports that vary by
  autonomous community, the INE hotel occupancy survey, and the Modelo 347 annual declaration.
  Invoice classifications F1 to F6 follow the AEAT specification.

### Questions that decide the answer

1. Which OPERA Cloud release is the property on? **Documented (26.1):** from 26.1 the Fiscal Folio
   Printing and Auto Check Out OPERA Controls can be active at the same time, and a child control
   (Auto Check Out Fiscal Folios) runs the fiscal workflow when Auto Check Out is chosen from Quick
   Check Out. Quick Check Out for zero-balance departures also sends the fiscal payload to the
   fiscal partner when Fiscal Folio Printing is active. Source:
   [26.1 release readiness guide](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.1/oprnc/c_feature_summary.htm) (document G48601-01), Cashiering and
   Financials. **Inference:** older tenants warrant workflow-specific checks. This entry does not
   establish that every earlier fiscal integration lacked automated checkout or that departures
   went unreported; inspect the configuration and fiscal records.
2. Do the 26.1 limits apply? **Documented (26.1):** Auto Check Out Fiscal Folios cannot be active
   with the Information Collection control, is hidden for Latin American properties, and should not
   be activated for Country Mode IT or RO, which need user input to choose a folio type before
   settlement. Zero-balance fiscal checkout is unavailable when folio type or print queue selection
   is required, when Fiscal Service Terminals is active without a primary terminal, or when an
   Information Collection method is BEFORE_SETTLEMENT. In those cases the departures are checked
   out manually from the billing screen.
3. What happens if the fiscal partner is unreachable? **Documented (26.1), zero-balance checkout
   only:** the Check Out Zero Balance Departures process stops and the status column shows
   "No response from fiscal service". If Offline Folio functionality is active, Oracle documents manual checkout through the
   billing screen. Do not generalise this behaviour to other checkout paths.
4. Is Advanced Packages active on a Portuguese property that is moving to 26.4?
5. **Documented (26.3):** the Simplified Settlement Workflow and Fiscal Folio Printing OPERA
   Controls are updated so they can be active at the same time (scale SMALL, must be enabled).
   Source: [26.3 release readiness guide](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.3/oprnc/c_feature_summary.htm) (document G55991-02). The order in
   which the fiscal document and settlement complete is not described in the entry. Test it before
   configuring it on a live property.

## File validation and reconciliation

- Validate XML against the authority's schema and rules for the applicable period; passing an
  OPERA export step does not prove authority acceptance or legal compliance.
- Validate CSV/flat-file encoding, escaping, delimiters, column order, decimal/date formats, signs,
  identifiers, and required fields against the receiver's current specification.
- Reconcile document counts and totals to trusted OPERA reports and source records using the
  approved accounting procedure.
- Preserve required numbering, document references, audit trails, and integrity controls; never
  alter them to make a file pass a superficial check.
- For credit notes, refunds, and reversals, verify both document classification and amount/sign
  conventions end to end. Do not assume all destinations use the same representation.

## Safe change workflow

1. Preserve the original output and validation error securely; redact personal and payment data
   before sharing.
2. Identify the exact legal requirement, receiver specification, OPERA release, and configuration.
3. Reproduce in an approved test environment with representative invoices, credits, taxes,
   rounding, dates, and edge cases.
4. Validate with the authority's current schema/tool or the receiver's approved validator.
5. Reconcile results and obtain required tax, finance, and operations approval.
6. Deploy through the customer's change-control process; monitor the first production submission
   and retain evidence according to policy.

## Official sources

- [Portuguese Tax and Customs Authority (AT)](https://info.portaldasfinancas.gov.pt/)
- [Spanish Tax Agency (AEAT)](https://sede.agenciatributaria.gob.es/)
- [Oracle Hospitality Hotels documentation index](https://docs.oracle.com/en/industries/hospitality/hotels.html)
- [OPERA Cloud Services 26.4 release readiness](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm)

National authority material controls legal requirements. Oracle documentation describes product
functionality, not whether a taxpayer is legally in scope.

## Additional public Oracle country coverage (reviewed 2026-10-19)

The following additions use public Oracle release documentation only. They are selected product changes, not complete country implementations or legal certification. No uploaded support document, customer checklist, screenshot, project note or actual configuration is distributed with this package.

### France — OPERA Cloud 26.4

When Service Types is active, DAILY_ARCHIVE and DAILY_ARCHIVE_DAY include service-type data. ServiceTypeHeader distinguishes goods, services and mixed folios; DocumentLine uses G or S. Unclassified transaction codes count as services; charge-free folios omit these elements. Deposit Folios and their Credit Bills no longer affect Grand Totals. Oracle requires recreation of both archive exports for the changes to apply [C1].

This is scoped to the stated release and country. The supplied screenshot was too low-resolution to verify; no configuration was inferred from it. This section does not establish current French tax rates, certification status or a complete archive configuration.

### Spain — OPERA Cloud 26.4, additional municipality detail

For Country Mode ES, the municipality field appears for profile address country ES/ESP. Oracle says it is optional and does not validate the selection. Profiles show six digits; registration-card formatting depends on the selected region. Updated R&A reports use the new field, falling back to previous behavior when it is absent [C1].

The country controls and import requirement are already described above. A completed implementation checklist is not evidence of a product-wide prerequisite, a successful deployment elsewhere or a current Oracle procedure. No customer checklist or its completion statuses are included here.

### Germany — OPERA Cloud 26.3 and OFIS Cloud 26.3

Oracle's OPERA Cloud 26.3 notes add ESTATISTIK as a fiscal partner. DATA MANAGEMENT is an option on Manage Fiscal Partner, visible only when ESTATISTIK is selected. The ESTATISTIK_STATS command generates the tourism-statistics universal payload. Country mappings use ESTATISTIK_COUNTRY and MC_ESTATISTIK [C2].

The separate OFIS Cloud 26.3 overview says Generic JSON remains the primary German fiscal delivery and ESTATISTIK is an additional delivery. It identifies Country Mode DE, applicable controls, role tasks, fiscal setup, outbound-domain allow-list configuration, country mappings and monthly report validation as configuration topics [C3]. The overview does not supply every operational value; do not invent endpoints, identifiers or mappings.

OPERA Cloud and OFIS Cloud are separate release scopes. These selected facts do not establish a complete German TSE, invoice-delivery, DSFinV-K or city-tax setup. The restricted country guide is not included or reproduced. Exact partner-specific procedures still require the applicable authorised documentation.

### Public Oracle sources

- **[C1] [OPERA Cloud 26.4 Feature Summary](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm)** — France daily archives/Grand Totals and Spain municipality-code sections read 2026-10-19.
- **[C2] [OPERA Cloud 26.3 Feature Summary](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.3/oprnc/c_feature_summary.htm)** — Germany eStatistik section read 2026-10-19.
- **[C3] [OFIS Cloud 26.3: Germany ESTATISTIK configuration overview](https://docs.oracle.com/en/industries/hospitality/opera-fiscal-integration-solution/26.3/ofrrg/c_germany_ofis_cloud_configuration_for_estatistik.htm)** — public overview read 2026-10-19; not a complete setup specification.

No tenant, export, report, partner delivery or authority acceptance was tested. Retain the source release when answering; do not silently generalise these changes to earlier releases or other countries.

## Expanded country research references

- [Italy](italy-fiscal.md)
- [France](france-fiscal.md)
- [Germany](germany-fiscal.md)
- [Usa](usa-fiscal.md)
- [Uk](uk-fiscal.md)

Read each source boundary before using guide-based topics. These references add original
research and acceptance workflows, not raw Oracle support documents or legal certification.
