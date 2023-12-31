# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    background_image = fields.Binary(string="Home Menu Background Image", attachment=True)

    @api.model
    def create(self, vals):
        """Override to ensure a default exists for all studio-created company/currency fields."""
        new_company = super().create(vals)
        company_fields = self.env['ir.model.fields'].sudo().search([
            ('name', '=', 'x_studio_company_id'),
            ('ttype', '=', 'many2one'),
            ('relation', '=', 'res.company'),
            ('store', '=', True),
            ('state', '=', 'manual')
        ])
        for company_field in company_fields:
            self.env['ir.default'].set(company_field.model_id.model, company_field.name,
                                       new_company.id, company_id=new_company.id)
        currency_fields = self.env['ir.model.fields'].sudo().search([
            ('name', '=', 'x_studio_currency_id'),
            ('ttype', '=', 'many2one'),
            ('relation', '=', 'res.currency'),
            ('store', '=', True),
            ('state', '=', 'manual')
        ])
        for currency_field in currency_fields:
            self.env['ir.default'].set(currency_field.model_id.model, currency_field.name,
                                       new_company.currency_id.id,company_id=new_company.id)
        return new_company