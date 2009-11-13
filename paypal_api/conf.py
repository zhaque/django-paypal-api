from django.conf import settings
# coding=utf-8

API_ENDPOINT = getattr(settings, 'PAYPAL_API_ENDPOINT', 'https://api-3t.sandbox.paypal.com/nvp')

# 3TOKEN or UNIPAY
API_AUTHENTICATION_MODE = getattr(settings, 'PAYPAL_API_AUTHENTICATION_MODE', '3TOKEN')

# 3TOKEN credentials
API_USERNAME = getattr(settings, 'PAYPAL_API_USERNAME', 'seller_1257693211_biz_api1.brianguertin.com')
API_PASSWORD = getattr(settings, 'PAYPAL_API_PASSWORD', '1257693266')
API_SIGNATURE = getattr(settings, 'PAYPAL_API_SIGNATURE', 'AlMm2rZ2QE1i-UGTrqfmMnj7OJaRAlHv3HOgcS.Jahlx481Z3i9KjXI1')

API_TEST_CUSTOMER = getattr(settings, 'PAYPAL_API_TEST_CUSTOMER', 'site.d_1229679144_per@brianguertin.com')

# UNIPAY credential
# SUBJECT = "patcol_1257523559_biz@gmail.com"

# in seconds
HTTP_TIMEOUT = 15

VERSION = '60.0'

ACK_SUCCESS = 'SUCCESS'
ACK_SUCCESS_WITH_WARNING = 'SUCCESSWITHWARNING'

