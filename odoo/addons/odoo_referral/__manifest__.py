# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.
{
    'name': "KamelChaker referral program",
    'summary': """Allow you to refer your friends to Odoo and get rewards""",
    'category': 'Hidden',
    'version': '1.0',
    'depends': ['base', 'web'],
    'data': [
        'views/templates.xml',
    ],
    'qweb': [
        "static/src/xml/systray.xml",
    ],
    'auto_install': True,
}
