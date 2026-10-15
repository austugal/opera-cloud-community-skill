---
name: opera-cloud
description: >-
  Version-aware reference for Oracle Hospitality OPERA Cloud, OPERA 5, and OHIP.
  Use for any question on OPERA, OHIP, IFC8, OXI, Ask Oracle AI, OPERA AI features and copilots,
  hospitality vendor integrations including Prologic First, SAF-T, SII, VERI*FACTU, ATCUD, SUN or
  back-office exports, night audit, OPERA Controls, rate plans and derivation, channel managers
  and distribution, REST and Distribution APIs, OAuth, Business Events and streaming, hospitality
  PMS configuration and operations, release upgrades, and troubleshooting.
license: MIT
---

# OPERA Cloud and Oracle Hospitality

Use this skill to answer OPERA Cloud, OPERA 5, and Oracle Hospitality Integration Platform (OHIP)
questions with scoped, verifiable guidance. The repository is a Markdown reference library, not
software that connects to or operates a hotel system.

## How to use this skill

1. Identify the product and context: OPERA Cloud or OPERA 5; property or enterprise; environment;
   release; and whether the question is operational, configuration, integration, or regulatory.
   Establish the installed release first. Properties upgrade on Oracle's schedule and are often
   behind the newest release, so a correct answer for one release can be wrong for another.
2. Open only the reference file(s) or specialist module relevant to the question, using the maps below.
3. For exact API paths, schemas, permissions, menu paths, controls, and release-specific behavior,
   verify against Oracle's documentation for the customer's deployed release. The references are
   navigation aids, not substitutes for live product specifications.
4. Give a direct answer with the assumptions and version context that materially affect it. If an
   essential detail is unknown, state that limitation and give the user a safe way to verify it.
5. For actions that can change configuration, money, guest records, inventory, or production
   integrations, distinguish read-only investigation from changes. Recommend testing in a
   non-production environment and obtaining the customer's normal approval before production
   changes.

## Reference map

| Question area | Read |
|---|---|
| Product architecture, environments, OAuth, request headers, client management | `references/architecture-and-auth.md` |
| REST API domains, modules, and operation patterns | `references/api-modules.md` |
| Async APIs, Business Events, subscriptions, and streaming | `references/async-streaming-events.md` |
| Distribution APIs, ARI, reservation notifications, channel migration | `references/distribution-channels.md` |
| IFC8, OXI, and interface configuration | `references/interfaces-ifc8.md` |
| Fiscal exports, SAF-T, SII, VERI*FACTU, and country-specific considerations (Portugal and Spain detail) | `references/fiscal-compliance.md` |
| Australia fiscal and GST research boundaries | `references/australia-fiscal.md` |
| Back-office ledger exports and formula-engine constraints | `references/backoffice-export.md` |
| Night audit, business dates, and OPERA Controls | `references/night-audit-controls.md` |
| Rate plans, restrictions, derivation, and hurdle logic | `references/rates-restrictions.md` |
| HTTP errors, retry behavior, and rate limits | `references/error-handling.md` |
| Ask Oracle AI Agent, OPERA AI features, and third-party copilots | `references/native-ai-and-copilots.md`; for an AI capability evaluation, also read `subskills/opera-ai-assessment/SKILL.md` |
| Vendor-listed partner integrations and compatibility evidence | `references/partner-integrations.md`; for a technical assessment, also read `subskills/opera-integration-assessment/SKILL.md` |
| Release tracking and upgrade checks | `references/version-changes.md` |
| OPERA 5 configuration | `references/opera5-pms.md` |
| Workstations, printers, and print tasks | `references/workstation-setup-guide.md` |
| BI Publisher stationery and RTF/XML validation | `references/bi-publisher-stationery-xml.md` |
| Mobile configuration and connectivity | `references/mobile-configuration-guide.md` |
| Support triage and general troubleshooting | `references/support-troubleshooting-guide.md` |
| Migration, supported imports, implementation, and training | `references/implementation-migration-training.md` |
| Compact API and operations overview | `references/quick-reference.md` |
| Repository research and maintenance policy (maintainers only) | `references/maintenance-sources-and-backlog.md` |

## Specialist modules

These original, task-specific playbooks add repeatable analysis workflows to this skill; they are
not external agent packages and do not access or operate a hotel system. Read one when its task
matches:

