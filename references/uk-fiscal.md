# United Kingdom: Edinburgh and Glasgow visitor-levy configuration research

## Source and release scope

Reviewed 2026-10-19 from the expanded user-supplied Oracle UK guide, DOC3023, portal version 17,
published 2026-09-30. The new Markdown contains the sections missing from the earlier collapsed
PDF: Glasgow, Edinburgh and a staged long-stay tax generate. This supersedes the discovery-only
limitation. Document version 17 is not an OPERA release.

This is an original summary and test workflow, not the raw support guide. Guide-based settings
below are conditional on its example configuration; verify the installed release and property's
approved requirements. No screenshots, signed asset links or sample guest records are included.

## Keep the two cities distinct

| Setting in the supplied Oracle examples | Edinburgh | Glasgow |
|---|---|---|
| Country mode | GB | GB |
| Package formula | CITY_TAX | CITY_TAX |
| Illustrative percentage | 5 | 5 |
| Room Net Gross | GROSS, for the stated VAT-inclusive setup | GROSS, for the stated VAT-inclusive setup |
| Maximum nights | 5 | No maximum configured in the guide's example |
| Stay-date start | 24 July 2026 | 25 January 2027 |
| Discounted amount | Y | Y |
| Exemption mechanism | Taxable/default and exempt Purpose of Stay codes | Taxable/default and exempt Purpose of Stay codes |

The examples assume room revenue includes 20% VAT and has no service charge; the levy transaction
is also modelled with 20% VAT inclusive. Do not copy GROSS or that tax treatment to a property with
different taxation, non-taxable accommodation, service charges or package composition without
reconciling the tax base. The levy is accommodation-based, not automatically multiplied by occupants.

## Guide-based configuration workflow

1. Confirm property country mode, roles, existing room-revenue transaction and tax generates.
2. Configure the levy transaction and its tax treatment for the approved scenario.
3. Configure a taxable Purpose of Stay and, where needed, a separate exempt code. Select the
   taxable default in Cashiering's Purpose of Stay for City Tax Calculation setting. A blank
   reservation purpose can therefore still produce a levy; do not use blank as an exemption.
4. Assign the exempt purpose explicitly to qualifying reservations. If Purpose of Stay is absent
   from Stay Details, check customization and access before concluding the feature is unavailable.
5. Configure CITY_TAX with the matching taxable-purpose code, calculation base, percentage,
   discounted-amount behaviour, start date and city-specific night limit. Do not confuse the
   property date display with a literal date string copied from a screenshot.
6. Include only eligible lodging packages in Packages To Include. Separate accommodation items
   from breakfast, parking and other extras. Check exact entry syntax against the actual UI.
7. Attach the levy package to the required rates. The Edinburgh guide discusses Rate Code
   Packages and Rate Schedules and notes the Rate Schedule restriction for Daily Rates.
8. For an Add to Rate Separate Line package, review Show Add Separate Line Packages to Rates in
   the LTB so the displayed price can include the levy. Reconcile Look to Book, reservation Rate
   Info, actual postings and folio presentation; price preview alone is insufficient.

## Public Oracle release verification: two independent date checks

[OPERA Cloud 26.2 readiness](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.2/oprnc/c_feature_summary.htm)
documents CITY_TAX Start Date and End Date based on stay dates. A stay beginning earlier can
therefore contain both untaxed and taxed nights.

[OPERA Cloud 26.4 readiness](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm)
adds Calculate for Reservations Created From. It uses the property's original reservation-creation
business date. Look to Book uses the current property business date before creation; block-created
reservations use their actual creation date, while split reservations use the main reservation's
creation date. Check installed-release availability before relying on this parameter.

A stay-date start does not by itself filter older bookings. Nor does a reservation creation-date
filter establish payment timing, entitlement to exemption or the full legal booking history.

## Scheme dates: authority cross-check, separate from Oracle product behaviour

The [Edinburgh council overview](https://www.edinburgh.gov.uk/business/visitor-levy-edinburgh)
and [implementation timeline](https://www.edinburgh.gov.uk/business/timeline-implementing-levy)
confirm a 5% accommodation charge before VAT, excluding extras, limited to the first five nights,
for stays from 24 July 2026. The timeline identifies the 1 October 2025 booking threshold and the
exclusion for qualifying bookings paid partly or fully before it. Verify the current detailed
scheme for amendments, refunds and exemptions; Oracle date fields do not prove legal eligibility.

The [Glasgow council timeline](https://www.glasgow.gov.uk/article/14802/Timeline) identifies
25 January 2027 for commencement and 1 April 2026 for advance bookings. Keep this separate from
Edinburgh's dates and cap. Council sources verify scheme context, not OPERA configuration.

## Staged long-stay generate in the supplied guide

The guide also describes UDF_TAX_FUNC for transaction-code generates. Its documented inputs are
OPERATION_NAME, BASE and RESV_NAME_ID, followed by in_tax1_nights, in_tax1_percent and
in_tax2_percent. The first three are system-supplied in the guide; the remaining inputs select
an initial number of nights and the percentages for that period and the remaining nights.

This is a distinct staged-tax example, not the CITY_TAX visitor-levy package. The guide's
27-night, 10%/5.5% demonstration is not a statement of current UK VAT law. Verify function
availability and tax requirements before configuration. Test the boundary night and advance
bill against Rate Info; do not invent production transaction codes from the example.

## Source-quality findings and acceptance tests

The Glasgow examples 2 and 3 contain inconsistent room-net/VAT figures for a GBP 200 gross
room amount. Do not repeat them as validated arithmetic. Independently, at the example's 20%
VAT-inclusive assumption, GBP 200 / 1.20 is GBP 166.666..., with VAT GBP 33.333...; those values
round to GBP 166.67 and GBP 33.33. Validate actual OPERA line-level rounding separately.

Use synthetic cases and record expected versus observed results:

| Test | Evidence needed |
|---|---|
| Ordinary eligible stay | Correct base, levy, VAT, ledger and folio totals |
| Explicit exemption versus blank purpose | Exempt reservation excluded; default behaviour verified |
| Before/on booking threshold | Correct creation-date treatment and separate payment/history assessment |
| Stay crossing commencement | Only eligible stay nights charged |
| Edinburgh six-night stay | Five-night cap verified; test crossing-date counting separately |
| Glasgow stay longer than five nights | No accidental Edinburgh cap inherited |
| Included breakfast and extra bed | Non-accommodation excluded; eligible lodging inclusion verified |
| Discount and rate change | Correct discounted base each night |
| Block and split reservations | Correct 26.4 creation-date semantics |
| Staged long-stay generate | Boundary and subsequent percentage verified separately from levy |
| Adjustment/cancellation | Reconciled reversal, folio and reporting result without duplicate charges |

[Oracle UK fiscal reference guide](https://iccp.custhelp.com/app/answers/answer_view/a_id/1003322)
may require an Oracle entitlement. Use it for exact supported configuration and current Oracle
clarifications. This reference does not claim live-property testing or legal certification.
