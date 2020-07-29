import os
APPID="2016092000554611"

APP_PRIVATE_KEY_STRING = open(os.path.join(os.path.dirname(__file__),'pem','private_key.pem')).read()
ALIPAY_PUBLIC_KEY_STRING = open(os.path.join(os.path.dirname(__file__),'pem','al_public_key.pem')).read()

SIGN_TYPE='RSA2'
DEBUG=True


GATEWAY='https://openapi.alipaydev.com/gateway.do?' if DEBUG else 'https://openapi.alipay.com/gateway.do?'