- `subskills/opera-ai-assessment/SKILL.md` for identifying AI products, verifying availability,
  separating guidance from transactional access, and assessing safeguards.
- `subskills/opera-integration-assessment/SKILL.md` for vendor claims, interface evidence, data
  flow, implementation checks, and integration troubleshooting.

## Product and integration map

OPERA Cloud is the property-management application. Its operational domains include reservations,
profiles, cashiering, rooms and housekeeping, rates, inventory, blocks, events, and end-of-day
processing. OHIP is the integration surface: external applications use its documented APIs and
event mechanisms rather than direct database access. Distribution interfaces serve channel
connectivity; IFC8 and OXI describe separate interface/integration patterns and must not be treated
as synonyms for OHIP.

OPERA 5 is a distinct product generation with different deployment and configuration conventions.
Do not transfer OPERA Cloud navigation or API assumptions to an OPERA 5 question (or vice versa).
For API work, use the sequence **identity and access → API/module and release → request context →
operation → response/error handling**. For event-driven work, distinguish event subscription and
delivery from the consuming application's connection, processing, and recovery.

## Answering and troubleshooting rules

- Never invent endpoint paths, request fields, response fields, control names, menu paths, limits,
  event names, or supported values. Confirm them in the applicable Oracle source or label them as
  unknown.
- Separate generally applicable concepts from version-, tenant-, property-, license-, and
  configuration-dependent behavior. Do not imply the references are current for every deployment.
- Distinguish Oracle-documented behavior from an observed symptom or hypothesis. A symptom is not
  proof of a cause; offer checks that discriminate between plausible causes.
- For troubleshooting, first establish the product, release, environment, scope of impact, start
  time, recent changes, exact error, and a safe reproduction. Then follow the matching reference
  and inspect evidence before recommending a change. Avoid blind restarts and speculative fixes.
- For API retries, check whether the operation is safe to retry and whether the failure is
  transient before retrying. Use the documented response body and retry guidance; do not assume
  every 4xx or 5xx has the same remedy.
- Treat credentials and guest, reservation, and folio data as sensitive. Never request secrets in
  chat, include real credentials in examples, or recommend logging tokens or full authorization
  headers. Minimize personal-data access and retention.
- For fiscal, accounting, and regulatory workflows, identify the country, output format, receiver,
  and effective requirements. Verify rules with the relevant authority and the customer's
  approved process; do not present a generic example as legal or tax advice.

## Evidence labels

Label each material claim with the strength of its evidence, and never present a weaker label as a
stronger one.

- **Documented:** stated in Oracle or authority documentation. Cite the source and the release.
- **Recorded:** retained from a secondary source or an earlier reference, but not confirmed against
  a primary source. Do not use it alone for a configuration or compliance decision.
- **Observed:** seen in a live system, log, or support case. Say "based on observed system
  behaviour". It is not Oracle-documented until a source says so.
- **Inference:** reasoning from documented or observed facts. Say it is inference.

If a claim cannot be tied to one of these, treat it as unknown and say how to verify it.

## Extended library (optional)

If the author's OPERA-CLOUD-REFERENCES library is available in the session (a checkout or the
opera-brain connector), read its `SKILL-ROUTER.md` before answering from memory. Route only to
files listed under its "Routing by topic". Never answer from files under its "Withdrawn" heading.
It holds deeper country fiscal guides, IFC8 sub-guides, night audit procedures and checklists, and
one file per product per release. If it is not available, answer from this skill and say that no
deeper reviewed library was consulted.

## Source hierarchy

Prefer, in order: the API specification and product documentation for the deployed release; the
customer's approved configuration and operational procedures; then this skill's general
references. When those sources disagree, call out the discrepancy and defer to the applicable
official/customer source rather than silently choosing one.

## Keeping references current

The Oracle Help Center is the source for OPERA Cloud release readiness, user, compatibility, and
security documentation. OHIP API contracts and onboarding material are maintained separately.
Check both when a change affects an integration. On 2026-10-15, Oracle's Hotels documentation index
listed OPERA Cloud Services 26.4, OPERA Cloud Distribution 26.4, and Hotel Property Interface 8.17
as the newest releases. The OHIP documentation was last recorded at 26.3 on 2026-10-13. These are
review-date observations, not assumptions about a property's installed release. Review
`references/version-changes.md` before relying on release-specific statements. Keep the references
generic, link official sources, and remove or qualify details that cannot be verified.
