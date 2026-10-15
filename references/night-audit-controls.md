# Night Audit and OPERA Controls

This guide describes common concepts only. Night-audit stages, dependencies, controls, reports,
and automation vary by OPERA product, release, property configuration, and business process.
Verify the property's configured procedure before taking action.

## Night audit / end of day

Night audit/end of day is a configured operational process that may close the business date,
process postings, and produce reports or exports. Its steps and effects depend on the property's
configuration and must be checked in the product documentation and runbook.

### What night audit does (typical sequence)

- Executes the configured end-of-day stages and prerequisite checks.
- May post configured charges, process reservations, advance the business date, or run reports and
  exports, depending on the property's setup.
- Must be monitored using the documented status and logs for the running release.

### Business date versus system date

- The business date is an operational date used by the PMS; its advancement is controlled by the
  configured end-of-day process.
- The system date/time is the real clock.
- These can differ. Do not equate the wall clock date with a property's business date or infer
  which date an API/report uses; check the relevant operation and property configuration.

### Integration implications

- Many exports and Business Events fire around night audit. A consumer that expects a daily file or
  a burst of events should align to the property's audit timing.
- Do not assume midnight equals the business-date rollover; confirm the property's audit schedule.

## OPERA Controls (configuration flags)

OPERA Controls are product configuration options that can influence available functions and
behavior. Names, scope, dependencies, and effects are release-specific.

### Concepts

- Controls are organised by functional group (for example reservations, cashiering, blocks, rate
  management, front desk, profiles, and so on).
- A control can be a simple on/off parameter, a setting with a value, or a function that unlocks a
  whole capability.
- Changing a control can change system behaviour broadly; treat control changes like any other
  production change (build/verify in UAT, approve, then apply).
- Control scope can differ by setting and product. Verify whether a particular setting applies at
  property, enterprise, or another level.

### Working with controls

- Before troubleshooting "OPERA will not let me do X", check whether a control governs X and how it
  is set for that property.
- When documentation says a feature requires a control, that control must be active for the API or
  UI behaviour to appear.
- Record control changes: they are easy to make and easy to forget, and they explain behaviour that
  otherwise looks like a bug.

### Verifying a control's exact name and effect

OPERA Control names and their grouping change across releases and are extensive. Do not guess a
control's exact name. Confirm it against the OPERA Controls documentation for the running release,
and state when an answer depends on a control being set a particular way.

## Authoritative reference

- [OPERA Cloud Services documentation](https://docs.oracle.com/en/industries/hospitality/hotels.html)
