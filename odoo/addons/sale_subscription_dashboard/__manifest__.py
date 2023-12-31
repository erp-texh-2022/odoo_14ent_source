# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Subscription Dashboard',
    'version': '1.0',
    'depends': ['sale_subscription'],
    'description': """
Sale Subscription Dashboard
===========================
It adds dashboards to :
1) Analyse the recurrent revenue and other metrics for subscriptions
2) Analyse the subscriptions modifications by salesman and compute their value.
    """,
    'website': 'https://www.kamel_chaker.com/page/accounting',
    'category': 'Sales/Subscriptions',
    'data': [
        'views/sale_subscription_dashboard_views.xml',
        'views/assets.xml',
        'views/report_dashboard.xml',
    ],
    'demo': [
    ],
    'qweb': [
        "static/src/xml/sale_subscription_dashboard.xml",
    ],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
