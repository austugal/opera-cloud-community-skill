# Australia: GST and OPERA Cloud implementation reference

Reviewed 2026-10-19. This community guide helps a hotel team turn an Australian GST requirement into a configuration and acceptance-test plan. It is not Oracle's official Australia Fiscal Reference Guide, a tax opinion, or evidence of a compliant hotel deployment.

## Scope and evidence

- **Authority guidance:** selected ATO indexed extracts support the limited tax statements below. Direct ATO page retrieval returned HTTP 403; the complete current guidance and exceptions were not inspected. Recheck the linked guidance with the property's finance or tax owner before implementation.
- **Oracle documentation:** the public OPERA Cloud **26.2** Configuring Generates page was read. It describes general product mechanisms, not a verified Australian configuration. Check the corresponding documentation for the deployed release; do not assume 26.2 behavior applies unchanged to 26.4 or OPERA 5.
- **Unverified country detail:** an Oracle support article titled "Australia - Oracle Hospitality OPERA Cloud Fiscal Reference Guide" was located on 2026-10-17, but only headings were seen. Its comp-accounting, ABN, worked-example and UDF content has not been validated or reproduced here. No hotel tenant was accessed.
- **Author guidance:** the discovery questions, mapping worksheet, test cases and output template below are proposed implementation practices, not statutory requirements or Oracle-certified steps.

## 1. Establish the property's context

Ask for the deployed OPERA release, test/production environment, property and legal supplier, GST registration status, approved tax treatment, invoice recipient, transaction-code catalogue and accounting destination. Use synthetic examples rather than guest records or identifiers.

Separate these questions before suggesting a setting:

| Decision | Evidence to obtain |
| --- | --- |
| What is being supplied? | Accommodation, food, parking, package components or another service; finance-approved classification for each |
| Who supplies and receives it? | Legal supplier and ABN source; guest, company, agent or other recipient; contractual invoicing arrangement |
| How is the price expressed? | GST inclusive or exclusive; discounts, package allocations, routing and rounding policy |
| Is it a long stay? | Continuous stay dates, premises classification, applicable election and approved Division 87 treatment |
| What must reconcile? | Posted revenue and GST, folio, adjustments, ledger export and finance's BAS workpapers |

Do not apply Portugal SAF-T/ATCUD or Spain SII/VERI*FACTU requirements to Australia. An Australian reference is a separate country scope within the same skill.

## 2. GST calculation: a bounded worked example

ATO commercial-residential guidance says short-term accommodation is a stay of less than 28 continuous days and GST is one-eleventh of its price [S2]. This is not a classification rule for every charge a hotel sells.

**Synthetic arithmetic example:** assume finance has confirmed one ordinary taxable accommodation charge, standard 10% GST, no concession, no discount, and no other tax or fee.

| Price basis | Net revenue | GST | Guest total |
| --- | ---: | ---: | ---: |
| A$110.00 including GST | A$100.00 | A$10.00 | A$110.00 |
| A$100.00 excluding GST | A$100.00 | A$10.00 | A$110.00 |

For this example only, inclusive GST = total / 11, and net = total - GST. Adding 10% again to an already inclusive A$110.00 produces a different total and fails this test. These figures are an expected-result calculation, not an OPERA configuration recipe. Check rounding with multiple lines and the property's actual posting rules.

## 3. Tax-invoice discovery

ATO indexed guidance identifies seller identity, seller ABN, issue date and a description of items. It also says invoices for sales of A$1,000 or more need the buyer's identity or ABN [S1]. Section 29-70 generally requires a supplier to provide a tax invoice within 28 days of a recipient's request [S4]; check the complete law and applicable exceptions.

Have finance approve the full invoice specification: tax-invoice designation, supplier details, recipient rules, quantities/prices, taxable components, GST presentation, totals and adjustment-document handling. This is a review checklist, not a claim that the selected extracts establish every required field.

Map approved fields to actual profile/property data and the deployed stationery data model. Do not invent an ABN XML element, profile field, UDF name or menu path. Use [stationery guidance](bi-publisher-stationery-xml.md) to inspect sanitised sample XML and render a test folio. A correct-looking RTF does not prove the ledger tax calculation is correct.

## 4. Long stays: decide the treatment before configuration

Division 87 addresses commercial accommodation supplied to an individual continuously for at least 28 days [S3]. ATO guidance distinguishes short-term, long-term and primarily long-term accommodation [S2]. **A 35-day booking alone does not justify setting GST to 5% for every night.**

Obtain the tax owner's written decision on the premises classification, whether a relevant election applies, which charges qualify, which days receive any concession, and what happens when a stay is extended, shortened or interrupted. Do not turn a general concession into a universal percentage or automatically backdate every charge.

Then design tests around 27, 28 and 29 continuous days, plus the actual longer stay. Record the expected treatment by charge and day. Test an initially short booking extended past the boundary and a long booking curtailed before it. If the treatment is unresolved, deliver the decision questions and test plan rather than recommending a production change.

## 5. Map the decision to OPERA mechanisms

