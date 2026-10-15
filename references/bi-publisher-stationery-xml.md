# BI Publisher stationery, RTF and XML

Reviewed 2026-10-15 against selected OPERA Cloud 26.4 user-guide pages. No Word add-in installation, tenant upload or rendered template test was performed.

## Documented model and setup

Stationery uses an RTF layout with a corresponding sample XML data model. Match the report group and sample to the intended output. An XML file used to preview stationery is not a fiscal submission file, an OHIP request or a migration CSV.

1. Confirm report permissions. Oracle's Reports prerequisites list View Internal Reports / Report Groups, Manage Reports and associated creation/copy tasks.
2. In Reports → Manage Reports, create a Customized Report for the property and correct stationery group. Download its sample RTF and sample XML.
3. Rename the RTF to a unique name that does not begin with SAMPLE. Keep the supplied XML name. Open the RTF in Word and load the matching sample XML through BI Publisher.
4. Edit the layout, save as RTF and upload the customised RTF to OPERA Cloud. Keep it below 10 MB; Oracle's page contains both “maximum 10MB” and “less than 10MB” wording, so avoid the boundary.
5. Set the applicable language, copies and report configuration. Oracle distinguishes parameter-form requirements for PMS stationery from Simple Diary/OSEM outputs; do not apply one setup to every group.

Source: Configuring Stationery Templates below. Use the actual deployed release's instructions if its UI differs.

## Fields, groups and preview

**Documented:** placeholders must exactly match case-sensitive XML element names. Repeating rows must follow the XML parent/child structure. Use the BI Publisher field picker after loading the appropriate sample XML; preserve the supplied grouping structure unless deliberately changing it. Preview with the same model. The editor guide also covers conditions, images/QR codes, dates/numbers and XPath.

Do not invent a tag because a field exists on a screen. Check whether the supported model exposes it and whether it is populated for the target report. Do not invent a general SQL query route into the SaaS database.

After an upgrade, Oracle documents refreshing customised stationery against the current model. Retrieve the new matching sample RTF/XML, compare available fields and re-test the custom layout. A custom layout does not automatically gain new data fields by changing text.

## Recommended test procedure (author guidance)

Keep the original layout and record a version for restoration. Test synthetic examples with absent fields, long names/addresses, multiple posting rows, page breaks, negative amounts, language variants and expected totals. Compare PDF preview, in-application output and physical print if used. For fiscal stationery, have the property fiscal owner approve mandatory content and identifiers; visual correctness alone does not establish compliance. Never place real guest XML or live folios in this public repository.

## Primary sources

- [Configuring Stationery Templates](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/t_reports_creating_and_running_custom_bi_pub_reports.htm).
- [Using Stationery Template Editor](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/c_reports_using_stationery_editor_new.htm).
- [Updating Customized Stationery with Current Data Model](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/t_reports_updating_customized_stationery_with_current_data_model.htm).
- [Stationery report groups](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/c_reports_stationery_reports_group.htm).
- [Reports prerequisites](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/r_prerequisites_for_reports.htm).
