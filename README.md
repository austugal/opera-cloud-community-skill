# opera-cloud-skill

A public, version-aware reference skill for Oracle Hospitality OPERA Cloud, OPERA 5, and the Oracle
Hospitality Integration Platform (OHIP). It helps an AI assistant answer product, operations,
configuration, integration, and troubleshooting questions using scoped guidance and an explicit
source-verification workflow.

**Quick links:** [Install](docs/demo-installation.md#install) ·
[Try the demo](docs/demo-installation.md#demo) · [Use the skill](SKILL.md) ·
[Coverage and gaps](maintenance/source-release-coverage.md) ·
[OXI XML sample guidance](docs/oxi-xml-samples.md)

## Common use cases

- Find release-aware OPERA Cloud, OPERA 5, or OHIP guidance and identify what must be checked
  against the deployed environment.
- Assess an integration, interface, or vendor compatibility claim without treating OXI, IFC8,
  OHIP, or Distribution as interchangeable.
- Investigate operational, configuration, AI-feature, or fiscal questions using the scoped
  references and their evidence limits.
- Discover external OXI XML examples safely; this repository links to a library but does not
  bundle its XML files.

## Purpose and architecture

This repository is a documentation product: Markdown files, a `SKILL.md` entry point, and
supporting reference documents. It has no application runtime, API client, build system, or
external package dependencies.

The skill uses a small-router / on-demand-reference design:

1. An agent matches a request to the skill's frontmatter description and reads `SKILL.md`.
2. `SKILL.md` establishes answer and safety rules, explains the product boundaries, and routes the
   question to focused references or specialist playbooks.
3. The agent consults the relevant Oracle release documentation and customer-approved procedures
   for exact, environment-specific behavior before recommending an action.

Conceptually, OPERA Cloud provides the PMS capabilities; OHIP is the documented programmatic
integration surface; Distribution APIs handle channel connectivity; and event delivery, IFC8, and
OXI are distinct integration concerns. OPERA 5 has its own product and configuration conventions.
The documentation describes these components and their relationships; it does not connect to or
operate them.

## Tech stack

- **Content:** Markdown, including YAML frontmatter in `SKILL.md`
- **Runtime/build dependencies:** none
- **Validation:** `python tools/validate_repository.py` checks skill frontmatter, reference
  routing, relative Markdown links, and selected secret patterns. Run
  `python -m unittest discover -s tests -v` for the validator's unit tests. GitHub Actions runs
  both commands on pushes and pull requests. These checks do not validate product claims or replace
  review against authoritative Oracle documentation.

## Maintenance status

Reviewed on 2026-10-15 against Oracle Help Center indexes. The Hotels index listed OPERA Cloud
Services 26.4, OPERA Cloud Distribution 26.4, and Hotel Property Interface 8.17. OHIP 26.3 was
last recorded on 2026-10-13 and was not re-checked. These are index observations, not a property
deployment inventory or verification of every claim in this repository. Confirm the deployed
release, modules, entitlements, and configuration before applying release-specific guidance.
Oracle documentation can change between reviews.

- [Oracle Hospitality Hotels documentation index](https://docs.oracle.com/en/industries/hospitality/hotels.html)
- [OPERA Cloud Services 26.4 release readiness](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm)
- [Oracle Hospitality Integration Platform documentation](https://docs.oracle.com/en/industries/hospitality/integration-platform/)
- [Oracle Hospitality documentation home](https://docs.oracle.com/en/industries/hospitality/)

Weekly OPERA skill research and maintenance runs through the owner's Copilot automation in the
owner's Copilot workspace; it is not configured in this public repository and does not publish
changes here. Changes to this repository are managed through reviewed pull requests. GitHub Actions
validates repository changes on pushes and pull requests; it does not conduct research. Review and
publication are verified separately.

## Where to start

- **New to the repository:** read this README, then `SKILL.md` for the assistant's workflow and
  topic routing.
- **New to the product architecture:** start with `references/architecture-and-auth.md`, then
  `references/api-modules.md` and `references/async-streaming-events.md`.
- **Working on a specific issue:** use the reference map in `SKILL.md`; do not load all references
  unless the question spans multiple domains.
- **Need exact/current behavior:** follow the official Oracle documentation for the deployed
  release. Reference documents may not reflect every tenant, property configuration, or release.

## Reference library

| File | Subject |
|---|---|
| `references/architecture-and-auth.md` | OPERA Cloud architecture, environments, OAuth, headers, and client management |
| `references/api-modules.md` | REST API module map and common domain operations |
| `references/async-streaming-events.md` | Asynchronous APIs, Business Events, streaming, and subscriptions |
| `references/distribution-channels.md` | Distribution APIs, ARI, reservation notifications, and channel migration |
| `references/interfaces-ifc8.md` | IFC8, OXI, and interface configuration |
| `references/fiscal-compliance.md` | Fiscal exports, SAF-T, SII, VERI*FACTU, and Portugal and Spain detail |
| `references/backoffice-export.md` | Ledger exports and formula-engine guidance |
| `references/night-audit-controls.md` | Night audit, business dates, and OPERA Controls |
| `references/rates-restrictions.md` | Rate plans, restrictions, derivation, and hurdle logic |
| `references/error-handling.md` | HTTP errors, retry behavior, and rate limits |
| `references/native-ai-and-copilots.md` | Ask Oracle AI Agent, selected OPERA Cloud AI features, and third-party assistant evidence |
| `references/partner-integrations.md` | Vendor-listed integrations, including evidence boundaries for Prologic First |
| `references/version-changes.md` | Release tracking and upgrade checks |
| `references/opera5-pms.md` | OPERA 5 configuration topics |
| `references/workstation-setup-guide.md` | Workstation, printer, and print-task setup |
| `references/mobile-configuration-guide.md` | OPERA mobile setup and troubleshooting |
| `references/support-troubleshooting-guide.md` | Support triage and general troubleshooting |
| `references/quick-reference.md` | Compact API and operations overview |
| `references/australia-fiscal.md` | Australian fiscal and GST research boundaries |
| `references/bi-publisher-stationery-xml.md` | BI Publisher stationery, RTF/XML, and validation |
| `references/implementation-migration-training.md` | Migration, supported imports, implementation, and training |
| `references/maintenance-sources-and-backlog.md` | Public research policy, source entry points, and rotating coverage backlog |
| `docs/oxi-xml-samples.md` | OXI XML sample discovery, boundaries, and safe evaluation checklist |

## Specialist playbooks

The skill includes two original task-specific playbooks inspired by role-based agent workflows.
They are loaded through the root `SKILL.md` router and do not bundle or copy third-party personas:

| Playbook | Use it for |
|---|---|
| `subskills/opera-ai-assessment/SKILL.md` | Identify Oracle-native, partner, custom, or proposed AI; verify release and availability; assess data access and safeguards |
| `subskills/opera-integration-assessment/SKILL.md` | Assess product/vendor compatibility claims, interface evidence, data flow, and implementation risk |
| `subskills/opera-ai-automation-contract/SKILL.md` | Turn an OPERA/OHIP operations request into a version-aware, safety-gated AI workflow automation contract |

## Principles

- **Public and factual:** cite or link public Oracle sources for factual claims; label observations
  and hypotheses clearly.
- **Version-aware:** verify version-specific details against the deployed release rather than
  assuming the latest or a historical reference applies. The review date above records a docs
  index check; it does not make old release-specific procedures current.
- **Safe:** no credentials, private endpoints, or customer-identifying examples; treat guest and
  financial data as sensitive.
- **Independent:** this is an unofficial community reference, not an Oracle product or substitute
  for Oracle documentation, customer procedures, or professional regulatory advice.

## Contributing

Corrections and additions are welcome by pull request. Keep changes public and non-sensitive. Cite
the relevant Oracle source for factual claims, state the release scope where applicable, and update
the routing table in `SKILL.md` and this file when adding or renaming a reference.

GitHub Discussions are enabled for questions and suggestions. No posts to external forums or
communities have been made for this project; no popularity claim is made.

## License

MIT. See `LICENSE`.

## Installation

This is an **unofficial community skill**, not an Oracle product or Oracle-endorsed resource. The
[demo and installation guide](docs/demo-installation.md) provides source-linked examples and
assistant-specific installation instructions. Install it only in the intended assistant and scope;
a GitHub repository URL does not configure other assistants, accounts, or computers.

See the [assistant-specific installation guide](docs/demo-installation.md#install).

## Example requests

- Try the [reproducible demo questions and answers](docs/demo-installation.md#demo).
- Use this skill to investigate why a fiscal zero-balance checkout stopped on OPERA Cloud 26.1.
- Explain which room and rate mappings must be confirmed before a channel-manager migration.
- Compare the documented Portugal package-control changes in 26.4 with our installed release.
- Draft a front-office checklist, identifying which steps depend on property configuration.
- Check which OPERA Cloud AI assistant is documented for our release and whether it can change records.
- Assess a vendor's published “Opera PMS” integration claim without assuming it means OHIP or OPERA Cloud.

### Example: Ask Oracle AI Agent

**Question:** Is Ask Oracle a transaction agent that can change a reservation, and is it available
at every property?

**Answer:** Oracle documents Ask Oracle as natural-language product and how-to guidance that uses
property, language, and current-screen context. The guide does not establish that it can edit
reservations, so contextual answers are not evidence of write access. Availability is released
incrementally and may be delayed; the Ask Oracle property control must be enabled, so availability
at a particular property is unknown without checking its configuration. When available, a
response's **Source** action opens related documentation; if Oracle Support requests it, the
**Message ID** can help investigate an incorrect answer. [Oracle: Using Ask Oracle AI Agent](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/c_getting_started_ask_oracle.htm)
· [Oracle: prerequisites](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/r_prerequisites_for_getting_started.htm#PrerequisitesUsingAskOracleAIAgent)
· [Repository AI evidence notes](references/native-ai-and-copilots.md#ask-oracle-workflow).

## Publication boundary

No live property data, customer configurations, credentials, guest records or support-case
attachments are included. Product and authority names identify the systems and public sources;
they do not imply endorsement or a customer relationship. The copyright holder is `austugal`.
