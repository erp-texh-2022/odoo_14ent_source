# -*- coding: utf-8 -*-
{
    'name': 'US - Accounting Reports',
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
        Accounting reports for US
    """,
    'website': 'https://www.kamel_chaker.com/page/accounting',
    'depends': [
        'l10n_us', 'account_reports'
    ],
    'data': [
        'data/account_financial_report_data.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
