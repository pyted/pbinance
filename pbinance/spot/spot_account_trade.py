from paux.param import to_local
from pbinance.client import Client
from typing import Union

# 账户与交易
class _SPOTAccountTradeEndpoints():
    set_order_test = ['https://api.binance.com/','POST', '/api/v3/order/test', True]  # 测试下单 (TRADE)
    set_order = ['https://api.binance.com/','POST', '/api/v3/order', True]  # 下单 (TRADE)
    cancel_order = ['https://api.binance.com/','DELETE', '/api/v3/order', True]  # 撤销订单 (TRADE)
    cancel_openOrders = ['https://api.binance.com/','DELETE', '/api/v3/openOrders', False]  # 撤销单一交易对的所有挂单 (TRADE)
    order_cancelReplace = ['https://api.binance.com/','POST', '/api/v3/order/cancelReplace', False]  # 撤消挂单再下单 (TRADE)
    get_order = ['https://api.binance.com/','GET', '/api/v3/order', True]  # 查询订单 (USER_DATA)
    get_openOrders = ['https://api.binance.com/','GET', '/api/v3/openOrders', True]  # 当前挂单 (USER_DATA)
    get_allOrders = ['https://api.binance.com/','GET', '/api/v3/allOrders', True]  # 查询所有订单 (USER_DATA)
    set_order_oco = ['https://api.binance.com/','POST', '/api/v3/order/oco', True]  # OCO下单(TRADE)
    cancel_orderList = ['https://api.binance.com/','DELETE', '/api/v3/orderList', True]  # 取消 OCO 订单(TRADE)
    get_orderList = ['https://api.binance.com/','GET', '/api/v3/orderList', True]  # 查询 OCO (USER_DATA)
    get_allOrderList = ['https://api.binance.com/','GET', '/api/v3/allOrderList', True]  # 查询所有 OCO (USER_DATA)
    get_openOrderList = ['https://api.binance.com/','GET', '/api/v3/openOrderList', True]  # 查询 OCO 挂单 (USER_DATA)
    get_account = ['https://api.binance.com/','GET', '/api/v3/account', True]  # 账户信息 (USER_DATA)
    get_myTrades = ['https://api.binance.com/','GET', '/api/v3/myTrades', True]  # 账户成交历史 (USER_DATA)
    get_rateLimit_order = ['https://api.binance.com/','GET', '/api/v3/rateLimit/order', False]  # 查询目前下单数 (TRADE)


