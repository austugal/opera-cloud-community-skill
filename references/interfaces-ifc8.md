# Interfaces, IFC8, and OXI

IFC8, OXI, Hotel Property Interface, and OHIP are not interchangeable names. Oracle's public
indexes list these products and documentation separately; an index entry does not establish that
an interface is supported, licensed, or configured in a particular property.

## What Oracle's public documentation lists

Checked 2026-10-15:

- The [Oracle Hotels documentation index](https://docs.oracle.com/en/industries/hospitality/hotels.html)
  lists Hotel Property Interface releases through 8.17. It separately lists **IFC8 Interface
  (FIAS, XML POS)** under OPERA 5 Integrations. That IFC8 entry does not state a release number.
- Oracle's [IFC8 documentation catalog](https://docs.oracle.com/cd/E94145_01/index.html) lists
  an OPERA IFC8 Information and Installation Guide, a FIAS interface specification, and an XML POS
  interface specification. The catalog descriptions were checked; the guide and specification
  contents were not reviewed here.
- The [OPERA Property Management 5.6 documentation catalog](https://docs.oracle.com/cd/E98457_01/)
  includes Oracle's [Hardware Sizing Guide for IFC8](https://docs.oracle.com/cd/E98457_01/docs/F33944.pdf).
  The catalog entry and document title were checked; the guide's sizing requirements were not
  reviewed for this reference.
- Oracle's [OHIP overview](https://www.oracle.com/hospitality/integration-platform/) describes
  shared sandbox API access and says it does not include access to the OPERA Cloud user interface
  or legacy interface methods such as OXI or OWS. This distinction does not establish IFC8
  architecture, compatibility, or deployment requirements.
- Oracle lists [OPERA Exchange Interface](https://docs.oracle.com/cd/E91116_01/index.html)
  separately under OPERA 5 Integrations. Do not infer its release compatibility or behavior from
  the listing alone.

This reference checked Oracle's indexes and catalog descriptions but did not review the IFC8 guide
or interface specification contents. Exact deployment topology and message flow, registration and
credentials, menu paths, endpoint/security requirements, code mappings, diagnostic settings, and
key-handling procedures therefore remain unverified here. They are not presented as Oracle
requirements.

## Safe investigation guidance

The following is author guidance, not an Oracle procedure:

1. Identify the OPERA product and release, named interface, interface version, and external system.
   Confirm each against documentation for that deployment.
2. Use the matching Oracle and vendor specifications, plus the customer's approved configuration
   and support process, to verify any setup or compatibility detail. Do not infer it from a product
   name or another deployment.
3. For a reported fault, record the time, affected scope, exact error, recent changes, and relevant
   sanitized evidence. Do not include credentials, guest data, or other sensitive information.
4. Use an authorized non-production environment for tests. Do not change or restart production
   components without evidence, approval, and a reviewed impact and recovery plan.

For OXI XML sample provenance and format boundaries, see
[`docs/oxi-xml-samples.md`](../docs/oxi-xml-samples.md). For current Oracle release indexes, see
[`references/version-changes.md`](version-changes.md).
