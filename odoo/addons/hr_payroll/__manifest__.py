#-*- coding:utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

{
    'name': 'Payroll',
    'category': 'Human Resources/Payroll',
    'sequence': 290,
    'summary': 'Manage your employee payroll records',
    'description': "",
    'installable': True,
    'application': True,
    'depends': [
        'hr_work_entry_contract',
        'mail',
        'web_dashboard',
    ],
    'data': [
        'security/hr_payroll_security.xml',
        'security/ir.model.access.csv',
        'wizard/hr_payroll_payslips_by_employees_views.xml',
        'wizard/hr_payroll_index_wizard_views.xml',
        'views/hr_contract_views.xml',
        'views/hr_salary_rule_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_payslip_input_views.xml',
        'views/hr_employee_views.xml',
        'data/hr_payroll_sequence.xml',
        'views/hr_payroll_report.xml',
        'data/hr_payroll_data.xml',
        'views/res_config_settings_views.xml',
        'views/report_contributionregister_templates.xml',
        'views/report_payslip_templates.xml',
        'views/hr_work_entry_views.xml',
        'views/resource_views.xml',
        'views/hr_payslip_template.xml',
        'views/hr_rule_parameter_views.xml',
        'views/hr_payroll_report_views.xml',
        'views/hr_payroll_menu.xml',
    ],
    'demo': ['data/hr_payroll_demo.xml'],
    'qweb': [
        "static/src/xml/payslip_tree_views.xml",
    ],
}
