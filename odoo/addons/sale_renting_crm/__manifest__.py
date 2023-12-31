# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

{
    'name': 'Opportunity to Rental',
    'version': '1.0',
    'category': 'Hidden',
    'description': """
This module adds a shortcut on one or several opportunity cases in the CRM.
===========================================================================

This shortcut allows you to generate a rental order based on the selected case.
    """,
    'depends': ['sale_renting', 'crm'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'auto_install': True,
}
