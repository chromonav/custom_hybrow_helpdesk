import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field


def execute():
    create_hd_team_customer_contact_doctype()
    create_hd_team_customer_contacts_field()


def create_hd_team_customer_contact_doctype():
    """Create the HD Team Customer Contact child table as a customization.

    This intentionally does not live as a source DocType JSON under the app's
    doctype directory. It is a custom child DocType created during migration, so
    the fork stays closer to upstream Helpdesk and only customizes the desk schema.
    """
    if frappe.db.exists("DocType", "HD Team Customer Contact"):
        return

    doc = frappe.get_doc(
        {
            "doctype": "DocType",
            "name": "HD Team Customer Contact",
            "module": "Helpdesk",
            "custom": 1,
            "istable": 1,
            "editable_grid": 1,
            "autoname": "autoincrement",
            "naming_rule": "Autoincrement",
            "fields": [
                {
                    "fieldname": "contact",
                    "fieldtype": "Link",
                    "label": "Contact",
                    "options": "Contact",
                    "reqd": 1,
                    "in_list_view": 1,
                    "in_standard_filter": 1,
                }
            ],
            "permissions": [],
        }
    )
    doc.insert(ignore_permissions=True)


def create_hd_team_customer_contacts_field():
    if frappe.db.exists("Custom Field", "HD Team-customer_contacts"):
        return

    create_custom_field(
        "HD Team",
        {
            "fieldname": "customer_contacts",
            "fieldtype": "Table",
            "label": "Customer Contacts",
            "options": "HD Team Customer Contact",
            "insert_after": "users",
            "description": "Customer contacts listed here can view all tickets for their linked Customer when the ticket belongs to this team. They are also included on outgoing ticket replies for this team.",
        },
        ignore_validate=True,
    )
