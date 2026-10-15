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
