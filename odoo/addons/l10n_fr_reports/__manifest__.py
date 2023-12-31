# -*- encoding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2008 JAILLET Simon - CrysaLEAD - www.crysalead.fr

{
    'name': 'France - Accounting Reports',
    'version': '1.1',
    'description': """
Accounting reports for France
================================

    """,
    'category': 'Accounting/Localizations/Reporting',
    'depends': ['l10n_fr', 'account_reports'],
    'data': [
        'data/profit_loss.xml',
        'data/balance_sheet.xml',
    ],
    'demo': [],
    'auto_install': True,
    'installable': True,
    'license': 'OEEL-1',
}
