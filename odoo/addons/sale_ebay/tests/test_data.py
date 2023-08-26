# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

# a full answer (anonymised) as given by eBay for a GetOrders request
EBAY_ANSWER_1 = {'Ack': 'Success',
 'Build': 'E1125_CORE_APIXO_19065730_R1',
 'HasMoreOrders': 'false',
 'OrderArray': {'Order': [{'AdjustmentAmount': {'_currencyID': 'USD',
                                                'value': '0.0'},
                           'AmountPaid': {'_currencyID': 'USD',
                                          'value': '21.45'},
                           'AmountSaved': {'_currencyID': 'USD',
                                           'value': '0.0'},
                           'BuyerUserID': 'happy_consumer',
                           'CheckoutStatus': {'IntegratedMerchantCreditCardEnabled': 'false',
                                              'LastModifiedTime': '2019-09-13T14:29:00.000Z',
                                              'PaymentMethod': 'PayPal',
                                              'Status': 'Complete',
                                              'eBayPaymentStatus': 'NoPaymentFailure'},
                           'CreatedTime': '2019-09-09T21:55:48.000Z',
                           'EIASToken': 'nY+sHZ2abcdefgh+sEZ22Pr+dj6x9nY+seQ==',
                           'IntegratedMerchantCreditCardEnabled': 'false',
                           'IsMultiLegShipping': 'false',
                           'OrderID': '22221988-17892013',
                           'OrderStatus': 'Completed',
                           'PaidTime': '2019-09-09T21:55:48.000Z',
                           'PaymentHoldStatus': 'None',
                           'PaymentMethods': 'PayPal',
                           'SellerEmail': 'paypal@kamel_chaker.com',
                           'ShippedTime': '2019-09-10T19:57:43.000Z',
                           'ShippingAddress': {'AddressID': '2988222222013',
                                               'AddressOwner': 'eBay',
                                               'CityName': 'New York',
                                               'Country': 'US',
                                               'CountryName': 'United States',
                                               'ExternalAddressID': None,
                                               'Name': 'New York Times',
                                               'Phone': '8006984637',
                                               'PostalCode': '10018',
                                               'StateOrProvince': 'NY',
                                               'Street1': '620 Eighth Avenue',
                                               'Street2': None},
                           'ShippingDetails': {'GetItFast': 'false',
                                               'InternationalShippingServiceOption': [{'ShipToLocation': 'Worldwide',
                                                                                       'ShippingService': 'USPSPriorityMailInternational',
                                                                                       'ShippingServicePriority': '1'},
                                                                                      {'ShipToLocation': 'Worldwide',
                                                                                       'ShippingService': 'UPSWorldWideExpressPlus',
                                                                                       'ShippingServicePriority': '2'},
                                                                                      {'ShipToLocation': 'Worldwide',
                                                                                       'ShippingService': 'UPSWorldWideExpress',
                                                                                       'ShippingServicePriority': '3'},
                                                                                      {'ShipToLocation': 'Worldwide',
                                                                                       'ShippingService': 'UPSWorldWideExpedited',
                                                                                       'ShippingServicePriority': '4'}],
                                               'SalesTax': {'SalesTaxAmount': {'_currencyID': 'USD',
                                                                               'value': '0.0'},
                                                            'SalesTaxPercent': '0.0',
                                                            'SalesTaxState': None,
                                                            'ShippingIncludedInTax': 'false'},
                                               'SellingManagerSalesRecordNumber': '4444',
                                               'ShippingServiceOptions': [{'ExpeditedService': 'false',
                                                                           'ShippingService': 'USPSPriority',
                                                                           'ShippingServicePriority': '1',
                                                                           'ShippingTimeMax': '3',
                                                                           'ShippingTimeMin': '1'},
                                                                          {'ExpeditedService': 'false',
                                                                           'ShippingService': 'FedExHomeDelivery',
                                                                           'ShippingServicePriority': '2',
                                                                           'ShippingTimeMax': '5',
                                                                           'ShippingTimeMin': '1'},
                                                                          {'ExpeditedService': 'false',
                                                                           'ShippingService': 'FedEx2Day',
                                                                           'ShippingServicePriority': '3',
                                                                           'ShippingTimeMax': '2',
                                                                           'ShippingTimeMin': '1'},
                                                                          {'ExpeditedService': 'true',
                                                                           'ShippingService': 'FedExStandardOvernight',
                                                                           'ShippingServicePriority': '4',
                                                                           'ShippingTimeMax': '1',
                                                                           'ShippingTimeMin': '1'}]},
                           'ShippingServiceSelected': {'ShippingService': 'USPSPriority',
                                                       'ShippingServiceCost': {'_currencyID': 'USD',
                                                                               'value': '9.5'}},
                           'Subtotal': {'_currencyID': 'USD', 'value': '11.95'},
                           'Total': {'_currencyID': 'USD', 'value': '21.45'},
                           'TransactionArray': {'Transaction': [{'ActualHandlingCost': {'_currencyID': 'USD',
                                                                                        'value': '1.5'},
                                                                 'ActualShippingCost': {'_currencyID': 'USD',
                                                                                        'value': '8.0'},
                                                                 'Buyer': {'Email': 'nytnews@nytimes.com',
                                                                           'UserFirstName': None,
                                                                           'UserLastName': None},
                                                                 'CreatedDate': '2019-09-09T21:55:48.000Z',
                                                                 'Item': {'ConditionDisplayName': 'New',
                                                                          'ConditionID': '1000',
                                                                          'ItemID': '222222',
                                                                          'SKU': '4032498228365',
                                                                          'Site': 'US',
                                                                          'Title': 'Product'},
                                                                 'OrderLineItemID': '22221988-17892013',  # same as OrderId in this case
                                                                 'Platform': 'eBay',
                                                                 'QuantityPurchased': '1',
                                                                 'ShippingDetails': {'CalculatedShippingRate': {'OriginatingPostalCode': '44408',
                                                                                                                'PackagingHandlingCosts': {'_currencyID': 'USD',
                                                                                                                                           'value': '1.5'},
                                                                                                                'ShippingIrregular': 'false',
                                                                                                                'ShippingPackage': 'PackageThickEnvelope',
                                                                                                                'WeightMajor': {'_measurementSystem': 'English',
                                                                                                                                '_unit': 'lbs',
                                                                                                                                'value': '0'},
                                                                                                                'WeightMinor': {'_measurementSystem': 'English',
                                                                                                                                '_unit': 'oz',
                                                                                                                                'value': '4'}},
                                                                                     'SellingManagerSalesRecordNumber': '4444',
                                                                                     'ShipmentTrackingDetails': {'ShipmentTrackingNumber': '9999',
                                                                                                                 'ShippingCarrierUsed': 'USPS'}},
                                                                 'Status': {'PaymentHoldStatus': 'None'},
                                                                 'Taxes': {'TaxDetails': {'Imposition': 'SalesTax',  # here it's a dict, but can be a list of dicts
                                                                                          'TaxAmount': {'_currencyID': 'USD',
                                                                                                        'value': '0.0'},
                                                                                          'TaxDescription': 'SalesTax',
                                                                                          'TaxOnHandlingAmount': {'_currencyID': 'USD',
                                                                                                                  'value': '0.0'},
                                                                                          'TaxOnShippingAmount': {'_currencyID': 'USD',
                                                                                                                  'value': '0.0'},
                                                                                          'TaxOnSubtotalAmount': {'_currencyID': 'USD',
                                                                                                                  'value': '0.0'}},
                                                                           'TotalTaxAmount': {'_currencyID': 'USD',
                                                                                              'value': '0.0'}},
                                                                 'TransactionID': '1718129248013',
                                                                 'TransactionPrice': {'_currencyID': 'USD',
                                                                                      'value': '11.95'},
                                                                 'TransactionSiteID': 'US'}]}},
                           {'AdjustmentAmount': {'_currencyID': 'USD',
                                                                            'value': '0.0'},
                                                       'AmountPaid': {'_currencyID': 'USD',
                                                                      'value': '55.88'},
                                                       'AmountSaved': {'_currencyID': 'USD',
                                                                       'value': '3.94'},
                                                       'BuyerUserID': 'consume_product',
                                                       'CheckoutStatus': {'IntegratedMerchantCreditCardEnabled': 'false',
                                                                          'LastModifiedTime': '2019-08-24T20:27:57.000Z',
                                                                          'PaymentMethod': 'PayPal',
                                                                          'Status': 'Complete',
                                                                          'eBayPaymentStatus': 'NoPaymentFailure'},
                                                       'CreatedTime': '2019-08-22T05:37:46.000Z',
                                                       'CreatingUserRole': 'Buyer',
                                                       'EIASToken': 'nY+sHZ2222222222222222222+seQ==',
                                                       'IntegratedMerchantCreditCardEnabled': 'false',
                                                       'IsMultiLegShipping': 'false',
                                                       'OrderID': '2522222222217',
                                                       'OrderStatus': 'Completed',
                                                       'PaidTime': '2019-08-22T05:37:47.000Z',
                                                       'PaymentHoldStatus': 'None',
                                                       'PaymentMethods': 'PayPal',
                                                       'SellerEmail': 'paypal@kamel_chaker.com',
                                                       'ShippedTime': '2019-08-22T20:13:12.000Z',
                                                       'ShippingAddress': {'AddressID': '404444461017',
                                                                           'AddressOwner': 'eBay',
                                                                           'CityName': 'Baton Rouge',
                                                                           'Country': 'US',
                                                                           'CountryName': 'United States',
                                                                           'ExternalAddressID': None,
                                                                           'Name': 'Alvaro Lupinacci',
                                                                           'Phone': '555555555',
                                                                           'PostalCode': '8888-9999',
                                                                           'StateOrProvince': 'AZ',
                                                                           'Street1': '55555 W Sea Horse Rd',
                                                                           'Street2': None},
                                                       'ShippingDetails': {'GetItFast': 'false',
                                                                           'SalesTax': {'SalesTaxAmount': {'_currencyID': 'USD',
                                                                                                           'value': '0.0'},
                                                                                        'SalesTaxPercent': '0.0',
                                                                                        'SalesTaxState': None,
                                                                                        'ShippingIncludedInTax': 'false'},
                                                                           'SellingManagerSalesRecordNumber': '4555',
                                                                           'ShippingServiceOptions': {'ExpeditedService': 'false',
                                                                                                      'ShippingService': 'USPSFirstClass',
                                                                                                      'ShippingServicePriority': '1',
                                                                                                      'ShippingTimeMax': '3',
                                                                                                      'ShippingTimeMin': '2'}},
                                                       'ShippingServiceSelected': {'ShippingService': 'USPSFirstClass',
                                                                                   'ShippingServiceCost': {'_currencyID': 'USD',
                                                                                                           'value': '6.94'}},
                                                       'Subtotal': {'_currencyID': 'USD', 'value': '48.94'},
                                                       'Total': {'_currencyID': 'USD', 'value': '55.88'},
                                                       'TransactionArray': {'Transaction': [{'ActualHandlingCost': {'_currencyID': 'USD',
                                                                                                                    'value': '1.5'},
                                                                                             'ActualShippingCost': {'_currencyID': 'USD',
                                                                                                                    'value': '1.97'},
                                                                                             'Buyer': {'Email': 'Invalid '
                                                                                                                'Request',
                                                                                                       'UserFirstName': None,
                                                                                                       'UserLastName': None},
                                                                                             'CreatedDate': '2019-08-22T05:37:46.000Z',
                                                                                             'Item': {'ConditionDisplayName': 'New',
                                                                                                      'ConditionID': '1000',
                                                                                                      'ItemID': '232323712180',
                                                                                                      'SKU': 'UUUUUU',
                                                                                                      'Site': 'US',
                                                                                                      'Title': 'Great Product'},
                                                                                             'OrderLineItemID': '232323712180-1717176961013',
                                                                                             'Platform': 'eBay',
                                                                                             'QuantityPurchased': '1',
                                                                                             'ShippingDetails': {'CalculatedShippingRate': {'OriginatingPostalCode': '44444',
                                                                                                                                            'PackageDepth': {'_measurementSystem': 'English',
                                                                                                                                                             '_unit': 'inches',
                                                                                                                                                             'value': '3'},
                                                                                                                                            'PackageLength': {'_measurementSystem': 'English',
                                                                                                                                                              '_unit': 'inches',
                                                                                                                                                              'value': '10'},
                                                                                                                                            'PackageWidth': {'_measurementSystem': 'English',
                                                                                                                                                             '_unit': 'inches',
                                                                                                                                                             'value': '8'},
                                                                                                                                            'PackagingHandlingCosts': {'_currencyID': 'USD',
                                                                                                                                                                       'value': '1.5'},
                                                                                                                                            'ShippingIrregular': 'false',
                                                                                                                                            'ShippingPackage': 'PackageThickEnvelope',
                                                                                                                                            'WeightMajor': {'_measurementSystem': 'English',
                                                                                                                                                            '_unit': 'lbs',
                                                                                                                                                            'value': '0'},
                                                                                                                                            'WeightMinor': {'_measurementSystem': 'English',
                                                                                                                                                            '_unit': 'oz',
                                                                                                                                                            'value': '1'}},
                                                                                                                 'SellingManagerSalesRecordNumber': '4666',
                                                                                                                 'ShipmentTrackingDetails': {'ShipmentTrackingNumber': '944444444',
                                                                                                                                             'ShippingCarrierUsed': 'USPS'}},
                                                                                             'Status': {'PaymentHoldStatus': 'None'},
                                                                                             'Taxes': {'TaxDetails': {'Imposition': 'SalesTax',
                                                                                                                      'TaxAmount': {'_currencyID': 'USD',
                                                                                                                                    'value': '0.0'},
                                                                                                                      'TaxDescription': 'SalesTax',
                                                                                                                      'TaxOnHandlingAmount': {'_currencyID': 'USD',
                                                                                                                                              'value': '0.0'},
                                                                                                                      'TaxOnShippingAmount': {'_currencyID': 'USD',
                                                                                                                                              'value': '0.0'},
                                                                                                                      'TaxOnSubtotalAmount': {'_currencyID': 'USD',
                                                                                                                                              'value': '0.0'}},
                                                                                                       'TotalTaxAmount': {'_currencyID': 'USD',
                                                                                                                          'value': '0.0'}},
                                                                                             'TransactionID': '1717176961013',
                                                                                             'TransactionPrice': {'_currencyID': 'USD',
                                                                                                                  'value': '19.99'},
                                                                                             'TransactionSiteID': 'US'},
                                                                                            {'ActualHandlingCost': {'_currencyID': 'USD',
                                                                                                                    'value': '1.5'},
                                                                                             'ActualShippingCost': {'_currencyID': 'USD',
                                                                                                                    'value': '1.97'},
                                                                                             'Buyer': {'Email': 'Invalid '
                                                                                                                'Request',
                                                                                                       'UserFirstName': None,
                                                                                                       'UserLastName': None},
                                                                                             'CreatedDate': '2019-08-22T05:37:46.000Z',
                                                                                             'Item': {'ConditionDisplayName': 'New',
                                                                                                      'ConditionID': '1000',
                                                                                                      'ItemID': '262626665862',
                                                                                                      'Site': 'US',
                                                                                                      'Title': 'Great Product'},
                                                                                             'OrderLineItemID': '262626665862-2424246915016',
                                                                                             'Platform': 'eBay',
                                                                                             'QuantityPurchased': '1',
                                                                                             'ShippingDetails': {'CalculatedShippingRate': {'OriginatingPostalCode': '44444',
                                                                                                                                            'PackagingHandlingCosts': {'_currencyID': 'USD',
                                                                                                                                                                       'value': '1.5'},
                                                                                                                                            'ShippingIrregular': 'false',
                                                                                                                                            'ShippingPackage': 'PackageThickEnvelope',
                                                                                                                                            'WeightMajor': {'_measurementSystem': 'English',
                                                                                                                                                            '_unit': 'lbs',
                                                                                                                                                            'value': '0'},
                                                                                                                                            'WeightMinor': {'_measurementSystem': 'English',
                                                                                                                                                            '_unit': 'oz',
                                                                                                                                                            'value': '2'}},
                                                                                                                 'SellingManagerSalesRecordNumber': '4666',
                                                                                                                 'ShipmentTrackingDetails': {'ShipmentTrackingNumber': '9999999999',
                                                                                                                                             'ShippingCarrierUsed': 'USPS'}},
                                                                                             'Status': {'PaymentHoldStatus': 'None'},
                                                                                             'Taxes': {'TaxDetails': {'Imposition': 'SalesTax',
                                                                                                                      'TaxAmount': {'_currencyID': 'USD',
                                                                                                                                    'value': '0.0'},
                                                                                                                      'TaxDescription': 'SalesTax',
                                                                                                                      'TaxOnHandlingAmount': {'_currencyID': 'USD',
                                                                                                                                              'value': '0.0'},
                                                                                                                      'TaxOnShippingAmount': {'_currencyID': 'USD',
                                                                                                                                              'value': '0.0'},
                                                                                                                      'TaxOnSubtotalAmount': {'_currencyID': 'USD',
                                                                                                                                              'value': '0.0'}},
                                                                                                       'TotalTaxAmount': {'_currencyID': 'USD',
                                                                                                                          'value': '0.0'}},
                                                                                             'TransactionID': '2424246915016',
                                                                                             'TransactionPrice': {'_currencyID': 'USD',
                                                                                                                  'value': '28.95'},
                                                                                             'TransactionSiteID': 'US'}]}}
                                                      ]},
 'OrdersPerPage': '100',
 'PageNumber': '1',
 'PaginationResult': {'TotalNumberOfEntries': '1', 'TotalNumberOfPages': '1'},
 'ReturnedOrderCountActual': '1',
 'Timestamp': '2019-09-13T15:55:31.908Z',
 'Version': '1125'}