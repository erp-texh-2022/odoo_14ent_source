# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

import base64
import io

from odoo.tests.common import SavepointCase
from PIL import Image
from datetime import datetime


class TestTimerButtons(SavepointCase):
    """ Test visibility of the following buttons:
        - START/STOP/PAUSE/RESUME
        - Send/Sign Report
    """

    @classmethod
    def setUpClass(cls):
        super(TestTimerButtons, cls).setUpClass()
        cls.customer = cls.env['res.partner'].create({'name': 'My Customer'})
        cls.env.company.timesheet_encode_uom_id = cls.env.ref('uom.product_uom_hour')
        cls.product_service = cls.env['product.product'].create({
            'name': 'My Service Product',
            'sale_ok': True,
            'type': 'service',
            'lst_price': 15,
        })
        cls.product_material = cls.env['product.product'].create({
            'name': 'My Material Product',
            'sale_ok': True,
            'invoice_policy': 'order',
            'lst_price': 5,
            'service_type': 'manual',
        })
        cls.project = cls.env['project.project'].create({
            'name': 'My Project',
            'partner_id': cls.customer.id,
            'allow_timesheet_timer': True,
            'allow_timesheets': True,
            'allow_worksheets': True,
            'allow_material': True,
            'allow_billable': True,
            'timesheet_product_id': cls.product_service.id,
            'is_fsm': True,
        })
        cls.task = cls.env['project.task'].create({
            'name': 'My Task',
            'project_id': cls.project.id,
            'partner_id': cls.customer.id,
            'worksheet_template_id': cls.env.ref('industry_fsm_report.fsm_worksheet_template').id,
        })

    def test_timer_buttons_01(self):
        # should not be visible if the task is marked as done
        self.task.fsm_done = True
        self.assertFalse(self.task.display_timer_start_primary)
        self.assertFalse(self.task.display_timer_start_secondary)
        self.assertFalse(self.task.display_timer_stop)
        self.assertFalse(self.task.display_timer_pause)
        self.assertFalse(self.task.display_timer_resume)

    def test_timer_buttons_02(self):
        # Start should be visible in non-primary if Time > 0
        self.env['account.analytic.line'].create({
            'task_id': self.task.id,
            'project_id': self.project.id,
            'date': datetime.now(),
            'name': 'My Timesheet',
            'user_id': self.env.uid,
            'unit_amount': 1,
        })
        self.assertTrue(self.task.total_hours_spent)
        self.assertFalse(self.task.display_timer_start_primary)
        self.assertTrue(self.task.display_timer_start_secondary)

    def test_timer_buttons_03(self):
        # Start should be visible in primary if Time = 0
        self.assertFalse(self.task.total_hours_spent)
        self.assertTrue(self.task.display_timer_start_primary)
        self.assertFalse(self.task.display_timer_start_secondary)

    def test_timer_buttons_04(self):
        # When the timer is not running, do not display: pause, stop, resume
        # when the timer is running, do not display the following buttons:
        # Start (Primary and secondary), Create sales Order, Mark as done,
        # Create Invoice, Sign report, Send report
        self.assertFalse(self.task.display_timer_pause)
        self.assertFalse(self.task.display_timer_stop)
        self.assertFalse(self.task.display_timer_resume)
        self.task.action_timer_start()
        self.assertTrue(self.task.display_timer_pause)
        self.assertTrue(self.task.display_timer_stop)
        self.assertFalse(self.task.display_timer_resume)
        self.assertFalse(self.task.display_timer_start_primary)
        self.assertFalse(self.task.display_timer_start_secondary)
        self.assertFalse(self.task.display_sign_report_primary)
        self.assertFalse(self.task.display_sign_report_secondary)
        self.assertFalse(self.task.display_send_report_primary)
        self.assertFalse(self.task.display_send_report_secondary)
        self.assertFalse(self.task.display_mark_as_done_primary)
        self.assertFalse(self.task.display_mark_as_done_secondary)
        self.assertFalse(self.task.display_create_invoice_primary)
        self.assertFalse(self.task.display_create_invoice_secondary)
        self.task.action_timer_pause()
        self.assertFalse(self.task.display_timer_pause)
        self.assertTrue(self.task.display_timer_resume)

    def test_timer_buttons_05(self):
        # only visible if the 'Timesheet Timer' feature is enabled on the project
        self.project.allow_timesheet_timer = False
        self.assertFalse(self.task.display_timer_start_primary)
        self.assertFalse(self.task.display_timer_start_secondary)
        self.assertFalse(self.task.display_timer_stop)
        self.assertFalse(self.task.display_timer_pause)
        self.assertFalse(self.task.display_timer_resume)

    def test_send_sign_report_buttons_01(self):
        # Sign/Send not visible if Time = 0 AND Worksheet = 0 AND Products = 0
        # Visible in non primary if Time > 0 OR Worksheet > 0 OR Products > 0
        # Visible in primary if Time > 0 AND Worksheet > 0 AND Products > 0
        # Send should be visible in primary if T,W,P > 0 and report not sent yet
        # Send should be visible in secondary if T || W || P > 0 or report already sent

        # Check Enabled Counter
        self.assertEqual(self.task.display_enabled_conditions_count, 3)
        self.project.allow_worksheets = False
        self.assertEqual(self.task.display_enabled_conditions_count, 2)
        self.project.allow_material = False
        self.assertEqual(self.task.display_enabled_conditions_count, 1)
        self.project.allow_timesheets = False
        self.assertEqual(self.task.display_enabled_conditions_count, 0)
        self.project.write({
            'allow_worksheets': True,
            'allow_material': True,
            'allow_timesheets': True,
            'timesheet_product_id': self.product_service.id,
        })
        self.assertEqual(self.task.display_enabled_conditions_count, 3)

        # Not visible
        self.assertFalse(self.task.display_sign_report_primary)
        self.assertFalse(self.task.display_sign_report_secondary)
        self.assertFalse(self.task.display_send_report_primary)
        self.assertFalse(self.task.display_send_report_secondary)

        # Secondary if time > 0 only
        self.assertEqual(self.task.display_satisfied_conditions_count, 0)
        timesheet = self.env['account.analytic.line'].create({
            'task_id': self.task.id,
            'project_id': self.project.id,
            'date': datetime.now(),
            'name': 'My Timesheet',
            'user_id': self.env.uid,
            'unit_amount': 1,
        })
        self.assertEqual(self.task.display_satisfied_conditions_count, 1)
        self.assertFalse(self.task.display_sign_report_primary)
        self.assertTrue(self.task.display_sign_report_secondary)
        self.assertFalse(self.task.display_send_report_primary)
        self.assertFalse(self.task.display_send_report_secondary) # Not signed yet
        timesheet.unlink()

        # Secondary if worksheet > 0 only
        self.assertEqual(self.task.display_satisfied_conditions_count, 0)
        worksheet = self.env[self.task.worksheet_template_id.model_id.model].create({
            'x_name': 'This is a name',
            'x_comments': 'This is a comment',
            'x_task_id': self.task.id,
        })
        # YTI FIXME: The triggers on the compute method are foireux
        self.task._compute_worksheet_count()
        self.assertEqual(self.task.display_satisfied_conditions_count, 1)
        self.assertTrue(self.task.worksheet_count)
        self.assertFalse(self.task.display_sign_report_primary)
        self.assertTrue(self.task.display_sign_report_secondary)
        self.assertFalse(self.task.display_send_report_primary)
        self.assertFalse(self.task.display_send_report_secondary) # Not signed yet
        worksheet.unlink()

        # Secondary if product > 0 only
        self.assertEqual(self.task.display_satisfied_conditions_count, 0)
        self.task._fsm_ensure_sale_order()
        self.product_material.with_context(fsm_task_id=self.task.id).fsm_add_quantity()
        self.assertEqual(self.task.display_satisfied_conditions_count, 1)
        self.assertTrue(self.task.material_line_product_count)
        self.assertFalse(self.task.display_sign_report_primary)
        self.assertTrue(self.task.display_sign_report_secondary)
        self.assertFalse(self.task.display_send_report_primary)
        self.assertFalse(self.task.display_send_report_secondary) # Not signed yet

        # Primary of all conditions met
        timesheet = self.env['account.analytic.line'].create({
            'task_id': self.task.id,
            'project_id': self.project.id,
            'date': datetime.now(),
            'name': 'My Timesheet',
            'user_id': self.env.uid,
            'unit_amount': 1,
        })
        self.assertEqual(self.task.display_satisfied_conditions_count, 2)
        worksheet = self.env[self.task.worksheet_template_id.model_id.model].create({
            'x_name': 'This is a name',
            'x_comments': 'This is a comment',
            'x_task_id': self.task.id,
        })
        # YTI FIXME: The triggers on the compute method are foireux
        self.task._compute_worksheet_count()
        self.assertEqual(self.task.display_satisfied_conditions_count, 3)
        self.assertTrue(self.task.display_sign_report_primary)
        self.assertFalse(self.task.display_sign_report_secondary)
        self.assertFalse(self.task.display_send_report_primary) # Report is not signed yet
        self.assertFalse(self.task.display_send_report_secondary) # Report is not signed yet

        # Send visible in primary if report is signed and not sent yet
        f = io.BytesIO()
        Image.new('RGB', (50, 50)).save(f, 'PNG')
        f.seek(0)
        image = base64.b64encode(f.read())
        self.task.worksheet_signature = image
        self.assertTrue(self.task.display_send_report_primary) # Report is signed, not sent yet
        self.assertFalse(self.task.display_send_report_secondary)
        self.task.fsm_is_sent = True
        self.assertFalse(self.task.display_send_report_primary)
        self.assertFalse(self.task.display_send_report_secondary) # Report is sent then do not display button

    def test_send_sign_report_button_02(self):
        # Sign not visible if the report is already signed
        f = io.BytesIO()
        Image.new('RGB', (50, 50)).save(f, 'PNG')
        f.seek(0)
        image = base64.b64encode(f.read())
        self.task.worksheet_signature = image
        self.assertFalse(self.task.display_sign_report_primary)
        self.assertFalse(self.task.display_sign_report_secondary)

    def test_send_sign_report_button_03(self):
        # Sign/send only visible if 'worksheets' is enabled on the project
        self.project.allow_worksheets = False
        self.assertFalse(self.task.display_sign_report_primary)
        self.assertFalse(self.task.display_sign_report_secondary)
        self.assertFalse(self.task.display_send_report_primary)
        self.assertFalse(self.task.display_send_report_secondary)

    def test_mark_as_done_01(self):
        # Visible in secondary if Time = 0 OR Worksheet = 0 OR Products = 0
        self.assertFalse(self.task.display_mark_as_done_primary)
        self.assertTrue(self.task.display_mark_as_done_secondary)

        # Not visible is not fsm task or already marked as done
        self.task.is_fsm = False
        self.assertFalse(self.task.display_mark_as_done_primary)
        self.assertFalse(self.task.display_mark_as_done_secondary)
        self.task.is_fsm = True
        self.task.fsm_done = True
        self.assertFalse(self.task.display_mark_as_done_primary)
        self.assertFalse(self.task.display_mark_as_done_secondary)
        self.task.fsm_done = False

        # Visible in non primary if Time > 0 OR Worksheet > 0 OR Products > 0
        timesheet = self.env['account.analytic.line'].create({
            'task_id': self.task.id,
            'project_id': self.project.id,
            'date': datetime.now(),
            'name': 'My Timesheet',
            'user_id': self.env.uid,
            'unit_amount': 1,
        })
        self.assertFalse(self.task.display_mark_as_done_primary)
        self.assertTrue(self.task.display_mark_as_done_secondary)

        # should be visible in primary if Time > 0 AND Worksheet > 0 AND Products > 0
        worksheet = self.env[self.task.worksheet_template_id.model_id.model].create({
            'x_name': 'This is a name',
            'x_comments': 'This is a comment',
            'x_task_id': self.task.id,
        })
        self.task._compute_worksheet_count()
        self.task._fsm_ensure_sale_order()
        self.product_material.with_context(fsm_task_id=self.task.id).fsm_add_quantity()
        self.assertTrue(self.task.display_mark_as_done_primary)
        self.assertFalse(self.task.display_mark_as_done_secondary)

    def test_create_invoice_01(self):
        # Not visible is not marked as done or not fully invoice or no billable activated
        self.assertFalse(self.task.display_create_invoice_primary)
        self.assertFalse(self.task.display_create_invoice_secondary)

        self.task._fsm_ensure_sale_order()

        self.product_material.with_context(fsm_task_id=self.task.id).fsm_add_quantity()
        self.task.sale_order_id.action_confirm()

        # SO is to invoice, but the task is not fsm_done
        self.assertFalse(self.task.display_create_invoice_primary)
        self.assertFalse(self.task.display_create_invoice_secondary)

        # should be visible in primary if the SO linked to the task has one of the
        # following invoice status: To Invoice, Upselling
        self.task.fsm_done = True
        self.assertEqual(self.task.sale_order_id.invoice_status, 'to invoice')
        self.assertTrue(self.task.display_create_invoice_primary)
        self.assertFalse(self.task.display_create_invoice_secondary)

        # Not visible if the SO is canceled
        old_state = self.task.sale_order_id.state
        self.task.sale_order_id.state = 'cancel'
        self.assertFalse(self.task.display_create_invoice_primary)
        self.assertFalse(self.task.display_create_invoice_secondary)
        self.task.sale_order_id.state = old_state

        # only visible if the Billable feature is enabled on the project
        self.project.allow_billable = False
        self.assertFalse(self.task.display_create_invoice_primary)
        self.assertFalse(self.task.display_create_invoice_secondary)
        self.project.allow_billable = True

        # should be visible in non primary if the SO linked to the task has
        # the 'Nothing to invoice' invoice status
        new_product = self.env['product.product'].create({
            'name': 'Invoice on delivery product',
            'sale_ok': True,
            'invoice_policy': 'delivery',
            'service_type': 'manual',
            'list_price': 90.0,
        })
        new_line = self.env['sale.order.line'].create({
            'order_id': self.task.sale_order_id.id,
            'product_id': new_product.id,
            'price_unit': 10,
            'product_uom_qty': 1,
        })
        self.task.sale_order_id._create_invoices()
        self.assertEqual(self.task.sale_order_id.invoice_status, 'no')
        self.assertFalse(self.task.display_create_invoice_primary)
        self.assertTrue(self.task.display_create_invoice_secondary)

        # Should not be visible after the order is fully invoiced
        new_line.product_uom_qty = 0
        invoice = self.task.sale_order_id.invoice_ids
        self.assertEqual(self.task.sale_order_id.invoice_status, 'invoiced')
        self.assertFalse(self.task.display_create_invoice_primary)
        self.assertFalse(self.task.display_create_invoice_secondary)

    def test_create_sale_order_01(self):
        # If customer is set on the project, and if there is no sale_line_id
        # create order should be visible
        product_task_in_project = self.env['product.product'].create({
            'name': 'Task in Project Service',
            'type': 'service',
            'service_tracking': 'task_in_project',
        })

        order = self.env['sale.order'].create({
            'partner_id': self.task.partner_id.id,
            'order_line': [(0, 0, {
                'product_id': product_task_in_project.id,
                'product_uom_qty': 1,
                'price_unit': 15,
            })]
        })
        order.action_confirm()
        order.flush()
        project = order.order_line.project_id
        self.assertTrue(project.sale_line_id)
        self.assertTrue(project.partner_id)
        self.assertFalse(project.display_create_order)

        self.project.allow_billable = False
        self.assertTrue(self.project.partner_id)
        self.assertFalse(self.project.sale_line_id)
        self.assertFalse(self.project.sale_order_id)
        self.assertFalse(self.project.display_create_order)

    def test_create_sale_order_02(self):
        # If allow_billable is true, "create sales order' should not be visible on tasks and project
        # as it's a fsm project.
        self.project.allow_billable = True
        # self.assertTrue(self.project.billable_type != 'no')
        self.assertFalse(self.project.display_create_order)
        self.assertFalse(self.task.display_create_order)

        # If allow_billable is false, "create sales order' should not be visible on project
        # but no on the tasks. There we could be on project rate, on employee rate
        self.project.allow_billable = False
        self.assertFalse(self.project.display_create_order)
        self.assertFalse(self.task.display_create_order)
