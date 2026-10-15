# Demo and installation guide

This short demo uses the public references in this repository and public primary sources. The
answers are examples of the evidence and uncertainty the skill is meant to surface; they are not
recordings of a particular model run or guarantees that every assistant will answer identically.

**Snapshot date:** 2026-10-15. Version and feature statements below reflect the dated sources cited
in each answer, not a live tenant check. Do not include credentials, guest details, or other
customer data in demo prompts.

## Demo

Try these prompts after installing the skill. Each answer links to the supporting reference and
the primary source where one is available.

### Is OPERA Cloud 26.4 the release my property is running?

**Example answer:** Oracle's Hotels documentation index listed OPERA Cloud Services 26.4 as its
newest release on 2026-10-15. **Whether your property is running 26.4 is unknown from this public
skill**: check the tenant's release information and confirm it with your administrator before
using release-specific instructions. [Repository maintenance note](../README.md#maintenance-status)
· [Oracle Hotels documentation index](https://docs.oracle.com/en/industries/hospitality/hotels.html)
· [26.4 release readiness](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm).

### Does an OHIP 401 response prove that my client secret expired?

**Example answer:** No. A 401 calls for checking the token, client configuration, and the
endpoint's authentication requirements; the status alone does not identify an expired secret.
Inspect the sanitized response and the current endpoint contract, and retry only when the cause is
understood and the operation is safe. [Authentication reference](../references/architecture-and-auth.md#authentication)
· [Error handling reference](../references/error-handling.md#http-status-codes-you-will-see)
· [Oracle OHIP documentation](https://docs.oracle.com/en/industries/hospitality/integration-platform/).

### Is Ask Oracle a transaction agent that can change a reservation, and is it available at every property?

**Example answer:** Oracle documents Ask Oracle as natural-language product and how-to guidance
that uses property, language, and current-screen context. The guide does not establish that it can
edit reservations, so contextual answers are not evidence of write access. Availability is
released incrementally and may be delayed; the Ask Oracle property control must be enabled, so
availability at a particular property is unknown without checking its configuration. When
available, a response's **Source** action opens related documentation; if Oracle Support requests
it, the **Message ID** can help investigate an incorrect answer.
[Oracle: Using Ask Oracle AI Agent](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/c_getting_started_ask_oracle.htm)
· [Oracle: prerequisites](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/r_prerequisites_for_getting_started.htm#PrerequisitesUsingAskOracleAIAgent)
· [Repository AI evidence notes](../references/native-ai-and-copilots.md#ask-oracle-workflow).

### What does OPERA Cloud 26.4's AI Rate Description Assistant do, and is it generally available?

**Example answer:** Oracle says it generates Rate Code Long Information using package details,
rate descriptions, and additional information supplied by the user. The 26.4 guide says availability
is limited to early adopters for evaluation and feedback; it does not establish general
availability or eligibility for your tenant. There is also a control-group inconsistency: the
feature description names **Reservations**, while its enablement instructions refer to **Rate
Management**. Check the current guide and tenant UI before enablement.
[Oracle 26.4 feature summary](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm#c_30560_29930_ai_assistant_added_to_rate_code_long_information)
· [Oracle rate-code configuration guide](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/t_creating_a_new_rate_code.htm#OCSUH-ConfiguringRateCodeRateInformation-5E9160B9)
· [Repository AI evidence notes](../references/native-ai-and-copilots.md#opera-cloud-264-ai-release-notes).

## Install

These instructions install the skill folder, not an application, connector, Oracle product, or
account-wide integration. Keep `SKILL.md`, `references/`, `subskills/`, and `LICENSE` together
inside the `opera-cloud` directory. Git is required for the clone commands.

### Codex CLI and IDE extension

OpenAI's official guide documents user skills under `$HOME/.agents/skills` and repository skills
under `.agents/skills`. Choose one scope.

**Personal install** — available to your Codex projects on this machine:

```powershell
$target = Join-Path $HOME ".agents\skills\opera-cloud"
New-Item -ItemType Directory -Force (Split-Path $target) | Out-Null
git clone https://github.com/austugal/opera-cloud-community-skill.git $target
```

```sh
target="$HOME/.agents/skills/opera-cloud"
mkdir -p "$(dirname "$target")"
git clone https://github.com/austugal/opera-cloud-community-skill.git "$target"
```

**Repository install** — put or copy the skill folder at
`<your-repository>/.agents/skills/opera-cloud/`. This is a repository-local install; commit the
files if you want teammates to receive them. From this community-skill checkout, copy the files
into a target repository (replace the example path first):

```powershell
$project = "C:\path\to\your-repository"
$target = Join-Path $project ".agents\skills\opera-cloud"
New-Item -ItemType Directory -Force $target | Out-Null
Copy-Item .\SKILL.md, .\LICENSE $target
Copy-Item .\references, .\subskills $target -Recurse
```

```sh
project="/path/to/your-repository"
target="$project/.agents/skills/opera-cloud"
mkdir -p "$target"
cp SKILL.md LICENSE "$target/"
cp -R references subskills "$target/"
```

Do not clone this repository into a path that already exists. If you cloned it personally and need
to update it, run `git pull --ff-only` from that skill folder, keeping local edits separately.

In Codex, invoke it as `$opera-cloud` or ask a matching OPERA question. Automatic selection depends
on the skill description and is not guaranteed for every prompt. If it does not appear after
installation, follow the host's current instructions to refresh or restart.

[Official Codex skills guide](https://learn.chatgpt.com/docs/build-skills) ·
[Codex skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

### Claude Code

Anthropic documents personal skills under `~/.claude/skills/<skill-name>/SKILL.md` and
repository-local skills under `.claude/skills/<skill-name>/SKILL.md`. Choose one scope.

**Personal install** — available to Claude Code on this machine:

```powershell
$target = Join-Path $HOME ".claude\skills\opera-cloud"
New-Item -ItemType Directory -Force (Split-Path $target) | Out-Null
git clone https://github.com/austugal/opera-cloud-community-skill.git $target
```

```sh
target="$HOME/.claude/skills/opera-cloud"
mkdir -p "$(dirname "$target")"
git clone https://github.com/austugal/opera-cloud-community-skill.git "$target"
```

**Repository install** — put or copy the skill folder at
`<your-repository>/.claude/skills/opera-cloud/`. Commit the files to share them with repository
users. From this community-skill checkout, copy the files into a target repository (replace the
example path first):

```powershell
$project = "C:\path\to\your-repository"
$target = Join-Path $project ".claude\skills\opera-cloud"
New-Item -ItemType Directory -Force $target | Out-Null
Copy-Item .\SKILL.md, .\LICENSE $target
Copy-Item .\references, .\subskills $target -Recurse
```

```sh
project="/path/to/your-repository"
target="$project/.claude/skills/opera-cloud"
mkdir -p "$target"
cp SKILL.md LICENSE "$target/"
cp -R references subskills "$target/"
```

In Claude Code, invoke it as `/opera-cloud` or ask a matching OPERA question.

The local `~/.claude/skills/` install is for Claude Code on this machine; it does not install the
skill into Cowork or cloud sessions. Follow Anthropic's account skill settings for those products.
If you cloned the skill personally and need to update it, run `git pull --ff-only` from that skill
folder, keeping local edits separately.

[Official Claude Code skills guide](https://code.claude.com/docs/en/skills) ·
[Skill locations](https://code.claude.com/docs/en/skills#where-skills-live).

### Other assistants

This guide makes direct-folder installation claims only for Codex and Claude Code. Other products
may use different import flows, file locations, or account-level distribution; use their official
documentation rather than assuming this repository installs into them.

## FAQ

**Is this an Oracle product or endorsed by Oracle?** No. It is an unofficial community reference
skill. Oracle names identify products and sources, not an endorsement or customer relationship.

**Does installing the skill connect to OPERA Cloud or access live property data?** No. It is a
Markdown reference library; it contains no application runtime, API client, or property
credentials.

**Can it determine my property's release, entitlements, or configuration?** No. Those are unknown
unless supplied by an authorized, customer-approved source. Check the tenant and its current
Oracle documentation; do not infer local facts from public examples.

**Are the sample answers current for every property?** No. The demo gives a dated, source-linked
example. Confirm the deployed release, enabled modules, and local procedures before acting.

## Share-ready description

> An unofficial community skill for exploring Oracle Hospitality OPERA Cloud, OPERA 5, and OHIP
> with concise, source-linked answers—and explicit “unknown” boundaries where public documentation
> cannot establish a property's release, configuration, or permissions. Try the four dated
> examples in the [demo and installation guide](https://github.com/austugal/opera-cloud-community-skill/blob/main/docs/demo-installation.md).
> Not affiliated with or endorsed by Oracle.
