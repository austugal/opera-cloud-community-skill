# Architecture, Environments, and Authentication

This is a conceptual overview. Tenant architecture, environment names, product access, and
authentication details vary by integration and release. Oracle's Help Center listed OPERA Cloud
Services 26.4 as the newest release on 2026-10-15. The OHIP documentation was last recorded at
26.3 on 2026-10-13. Verify against the release actually deployed.

## OPERA Cloud architecture

OPERA Cloud is Oracle Hospitality's cloud property-management service. It provides hotel
operational functions, while supported integration capabilities are exposed through products such
as the Oracle Hospitality Integration Platform (OHIP). This is a high-level mental model, not a
deployment or network diagram.

- **User experience:** browser and supported mobile experiences.
- **PMS application:** property operations such as reservations, profiles, cashiering, rooms,
  housekeeping, rates, inventory, blocks, events, and end of day.
- **Integration:** documented OHIP APIs, asynchronous operations, events/streaming, and separate
  distribution or interface products as applicable.
- **Data:** hotel and enterprise data managed within Oracle's service.

Use Oracle-supported interfaces for the product and use case. Do not infer that every device,
payment system, channel, or external application connects directly through OHIP.

## Environments and change control

Customers may have production and non-production environments, but their topology, names, data
refreshes, access, and release alignment are customer-specific. Confirm which environment is in
scope before troubleshooting or making changes.

Use a representative non-production environment for testing when available. Follow the customer's
change-control, approval, backup, and rollback processes before making production changes. Do not
assume a configuration shell export/import or property refresh is required or available; follow
the applicable product and release documentation.

## OHIP: the integration platform

OHIP provides documented integration capabilities, including REST APIs and event-related
functionality. API module availability, security configuration, portals, and event delivery
options depend on the integration and release. Use:

- `api-modules.md` for the conceptual API map.
- `async-streaming-events.md` for asynchronous work and event delivery.
- `distribution-channels.md` for distribution concepts.

Partner/integration and customer administration experiences may have different access and
responsibilities. Use current OHIP documentation and the features available to the account rather
than relying on historical portal labels.

## OHIP onboarding, portal roles and environments (OCIM)

Reviewed 2026-10-17 against the OHIP User Guide (pages marked `Test Release`, publisher months July
to October 2026). Re-check before relying on a detail for a dated commitment.

