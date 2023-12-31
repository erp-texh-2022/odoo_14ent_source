# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

from . import models
from . import report
from . import controllers

def post_init(cr, registry):
    from odoo import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})
    env['project.project'].search([('is_fsm', '=', True)]).write({'allow_worksheets': True})
    fsm_project = env.ref("industry_fsm.fsm_project", raise_if_not_found=False)
    fsm_worksheet_template2 = env.ref("industry_fsm_report.fsm_worksheet_template2", raise_if_not_found=False)
    if fsm_project:
        template_id = fsm_worksheet_template2 or env.ref("industry_fsm_report.fsm_worksheet_template")
        fsm_project.write(
            {
                "worksheet_template_id": template_id.id,
            }
        )

    fsm_product = env.ref("industry_fsm.field_service_product", raise_if_not_found=False)
    if fsm_product:
        fsm_product.write(
            {"worksheet_template_id": env.ref("industry_fsm_report.fsm_worksheet_template").id,}
        )
