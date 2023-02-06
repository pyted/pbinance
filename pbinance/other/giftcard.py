from finance_utils.component.local import to_local
from pbinance.client import Client
from typing import Union


# 币安码
class _GiftCardEndpoints():
    set_createCode = ['https://api.binance.com/','POST', '/sapi/v1/giftcard/createCode', True]  # 创建币安码 (USER_DATA)
    set_redeemCode = ['https://api.binance.com/','POST', '/sapi/v1/giftcard/redeemCode', True]  # 兑现币安码 (USER_DATA)
    get_verify = ['https://api.binance.com/','GET', '/sapi/v1/giftcard/verify', True]  # 验证币安码 (USER_DATA)
    get_cryptography_rsa_public_key = ['https://api.binance.com/','GET', '/sapi/v1/giftcard/cryptography/rsa-public-key', True]  # 获取RSA Public Key (USER_DATA)
    set_buyCode = ['https://api.binance.com/','POST', '/sapi/v1/giftcard/buyCode', True]  # 购买币安码 (TRADE)
    get_buyCode_token_limit = ['https://api.binance.com/','GET', '/sapi/v1/giftcard/buyCode/token-limit', True]  # 获取货币使用限制 (USER_DATA)


class GiftCard(Client):
    endpoints = _GiftCardEndpoints

    # 创建币安码 (USER_DATA)
    def set_createCode(self, token: str = '', amount: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-118

        Name      	Type  	Mandatory	Description
        token     	str   	YES      	币安码中的数字货币币种
        amount    	DOUBLE	YES      	币安码中的数字货币数量
        recvWindow	int   	NO
        '''
        return self.send_request(*self.endpoints.set_createCode, **to_local(locals()))

    # 兑现币安码 (USER_DATA)
    def set_redeemCode(self, code: str = '', externalUid: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-119

        Name       	Type	Mandatory	Description
        code       	str 	YES      	用于赎回的binance code，支持加密&未加密两种方式
        externalUid	str 	NO       	每个外部用户 ID 代表合作伙伴平台上的某个用户。该功能帮助您识别不同用户的兑现行为，例如兑现频次和金额。它还有助于对单个账户进行风险和限额控制，例如设置单个账户每日兑现金额、频次和卡密输错次数的上限。这也将防止单个帐户突破合作伙伴的每日兑现限额从而导致合作伙伴的账户在当日无法继续制码或者兑现。如果您有外部的网站且有不同的用户在您的平台上兑现 Binance Code或礼品卡，我们强烈建议您使用此功能并将您用户的用户 ID 传输给我们来进行风控。为保护用户的信息安全，您可以选择以任何格式（上限为 400 个字符）传输用户 ID。
        recvWindow 	int 	NO
        '''
        return self.send_request(*self.endpoints.set_redeemCode, **to_local(locals()))

    # 验证币安码 (USER_DATA)
    def get_verify(self, referenceNo: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-120

        Name       	Type	Mandatory	Description
        referenceNo	str 	YES      	参考号
        recvWindow 	int 	NO
        '''
        return self.send_request(*self.endpoints.get_verify, **to_local(locals()))

    # 获取RSA Public Key (USER_DATA)
    def get_cryptography_rsa_public_key(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#rsa-public-key-user_data

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_cryptography_rsa_public_key, **to_local(locals()))

    # 购买币安码 (TRADE)
    def set_buyCode(self, baseToken: str = '', faceToken: str = '', baseTokenAmount: Union[float, int] = '',
                    recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-24

        Name           	Type  	Mandatory	Description
        baseToken      	str   	YES      	你用来支付的货币，例如：BUSD
        faceToken      	str   	YES      	你购买的礼品卡面额，例如：BNB。如果 faceToken = baseToken，将等同于使用 createCode API
        baseTokenAmount	DOUBLE	YES      	支付的货币数量，例如：1.002
        recvWindow     	int   	NO
        '''
        return self.send_request(*self.endpoints.set_buyCode, **to_local(locals()))

    # 获取货币使用限制 (USER_DATA)
    def get_buyCode_token_limit(self, baseToken: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-121

        Name      	Type	Mandatory	Description
        baseToken 	str 	YES      	你用来支付的货币，例如：BUSD
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_buyCode_token_limit, **to_local(locals()))
