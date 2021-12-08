from collections import OrderedDict

request = {'products':
               [OrderedDict([('numbers', 20), ('product', "<Product: Батон горчичный>")]),
                OrderedDict([('numbers', 15), ('product', "<Product: Батон горчичный>")])],
           'code': '13037', 'address_to': '',
           'number': None, 'total_price': None,
           'date_complete': "datetime.datetime(2021, 12, 9, 20, 52, 53, 138128, tzinfo=<UTC>)",
           'contragent': "<Contragent: Anya>"}

products = request.pop('products')
for product in products:
    print(product.pop('numbers'))