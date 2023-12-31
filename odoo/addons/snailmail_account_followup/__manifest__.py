# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

{
    'name': 'Snail Mail Follow-Up',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'summary': "Extension to send follow-up documents by post",
    'description': """
Extension to send follow-up documents by post
    """,
    'depends': ['snailmail_account', 'account_followup'],
    'data': [
        'security/ir.model.access.csv',
        'data/account_followup_data.xml',
        'views/account_followup_views.xml',
        'views/assets.xml',
        'wizard/followup_send_views.xml',
    ],
    'qweb': ['static/src/xml/account_followup_template.xml'],
    'demo': ['data/account_followup_demo.xml'],
    'auto_install': True,
    'license': 'OEEL-1',
}
