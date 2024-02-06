# -*- coding: utf-8 -*-
{
    'name': 'Alfinf Account Analytic Line Date Finish',
    'version': '16.0.1.0.0',
    'category': 'Tools',
    'summary': 'Alfinf Account Analytic Line Date Finish',
    'license': 'AGPL-3',
    'author': 'Xtendoo',
    'depends': [
        'helpdesk_mgmt',
        'helpdesk_mgmt_timesheet',
        'project',
    ],
    'data': [
        'views/helpdesk_ticket_view.xml',
        'views/project_task_form_view.xml',
        'views/account_analytic_line_view.xml',
    ],
    'application': True,
}
