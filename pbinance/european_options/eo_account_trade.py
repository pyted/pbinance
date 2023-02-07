from paux.param import to_local
from pbinance.client import Client
from typing import Union


# 账户与交易
class _EOAccountTradeEndpoints():
    get_account = ['https://eapi.binance.com/','GET', '/eapi/v1/account', True]  # 账户信息 (TRADE)
    set_transfer = ['https://eapi.binance.com/','POST', '/eapi/v1/transfer', True]  # 资金划转 (TRADE)
    set_order = ['https://eapi.binance.com/','POST', '/eapi/v1/order', True]  # 下单 (TRADE)
    set_batchOrders = ['https://eapi.binance.com/','POST', '/eapi/v1/batchOrders', True]  # 批量下单 (TRADE)
    cancel_order = ['https://eapi.binance.com/','DELETE', '/eapi/v1/order', True]  # 撤销订单 (TRADE)
    cancel_batchOrders = ['https://eapi.binance.com/','DELETE', '/eapi/v1/batchOrders', True]  # 批量撤销订单 (TRADE)
    cancel_allOpenOrders = ['https://eapi.binance.com/','DELETE', '/eapi/v1/allOpenOrders', True]  # 撤销单交易对全部订单 (TRADE)
    cancel_allOpenOrdersByUnderlying = ['https://eapi.binance.com/','DELETE', '/eapi/v1/allOpenOrdersByUnderlying', True]  # 撤销特定标的全部订单 (TRADE)
    get_openOrders = ['https://eapi.binance.com/','GET', '/eapi/v1/openOrders', True]  # 查询当前挂单 (USER_DATA)
    get_historyOrders = ['https://eapi.binance.com/','GET', '/eapi/v1/historyOrders', True]  # 查询历史订单 (USER_DATA)
    get_position = ['https://eapi.binance.com/','GET', '/eapi/v1/position', True]  # 仓位信息 (USER_DATA)
    get_userTrades = ['https://eapi.binance.com/','GET', '/eapi/v1/userTrades', True]  # 账户成交历史 (USER_DATA)
    get_exerciseRecord = ['https://eapi.binance.com/','GET', '/eapi/v1/exerciseRecord', True]  # 用户行权历史(USER_DATA)
    get_bill = ['https://eapi.binance.com/','GET', '/eapi/v1/bill', True]  # 获取账户资金流水(USER_DATA)


