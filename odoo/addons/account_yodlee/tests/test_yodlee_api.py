# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

from unittest.mock import patch
from odoo.addons.account.tests.common import AccountTestInvoicingCommon
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.tests import tagged
from odoo import fields, tools
import requests
import json

class MockResponse:
    def __init__(self, url, text, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.text = text
        self.url = url

    def json(self):
        if type(self.json_data) == dict:
            return self.json_data
        else:
            raise ValueError

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(self)

@tagged('post_install', '-at_install')
class TestYodleeApi(AccountTestInvoicingCommon):

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass(chart_template_ref=chart_template_ref)
        cls.db_name = cls.env.cr.dbname
        cls.db_uid = cls.env['ir.config_parameter'].get_param('database.uuid')
        cls.url = 'https://onlinesync.kamel_chaker.com/yodlee/api/2'
        cls.no_account = False
        cls.online_identifier = '2829798'
        cls.online_bank_number = '836726'
        cls.online_vendor_name = False
        cls.statement_count = 1

        cls.env.user.groups_id |= cls.env.ref('base.group_system')
        cls.env.user.groups_id |= cls.env.ref('base.group_user')

        cls.company_data['company'].partner_id.email = 'test@xyz.com'

        cls.bank_journal = cls.env['account.journal'].create({
            'name': 'Bank journal - plaid',
            'code': 'TEST',
            'type': 'bank',
        })

        # Create the initial statement.
        initial_statement = cls.env['account.bank.statement'].create({
            'journal_id': cls.bank_journal.id,
            'date': '%s-01-01' % datetime.today().strftime('%Y'),
            'balance_start': 5103.0,
            'balance_end_real': 9944.87,
            'line_ids': [
                (0, 0, {'payment_ref': 'line1', 'amount': 750.0}),
                (0, 0, {'payment_ref': 'line2', 'amount': 1275.0}),
                (0, 0, {'payment_ref': 'line3', 'amount': -32.58}),
                (0, 0, {'payment_ref': 'line4', 'amount': 650.0}),
                (0, 0, {'payment_ref': 'line5', 'amount': 2000.0}),
                (0, 0, {'payment_ref': 'line6', 'amount': 102.78}),
                (0, 0, {'payment_ref': 'line7', 'amount': 96.67}),
            ],
        })
        initial_statement.button_post()

    def setUp(self):
        super().setUp()
        patcher_post = patch('odoo.addons.account_yodlee.models.yodlee.requests.post', side_effect=self.yodlee_post)
        patcher_get = patch('odoo.addons.account_yodlee.models.yodlee.requests.get', side_effect=self.yodlee_get)
        patcher_post.start()
        self.addCleanup(patcher_post.stop)
        patcher_get.start()
        self.addCleanup(patcher_get.stop)

    def create_account_provider(self):
        return self.env['account.online.provider'].create({
            'name': 'test',
            'provider_type': 'yodlee', 
            'provider_account_identifier': '123',
            'provider_identifier': 'inst_1',
            'status': 'SUCCESS',
            'status_code': 0,
            'account_online_journal_ids': [
                (0, 0, {
                    'name': 'myAccount', 
                    'account_number': '0000', 
                    'online_identifier': '801503', 
                    'balance': 500.0, 
                    'last_sync': datetime.today() - relativedelta(days=15),
                }),
            ],
        })

    # Method that simulate succesfull requests.post and response
    # Post request are only used in create user and get token for cobrand and user
    def yodlee_post(self, *args, **kwargs):
        resp = {
            "user": {
                "id": "1111484545",
                "loginName": "LOGINNAME",
                "name": {
                    "first": "FNAME",
                    "last": "LNAME"
                },
                "session": {
                    "userSession": "0654564_0:45334565b43546ffe354a5"
                },
                "preferences": {
                    "currency": "USD",
                    "timeZone": "PST",
                    "dateFormat": "MM/dd/yyyy",
                    "locale": "en_US"
                }
            }
        }
        if kwargs['url'] == self.url+'/user/register':
            return MockResponse(kwargs['url'], '', resp, 200)
        elif kwargs['url'] == self.url+'/cobrand/login':
            self.assertEqual(json.loads(kwargs['data']), json.loads('{"cobrand": {"cobrandLogin": "'+self.db_name+'", "cobrandPassword": "'+self.db_uid+'"}}'))
            resp = {    
                "cobrandId" : "10000004", 
                "applicationId" : "17CBE222A42161A5GG896M47CF4C1A00", 
                "session" : {
                    "cobSession": "06142010_0:4044d058bb39ae11f52584f11189f75bba5" 
                },
                "locale" : "en_US"
            }
            return MockResponse(kwargs['url'], '', resp, 200)
        elif kwargs['url'] == self.url+'/user/login':
            self.assertTrue(kwargs['headers'].get('Authorization'), 'headers should have authorization key present')
            return MockResponse(kwargs['url'], '', resp, 200)
        elif kwargs['url'] == self.url+'/add_institution':
            return MockResponse(kwargs['url'], '', {'add': True}, 200)
        else:
            self.assertEqual(args[0], ' ', 'Call to that url not supposed to happen')

    # Method that simulate the GET requests of yodlee
    def yodlee_get(self, *args, **kwargs):
        self.assertTrue(kwargs['headers'].get('Authorization'), 'headers should have authorization key present')
        if kwargs['url'] == self.url + '/accounts':
            if self.no_account:
                return MockResponse(kwargs['url'], '', {}, 200)
            self.assertEqual(kwargs['params'], {'providerAccountId': '123'})
            resp = {
                "account": [
                   {
                      "CONTAINER": "bank",
                      "providerAccountId": 12345,
                      "accountName": "SMB account",
                      "id": 801503,
                      "accountNumber": "xxxx4933",
                      "availableBalance": {
                         "amount": 4699,
                         "currency": "USD"
                      },
                      "accountType": "SAVINGS",
                      "createdDate": "2016-08-25T09:16:32Z",
                      "isAsset": True,
                      "isManual": False,
                      "balance": {
                         "amount": 84699,
                         "currency": "USD"
                      },
                      "providerId": 16441,
                      "providerName": "Dag Site",
                      "overDraftLimit": {
                         "amount": 654,
                         "currency": "INR"
                      },
                      "refreshinfo": {
                         "statusCode": 0,
                         "statusMessage": "OK",
                         "lastRefreshed": "2015-09-20T14:46:23Z",
                         "lastRefreshAttempt": "2015-09-20T14:46:23Z",
                         "nextRefreshScheduled": "2015-09-23T14:46:23Z"
                      }, 
                      "accountStatus": "ACTIVE"
                   }
                ]
            }
            return MockResponse(kwargs['url'], '', resp, 200)
        elif kwargs['url'] == self.url + '/providerAccounts/123':
            resp = {
                "providerAccount": {
                    "id": 123,
                    "providerId":16441,
                    "lastUpdated":"2016-08-21T07:18:32Z",
                    "isManual":False,
                    "createdDate":"2016-08-21",
                    "aggregationSource": "USER",
                    "refreshInfo": {
                       "statusCode": 0,
                       "statusMessage": "OK",
                       "status": "SUCCESS",
                       "nextRefreshScheduled": datetime.strftime(datetime.today(), '%Y-%m-%d'),
                       "lastRefreshed": datetime.strftime(datetime.today(), '%Y-%m-%d'),
                       "lastRefreshAttempt": datetime.strftime(datetime.today(), '%Y-%m-%d')
                    }
                }
            }
            return MockResponse(kwargs['url'], '', resp, 200)
        elif kwargs['url'] == self.url + '/transactions':
            resp = {
               "transaction": [
               {
                  "CONTAINER": "bank",
                  "id": self.online_identifier,
                  "amount": {
                    "amount": 12345.12,
                    "currency": "USD"
                  },
                  "runningBalance":{
                    "amount": 1000,
                    "currency": "USD"
                  },
                  "baseType": "DEBIT",
                  "categoryType": "EXPENSE",
                  "categoryId": 143,
                  "category": "Electronics / General Merchandise",
                  "categorySource": "SYSTEM",
                  "highLevelCategoryId": 10000004,
                  "date": datetime.strftime(datetime.today(), '%Y-%m-%d'),
                  "transactionDate": datetime.strftime(datetime.today(), '%Y-%m-%d'),
                  "postDate": datetime.strftime(datetime.today(), '%Y-%m-%d'),
                  "description":{
                    "original": "0150 Amazon  Santa Ana CA 55.73USD",
                    "consumer": "Electronic Purchases",
                    "simple": "Amazon Purchase"
                  },
                  "isManual": False,
                  "status": "POSTED",
                  "accountId": self.online_bank_number,
                  "type":"DEBIT",
                  "subType": "DEBIT_CARD_WITHDRAWAL_AT_STORE",
                  "merchant":{
                    "id": self.online_vendor_name,
                    "source": "FACTUAL",
                    "name": "Amazon"
                  }
               }
               ]
            }
            return MockResponse(kwargs['url'], '', resp, 200)
        else:
            self.assertEqual(kwargs['url'], ' ', 'Call to that url not supposed to happen')

    def test_yodlee_create_institution(self):
        """ Test adding a new institution with yodlee """
        # Simulate a user that just complete the authentication process with yodlee, meaning we have received a
        # response with several information that will help us create the record
        
        # Patch request.post with defined method
        informations = json.dumps([{"providerAccountId":123,"bankName":"Dag Site","status":"SUCCESS","providerId":16441}])
        res = self.env['account.online.provider'].callback_institution(informations, 'add', self.bank_journal.id)
        acc_online_provider = self.env['account.online.provider'].search([('company_id', '=', self.company_data['company'].id)])
        self.assertEqual(len(acc_online_provider), 1, 'An account_online_provider should have been created')
        self.assertEqual(acc_online_provider.name, 'Dag Site')
        self.assertEqual(acc_online_provider.provider_type, 'yodlee')
        self.assertEqual(acc_online_provider.provider_account_identifier, '123')
        self.assertEqual(acc_online_provider.provider_identifier, '16441')
        self.assertEqual(acc_online_provider.status, 'SUCCESS')
        self.assertEqual(len(acc_online_provider.account_online_journal_ids), 1, 'An account should have been created with the account_online_provider')
        self.assertEqual(acc_online_provider.account_online_journal_ids.name, 'SMB account')
        self.assertEqual(acc_online_provider.account_online_journal_ids.account_number, 'xxxx4933')
        self.assertEqual(acc_online_provider.account_online_journal_ids.online_identifier, '801503')
        self.assertEqual(acc_online_provider.account_online_journal_ids.balance, 84699)

        # Try calling same method again, it should update previously created entry
        self.env['account.online.provider'].callback_institution(informations, 'add', self.bank_journal.id)
        acc_online_provider = self.env['account.online.provider'].search([('company_id', '=', self.company_data['company'].id)])
        self.assertEqual(len(acc_online_provider), 1, 'No new account_online_provider should have been created')
        self.assertEqual(len(acc_online_provider.account_online_journal_ids), 1, 'No new account_online_journal should have been created')

    def test_yodlee_create_institution_fail(self):
        """ Test adding a new institution with yodlee that failed"""
        # Simulate a user that just complete the authentication process with yodlee, meaning we have received a
        # response with several information that will help us create the record
        
        # Patch request.post with defined method
        self.no_account = True
        informations = json.dumps([{"providerAccountId":123,"bankName":"Dag Site","status":"FAILED",
            "reason":"crashMsg","providerId":16441}])
        res = self.env['account.online.provider'].callback_institution(informations, 'add', self.bank_journal.id)

        acc_online_provider = self.env['account.online.provider'].search([('company_id', '=', self.company_data['company'].id)])
        self.assertEqual(len(acc_online_provider), 1, 'An account_online_provider should have been created')
        self.assertEqual(acc_online_provider.name, 'Dag Site')
        self.assertEqual(acc_online_provider.provider_type, 'yodlee')
        self.assertEqual(acc_online_provider.provider_account_identifier, '123')
        self.assertEqual(acc_online_provider.provider_identifier, '16441')
        self.assertEqual(acc_online_provider.status, 'FAILED')

    def test_yodlee_create_institution_between(self):
        """ Test adding a new institution with yodlee where user left during process"""
        # Simulate a user that just complete the authentication process with yodlee, meaning we have received a
        # response with several information that will help us create the record
        
        # Patch request.post with defined method
        self.no_account = True
        informations = json.dumps([{"providerAccountId":123,"bankName":"Dag Site","status":"ACTION_ABANDONED","providerId":16441}])
        res = self.env['account.online.provider'].callback_institution(informations, 'add', self.bank_journal.id)

        acc_online_provider = self.env['account.online.provider'].search([('company_id', '=', self.company_data['company'].id)])
        self.assertEqual(len(acc_online_provider), 1, 'An account_online_provider should have been created')
        self.assertEqual(acc_online_provider.name, 'Dag Site')
        self.assertEqual(acc_online_provider.provider_type, 'yodlee')
        self.assertEqual(acc_online_provider.provider_account_identifier, '123')
        self.assertEqual(acc_online_provider.provider_identifier, '16441')
        self.assertEqual(acc_online_provider.status, 'ACTION_ABANDONED')

    def test_yodlee_fetch_transactions(self):
        """ Test receiving some transactions with yodlee """
        # Create fake account.online.provider
        acc_online_provider = self.create_account_provider()
        self.bank_journal.account_online_journal_id = acc_online_provider.account_online_journal_ids

        informations = json.dumps([{"providerAccountId":123,"bankName":"Dag Site","status":"SUCCESS","providerId":16441}])
        ret = self.env['account.online.provider'].callback_institution(informations, 'add', self.bank_journal.id)

        # Check that we've a bank statement with 3 lines (we assumed that the demo data have been loaded and a
        # bank statement has already been created, otherwise the statement should have 4 lines as a new one for
        # opening entry will be created)
        bank_stmt_all = self.env['account.bank.statement'].search([('journal_id', '=', self.bank_journal.id)])
        bank_stmt = bank_stmt_all[0]
        self.assertEqual(len(bank_stmt), 1, 'There should be at least one bank statement created')
        self.assertEqual(len(bank_stmt.line_ids), self.statement_count, 'The statement should have 1 lines')
        self.assertEqual(bank_stmt.state, 'open')
        self.assertEqual(bank_stmt.line_ids.payment_ref, '0150 Amazon  Santa Ana CA 55.73USD')
        self.assertEqual(bank_stmt.line_ids.amount, -12345.12)
        self.assertEqual(bank_stmt.line_ids.online_identifier, "2829798:bank")
        self.assertEqual(bank_stmt.line_ids.partner_id, self.env['res.partner']) #No partner defined on line
        self.assertEqual(acc_online_provider.account_online_journal_ids.last_sync, fields.Date.today())
            
        # Call again and check that we don't have any new transactions
        acc_online_provider.account_online_journal_ids.last_sync = fields.Date.today() - relativedelta(days=15)
        acc_online_provider.callback_institution(informations, 'add', self.bank_journal.id)
        bank_stmt = self.env['account.bank.statement'].search([('journal_id', '=', self.bank_journal.id)])
        self.assertEqual(len(bank_stmt), len(bank_stmt_all), 'There should not be a new statement created')
        self.assertEqual(len(bank_stmt[0].line_ids), self.statement_count, 'The existing statement should still have 1 lines')

    def test_yodlee_cron_fetch_transactions(self):
        """ Test receiving some transactions with yodlee using the cron"""
        # Create fake account.online.provider
        acc_online_provider = self.create_account_provider()
        self.bank_journal.account_online_journal_id = acc_online_provider.account_online_journal_ids

        acc_online_provider.cron_fetch_online_transactions()

        self.assertEqual(acc_online_provider.last_refresh, fields.Datetime.now().replace(hour=0, minute=0, second=0))

        # Check that we've a bank statement with 3 lines (we assumed that the demo data have been loaded and a
        # bank statement has already been created, otherwise the statement should have 4 lines as a new one for
        # opening entry will be created)
        bank_stmt = self.env['account.bank.statement'].search([('journal_id', '=', self.bank_journal.id)], limit=1)
        self.assertEqual(len(bank_stmt.line_ids), 1, 'The statement should have 1 lines')
        self.assertEqual(bank_stmt.state, 'open')
        self.assertEqual(bank_stmt.line_ids.payment_ref, '0150 Amazon  Santa Ana CA 55.73USD')
        self.assertEqual(bank_stmt.line_ids.amount, -12345.12)
        self.assertEqual(bank_stmt.line_ids.online_identifier, "2829798:bank")
        self.assertEqual(acc_online_provider.account_online_journal_ids.last_sync, fields.Date.today())

    def test_assign_partner_automatically(self):
        """ Test receiving some transactions with yodlee and assigning automatically to correct partner """
        # Create fake account.online.provider
        acc_online_provider = self.create_account_provider()
        self.bank_journal.account_online_journal_id = acc_online_provider.account_online_journal_ids

        agrolait = self.env['res.partner'].create({
            'name': 'Res Partner 2',
            'online_partner_bank_account': '836726',
        })

        informations = json.dumps([{"providerAccountId":123,"bankName":"Dag Site","status":"SUCCESS","providerId":16441}])
        ret = self.env['account.online.provider'].callback_institution(informations, 'add', self.bank_journal.id)

        bank_stmt = self.env['account.bank.statement'].search([('journal_id', '=', self.bank_journal.id)], limit=1)
        self.assertEqual(len(bank_stmt.line_ids), self.statement_count, 'The statement should have 1 lines')
        self.assertEqual(bank_stmt.state, 'open')
        self.assertEqual(bank_stmt.journal_id.id, self.bank_journal.id)
        self.assertEqual(bank_stmt.line_ids.amount, -12345.12)
        self.assertEqual(bank_stmt.line_ids.online_identifier, "2829798:bank")
        self.assertEqual(bank_stmt.line_ids.partner_id, agrolait)
        bank_stmt.button_reopen()
        bank_stmt.line_ids.write({'name': '/'})
        bank_stmt.unlink()

        # Check that partner assignation also work with vendor name
        self.online_bank_number = False
        self.online_vendor_name = "123"
        self.online_identifier = 'lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDjf'
        ASUSTeK = self.env.ref("base.res_partner_1")
        ASUSTeK.write({'online_partner_vendor_name': '123'})
        acc_online_provider.account_online_journal_ids[0].write({'last_sync': datetime.today() - relativedelta(days=15)})
        ret = self.env['account.online.provider'].callback_institution(informations, 'add', self.bank_journal.id)
        bank_stmt = self.env['account.bank.statement'].search([('journal_id', '=', self.bank_journal.id)], limit=1)
        self.assertEqual(len(bank_stmt.line_ids), self.statement_count, 'The statement should have 1 lines')
        self.assertTrue(bank_stmt.line_ids.online_identifier.startswith("lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDjf"))
        self.assertEqual(bank_stmt.line_ids.partner_id, ASUSTeK)
        bank_stmt.button_reopen()
        bank_stmt.line_ids.write({'name': '/'})
        bank_stmt.unlink()

        # Check that if we have both partner with same info, no partner is displayed
        self.online_identifier = 'lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDja'
        agrolait.write({'online_partner_vendor_name': '123'})
        acc_online_provider.account_online_journal_ids[0].write({'last_sync': datetime.today() - relativedelta(days=15)})
        ret = self.env['account.online.provider'].callback_institution(informations, 'add', self.bank_journal.id)
        bank_stmt = self.env['account.bank.statement'].search([('journal_id', '=', self.bank_journal.id)], limit=1)
        self.assertEqual(len(bank_stmt.line_ids), self.statement_count, 'The statement should have 1 lines')
        self.assertTrue(bank_stmt.line_ids.online_identifier.startswith("lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDja"))
        self.assertEqual(bank_stmt.line_ids.partner_id, self.env['res.partner'])
        bank_stmt.button_reopen()
        bank_stmt.line_ids.write({'name': '/'})
        bank_stmt.unlink()

        # Check that bank account number take precedence over vendor name
        self.online_bank_number = "836726"
        self.online_identifier = 'lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDjb'
        acc_online_provider.account_online_journal_ids[0].write({'last_sync': datetime.today() - relativedelta(days=15)})
        ret = self.env['account.online.provider'].callback_institution(informations, 'add', self.bank_journal.id)
        bank_stmt = self.env['account.bank.statement'].search([('journal_id', '=', self.bank_journal.id)], limit=1)
        self.assertEqual(len(bank_stmt.line_ids), self.statement_count, 'The statement should have 1 lines')
        self.assertTrue(bank_stmt.line_ids.online_identifier.startswith("lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDjb"))
        self.assertEqual(bank_stmt.line_ids.partner_id, agrolait)
