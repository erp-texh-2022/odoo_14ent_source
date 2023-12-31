# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class SocialMediaPushNotifications(models.Model):
    _inherit = 'social.media'

    media_type = fields.Selection(selection_add=[('push_notifications', 'Push Notifications')])

    def action_add_account(self):
        self.ensure_one()

        if self.media_type != 'push_notifications':
            return super(SocialMediaPushNotifications, self).action_add_account()

        return None