Oracle's 26.2 guide documents generate rules at transaction-code, subgroup or group level; the Generates panel is unavailable for Payment and Wrapper groups. It describes percentage calculations, tax-type rules, predefined UDF functions, advanced day/adjustment handling, and Calculate Posting [S5]. These capabilities do not establish that a particular UDF or day threshold implements Australian law.

Use this implementation worksheet after finance approves the treatment:

| Area | Proposed validation work |
| --- | --- |
| Transaction codes | Inventory room revenue, package elements, other charges, GST and adjustment codes; record applicable inherited rules |
| Inclusive/exclusive basis | Inspect the actual rule and price basis; compare a controlled posting with the A$110 example where applicable |
| Tax types | Confirm the active control and authorised selection process; verify each relevant type with approved cases |
| UDF or advanced handling | Obtain the release-specific country documentation and exact supported function before prescribing parameters |
| Comp/routed charges | Test guest, company and comp windows separately; do not infer tax removal from a window transfer |
| Packages and interfaces | Trace allocation and incoming gross/net amounts; check whether POS or another system already calculated GST |
| Folio and export | Reconcile source charges, generated tax, displayed totals and ledger mapping using matching transaction IDs |

In 26.2, Calculate Posting is documented under the selected transaction entity's Generates actions [S5]. It is a useful preliminary calculation check, but cannot replace posting, end-of-day, folio and export tests. This guide has not run it in a tenant.

## 6. Acceptance-test matrix

The expected result must be approved before execution. Use a non-production property and fictional profiles. Retain sanitised evidence and the tested release/configuration revision.

| Case | Evidence and acceptance criterion |
| --- | --- |
| Standard taxable room charge | Under the stated example assumptions, A$110 inclusive splits into A$100 revenue and A$10 GST across posting, folio and export |
| Recipient boundary | Test A$999.99, A$1,000.00 and A$1,000.01 invoice totals; confirm approved recipient-identification behavior |
| Several charges/rounding | Test multiple small amounts, discounts and package components; reconcile the approved rounding method |
| Long stay | Test 27/28/29 days and extension/early departure against the approved day-by-day treatment |
| Deposit and settlement | Trace receipt, application and final invoice; finance determines tax timing and classification, not this guide |
| Refund/adjustment | Verify reference to the original transaction, approved tax reversal and matching accounting output |
| Routing and comp window | Verify moving or splitting charges does not unintentionally duplicate or remove tax; inspect each resulting folio |
| Interface posting | Compare a synthetic source transaction with its OPERA posting; no double tax calculation or duplicate receipt |
| End of day/export | Reconcile revenue and tax totals before and after end of day, including approved long-stay adjustments |

Before production, capture the configuration baseline, obtain the property's change approval, and agree verification and recovery steps. Never blindly replay financial transactions to repair a discrepancy.

## 7. Suggested answer structure for an Australian request

Lead with what the hotel is trying to achieve: for example, "Prepare an Australian GST configuration and testing plan for a new property." Do not label an implementation request as an incident.

Return:

1. The requested outcome, deployed release and confirmed assumptions.
2. Documented facts with source dates and retrieval limitations.
3. The configuration mapping and synthetic expected results.
4. The acceptance tests and evidence the team should retain.
5. Open decisions, responsible owners and next action.

If asked for an exact Australian comp-tax control or UDF, explicitly state that the country guide has not been validated here. Request the applicable authorised documentation or ask the administrator to verify it; do not fabricate instructions. Do not request private guest data or redistribute restricted support content.

## Sources and review record

- **[S1] [ATO: Tax invoices](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/tax-invoices).** Selected indexed extracts reviewed 2026-10-19; direct retrieval returned 403. Verify complete current requirements.
- **[S2] [ATO: Commercial residential property](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/property/gst-and-commercial-property/commercial-residential-property)** and [Commercial residential premises and GST](https://www.ato.gov.au/businesses-and-organisations/assets-and-property/property/property-used-in-running-a-business/commercial-residential-premises-and-gst). Selected indexed extracts reviewed 2026-10-19; first page's direct retrieval returned 403. No full review of concessions or elections.
- **[S3] [ATO: GSTB 2001/2](https://www.ato.gov.au/law/view/print?DocID=GSB%2FGSTB20012%2FNAT%2FATO%2F00001&PiT=99991231235958).** Selected indexed extract reviewed 2026-10-19; direct retrieval returned 403. Confirm current status and complete conditions.
- **[S4] [GST Act section 29-70, ATO legal database](https://www.ato.gov.au/law/view/document?LocID=%22PAC%2F19990055%2F29-70%282%29%22).** Indexed extract reviewed 2026-10-15 in the preceding guide; complete law not revalidated in this update.
- **[S5] [Oracle OPERA Cloud 26.2: Configuring Generates](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.2/ocsuh/t_admin_financial_transaction_management_configuring_generates.htm).** Public page read 2026-10-19; no tenant validation. This source version is deliberate and is not a claim about the latest release.

For broader country research and publication boundaries, see [maintenance sources](maintenance-sources-and-backlog.md). Recheck authority and product documentation whenever tax treatment, release or property configuration changes.
