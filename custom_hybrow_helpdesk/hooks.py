app_name = "custom_hybrow_helpdesk"
app_title = "Custom Hybrow Helpdesk"
app_publisher = "Hybrowlabs"
app_description = "Hybrow custom fork of Frappe Helpdesk"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@frappe.io"
app_license = "AGPLv3"

add_to_apps_screen = [
    {
        "name": "custom_hybrow_helpdesk",
        "logo": "/assets/custom_hybrow_helpdesk/desk/favicon.svg",
        "title": "Custom Hybrow Helpdesk",
        "route": "/helpdesk",
        "has_permission": "custom_hybrow_helpdesk.api.permission.has_app_permission",
    }
]

after_install = "custom_hybrow_helpdesk.setup.install.after_install"
after_migrate = [
    "custom_hybrow_helpdesk.search.build_index_in_background",
    "custom_hybrow_helpdesk.search.download_corpus",
]

scheduler_events = {
    "all": [
        "custom_hybrow_helpdesk.search.build_index_if_not_exists",
        "custom_hybrow_helpdesk.search.download_corpus",
    ],
    "daily": [
        "custom_hybrow_helpdesk.helpdesk.doctype.hd_ticket.hd_ticket.close_tickets_after_n_days"
    ],
}


website_route_rules = [
    {
        "from_route": "/helpdesk/<path:app_path>",
        "to_route": "custom_hybrow_helpdesk",
    },
]

user_invitation = {
    "allowed_roles": {
        "Agent Manager": ["Agent", "Agent Manager"],
        "System Manager": ["Agent", "Agent Manager", "System Manager"],
    },
    "after_accept": "custom_hybrow_helpdesk.helpdesk.hooks.user_invitation.after_accept",
}

doc_events = {
    "Contact": {
        "before_insert": "custom_hybrow_helpdesk.overrides.contact.before_insert",
    },
    "Assignment Rule": {
        "on_trash": "custom_hybrow_helpdesk.extends.assignment_rule.on_assignment_rule_trash",
    },
}

has_permission = {
    "HD Ticket": "custom_hybrow_helpdesk.helpdesk.doctype.hd_ticket.hd_ticket.has_permission",
}

permission_query_conditions = {
    "HD Ticket": "custom_hybrow_helpdesk.helpdesk.doctype.hd_ticket.hd_ticket.permission_query",
}

# DocType Class
# ---------------
# Override standard doctype classes
override_doctype_class = {
    "Email Account": "custom_hybrow_helpdesk.overrides.email_account.CustomEmailAccount",
}

ignore_links_on_delete = [
    "HD Notification",
    "HD Ticket Comment",
]

# setup wizard
# setup_wizard_requires = "assets/custom_hybrow_helpdesk/js/setup_wizard.js"
# setup_wizard_stages = "custom_hybrow_helpdesk.setup.setup_wizard.get_setup_stages"
setup_wizard_complete = "custom_hybrow_helpdesk.setup.setup_wizard.setup_complete"


# Testing
# ---------------

before_tests = "custom_hybrow_helpdesk.test_utils.before_tests"
