# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class HrAppraisalNote(models.Model):
    _name = "hr.appraisal.note"
    _description = "Appraisal Assessment Note"

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, required=True)
