# OXI XML sample discovery and safe evaluation

This guide points to an independent public example library; it does not add XML payloads to this
repository. OXI (OPERA Exchange Interface) message XML is a legacy, interface- and version-specific
integration format. Do not assume an example is compatible with a particular OXI deployment or
an Oracle-published or Oracle-validated example.

## Independent sample library

[Aperture's XML Samples library](https://aperture-operacloud.pages.dev/xml-library.html) describes
16 downloadable examples in the `profile.fidelio.4.0` namespace. The page groups them as:

- **Profiles:** individual/guest, company, travel agent, group, source, contact, negotiated rate,
  activity, and relationship examples.
- **Blocks and reservations:** a new reservation, block request and response, and a stay message.
- **Messages and legacy:** a message-request envelope, profile resync request, and an OPERA 5-era
  profile.

These categories and the namespace are claims shown on the linked site, not Oracle documentation or
an Oracle endorsement. The site describes its examples as anonymized and illustrative, but those
anonymization and compatibility claims have not been independently validated in this repository.
The page checked here does not establish a reusable license: "free to download" is not permission
to redistribute or adapt. Review the site's current terms and license before reuse. This skill links
to the library only; no sample files or copied XML payloads are bundled here.

## Related OPERA Cloud practice site

[OC Practice](https://opera-cloud-practice.pages.dev/) redirected unauthenticated visitors to an
access page when checked on 2026-10-15. The page advertises a reference library, Copilot, PIW
Builder, SAF-T Validator, and IFC8 guides. These are publisher descriptions, not independently
verified product capabilities or Oracle documentation. The IFC8 material is a research lead only;
no setup claims are repeated here without confirmation in applicable primary Oracle documentation.

The site's materials are reported as CC BY-NC-SA. The public access page does not expose terms that
let this repository independently verify the license or its scope. In any event, that license is
not authorization to import or relicense third-party XML as part of this MIT-licensed skill, and a
license does not establish Oracle compatibility. No XML payloads are copied or bundled here.

## Keep XML formats distinct

- **OXI messages** are XML for a specific legacy OPERA Exchange Interface integration. Confirm the
  exact interface, version, message type, direction, schema, and property configuration.
- **OHIP** is Oracle's documented REST integration surface. Use the endpoint's current contract and
  its specified request/response format (commonly JSON); an OXI XML example is not an OHIP payload.
- **BI Publisher stationery XML** is a sample data model for designing or previewing an RTF
  stationery layout, not an OXI message or fiscal submission. See
  [`references/bi-publisher-stationery-xml.md`](../references/bi-publisher-stationery-xml.md).
- **Fiscal XML exports** are jurisdiction-, product-, and version-specific outputs. They are not
  OXI messages or BI Publisher stationery data. Start with
  [`references/fiscal-compliance.md`](../references/fiscal-compliance.md) and the relevant country
  guidance.

For the general interface boundaries, see
[`references/interfaces-ifc8.md`](../references/interfaces-ifc8.md). For API architecture, see
[`references/architecture-and-auth.md`](../references/architecture-and-auth.md) and
[`references/api-modules.md`](../references/api-modules.md).

## Safe evaluation workflow

1. **Check provenance and rights.** Read the source page, its current terms, and any license
   attached to the actual file. Do not redistribute or adapt files without permission.
2. **Inspect before use.** Review the full XML locally for real guest names, addresses, contact
   details, account identifiers, payment data, credentials, or property-specific values. Do not
   assume data is anonymized because the source says so.
3. **Match the contract.** Identify the exact OPERA product, licensed OXI/interface version, message
   direction and type, and applicable schema/documentation. Validate structure and required fields
   against those sources; do not infer support from a plausible-looking example.
4. **Test safely.** Replace values with synthetic data and test only in an authorized non-production
   UAT environment for the matching interface. Verify mappings, acknowledgements/rejections,
   retries, duplicate handling, and resulting data with the integration owner.
5. **Stop before production.** Never post a sample or unverified message to production. Require
   customer approval, a reviewed change plan, and the normal release controls for any later
   production deployment.

## Requesting useful examples

When requesting or evaluating an example, record the OPERA product and release, OXI/interface
version, message name and direction, schema or Oracle/vendor documentation, whether the source
license permits the intended use, and the synthetic UAT checks still needed. Never send real
guest, reservation, payment, credential, or property data in a sample request.
