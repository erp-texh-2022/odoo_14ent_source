# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sell Helpdesk Timesheet',
    'category': 'Hidden',
    'summary': 'Project, Helpdesk, Timesheet and Sale Orders',
    'depends': ['helpdesk_timesheet', 'sale_timesheet'],
    'description': """
        Bill timesheets logged on helpdesk tickets.
    """,
    'auto_install': True,
    'data': [
        'views/helpdesk_views.xml',
        'views/helpdesk_portal_templates.xml',
    ],
    'demo': ['data/helpdesk_sale_timesheet_demo.xml'],
    'license': 'OEEL-1',
}
