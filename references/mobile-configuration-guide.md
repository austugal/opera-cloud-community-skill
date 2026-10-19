# OPERA Mobile Applications: Configuration and Support

Mobile features, application names, supported devices, operating systems, and setup depend on the
OPERA product/release, licensing, deployment model, and property configuration. This guide is a
verification checklist, not a compatibility promise or installation manual. Do not rely on old
minimum OS versions, network ports, OAuth setup, offline capabilities, or feature lists without
checking current Oracle documentation.

## Identify the product

First establish whether the property uses an OPERA Cloud mobile experience or an OPERA 5 mobile
product, the exact release, the named app/client, and the intended workflow. Do not apply an OPERA
Cloud setup or integration model to OPERA 5, or assume that a similarly named application has the
same features.

## Verify before deployment

Use the release-specific Oracle user, security, and compatibility documentation to confirm:

- Supported device models, operating-system versions, browser/app versions, and distribution
  channels.
- Required product licenses, property configuration, roles, privileges, and user assignments.
- Authentication method, account provisioning, session policy, and any integration dependencies.
- Network destinations, proxy/certificate requirements, supported connectivity, and data handling.
- Whether offline operation exists, which actions are supported offline, how conflicts are handled,
  and what happens to queued changes.
- Mobile application's privacy, notification, device-management, and audit capabilities.

Do not create OHIP credentials for a mobile application unless the documented product design
specifically requires that integration.

## Security and privacy

- Install only the Oracle-supported app/client through an approved distribution channel.
- Apply the organization's mobile-device management, encryption, screen-lock, patching, and
  lost-device procedures.
- Use individual accounts and least privilege; avoid shared logins.
- Protect guest, reservation, location, and payment data on device and in transit. Never store
  payment credentials or tokens outside the product's approved secure mechanism.
- Define device revocation, session termination, incident reporting, and data-removal procedures.
- Review logs and telemetry for personal data before enabling or exporting them.

## Troubleshooting

1. Record product/release, app version, device/OS, environment, property, user role, time, and exact
   sanitized error.
2. Determine whether the issue affects one user/device, one property, or all users.
3. Check the documented service status, access/role assignments, property configuration, supported
   client versions, and connectivity requirements.
4. Compare with a supported device/network or non-production environment where approved.
5. Capture relevant app/service diagnostics without collecting passwords, tokens, or unnecessary
   guest/payment data.
6. Escalate through the customer's Oracle support or mobile-management process with timestamps,
   correlation IDs, and sanitized evidence.

Do not prescribe a fixed cache age, latency threshold, port, session timeout, or restart without a
documented requirement and evidence for the affected release.

## Official references

- [OPERA Cloud Services documentation](https://docs.oracle.com/en/industries/hospitality/hotels.html)
- [Oracle Hospitality documentation home](https://docs.oracle.com/en/industries/hospitality/)

Select the mobile user guide, security guide, and compatibility information for the exact product
and release in the Oracle Help Center.

## Historical Hotel Mobile documentation boundary

Oracle publicly hosts [Hotel Mobile 1.4 installation and configuration, F17752-06](https://docs.oracle.com/cd/F17749_01/doc.14/f17752.pdf),
dated **June 2020**. Treat it as a release-specific historical reference, not current OPERA Cloud
mobile installation guidance. Do not copy its old operating-system requirements or deployment
instructions into a modern Cloud project without current product/release confirmation. The source
PDF is linked, not redistributed in this package.
