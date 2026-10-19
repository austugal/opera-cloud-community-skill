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

## Verified 26.4 detail: date rollover, income audit and automation

Reviewed 2026-10-19. The following additions are scoped to public Oracle OPERA Cloud 26.4 documentation. They supplement the general concepts above; they are not an executed hotel runbook.

### Date advancement does not mean all procedures have finished

The Update Business Date procedure advances the date while later End of Day procedures can continue processing room/package charges, ledgers, statistics, exports and reports for the preceding operating date [E1].

Oracle distinguishes automatic execution from ordinary manual processing. Automatic End of Day can halt on unresolved departures, open folios, scheduled room moves or arrivals with deposit balances, with behavior depending on the documented controls. Automatic processing marks arrivals as no-shows and closes cashiers even where the corresponding ordinary-process controls would not do so. Do not treat scheduled execution as a promise that every exception is resolved without intervention [E1].

### Income Audit and finalized exports

With Income Audit active, an earlier business date can remain open after advancement, allowing guest-ledger charges and adjustments for in-house reservations. Interim procedures/reports run and the routine pauses with that date open. Completing the audit runs final procedures and reports and closes the date. Dates must be finalized chronologically [E2].

Oracle places Back Office Export and other procedures requiring finalized revenue in the final procedure list. An advanced date or interim report is therefore not evidence that final-revenue exports have completed. An income-audit cashier must be configured [E2].

### Automatic scheduling, notification and recovery limits

Oracle documents Financials > End of Day > Manage End of Day Scheduler. A schedule has a property, start date/time and optional end date; an omitted end date defaults to ten years later [E3].

The scheduler sends start, completion and intervention-error notifications to the recipients configured in Automatic End of Day Email. It retries resumption after five minutes, up to three attempts; after the threshold it stops and sends instructions for manual execution. This is a scheduler-specific rule, not an OHIP retry policy [E3].

The scheduler also supports skipping the current business date for manual processing, viewing schedule details, and opening its Changes Log [E3]. This reference does not execute, skip or reschedule any financial process.

### Control distinctions and a documentation ambiguity

Automatic End of Day enables scheduled execution. Auto Continue advances between procedures without a confirmation pause. These are separate controls [E4].

Automatic End of Day Email identifies automatic-process notification recipients; End of Day Email Address concerns emailed reports and completion email [E4]. No actual addresses belong in this reference.

The 26.4 controls page says Income Audit allows five open dates, while separately listing Maximum Number of Open Business Dates with values 1–365. The reviewed text does not reconcile those statements. Do not assert either as a universal effective limit: verify the applicable control interaction with Oracle for the deployed release [E4].

### Oracle sources for the additions

- **[E1] [About End of Day](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/c_endofday_procedures.htm)** — sequence, business date and automatic-process behavior.
- **[E2] [Income Audit](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/c_endofday_income_audit.htm)** — interim/final procedures, exports and chronological closure.
- **[E3] [Managing Automatic End of Day Schedules](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/t_managing_automatic_end_of_day_schedule.htm)** — schedule, notifications, retries and log access.
- **[E4] [OPERA Controls — End of Day](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/c_opera_controls_end_of_day.htm)** — exact controls and the unresolved open-date limit wording.

These public sources were read; no tenant, scheduled job, financial posting, notification delivery or export run was tested.
