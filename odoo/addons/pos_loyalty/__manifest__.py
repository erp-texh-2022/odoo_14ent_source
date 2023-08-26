# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.


{
    'name': 'Loyalty Program',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'summary': 'Loyalty Program for the Point of Sale ',
    'description': """

This module allows you to define a loyalty program in
the point of sale, where customers earn loyalty points
and get rewards.

""",
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_loyalty_views.xml',
        'views/pos_config_views.xml',
        'security/ir.model.access.csv',
        'views/pos_loyalty_templates.xml',
    ],
    'qweb': [
        'static/src/xml/OrderReceipt.xml',
        'static/src/xml/RewardButton.xml',
        'static/src/xml/PointsCounter.xml',
        'static/src/xml/Loyalty.xml',
    ],
    'demo': [
        'data/pos_loyalty_demo.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
