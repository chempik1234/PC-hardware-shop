# from cloudipsp import Api, Checkout
# api = Api(merchant_id=1396424,
#           secret_key='test')
# checkout = Checkout(api=api)
# data = {
#     'merchant_id': 123456,
#     'amount': 250,
#     'currency': 'USD',
#     'card_number': '4444555566661111',
#     'expire_date': '12/30',
#     'cvv2': '111',
#     'custom': {
#         'customer': {
#             'label': 'Customer',
#             'value': 'John Doe'
#         },
#         'user_id': {
#             'label': 'User ID',
#             'value': 1234567890
#         }
#     }
# }
# url = checkout.url(data).get('checkout_url')