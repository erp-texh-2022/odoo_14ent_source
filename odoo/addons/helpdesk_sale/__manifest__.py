# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

{
    'name': 'Helpdesk After Sales',
    'category': 'Services/Helpdesk',
    'summary': 'Project, Tasks, After Sales',
    'depends': ['helpdesk', 'sale_management'],
    'auto_install': True,
    'description': """
Manage the after sale of the products from helpdesk tickets.
    """,
    'data': [
        'views/helpdesk_views.xml',
    ],
    'demo': ['data/helpdesk_sale_demo.xml'],
}
