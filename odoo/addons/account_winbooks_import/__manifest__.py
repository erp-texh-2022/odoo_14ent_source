# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

{
    'name': "Account Winbooks Import",
    'summary': """Import Data From Winbooks""",
    'description': """
        Import Data From Winbooks
    """,
    'category': 'Accounting/Accounting',
    'depends': ['account_accountant', 'base_vat'],
    'external_dependencies': {'python': ['dbfread']},
    'data': [
        'security/ir.model.access.csv',
        'wizard/import_wizard_views.xml',
        'views/account_onboarding_templates.xml',
    ],
}
