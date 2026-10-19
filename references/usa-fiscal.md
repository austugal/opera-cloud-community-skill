# United States: state and city tax configuration research

Use for USA OPERA Cloud tax questions, especially Hawaii, Massachusetts and New York City.
Always establish state, city, effective date, deployed release, property country configuration,
transaction codes, packages, tax inclusivity and licensed features. There is no single nationwide
hotel-tax configuration in this reference.

## Guide-based topics

The supplied Oracle USA guide is DOC6541, portal version 18, published 2026-02-05. It contains
three local scenarios, not a complete survey of US jurisdictions.

| Scenario | Documented topic and implementation questions |
|---|---|
| Hawaii | A generate using `gen_tax_udf_full` addresses tax on the full rate amount when a package is present. Establish the rate/package base, other taxes and whether the reservation actually qualifies. Verify the exact function signature in the deployed Oracle guide before configuring it. |
| Massachusetts | Exclusive-tax handling when a main charge is routed to a comp window. Verify the Casino and Gaming add-on, the automatic-transfer prerequisite, the relevant comp control and the intended guest-window tax result. |
| New York City | `ROOM_TYPE_BASED_CHARGE` supports a room-type-based generate. Investigate room groups/amounts, posting days, fallback amount, house-use/pseudo/complimentary treatment and minimum-rate conditions. |

The guide's rates and sample amounts are illustrations. Do not present them as current Hawaii,
Massachusetts or NYC tax rates, and do not generalise these local scenarios to other states.
Recheck function fields against the installed release because later room-type/date-range
capabilities can change the relevant setup.

## Acceptance workflow (original)

1. Document the tax authority-approved rate and effective date separately from Oracle's product example.
2. Hawaii: compare a room-only stay with included and directly attached packages; independently
   reconcile lodging, package allocation and each tax base.
3. Comp routing: test below, equal to and above a routing limit; verify both the routed principal
   and the tax left on the guest window. Do not assume inclusive and exclusive taxes behave alike.
4. Room-type charge: test every configured group, an unmatched room type, posting-day boundary,
   minimum-rate boundary and the intended exclusions. If Room Type to Charge or date ranges are
   used, verify their release-specific behaviour explicitly.
5. Compare the rate preview with posted room-and-tax results, folio totals, adjustment and reversal.
   Treat differences as evidence to investigate, not permission to change the tax law assumptions.

Source locator: [Oracle USA fiscal reference guide](https://iccp.custhelp.com/app/answers/answer_view/a_id/1006848)
(access may require an Oracle entitlement). This reference provides research and test coverage;
it does not bundle the guide's screenshots or prescribe production tax settings.

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
