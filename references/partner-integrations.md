# Partner integrations and vendor claims

Reviewed 2026-10-15. The Prologic First page metadata reports a last-modified date of 2026-07-15. This is a source-tracking aid, not an Oracle certification or compatibility matrix. Vendor-published integration lists describe the vendor's claims; verify the exact product, version, interface, and deployment with both vendors before designing or changing an integration.

## Prologic First

“Prologic” is not a sufficient product identifier. Prologic First's public product pages distinguish **Web Prol'IFIC ERP** from its **WISH PMS**. Its [Technology Integration Partners](https://prologicfirst.com/integration-partners/) page lists “Opera (PMS)” and “Opera (PMS (Sun Standard))” under Web Prol'IFIC, and “Opera (PMS)” under Touché.

**Evidence: vendor-published partner listing.** The page does not identify the OPERA product generation or release, interface or protocol, data direction, supported objects, availability by region, or whether an entry means OPERA Cloud, OPERA 5, OHIP, or another interface. The listing alone does not establish Oracle certification or current support. Do not infer these details from “Opera (PMS).”

The vendor's linked Web Prol'IFIC and WISH public pages are product overviews, not technical
integration specifications. The sources reviewed here do not establish a connector's technical
contract or compatibility. Treat those details as unknown unless Prologic First and Oracle provide
current technical confirmation for the proposed products and versions.

Oracle's OPERA Cloud Services 26.4 Feature Summary separately lists an OPERA Cloud Central capability titled [“OPERA Cloud Central added with Third-Party PMS Integration capability”](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm#c_34697_opera_cloud_central_added_with_third_party_pms_integration_capability), marked for Central. That entry does not name Prologic First or establish that its listed “Opera (PMS)” connection uses this capability.

The source confirms that Prologic First publicly lists OPERA-related integrations for named products, but is not a technical integration specification. For a deployment, ask Prologic First and Oracle to confirm in writing:

- Exact Prologic First product, edition, deployment, and version, and exact OPERA product, release, property, and enabled modules.
- Whether the proposed connection is supported for those versions; the interface/API or certified connector name; and the responsible support parties.
- Data flow direction, objects and fields, event timing (real-time, event-driven, polling, or batch), conflict handling, retries, idempotency, and reconciliation.
- Authentication, role and property scope, network requirements, personal/payment-data handling, logging, retention, test plan, and production change approval.

Until these are confirmed from current vendor and Oracle technical sources, treat the method and compatibility as **unknown**. Do not describe the vendor page as proof of OHIP support.

## Primary vendor sources

- [Prologic First: Technology Integration Partners](https://prologicfirst.com/integration-partners/)
- [Prologic First: Web Prol'IFIC ERP](https://prologicfirst.com/hotelsoftware/hotel-back-office-software/)
- [Prologic First: WISH PMS](https://prologicfirst.com/hotelsoftware/hotel-front-office-software/)
- [OPERA Cloud Services 26.4 Feature Summary](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm)
