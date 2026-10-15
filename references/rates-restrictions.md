# Rate Plans, Restrictions, and Hurdle Logic

Rates and restrictions depend on enabled functionality, configuration, distribution product, and
release. Use the property's actual effective data and the current product/API documentation; this
overview does not define an exhaustive hierarchy or calculation contract.

## Rate plan structure

A rate plan (rate code) defines what a guest pays and under what conditions. Key attributes:

- Rate code: the identifier.
- Rate detail: amounts by date range, day of week, and occupancy (single, double, extra adult,
  extra child).
- Room types: which room types the rate applies to.
- Market segment and source: classification used for reporting and statistics.
- Packages: bundled elements (for example breakfast) attached to the rate, each with its own
  posting and allocation rules.
- Booking rules: advance booking, minimum/maximum stay, eligibility.
- Derivation: whether the rate stands alone or derives from another rate.

## Derived rates

A derived rate calculates its amount from a base rate rather than holding its own amounts.

- Derivation methods and their calculation rules are configuration- and release-specific.
- Check the derived plan's current setup and calculated result rather than assuming exactly how a
  base-rate change propagates.
- When auditing "why did this rate change", check whether it is derived before looking for a direct
  edit.

## Restrictions

Restrictions control whether and how rooms can be sold for given dates. Common restriction types:

- Open / Close: whether the rate or room type is sellable at all for the date.
- Closed to Arrival (CTA): cannot start a stay on that date.
- Closed to Departure (CTD): cannot end a stay on that date.
- Minimum Length of Stay (MinLOS): a stay touching the date must be at least N nights.
- Maximum Length of Stay (MaxLOS): a stay touching the date must be at most N nights.
- Minimum/Maximum advance booking: how far ahead a booking can or must be made.

Restrictions may be configured at different scopes. The effective sell decision can also depend on
availability, channel rules, eligibility, and other business logic. Inspect the actual request
context and documented precedence rather than assuming a universal combination rule.

## Distribution and channels

Where the configured channel integration publishes rates or restrictions, inspect its mappings,
delivery status, and channel-side interpretation (see `distribution-channels.md`). A discrepancy
may result from configuration, delayed/failed delivery, channel rules, or another part of the
calculation; do not infer a single cause without evidence.

## Hurdle rates (revenue management integration)

A hurdle rate is a revenue-management concept: the minimum rate the system will accept for a date,
below which a booking is not offered, used to protect inventory for higher-value demand. When OPERA
is integrated with a revenue management system:

- A revenue-management integration may exchange pricing or availability decisions with OPERA or a
  distribution service.
- Confirm which component calculates and enforces a hurdle for the actual integration.
- Exact behaviour depends on the revenue management integration and the OPERA/distribution release;
  confirm against the documentation for the versions in use.

## Practical rate troubleshooting

1. Is the rate derived? If so, inspect the base rate.
2. Are restrictions blocking the date (open/close, CTA/CTD, MinLOS/MaxLOS)?
3. Does the rate apply to the room type and occupancy being booked?
4. For a channel discrepancy, is the rate/room mapping correct and has the latest change synced?
5. For a revenue-managed property, is a hurdle suppressing the rate?

## Authoritative references

- [OPERA Cloud Services documentation](https://docs.oracle.com/en/industries/hospitality/hotels.html)
- [OHIP documentation index](https://docs.oracle.com/en/industries/hospitality/integration-platform/)
