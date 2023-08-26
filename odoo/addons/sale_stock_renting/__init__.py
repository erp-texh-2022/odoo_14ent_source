# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

from . import models
from . import wizard
from . import report

from odoo import api, SUPERUSER_ID

def _ensure_rental_stock_moves_consistency(cr, registry):
    """Ensure currently rented products are placed in rental location.

    If not, the rental stock moves generated at return would be inconsistent.
    """
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        query = """
            SELECT id FROM sale_order_line
            WHERE qty_delivered > qty_returned AND is_rental
        """
        env.cr.execute(query)
        res_ids = [x[0] for x in env.cr.fetchall()]
        lines_to_move = env['sale.order.line'].browse(res_ids)
        lines_to_move.mapped('company_id')._create_rental_location()
        for line in lines_to_move:
            line._move_qty(line.qty_delivered - line.qty_returned, line.order_id.warehouse_id.lot_stock_id, line.company_id.rental_loc_id)
