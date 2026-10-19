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

The original catalog review did not establish detailed deployment requirements. The selected
public documentation additions below extend that review; unreviewed settings and interface
specifications still require verification for the exact deployment.

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

## Public configuration and integration guidance (reviewed 2026-10-19)

The public [Hotel Property Interface 8.17 configuration guide](https://docs.oracle.com/en/industries/hospitality/hotel-property/8.17/ifccg/G55568_05.pdf)
identifies itself as release **8.17.1.0, September 2026**. Its opening configuration section documents:

- A separate IFC8 instance for each connection to a property vendor system.
- A startup-selected configuration file; first startup creates the initial configuration.
- Separate paths for a new interface and migration using an existing 8.13.x/8.14.x-or-later configuration.
- OPERA Cloud, hosted/on-premises OPERA V5, and legacy Suite8 as PMS choices.
- For this release's new-interface setup, .NET 10.x Desktop Runtime **x86**.

These selected requirements are not a complete installation procedure or a compatibility certification
for any vendor. Do not apply them to older IFC8 releases without checking their guide.

Oracle's [Property Interfaces overview](https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/c_property_interfaces.htm)
separates legacy FIAS/XML-POS messaging from the REST migration options. Legacy vendor connections
can exchange messages over synchronous TCP/IP or serial links. REST migration can involve inbound
OHIP operations, outbound streaming events, and separate synchronous outbound connections for
request/response operations such as key creation. Do not replace every legacy operation with a
streaming subscription or assume complete functional parity.

Use Oracle's operation-mapping table as a starting point, then verify the current API specification,
release and vendor support. The overview's room-number-only posting limitation and its simple-posting
mapping require careful interpretation; the table alone is not proof that a requested identifier or
payload is supported. Never invent a reservation identifier or retry a posting without reconciliation.
