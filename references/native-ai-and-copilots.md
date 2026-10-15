# Native AI, Ask Oracle and copilots

Reviewed 2026-10-15. Scope: selected Oracle OPERA Cloud 26.4 documentation; no tenant or entitlement test. These are newly captured documented capabilities, not claims of a new launch today.

## Documented capabilities

| Feature | Documented purpose | Boundary to verify |
|---|---|---|
| Ask Oracle AI Agent | Product questions and contextual how-to guidance in an in-application chat panel | Incremental rollout; property enablement and signed-in session context |
| AI Reservation Summary at Check In | Surfaces relevant guest/stay details; omits fields without data | Front Desk control; review against reservation details |
| AI Booking Suggestions | Booking/package suggestions in Central Reservation Sales Screen using guest stay history | Look to Book control and Central context |
| AI Room Types Description Assistant | Generates long descriptions; can preview regeneration after configuration changes | Room Management control; user decides whether to replace text |
| AI Channel Rate Description Assistant | Drafts channel rate descriptions from rate/package/channel attributes | Channel Management control; review/edit before saving |
| Task Sheet Instructions Translation | Displays free-text room instructions in the user's login language | Rooms Management control and Mobile Task Companion |
| Smart Service Order Task Request | Images suggest location and configured service tasks; remarks can be translated | Review and adjust suggestions before creating the service order |

The feature-summary entries above establish selected features, not universal availability or measured productivity gains. Check the relevant entry and prerequisite page for the installed release before enablement.

## Ask Oracle workflow

**Documented:** activate General parameter Ask Oracle [AI_CHATBOT_IN_UI] for the property through OPERA Controls. When enabled for at least one property, it is also available at hub level. Open Ask Oracle from the navigation bar. Ask a product question, review the answer and any source link, then use follow-up questions as needed. It uses relevant property, language and screen context. Documentation describes feedback, message IDs for Support and optional voice input. Availability can be delayed by incremental release.

**Evidence boundary:** these reviewed pages describe product guidance. They do not establish autonomous reservation changes, fiscal posting, payment authority, a native MCP server or unrestricted live hotel-data queries. Streaming response text is not proof of streaming reservation data. Confirm any additional transactional feature separately.

## Identify a copilot before attributing capabilities

Treat “copilot” as an ambiguous label until its vendor, product URL, version, native/partner/custom status and documentation are known. The reviewed native product is named Ask Oracle AI Agent. No separately named OPERA copilot was verified in this review. A Microsoft/GitHub copilot or a custom knowledge assistant does not acquire OHIP access from its name. Oracle Fusion/OCI AI documentation alone does not establish OPERA Cloud functionality.

For a proposed assistant, record its data route, permission scope, refresh model, retention and approval requirements separately from its language model. Mark proposals as proposals.

## Primary sources

- [26.4 feature summary](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm), selected AI entries.
- [Using Ask Oracle AI Agent](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/c_getting_started_ask_oracle.htm).
- [Getting Started prerequisites](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/r_prerequisites_for_getting_started.htm).
