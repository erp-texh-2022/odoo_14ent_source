# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class SocialStream(models.Model):
    """"social.streams are used to fill the 'Feed' view that allows users to follow the social.media activity
    based on their interest (a Facebook Page, a Twitter hashtag, ...).

    They use the social.media third party API to fetch the stream data and create social.stream.posts
    that are displayed on the Feed kanban view. """

    _name = 'social.stream'
    _description = 'Social Stream'
    _order = 'sequence asc, id asc'

    name = fields.Char("Title", translate=True)
    media_id = fields.Many2one('social.media', string="Social Media", required=True)
    media_image = fields.Binary(related='media_id.image', string="The related Social Media's image")
    sequence = fields.Integer('Sequence', help="Sequence used to order streams (mainly for the 'Feed' kanban view)")
    account_id = fields.Many2one('social.account', 'Social Account', required=True, ondelete='cascade')
    stream_type_id = fields.Many2one('social.stream.type', string="Type", required=True, ondelete='cascade')
    stream_type_type = fields.Char(related='stream_type_id.stream_type')

    @api.onchange('media_id', 'account_id')
    def _onchange_media_id(self):
        for stream in self:
            stream.stream_type_id = False
            if stream.account_id and stream.account_id.media_id != stream.media_id:
                stream.account_id = False

    @api.model_create_multi
    def create(self, vals_list):
        res = super(SocialStream, self).create(vals_list)
        res._apply_default_name()
        for stream in res:
            stream._fetch_stream_data()
        return res

    @api.model
    def refresh_all(self):
        """ Fetches the stream.post based on third party API endpoints (Facebook/Twitter/...) and inserts new stream.posts into database.
        If any post is inserted into a stream created by the current user, the method returns 'True' to indicate caller that
        changes were made and a refresh is required.

        That means it will not always match the filter used on the view but it's the most common use case so it's not an issue.
        (For cases when it does not match the user's filter, the view will need simple to be refreshed manually). """

        new_content = False
        for stream in self.env['social.stream'].search([]):
            new_content |= stream._fetch_stream_data()

        return new_content

    def _fetch_stream_data(self):
        """ Every social module should override this method.

        This is the method responsible for creating the social.stream.posts using the social.media
        third party API.

        It will be called manually every time we need to refresh the social.stream data:
            - social.stream creation/edition
            - 'Feed' kanban loading
            - 'Refresh' button on 'Feed' kanban
            - ...

        This method should return 'True' if new social.posts are inserted,  please check the 'refresh_all' method for
        further implementation instructions. """

        self.ensure_one()

    def _apply_default_name(self):
        for stream in self:
            stream.write({'name': stream.stream_type_id.name})
