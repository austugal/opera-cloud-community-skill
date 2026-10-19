# United Kingdom: visitor-levy discovery and source boundary

Use for UK OPERA Cloud fiscal research, including Scottish visitor-levy questions. Establish the
property's jurisdiction, municipality, deployed OPERA release, relevant dates and approved levy
requirements before selecting a package or charge configuration.

## What was actually available

The supplied Oracle UK guide is DOC3023, portal version 17, published 2026-09-30. Its three-page
print has the OPERA Cloud content collapsed. The visible revision history identifies Edinburgh
visitor-levy/city-tax coverage, a Glasgow addition and an update to CITY_TAX parameters. It does
**not** expose their configuration instructions, formulas or eligibility rules.

Consequently this skill includes UK discovery and source routing, not a verified Edinburgh or
Glasgow implementation recipe. Never reconstruct the missing content from the revision titles,
copy a German CITY_TAX configuration into Scotland, or invent rates and commencement dates.

## Discovery workflow (original)

1. Obtain the expanded current Oracle UK reference for the relevant city and deployed release.
2. Record the applicable scheme's booking/stay dates, taxable base, cap, exemptions and treatment
   of packages. Keep legal assumptions separate from Oracle's configurable fields.
3. Determine the supported OPERA mechanism from the expanded source: function, control,
   prerequisites and necessary roles. Verify rather than assuming CITY_TAX has identical parameters
   across releases or countries.
4. Build synthetic cases for an ordinary stay, exempt stay, included package, discounted rate,
   changed booking, cancellation and a stay crossing an effective-date or maximum-night boundary.
5. Compare expected levy, rate preview, postings, invoice and reporting totals. Record discrepancies
   and resolve them with the applicable Oracle documentation before production configuration.

Source locator: [Oracle UK fiscal reference guide](https://iccp.custhelp.com/app/answers/answer_view/a_id/1003322)
(access may require an Oracle entitlement). An expanded print/export is needed to extend this
reference to precise Edinburgh/Glasgow configuration. Do not describe this limited coverage as
full UK fiscal compliance or a complete implementation guide.

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
