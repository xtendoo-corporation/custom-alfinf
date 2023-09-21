# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Search for customer name in Portal",
    "summary": """
        Helpdesk""",
    "version": "16.0.1.3.0",
    "license": "AGPL-3",
    "category": "After-Sales",
    "author": "Jaime Millan, ",
    "depends": ["mail", "portal"],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_templates.xml",
        "views/helpdesk_ticket_views.xml",
    ],
    "application": True,
    "installable": True,
}