class SPOTAccountTrade(Client):
    endpoints = _SPOTAccountTradeEndpoints

    # 测试下单 (TRADE)
    def set_order_test(self, symbol: str = '', side: str = '', type: str = '', timeInForce: str = '',
                       quantity: Union[float, int] = '', quoteOrderQty: Union[float, int] = '',
                       price: Union[float, int] = '', newClientOrderId: str = '', stopPrice: Union[float, int] = '',
                       trailingDelta: int = '', icebergQty: Union[float, int] = '', newOrderRespType: str = '',
                       strategyId: int = '', strategyType: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-2

        Name            	Type            	Mandatory	Description
        symbol          	str             	YES
        side            	str             	YES      	详见枚举定义：订单方向
        type            	str             	YES      	详见枚举定义：订单类型
        timeInForce     	str             	NO       	详见枚举定义：有效方式
        quantity        	Union[float,int]	NO
        quoteOrderQty   	Union[float,int]	NO
        price           	Union[float,int]	NO
        newClientOrderId	str             	NO       	客户自定义的唯一订单ID。 如果未发送，则自动生成
        stopPrice       	Union[float,int]	NO
        trailingDelta   	int             	NO
        icebergQty      	Union[float,int]	NO
        newOrderRespType	str             	NO       	设置响应JSON。 ACK，RESULT或FULL； "MARKET"和" LIMIT"订单类型默认为"FULL"，所有其他订单默认为"ACK"。
        strategyId      	int             	NO
        strategyType    	int             	NO
        recvWindow      	int             	NO
        '''
        return self.send_request(*self.endpoints.set_order_test, **to_local(locals()))

    # 下单  (TRADE)
    def set_order(self, symbol: str = '', side: str = '', type: str = '', timeInForce: str = '',
                  quantity: Union[float, int] = '', quoteOrderQty: Union[float, int] = '',
                  price: Union[float, int] = '', newClientOrderId: str = '', stopPrice: Union[float, int] = '',
                  trailingDelta: int = '', icebergQty: Union[float, int] = '', newOrderRespType: str = '',
                  strategyId: int = '', strategyType: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-3

        Name            	Type            	Mandatory	Description
        symbol          	str             	YES
        side            	str             	YES      	详见枚举定义：订单方向
        type            	str             	YES      	详见枚举定义：订单类型
        timeInForce     	str             	NO       	详见枚举定义：有效方式
        quantity        	Union[float,int]	NO
        quoteOrderQty   	Union[float,int]	NO
        price           	Union[float,int]	NO
        newClientOrderId	str             	NO       	客户自定义的唯一订单ID。 如果未发送，则自动生成
        stopPrice       	Union[float,int]	NO
        trailingDelta   	int             	NO
        icebergQty      	Union[float,int]	NO
        newOrderRespType	str             	NO       	设置响应JSON。 ACK，RESULT或FULL； "MARKET"和" LIMIT"订单类型默认为"FULL"，所有其他订单默认为"ACK"。
        strategyId      	int             	NO
        strategyType    	int             	NO
        recvWindow      	int             	NO
        '''
        return self.send_request(*self.endpoints.set_order, **to_local(locals()))

    # 撤销订单 (TRADE)
    def cancel_order(self, symbol: str = '', orderId: int = '', origClientOrderId: str = '', newClientOrderId: str = '',
                     recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-4

        Name             	Type	Mandatory	Description
        symbol           	str 	YES
        orderId          	int 	NO
        origClientOrderId	str 	NO
        newClientOrderId 	str 	NO       	用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。
        recvWindow       	int 	NO
        '''
        return self.send_request(*self.endpoints.cancel_order, **to_local(locals()))

    # 撤销单一交易对的所有挂单 (TRADE)
    def cancel_openOrders(self, symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-5

        Name      	Type	Mandatory	Description
        symbol    	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.cancel_openOrders, **to_local(locals()))

    # 撤消挂单再下单 (TRADE)
    def order_cancelReplace(self, symbol: str = '', side: str = '', type: str = '', cancelReplaceMode: str = '',
                            timeInForce: str = '', quantity: Union[float, int] = '',
                            quoteOrderQty: Union[float, int] = '', price: Union[float, int] = '',
                            cancelNewClientOrderId: str = '', cancelOrigClientOrderId: str = '',
                            cancelOrderId: int = '', newClientOrderId: str = '', strategyId: int = '',
                            strategyType: int = '', stopPrice: Union[float, int] = '', trailingDelta: int = '',
                            icebergQty: Union[float, int] = '', newOrderRespType: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-6

        Name                   	Type            	Mandatory	Description
        symbol                 	str             	YES
        side                   	str             	YES
        type                   	str             	YES
        cancelReplaceMode      	str             	YES
        timeInForce            	str             	NO
        quantity               	Union[float,int]	NO
        quoteOrderQty          	Union[float,int]	NO
        price                  	Union[float,int]	NO
        cancelNewClientOrderId 	str             	NO       	用户自定义的id，如空缺系统会自动赋值
        cancelOrigClientOrderId	str             	NO
        cancelOrderId          	int             	NO
        newClientOrderId       	str             	NO       	用于辨识新订单。
        strategyId             	int             	NO
        strategyType           	int             	NO
        stopPrice              	Union[float,int]	NO
        trailingDelta          	int             	NO
        icebergQty             	Union[float,int]	NO
        newOrderRespType       	str             	NO
        recvWindow             	int             	NO
        '''
        return self.send_request(*self.endpoints.order_cancelReplace, **to_local(locals()))

    # 查询订单 (USER_DATA)
    def get_order(self, symbol: str = '', orderId: int = '', origClientOrderId: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-20

        Name             	Type	Mandatory	Description
        symbol           	str 	YES
        orderId          	int 	NO
        origClientOrderId	str 	NO
        recvWindow       	int 	NO
        '''
        return self.send_request(*self.endpoints.get_order, **to_local(locals()))

    # 当前挂单 (USER_DATA)
    def get_openOrders(self, symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-21

        Name      	Type	Mandatory	Description
        symbol    	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_openOrders, **to_local(locals()))

    # 查询所有订单 (USER_DATA)
    def get_allOrders(self, symbol: str = '', orderId: int = '', startTime: int = '', endTime: int = '',
                      limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-22

        Name      	Type	Mandatory	Description
        symbol    	str 	YES
        orderId   	int 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	默认 500; 最大 1000.
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_allOrders, **to_local(locals()))

    # OCO下单(TRADE)
    def set_order_oco(self, symbol: str = '', listClientOrderId: str = '', side: str = '',
                      quantity: Union[float, int] = '', limitClientOrderId: str = '', limitStrategyId: int = '',
                      limitStrategyType: int = '', price: Union[float, int] = '',
                      limitIcebergQty: Union[float, int] = '', trailingDelta: int = '', stopClientOrderId: str = '',
                      stopPrice: Union[float, int] = '', stopStrategyId: int = '', stopStrategyType: int = '',
                      stopLimitPrice: Union[float, int] = '', stopIcebergQty: Union[float, int] = '',
                      stopLimitTimeInForce: str = '', newOrderRespType: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#oco-trade

        Name                	Type            	Mandatory	Description
        symbol              	str             	YES
        listClientOrderId   	str             	NO       	整个orderList的唯一ID
        side                	str             	YES      	详见枚举定义：订单方向
        quantity            	Union[float,int]	YES
        limitClientOrderId  	str             	NO       	限价单的唯一ID
        limitStrategyId     	int             	NO
        limitStrategyType   	int             	NO
        price               	Union[float,int]	YES
        limitIcebergQty     	Union[float,int]	NO
        trailingDelta       	int             	NO
        stopClientOrderId   	str             	NO       	止损/止损限价单的唯一ID
        stopPrice           	Union[float,int]	YES
        stopStrategyId      	int             	NO
        stopStrategyType    	int             	NO
        stopLimitPrice      	Union[float,int]	NO
        stopIcebergQty      	Union[float,int]	NO
        stopLimitTimeInForce	str             	NO
        newOrderRespType    	str             	NO       	详见枚举定义：订单返回类型
        recvWindow          	int             	NO
        '''
        return self.send_request(*self.endpoints.set_order_oco, **to_local(locals()))

    # 取消 OCO 订单(TRADE)
    def cancel_orderList(self, symbol: str = '', orderListId: int = '', listClientOrderId: str = '',
                         newClientOrderId: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#oco-trade-2

        Name             	Type	Mandatory	Description
        symbol           	str 	YES
        orderListId      	int 	NO
        listClientOrderId	str 	NO
        newClientOrderId 	str 	NO       	用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。
        recvWindow       	int 	NO
        '''
        return self.send_request(*self.endpoints.cancel_orderList, **to_local(locals()))

    # 查询 OCO (USER_DATA)
    def get_orderList(self, orderListId: int = '', origClientOrderId: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#oco-user_data

        Name             	Type	Mandatory	Description
        orderListId      	int 	NO
        origClientOrderId	str 	NO
        recvWindow       	int 	NO
        '''
        return self.send_request(*self.endpoints.get_orderList, **to_local(locals()))

    # 查询所有 OCO (USER_DATA)
    def get_allOrderList(self, fromId: int = '', startTime: int = '', endTime: int = '', limit: int = '',
                         recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#oco-user_data-2

        Name      	Type	Mandatory	Description
        fromId    	int 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	默认值: 500; 最大值: 1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_allOrderList, **to_local(locals()))

    # 查询 OCO 挂单 (USER_DATA)
    def get_openOrderList(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#oco-user_data-3

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_openOrderList, **to_local(locals()))

    # 账户信息 (USER_DATA)
    def get_account(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-23

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_account, **to_local(locals()))

    # 账户成交历史 (USER_DATA)
    def get_myTrades(self, symbol: str = '', orderId: int = '', startTime: int = '', endTime: int = '',
                     fromId: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-24

        Name      	Type	Mandatory	Description
        symbol    	str 	YES
        orderId   	int 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        fromId    	int 	NO       	起始Trade id。 默认获取最新交易。
        limit     	int 	NO       	默认 500; 最大 1000.
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_myTrades, **to_local(locals()))

    # 查询目前下单数 (TRADE)
    def get_rateLimit_order(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-7

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_rateLimit_order, **to_local(locals()))
