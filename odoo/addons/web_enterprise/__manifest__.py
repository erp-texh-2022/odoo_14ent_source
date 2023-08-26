# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web Enterprise',
    'category': 'Hidden',
    'version': '1.0',
    'description':
        """
KamelChaker Enterprise Web Client.
===========================

This module modifies the web addon to provide Enterprise design and responsiveness.
        """,
    'depends': ['web'],
    'auto_install': True,
    'data': [
        'views/webclient_templates.xml',
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    'license': 'OEEL-1',
}
