# OPERA Workstations: Setup and Compatibility

OPERA Cloud and OPERA 5 have different deployment and client requirements. Hardware, operating
systems, browsers, Java components, printers, network rules, and workstation configuration are
release-specific. This guide does not prescribe a universal workstation build. Do not install
legacy browser components, runtime versions, certificates, or network exceptions based on this
document alone.

## Identify the workstation role

Record:

- Product: OPERA Cloud or OPERA 5; exact release/patch and deployment model.
- Workflow: browser-based access, OPERA 5 client, printing, payment device, or other interface.
- Workstation model, operating system/build, browser/client, and managed security baseline.
- Property, user role, network path, relevant interface/printer model, and the exact symptom.

## Compatibility and security

Before preparing a workstation, consult the Oracle compatibility matrix and documentation for the
exact product/release. Confirm supported operating system, browser, client components, peripherals,
certificates, ports/hosts, and any deprecation or end-of-support notices. For OPERA Cloud, do not
assume a workstation needs direct server/database access, Java, or inbound connectivity. For
OPERA 5, do not assume historical ports, browser modes, or runtimes remain supported.

Apply the organization's endpoint-management requirements: supported OS patches, endpoint
protection, disk encryption, least privilege, screen locking, approved software, and credential
handling. Do not bypass browser certificate validation, weaken security zones, expose servers, or
create firewall exceptions as a troubleshooting shortcut.

## Printers and peripherals

Use the product/release documentation to configure supported printers, print services, workstation
assignments, print tasks, and peripheral interfaces. Check each layer independently:

1. OS/device discovery and vendor-supported driver.
2. Product-side printer/device configuration and property/workstation assignment.
3. User permissions and task/template selection.
4. Queue/service health and sanitized product logs.
5. A controlled test document that does not expose real guest/payment data.

Do not assume Windows printer configuration alone makes a device available to OPERA, or that
OPERA 5 print-task configuration applies to OPERA Cloud.

## Network troubleshooting

Use the official compatibility/network-and-communications guide for release-specific destinations,
ports, proxy support, TLS, certificate chains, and DNS requirements. Do not infer required ports
from old workstation guides or open broad firewall rules.

Compare a failing workstation with a known-good supported one. Use approved DNS/TLS/connectivity
tests against documented Oracle/customer endpoints and collect timestamps or request IDs. A ping,
fixed latency threshold, or reachability to one host does not prove that an OPERA workflow is
healthy.

## Troubleshooting checklist

1. Capture product/release, workstation and OS build, user/property, affected workflow, start time,
   exact error, recent changes, and scope.
2. Determine whether the fault is limited to one user, workstation, printer/peripheral, property,
   or environment.
3. Check product compatibility, role/privileges, property/workstation assignment, device setup,
   and documented service status.
4. Inspect approved client, service, OS, and interface diagnostics; redact credentials and personal
   data.
5. Make one reversible change at a time under the customer's IT/change-control process.
6. Escalate with sanitized evidence to the hotel IT team, interface vendor, or Oracle Support as
   appropriate.

Avoid unsupported log paths, ports, CPU/latency thresholds, administrator requirements, restart
steps, or configuration scripts. Obtain those details from the actual managed environment and
current product documentation.

## Official references

- [OPERA Cloud Services documentation and compatibility matrix](https://docs.oracle.com/en/industries/hospitality/hotels.html)
- [Oracle Hospitality documentation home](https://docs.oracle.com/en/industries/hospitality/)

For OPERA 5, locate the matching product/patch documentation in Oracle Help Center; the currently
available legacy libraries may cover only particular older releases.
