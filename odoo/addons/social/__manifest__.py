# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

{
    'name': 'Social Marketing',
    'category': 'Marketing/Social Marketing',
    'sequence': 175,
    'summary': 'Manage your social media and website visitors',
    'version': '1.0',
    'description': """Manage your social media and website visitors""",
    'website': 'https://www.kamel_chaker.com/page/social-marketing',
    'depends': ['web', 'mail', 'iap', 'link_tracker'],
    'qweb': [
        'static/src/xml/social_templates.xml',
    ],
    'data': [
        'security/social_security.xml',
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/assets.xml',
        'views/social_menu_views.xml',
        'views/social_account_views.xml',
        'views/social_live_post_views.xml',
        'views/social_media_views.xml',
        'views/social_post_views.xml',
        'views/social_stream_post_views.xml',
        'views/social_stream_views.xml',
        'views/res_config_settings_views.xml',
        'views/utm_campaign_views.xml',
        'views/social_templates.xml'
    ],
    'demo': [
        'data/social_demo.xml'
    ],
    'application': True,
    'installable': True,
}