class EOAccountTrade(Client):
    endpoints = _EOAccountTradeEndpoints

    # 账户信息 (TRADE)
    def get_account(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#trade

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_account, **to_local(locals()))

    # 资金划转 (TRADE)
    def set_transfer(self, currency: str = '', type: str = '', amount: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#trade-2

        Name      	Type            	Mandatory	Description
        currency  	str             	YES      	资产类型, e.g USDT
        type      	str             	YES      	IN: 从现货钱包转到期权钱包 OUT: 从期权钱包转到现货钱包
        amount    	Union[float,int]	YES      	数量如100
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_transfer, **to_local(locals()))

    # 下单 (TRADE)
    def set_order(self, symbol: str = '', side: str = '', type: str = '', quantity: Union[float, int] = '',
                  price: Union[float, int] = '', timeInForce: str = '', reduceOnly: str = '', postOnly: str = '',
                  newOrderRespType: str = '', clientOrderId: str = '', isMmp: bool = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#trade-3

        Name            	Type            	Mandatory	Description
        symbol          	str             	YES      	交易对
        side            	str             	YES
        type            	str             	YES
        quantity        	Union[float,int]	YES      	下单数量
        price           	Union[float,int]	NO       	委托价格
        timeInForce     	str             	NO       	有效时间
        reduceOnly      	str             	NO
        postOnly        	str             	NO
        newOrderRespType	str             	NO       	"ACK", "RESULT", 默认 "ACK"
        clientOrderId   	str             	NO       	用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。
        isMmp           	bool            	NO       	是否为MMP订单true/false
        recvWindow      	int             	NO
        '''
        return self.send_request(*self.endpoints.set_order, **to_local(locals()))

    # 批量下单 (TRADE)
    def set_batchOrders(self, orders: list = '', recvWindow: int = '', symbol: str = '', side: str = '', type: str = '',
                        quantity: Union[float, int] = '', price: Union[float, int] = '', timeInForce: str = '',
                        reduceOnly: str = '', postOnly: str = '', newOrderRespType: str = '', clientOrderId: str = '',
                        isMmp: bool = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#trade-4

        Name            	Type            	Mandatory	Description
        orders          	list            	YES      	订单列表，最多支持5个订单
        recvWindow      	int             	NO
        symbol          	str             	YES      	交易对
        side            	str             	YES
        type            	str             	YES
        quantity        	Union[float,int]	YES      	下单数量
        price           	Union[float,int]	NO       	委托价格
        timeInForce     	str             	NO       	有效时间
        reduceOnly      	str             	NO
        postOnly        	str             	NO
        newOrderRespType	str             	NO       	"ACK", "RESULT", 默认 "ACK"
        clientOrderId   	str             	NO
        isMmp           	bool            	NO       	是否为MMP订单true/false
        '''
        return self.send_request(*self.endpoints.set_batchOrders, **to_local(locals()))

    # 撤销订单 (TRADE)
    def cancel_order(self, symbol: str = '', orderId: int = '', clientOrderId: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#trade-5

        Name         	Type	Mandatory	Description
        symbol       	str 	YES      	交易对
        orderId      	int 	NO       	系统订单号
        clientOrderId	str 	NO       	用户自定义的订单号
        recvWindow   	int 	NO
        '''
        return self.send_request(*self.endpoints.cancel_order, **to_local(locals()))

    # 批量撤销订单 (TRADE)
    def cancel_batchOrders(self, symbol: str = '', orderIds: list = '', clientOrderIds: list = '',
                           recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#trade-6

        Name          	Type        	Mandatory	Description
        symbol        	str         	YES      	交易对
        orderIds      	LIST<LONG>  	NO
        clientOrderIds	LIST<STRING>	NO
        recvWindow    	int         	NO
        '''
        return self.send_request(*self.endpoints.cancel_batchOrders, **to_local(locals()))

    # 撤销单交易对全部订单 (TRADE)
    def cancel_allOpenOrders(self, symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#trade-7

        Name      	Type	Mandatory	Description
        symbol    	str 	YES      	交易对
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.cancel_allOpenOrders, **to_local(locals()))

    # 撤销特定标的全部订单 (TRADE)
    def cancel_allOpenOrdersByUnderlying(self, underlying: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#trade-8

        Name      	Type	Mandatory	Description
        underlying	str 	YES      	标的资产如BTCUSDT
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.cancel_allOpenOrdersByUnderlying, **to_local(locals()))

    # 查询当前挂单 (USER_DATA)
    def get_openOrders(self, symbol: str = '', orderId: int = '', startTime: int = '', endTime: int = '',
                       limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#user_data

        Name      	Type	Mandatory	Description
        symbol    	str 	NO       	交易对(不传返回所有订单)
        orderId   	int 	NO       	只返回此orderID及之后的订单，缺省返回最近的订单
        startTime 	int 	NO       	开始时间
        endTime   	int 	NO       	结束时间
        limit     	int 	NO       	返回数量，默认100 最大1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_openOrders, **to_local(locals()))

    # 查询历史订单 (USER_DATA)
    def get_historyOrders(self, symbol: str = '', orderId: int = '', startTime: int = '', endTime: int = '',
                          limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#user_data-2

        Name      	Type	Mandatory	Description
        symbol    	str 	YES      	交易对
        orderId   	int 	NO       	只返回此orderID及之后的订单，缺省返回最近的订单
        startTime 	int 	NO       	起始时间
        endTime   	int 	NO       	结束时间
        limit     	int 	NO       	返回的结果集数量 默认值:500 最大值:1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_historyOrders, **to_local(locals()))

    # 仓位信息 (USER_DATA)
    def get_position(self, symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#user_data-3

        Name      	Type	Mandatory	Description
        symbol    	str 	NO       	交易对如BTC-200730-9000-C
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_position, **to_local(locals()))

    # 账户成交历史 (USER_DATA)
    def get_userTrades(self, symbol: str = '', fromId: int = '', startTime: int = '', endTime: int = '',
                       limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#user_data-4

        Name      	Type	Mandatory	Description
        symbol    	str 	NO       	交易对
        fromId    	int 	NO       	返回该fromId及之后的成交，缺省返回最近的成交
        startTime 	int 	NO       	起始时间
        endTime   	int 	NO       	结束时间
        limit     	int 	NO       	返回的结果集数量 默认值:100 最大值:1000.
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_userTrades, **to_local(locals()))

    # 用户行权历史(USER_DATA)
    def get_exerciseRecord(self, symbol: str = '', startTime: int = '', endTime: int = '', limit: int = '',
                           recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#user_data-5

        Name      	Type	Mandatory	Description
        symbol    	str 	NO       	交易对如 BTC-200730-9000-C
        startTime 	int 	NO       	起始时间如1593511200000
        endTime   	int 	NO       	结束时间如1593512200000
        limit     	int 	NO       	默认1000, 最大1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_exerciseRecord, **to_local(locals()))

    # 获取账户资金流水(USER_DATA)
    def get_bill(self, currency: str = '', recordId: int = '', startTime: int = '', endTime: int = '', limit: int = '',
                 recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#user_data-6

        Name      	Type	Mandatory	Description
        currency  	str 	YES      	资产类型如USDT
        recordId  	int 	NO       	返回该recordId及之后的成交，缺省返回最近的成交
        startTime 	int 	NO       	起始时间如1593511200000
        endTime   	int 	NO       	结束时间如1593512200000
        limit     	int 	NO       	默认100 最大1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_bill, **to_local(locals()))
