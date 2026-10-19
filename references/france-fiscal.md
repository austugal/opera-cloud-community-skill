# France: archives, folios, deposits and fiscal integration

Use this reference alongside [fiscal compliance](fiscal-compliance.md), which retains the verified
26.4 archive/service-type changes. Establish OPERA release, country configuration, archive solution,
OFIS version/partner and whether the question concerns cashiering, tourist tax or e-invoicing.

## Guide-based topic coverage

The supplied France guide is DOC6506, portal version 39, published 2026-09-28. Its examples span
multiple revisions; the publication date does not make every screenshot a current procedure.

| Area | Research and validation focus |
|---|---|
| Controls and roles | Separate configuration prerequisites from user tasks. Review cashiering, deposits, invoice/credit-bill controls, export permissions and sensitive-data access for the chosen workflow. |
| Deposits | Trace payment, deposit folio, tax recognition, application to the stay and reversal. Reconcile deposit and guest ledgers and the final invoice. |
| Folio stationery | Review document title, original/associated document identifiers, operator/cashier, goods/services, VAT totals, discounts, quantities and unit prices against the applicable data model. |
| Template calculations | Test zero quantities, rounding and negative adjustments. Do not paste OCR-derived RTF/XML expressions into production templates. |
| Certification and signatures | Verify the certificate and deployed version actually applicable to the property; a sample certification logo does not establish certification of another build. |
| Daily archives | Distinguish scheduled daily generation from a manually selected business date. Check completeness, delivery, ability to retrieve/decrypt and authorised access. |
| Period totals and audit trail | Reconcile daily/monthly/yearly period boundaries, document references and audit events. Preserve original exports and investigate gaps without editing fiscal history. |
| Tourist tax | Identify classified/unclassified accommodation, municipality, date, occupants, exempt persons, tax base, package treatment, caps and additional taxes. Never use illustrated percentages as today's rates. |
| Credit bills | Verify the original document, transaction/adjustment relationships and resulting VAT/accounting totals; a negative posting alone is not proof of the proper credit-bill workflow. |
| Export privacy | Check sensitive-data classification, download permission and secure delivery destination. Avoid guest data in troubleshooting examples. |
| E-invoicing/OFIS | Identify payee type, identifiers, e-invoice address, service classification, fiscal buckets, partner parameters and document/transaction mapping. Separate payload creation from accepted delivery. |

## Publicly verified release boundary

[OPERA Cloud 26.4 release readiness](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm)
changes daily archives for service types and excludes deposit folios and their credit bills from
grand totals. The existing fiscal-compliance reference explains the scoped changes and the need
to recreate the relevant export templates. Treat recreation as a controlled upgrade change:
preserve configuration evidence and existing archives, test first and check the replacement output.

## Acceptance workflow (original)

Build a small synthetic test matrix: ordinary invoice; mixed goods/services; payment-only document;
deposit then settlement; deposit reversal; credit bill; zero-quantity line; exempt tourist;
and a stay crossing month end. For each, record expected ledger effect, folio output, archive
record and delivery result. Test retrieval and access restrictions as well as generation.

Keep cashiering archives, tourist-tax calculation and electronic-invoice delivery as separate
acceptance criteria. Successful execution of one does not certify the others or establish legal
compliance. Confirm current retention and reporting obligations outside historical examples.

Source locator: [Oracle France fiscal reference guide](https://iccp.custhelp.com/app/answers/answer_view/a_id/1006813)
(access may require an Oracle entitlement). Raw forms, XML samples and screenshots are not bundled.

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
