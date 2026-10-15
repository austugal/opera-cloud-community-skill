# Back-Office Financial (Ledger) Exports and the Formula Engine

OPERA Cloud produces financial exports that feed back-office / general-ledger systems (for example
SunSystems and other finance platforms). This file covers the generic structure and the formula
engine constraints. It contains no client-specific mappings or credentials.

**Important:** export configuration, available formulas, paths, signs, and field mappings depend
on the product release, export definition, accounting policy, and receiver specification. This guide
is not a universal OPERA formula-language reference. Verify each function and output requirement
in the applicable Oracle documentation and the target system's specification before use.

## What a back-office export is

A back-office export takes OPERA financial data and writes a file in a configured structure for a
finance system. Locate and configure it using the menu and permissions documented for the exact
product and release; do not rely on a generic menu path.

The export defines columns, each populated by a value or a formula, and produces a file per run
(commonly daily, aligned with night audit).

## Typical ledger export column structure

A city-ledger style export usually carries columns along these lines (exact layout is per
configuration and per finance system):

| Column | Typical content | Notes |
|--------|-----------------|-------|
| Journal type | Fixed code identifying the journal | e.g. a city-ledger marker |
| Transaction date | Posting / transaction date | |
| Transaction amount | Signed amount | Credit lines may need special sign handling |
| Indicator field | Document/indicator flag | Distinguishes normal versus credit-note lines |
| Account code | General-ledger account mapping | Maps OPERA transaction code to GL account |
| Cost centre | Property / department code | |
| Description | Transaction description | |
| Amount decimals | Decimal portion of the amount | Formula must keep the sign correct |

## Credit note handling

Credit-note representation and sign conventions are determined by the OPERA export, accounting
policy, and receiving system. Do not convert signs or set a document indicator based on a generic
example; reconcile a known credit note end to end and verify the target specification.

## Formula engine constraints (important)

Formula support is specific to the export feature and release. Do not assume the expression editor
uses SQL, spreadsheet syntax, or a shared formula dialect.

### Supported operators

- Confirm supported arithmetic operators, literals, conditional syntax, and functions in the
  product documentation and editor for the target release.

### Not supported (will cause problems)

- Do not assume `ABS()`, `GREATEST()`, `SIGN()`, or any other function is supported unless the
  applicable formula reference says so. Diagnose rejected expressions from editor validation and
  documented behavior, not an unverified function limitation.

### Absolute-value workaround

Do not use an absolute-value workaround until the target expression language, numeric precision,
null behavior, and accounting sign convention have been verified. Test boundary values and both
positive and negative transactions in a non-production environment.

### Encoding pitfall

If a formula parser reports an unexpected character, inspect the exact characters, quoting, and
encoding in the expression. Do not assume a particular clipboard artifact or empty-string syntax;
use only the literal form documented for that editor.

### Validation reality

- The formula engine validates on save, but a successful save does not prove correct execution.
- Always run a sample export in UAT and inspect the output file against the finance system's
  expected format before promoting.

## UAT to production workflow for exports

1. Follow the customer's approved configuration transport and change-control procedure.
2. Test with representative debit, credit, tax, adjustment, zero, and boundary-value transactions.
3. Validate the generated file against the receiver's documented schema and reconcile totals.
4. Obtain the required finance and operations approvals before production deployment.
5. Preserve a rollback path and verify the first production output using the approved controls.

## Authoritative references

- [OPERA Cloud Services documentation](https://docs.oracle.com/en/industries/hospitality/hotels.html)
- [OHIP documentation index](https://docs.oracle.com/en/industries/hospitality/integration-platform/)

Use the current release documentation for export setup and the receiving finance system's current
format specification for mappings and sign conventions.
