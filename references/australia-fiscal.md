# Australia: fiscal discovery and validation

Reviewed 2026-10-15. Scope: selected indexed ATO primary-source extracts, not a complete legal review. Direct retrieval of the ATO law pages returned access errors. An Oracle support-portal article titled "Australia - Oracle Hospitality OPERA Cloud Fiscal Reference Guide" was located on 2026-10-17 (login required); only its headings were seen, covering property configuration, a comp accounting control for deducting inclusive tax from the comp window, ABN, worked comp-window examples and a UDF tax function. Its content has not been captured or validated here, and no tenant was available. Treat exact configuration as unverified.

## Authority requirements identified

**Documented in ATO primary-source indexed extracts:** GST Act section 29-70 requires the recipient's identity or ABN when the total price is at least A$1,000, and generally requires a supplier to provide a tax invoice within 28 days of a recipient's request. Read the current complete law, applicable exceptions and ATO invoice guidance before applying this to a property.

**Documented in ATO indexed guidance:** Division 87 concerns long-term commercial accommodation, including a continuous period of at least 28 days. Its concessional treatment depends on the premises and supply conditions; it is not a universal instruction to halve the GST rate for every long stay. Obtain the current complete authority guidance and the property's tax decision before configuring thresholds or tax generates.

## Recommended OPERA validation work (author guidance)

Have the finance owner specify supplier identity/ABN, tax invoice fields, recipient identification rules, GST treatment and invoice/adjustment processes. Map those requirements to supported property tax/transaction configuration and stationery fields. Reconcile sample postings, tax totals, folios, refunds/adjustments and accounting/BAS workpapers in a test environment. Test short stays and relevant long-stay boundaries under the approved interpretation. Verify deposits, packages, inclusions and mixed supplies separately.

Do not translate Portugal SAF-T/ATCUD or Spain SII/VERI*FACTU rules into Australia, or invent an Australian OPERA fiscal control name. A configured RTF is presentation, not proof of tax calculation or reporting compliance.

## Primary sources and retrieval limitations

- [GST Act section 29-70, ATO legal database](https://www.ato.gov.au/law/view/document?LocID=%22PAC%2F19990055%2F29-70%282%29%22): indexed extract reviewed; direct page blocked.
- [GSTR 2013/1 tax invoices](https://www.ato.gov.au/law/view/document?LocID=%22GST%2FGSTR20131%2FNAT%2FATO%2Ffp81%22&PiT=20231128000001): indexed extract reviewed; historical point-in-time URL, verify current consolidated guidance.
- [GSTB 2001/2 long-term accommodation](https://www.ato.gov.au/law/view/print?DocID=GSB%2FGSTB20012%2FNAT%2FATO%2F00001&PiT=99991231235958): indexed extract reviewed; direct page inaccessible.
