# -*- encoding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.
{
    'name': 'Luxembourg - Accounting Reports',
    'version': '1.0',
    'description': """
Accounting reports for Luxembourg
=================================
    """,
    'category': 'Accounting/Localizations/Reporting',
    'depends': ['l10n_lu', 'account_reports'],
    'data': [
        'data/account_financial_html_report_pl.xml',
        'data/account_financial_html_report_pl_abr.xml',
        'data/account_financial_html_report_bs.xml',
        'data/account_financial_html_report_bs_abr.xml',
    ],
    'auto_install': True,
    'license': 'OEEL-1',
}
