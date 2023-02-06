from finance_utils.component.local import to_local
from pbinance.client import Client
from typing import Union


# 闪兑
class _ConvertEndpoints():
    get_exchangeInfo = ['https://api.binance.com/','GET', '/sapi/v1/convert/exchangeInfo', False]  # 查询可交易币对信息 (USER_DATA)
    get_assetInfo = ['https://api.binance.com/','GET', '/sapi/v1/convert/assetInfo', False]  # 查询可交易币种精度 (USER_DATA)
    set_getQuote = ['https://api.binance.com/','POST', '/sapi/v1/convert/getQuote', False]  # 发送获取报价请求 (USER_DATA)
    set_acceptQuote = ['https://api.binance.com/','POST', '/sapi/v1/convert/acceptQuote', False]  # 接受报价 (TRADE)
    get_orderStatus = ['https://api.binance.com/','GET', '/sapi/v1/convert/orderStatus', False]  # 查询订单状态 (USER_DATA)
    get_tradeFlow = ['https://api.binance.com/','GET', '/sapi/v1/convert/tradeFlow', True]  # 获取闪兑交易记录 (USER_DATA)


class Convert(Client):
    endpoints = _ConvertEndpoints

    # 查询可交易币对信息 (USER_DATA)
    def get_exchangeInfo(self, fromAsset: str = '', toAsset: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-112

        Name     	Type	Mandatory     	Description
        fromAsset	str 	EITHER OR BOTH	用户售出币种
        toAsset  	str 	EITHER OR BOTH	用户买入币种
        '''
        return self.send_request(*self.endpoints.get_exchangeInfo, **to_local(locals()))

    # 查询可交易币种精度 (USER_DATA)
    def get_assetInfo(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-113

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO       	此值不能大于 60000
        '''
        return self.send_request(*self.endpoints.get_assetInfo, **to_local(locals()))

    # 发送获取报价请求 (USER_DATA)
    def set_getQuote(self, fromAsset: str = '', toAsset: str = '', fromAmount: Union[float, int] = '',
                     toAmount: Union[float, int] = '', validTime: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-114

        Name      	Type            	Mandatory	Description
        fromAsset 	str             	YES
        toAsset   	str             	YES
        fromAmount	Union[float,int]	EITHER   	这是成交后将被扣除的金额
        toAmount  	Union[float,int]	EITHER   	这是成交后将会获得的金额
        validTime 	str             	NO       	可以支持10s、30s、1m、2m等值，默认值为 10s
        recvWindow	int             	NO       	此值不能大于 60000
        '''
        return self.send_request(*self.endpoints.set_getQuote, **to_local(locals()))

    # 接受报价 (TRADE)
    def set_acceptQuote(self, quoteId: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-23

        Name      	Type	Mandatory	Description
        quoteId   	str 	YES
        recvWindow	int 	NO       	此值不能大于 60000
        '''
        return self.send_request(*self.endpoints.set_acceptQuote, **to_local(locals()))

    # 查询订单状态 (USER_DATA)
    def get_orderStatus(self, orderId: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-115

        Name   	Type	Mandatory	Description
        orderId	str 	YES
        '''
        return self.send_request(*self.endpoints.get_orderStatus, **to_local(locals()))

    # 获取闪兑交易记录 (USER_DATA)
    def get_tradeFlow(self, startTime: int = '', endTime: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-116

        Name      	Type	Mandatory	Description
        startTime 	int 	YES
        endTime   	int 	YES
        limit     	int 	NO       	默认 100, 最大 1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_tradeFlow, **to_local(locals()))
