# Roles, tasks and property access — OPERA Cloud 26.4

Reviewed 2026-10-19 against the public Oracle 26.4 pages linked below. This reference summarises documented behavior; it does not include tenant configurations, employer material, customer data or a tested role design. Verify the deployed release before applying it.

## Roles and access boundaries

Oracle documents the following [R1]:

- Roles are created in OPERA Cloud Identity Manager or a federated identity manager, imported into OPERA Cloud, and assigned tasks.
- Chain roles provide common privileges across the tenancy; property roles apply to one property.
- Property roles normally use templates. The Property Role without Template control permits standalone property roles.
- With Activate Template Tasks on all Dependent Property Roles enabled, template task selections and deselections propagate to dependent property roles.
- Users may have multiple chain and property roles. Transaction Code by User Role requires a property role even when a chain role is assigned.
- Roles alone do not provide property access: hub assignment is also required.
- Role task changes can take up to ten minutes to take effect.
- Role-management activity is recorded in Changes Log under Configuration, with action type SEC_TASK_ACTION.

## Task assignment and upgrade visibility

In Role Manager, select Manage Property Roles or Manage Chain Roles, find the role and use Actions > Edit. Tasks can be filtered by granted status or name, selected and saved. Report-group tasks control access to report groups [R2].

Oracle notes that tasks remain listed even when their corresponding OPERA Controls are inactive. A listed task therefore does not establish that the associated feature is enabled. After an upgrade, categories indicate newly available tasks. A green All indicator means all tasks in that category are assigned [R2].

## Location and property context

For the documented Central Management Services or Foundation multi-property context, selecting a hub exposes the properties associated with it; selecting a property limits the location to that property. Effective access combines hubs and assigned roles [R3].

The documented location selector is in the top-right user/location panel: Change Location, choose Hub or Property, search and select. The session reinitializes. Within a hub, a default property can be selected for searches; a search default is not an additional role grant [R3].

## Answer boundary

Use these documented distinctions when explaining missing access or an upgrade-related task question. Do not invent a universal front-office/finance role template or imply that this reference grants access. Exact permissions remain subject to the current Oracle task documentation and the administrator's authorised configuration.

## Oracle sources

- **[R1] [About Roles](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/c_manage_roles.htm)** — roles, hubs, propagation, timing and audit logging.
- **[R2] [Assigning Tasks to a Role](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/t_manage_property_roles_assigning_tasks_to_roles.htm)** — task assignment, upgrade indicators and control-independent task visibility.
- **[R3] [Changing Your Location in Central or Multi Property Operations](https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.4/ocsuh/t_logging_into_a_hub_or_different_property.htm)** — location scope, selector and default-property behavior.

Selected public pages read; no identity-provider configuration, tenant access or live permission test performed.
