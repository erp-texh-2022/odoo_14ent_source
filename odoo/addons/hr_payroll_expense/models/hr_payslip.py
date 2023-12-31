# -*- coding:utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    input_line_ids = fields.One2many(compute='_compute_input_line_ids', store=True, readonly=False,
        states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    expense_sheet_ids = fields.One2many(
        'hr.expense.sheet', 'payslip_id', string='Expenses',
        help="Expenses to reimburse to employee.",
        states={'draft': [('readonly', False)], 'verify': [('readonly', False)]})
    expenses_count = fields.Integer(compute='_compute_expenses_count')

    @api.depends('expense_sheet_ids.expense_line_ids', 'expense_sheet_ids.payslip_id')
    def _compute_expenses_count(self):
        for payslip in self:
            payslip.expenses_count = len(payslip.mapped('expense_sheet_ids.expense_line_ids'))

    @api.onchange('input_line_ids')
    def _onchange_input_line_ids(self):
        expense_type = self.env.ref('hr_payroll_expense.expense_other_input', raise_if_not_found=False)
        if not self.input_line_ids.filtered(lambda line: line.input_type_id == expense_type):
            self.expense_sheet_ids.write({'payslip_id': False})

    @api.onchange('employee_id', 'struct_id', 'contract_id', 'date_from', 'date_to')
    def _onchange_employee(self):
        res = super()._onchange_employee()
        if self.state == 'draft':
            self.expense_sheet_ids = self.env['hr.expense.sheet'].search([
                ('employee_id', '=', self.employee_id.id),
                ('state', '=', 'approve'),
                ('payment_mode', '=', 'own_account'),
                ('refund_in_payslip', '=', True),
                ('payslip_id', '=', False)])
        return res

    @api.depends('expense_sheet_ids')
    def _compute_input_line_ids(self):
        expense_type = self.env.ref('hr_payroll_expense.expense_other_input', raise_if_not_found=False)
        for payslip in self:
            total = sum(payslip.expense_sheet_ids.mapped('total_amount'))
            if not total or not expense_type:
                payslip.input_line_ids = payslip.input_line_ids
                continue
            lines_to_keep = payslip.input_line_ids.filtered(lambda x: x.input_type_id != expense_type)
            input_lines_vals = [(5, 0, 0)] + [(4, line.id, False) for line in lines_to_keep]
            input_lines_vals.append((0, 0, {
                'amount': total,
                'input_type_id': expense_type
            }))
            payslip.update({'input_line_ids': input_lines_vals})

    def action_payslip_done(self):
        res = super(HrPayslip, self).action_payslip_done()
        for expense in self.expense_sheet_ids:
            expense.action_sheet_move_create()
            expense.set_to_paid()
        return res

    def open_expenses(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Reimbursed Expenses'),
            'res_model': 'hr.expense',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.mapped('expense_sheet_ids.expense_line_ids').ids)],
        }
