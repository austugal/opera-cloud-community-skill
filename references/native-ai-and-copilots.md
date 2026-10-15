# Native AI, Ask Oracle and copilots

Reviewed 2026-10-15. Scope: selected Oracle OPERA Cloud 26.4 documentation, including Release Readiness Guide G58711-04, published 2026-10-06; no tenant or entitlement test. These are documented capabilities visible in the reviewed materials, not claims of a launch on the review date.

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
| AI Rate Description Assistant (26.4) | Generates Rate Code Long Information using package details, rate descriptions, and additional information supplied by the user | The 26.4 guide says availability is limited to early adopters for evaluation and feedback; its enablement text inconsistently names the Reservations and Rate Management control groups, so verify the current tenant guide |

The feature-summary entries above establish selected features, not universal availability or measured productivity gains. Check the relevant entry and prerequisite page for the installed release before enablement.

### OPERA Cloud 26.4 AI release notes

The 26.4 Feature Summary lists the AI Rate Description Assistant as requiring enablement and describes its generated text as Rate Code **Long Information**. Oracle says the feature is available to a limited set of early adopters for evaluation and feedback; do not describe it as generally available. The feature summary also lists an updated Ask Oracle chat experience and a Distribution-scoped AI Channel Rate Description Assistant control. Check the linked release entry and property entitlement before treating either as available in a tenant.

The Rate Description Assistant entry itself is inconsistent about the control group: its description says **Reservations**, while its enablement steps direct administrators to **Rate Management**. Confirm the current guide and tenant UI instead of relying on either group name in isolation.

Oracle's reviewed user guide names the in-product assistant **Ask Oracle AI Agent**. “OPERA AI copilot” or “OPERA Cloud copilot” should be treated as informal or ambiguous wording unless a source identifies a separate product by that name. Do not conflate Ask Oracle with a third-party assistant, custom bot, OHIP integration, or agent that can perform transactions.

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
- [AI Assistant Added to Rate Code Long Information](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm#c_30560_29930_ai_assistant_added_to_rate_code_long_information).
- [Configuring Rate Code Rate Information](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/t_creating_a_new_rate_code.htm#OCSUH-ConfiguringRateCodeRateInformation-5E9160B9).
- [Ask Oracle Chat Experience Updated](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm#c_35255_35440_35441_35613_ask_oracle_chat_experience_updated).
- [AI Channel Rate Description Assistant OPERA Control Added](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/oprnc/c_feature_summary.htm#c_27851_30563_ai_channel_rate_description_assistant_opera_control_added).
