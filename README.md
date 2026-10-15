# opera-cloud-skill

A public, version-aware reference skill for Oracle Hospitality OPERA Cloud, OPERA 5, and the Oracle
Hospitality Integration Platform (OHIP). It helps an AI assistant answer product, operations,
configuration, integration, and troubleshooting questions using scoped guidance and an explicit
source-verification workflow.

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
- **Validation:** manual review of document structure, reference links, and factual claims against
  authoritative Oracle documentation; there is no code test suite or build command

## Maintenance status

Reviewed on 2026-10-15 against Oracle Help Center indexes. Oracle's Hotels documentation index
lists OPERA Cloud Services 26.4 and OPERA Cloud Distribution 26.4 as the newest releases, with
Hotel Property Interface at 8.17. The OHIP documentation was last recorded at 26.3 on 2026-10-13
and was not re-checked. This is the documentation set visible on the review dates, not a claim that
every customer runs that release. Properties often run an older one. The applicable release,
modules, product entitlements, and property configuration must be confirmed before applying any
guidance. Oracle documentation can change between scheduled reviews.

- [Oracle Hospitality Hotels documentation index](https://docs.oracle.com/en/industries/hospitality/hotels.html)
- [OPERA Cloud Services 26.4 release readiness](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm)
- [Oracle Hospitality Integration Platform documentation](https://docs.oracle.com/en/industries/hospitality/integration-platform/)
- [Oracle Hospitality documentation home](https://docs.oracle.com/en/industries/hospitality/)

A separate daily ChatGPT task is configured to maintain this repository and the installed skill;
it runs outside this repository. No GitHub Actions maintenance workflow is bundled here, and a
schedule does not guarantee that research, publication, or skill persistence succeeded. Re-check
authoritative sources when using release-specific or regulatory guidance.

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

## Specialist playbooks

The skill includes two original task-specific playbooks inspired by role-based agent workflows.
They are loaded through the root `SKILL.md` router and do not bundle or copy third-party personas:

| Playbook | Use it for |
|---|---|
| `subskills/opera-ai-assessment/SKILL.md` | Identify Oracle-native, partner, custom, or proposed AI; verify release and availability; assess data access and safeguards |
| `subskills/opera-integration-assessment/SKILL.md` | Assess product/vendor compatibility claims, interface evidence, data flow, and implementation risk |

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

## License

MIT. See `LICENSE`.

## Installation

This is an **unofficial community skill**, not an Oracle product or Oracle-endorsed resource. The
[demo and installation guide](docs/demo-installation.md) has source-linked sample answers, a FAQ,
and separate install instructions for Codex and Claude Code based on their current official
documentation. The instructions install only into the chosen assistant and scope; a GitHub
repository URL does not configure every assistant, account, or computer.

This public repository starts from a reviewed content snapshot; it does not include the private
source repository's commit history. Agency Agents is a separate project and its personas are not
bundled here; the specialist playbooks in this repository are original, OPERA-focused workflows.
Review-date checks cover selected claims, not every procedure in every release.

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
