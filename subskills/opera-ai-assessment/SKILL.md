---
name: opera-ai-assessment
description: >-
  Evaluate Oracle Hospitality OPERA AI features and third-party hotel copilots.
  Use when identifying a named assistant, checking release availability or entitlements,
  separating guidance from transactions, or assessing data access and operational risk.
---

# OPERA AI capability assessment

Use this specialist module with the root `SKILL.md` and `references/native-ai-and-copilots.md`.
It is an evidence-led assessment workflow, not an autonomous agent and does not connect to OPERA.

## Workflow

1. Identify the exact displayed product name, vendor, product version, deployment, OPERA release, property/enterprise scope, country, and date. Treat “copilot,” “AI agent,” and “assistant” as generic labels until a primary source identifies the product.
2. Classify it as Oracle-native, a named partner product, a customer-built/custom assistant, or a proposal. Do not attribute one product's features, certifications, or data access to another.
3. Read the current Oracle release entry and product guide for each claimed native capability. Record the release, guide title/ID or page, source date, required subscription, OPERA Control, role/task, rollout status, and any early-access limitation. Verify exact tenant availability with an authorized administrator.
4. Describe what the source actually says the feature does. Separate answering and content generation from reading live guest/property data, writing records, posting financial transactions, or taking other actions.
5. For partner or custom assistants, require evidence for the data source and route, API or connector, authentication and role scope, refresh mode, storage/retention, audit logs, human approval, and error/recovery behavior. Mark anything not evidenced as unknown.
6. Recommend a non-production evaluation with synthetic or approved data, representative questions, factual checks against OPERA, and an explicit human review for generated content. Do not use generated text as authority for a payment, tax, legal, safety, or production change.

## Required answer shape

State the verified product identity and evidence level; supported use case and release; availability/entitlement boundary; whether it only guides or can access/change data; operational safeguards; source links; and unresolved questions. If the identity or capability is not source-verifiable, say so instead of filling gaps with likely behavior.

## Safety boundaries

- Never ask for credentials, tokens, real guest records, folios, payment-card data, or private prompts/logs.
- Do not assume AI output is correct, current, or tenant-specific. Check material instructions in the deployed-release guide and approved property procedure.
- Do not infer autonomous action, database access, OHIP access, or a particular model/provider from marketing language.
- Do not enable controls or test against production without the customer's permissions and change approval.
