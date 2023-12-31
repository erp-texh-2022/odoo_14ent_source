# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

{
    'name': "Project Enterprise",
    'summary': """Bridge module for project and enterprise""",
    'description': """
Bridge module for project and enterprise
    """,
    'category': 'Services/Project',
    'version': '1.0',
    'depends': ['project', 'web_map', 'web_gantt'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/project_task_views.xml',
        'views/assets.xml',
    ],
    'auto_install': True,
    'license': 'OEEL-1',
}