**Documented prerequisites.** A hotel needs an OPERA Cloud Foundation SKU ("OHIP is not available
for hotels using a legacy OPERA Cloud SKU"), its chain onboarded with OHIP, and chain and properties
on Oracle Cloud Infrastructure, not a legacy data center. Partner subscriptions follow the OCI Cloud
Account Activation process: provisioning does not begin until the "Action Required: Welcome to New
Oracle Cloud Service Subscription(s)" email is actioned.
([Quick Start for Hoteliers](https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_quick_start_for_hoteliers_uat_ocim.htm),
[Getting Started for Partners](https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_getting_started_for_partners.htm))

**Documented portal roles.** OHIPADMIN, OHIPDEVELOPER, OHIPANALYTICS, OHIPENVIRONMENTS, OHIPVIEW and
DEVELOPERPORTALACCESS (marked for future deprecation). Only chain-level users can hold them, and
"Developer Portal users do not have the ability to call APIs." OHIPADMIN, OHIPENVIRONMENTS and
DEVELOPERPORTALACCESS can approve partner connections and streaming applications.
([Assigning Roles to Users](https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_assigning_roles_to_users_ocim.htm))

**Documented environment model.** One environment is one chain in one OPERA environment and one
clientId. Only partners and customers with OPERA Cloud Central can add an environment; the partner
supplies the customer's Enterprise ID and chain code and the customer approves. Re-adding a removed
environment needs the same Enterprise ID and chain code. The first hotel call needs a specific hotel
ID, not the chain ID.
([Environments (OCIM)](https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_environments_gateways_and_credentials.htm),
[Adding an Environment](https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_adding_an_environment.htm))

**Documented credential behaviour.** On OCIM a client secret is viewable only when issued; a lost
secret means issuing a new one and updating every integration on that client. Reissuing a legacy
GUID clientId to the human-readable format introduced in OHIP Portal 25.3.1 also issues a new secret,
and the old pair stops working. Customers can create several clients per environment; partners have
one per customer environment.
([Issuing the Client Secret](https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_issuing_the_client_secret_ocim.htm),
[Managing Client Applications](https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_managing_client_applications_customers_only_ocim.htm))

**Documented controls.** With IP Allow Listing enabled, partner calls from unlisted ranges are
declined with HTTP 403. Partner sandbox hotel IDs: `SAND01` for the SSD sandbox, `OHIPSB02` for the
OCIM sandbox. Shared sandboxes can generate Business Events from other partners' activity.
([Viewing Environment Details](https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_viewing_environment_details.htm),
[Quick Start for Partners (Sandbox)](https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_quick_start_for_partners_using_the_partner_sandbox.htm))

**Author guidance.** Treat secret issue, clientId reissue, environment removal and enabling IP Allow
Listing as change-window events: list every consumer of the client first.

## Authentication

Use the grant, endpoint, scope, and credentials assigned for the particular integration. Oracle's
public [OHIP OAuth specification](https://github.com/oracle/hospitality-api-docs/blob/4bd129b455bc5e3ab0f900ac47983611e58659b4/rest-api-specs/security/v1/publishedoauth.json)
identifies itself as version 26.2.0.0. This pinned public source was reviewed on 2026-10-15; it
documents this token-request shape:

- `POST /oauth/v1/tokens` with `application/x-www-form-urlencoded` fields.
- HTTP Basic authentication with the Client ID and Client Secret, plus the required `x-app-key`
  header.
- `grant_type=password` with an OPERA Cloud integration username and password, or
  `grant_type=client_credentials` with an assigned `scope`.
- An optional `enterpriseId` header only for client-credentials use with OCIM environments.
- A JSON token response containing `access_token`, `token_type`, and `expires_in`. The
  specification describes `token_type` as the type of access token issued (`Bearer`) and says
  `expires_in` is typically 3600 seconds.

This is the contract in that published 26.2 specification, not proof that every tenant or
integration uses both grants or the same token configuration. The current public specification's
version does not establish the deployed OPERA Cloud or OHIP release. Confirm the applicable grant,
token URL, scope, audience, required headers, and credential provisioning in the integration's
current OHIP instructions and tenant documentation before implementation.

Conceptual flow:

1. Register the integration and obtain the credential material and application key required by its
   current configuration.
2. Request an access token using the documented grant and token endpoint.
3. Send the token and all required application/property context on API requests as specified by
   each API.
4. Protect, rotate, and revoke credentials using the customer-approved secret-management process.

The authorization header carries a bearer token when required by the API contract. Required
headers, property context identifiers, content types, and authentication behavior are
endpoint- and version-specific. Use the matching API specification. Never put real credentials in
examples, tickets, source control, or logs.

### Token handling

- Cache and reuse tokens according to the documented expiry and security policy; avoid requesting
  a new token for every API operation unless the integration requires it.
- Refresh only according to the documented token lifecycle.
- On an authorization failure, check token validity, audience, client configuration, clock
  handling, and entitlements. Retry only if the cause is understood and the operation is safe to
  repeat.
- Keep client secrets in an approved secret store; do not log tokens or full authorization headers.

## Security ground rules

- Request only the APIs, properties, and data needed.
- Treat guest profiles, reservation information, and folios as sensitive personal or financial
  data. Follow applicable retention, access, and privacy requirements.
- Rotate credentials according to policy and promptly revoke exposed credentials.
- Distinguish an authenticated request from one authorized for a particular operation/property.

## Authoritative references

- [Oracle Hospitality OPERA Cloud Services documentation](https://docs.oracle.com/en/industries/hospitality/hotels.html)
- [Oracle Hospitality Integration Platform documentation](https://docs.oracle.com/en/industries/hospitality/integration-platform/)
- [Oracle Hospitality APIs: published OHIP OAuth specification (v26.2.0.0)](https://github.com/oracle/hospitality-api-docs/blob/4bd129b455bc5e3ab0f900ac47983611e58659b4/rest-api-specs/security/v1/publishedoauth.json)

A customer's tenant may run an older version or a different configuration from the newest
published release.
