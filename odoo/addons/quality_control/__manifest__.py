# -*- encoding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

{
    'name': 'Quality',
    'version': '1.0',
    'category': 'Manufacturing/Quality',
    'sequence': 120,
    'summary': 'Control the quality of your products',
    'website': 'https://www.kamel_chaker.com/page/quality-management-software',
    'depends': ['quality'],
    'description': """
Quality Control
===============
* Define quality points that will generate quality checks on pickings,
  manufacturing orders or work orders (quality_mrp)
* Quality alerts can be created independently or related to quality checks
* Possibility to add a measure to the quality check with a min/max tolerance
* Define your stages for the quality alerts
""",
    'data': [
        'data/quality_control_data.xml',
        'views/quality_templates.xml',
        'views/quality_views.xml',
        'views/stock_picking_views.xml',
    ],
    'demo': [
        'data/quality_control_demo.xml',
    ],
    'application': True,
    'license': 'OEEL-1',
}
