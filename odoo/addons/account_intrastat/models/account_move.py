# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    intrastat_transport_mode_id = fields.Many2one('account.intrastat.code', string='Intrastat Transport Mode',
        readonly=True, states={'draft': [('readonly', False)]}, domain="[('type', '=', 'transport')]")
    intrastat_country_id = fields.Many2one('res.country', string='Intrastat Country',
        help='Intrastat country, arrival for sales, dispatch for purchases',
        readonly=True, states={'draft': [('readonly', False)]}, domain=[('intrastat', '=', True)])

    def _get_invoice_intrastat_country_id(self):
        ''' Hook allowing to retrieve the intrastat country depending of installed modules.
        :return: A res.country record's id.
        '''
        self.ensure_one()
        return self.partner_id.country_id.id

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        # OVERRIDE to set 'intrastat_country_id' depending of the partner's country.
        res = super(AccountMove, self)._onchange_partner_id()
        if self.partner_id.country_id.intrastat:
            self.intrastat_country_id = self._get_invoice_intrastat_country_id()
        else:
            self.intrastat_country_id = False
        return res


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    intrastat_transaction_id = fields.Many2one('account.intrastat.code', string='Intrastat', domain="[('type', '=', 'transaction')]")
    intrastat_product_origin_country_id = fields.Many2one('res.country', string='Product Country')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        res = super()._onchange_product_id()
        for line in self:
            line.intrastat_product_origin_country_id = line.product_id.product_tmpl_id.intrastat_origin_country_id
        return res
