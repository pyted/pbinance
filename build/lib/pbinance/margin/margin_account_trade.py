from finance_utils.component.local import to_local
from pbinance.client import Client
from typing import Union


class _MarginAccountTradeEndpoints():
    set_transfer = ['https://api.binance.com/', 'POST', '/sapi/v1/margin/transfer', True]  # 全仓杠杆账户划转 (MARGIN)
    set_loan = ['https://api.binance.com/', 'POST', '/sapi/v1/margin/loan', True]  # 杠杆账户借贷 (MARGIN)
    set_repay = ['https://api.binance.com/', 'POST', '/sapi/v1/margin/repay', True]  # 杠杆账户归还借贷 (MARGIN)
    get_asset = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/asset', False]  # 查询杠杆资产 (MARKET_DATA)
    get_pair = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/pair', False]  # 查询全仓杠杆交易对 (MARKET_DATA)
    get_allAssets = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/allAssets', False]  # 获取所有杠杆资产信息 (MARKET_DATA)
    get_allPairs = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/allPairs', False]  # 获取所有全仓杠杆交易对(MARKET_DATA)
    get_priceIndex = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/priceIndex', False]  # 查询杠杆价格指数 (MARKET_DATA)
    set_order = ['https://api.binance.com/', 'POST', '/sapi/v1/margin/order', True]  # 杠杆账户下单 (TRADE)
    cancel_order = ['https://api.binance.com/', 'DELETE', '/sapi/v1/margin/order', True]  # 杠杆账户撤销订单 (TRADE)
    cancel_openOrders = ['https://api.binance.com/', 'DELETE', '/sapi/v1/margin/openOrders', True]  # 杠杆账户撤销单一交易对的所有挂单 (TRADE)
    get_transfer = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/transfer', True]  # 获取全仓杠杆划转历史 (USER_DATA)
    get_loan = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/loan', True]  # 查询借贷记录 (USER_DATA)
    get_repay = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/repay', True]  # 查询还贷记录 (USER_DATA)
    get_interestHistory = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/interestHistory', True]  # 获取利息历史 (USER_DATA)
    get_cross_account = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/account', True]  # 查询全仓杠杆账户详情 (USER_DATA)
    get_forceLiquidationRec = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/forceLiquidationRec', True]  # 获取账户强制平仓记录(USER_DATA)
    get_order = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/order', True]  # 查询杠杆账户订单 (USER_DATA)
    get_openOrders = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/openOrders', True]  # 查询杠杆账户挂单记录 (USER_DATA)
    get_allOrders = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/allOrders', True]  # 查询杠杆账户的所有订单 (USER_DATA)
    set_order_oco = ['https://api.binance.com/', 'POST', '/sapi/v1/margin/order/oco', True]  # 杠杆账户 OCO 下单(TRADE)
    cancel_orderList = ['https://api.binance.com/', 'DELETE', '/sapi/v1/margin/orderList', True]  # 取消杠杆账户 OCO 订单(TRADE)
    get_orderList = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/orderList', True]  # 查询杠杆账户 OCO (USER_DATA)
    get_allOrderList = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/allOrderList', True]  # 查询特定杠杆账户所有 OCO (USER_DATA)
    get_openOrderList = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/openOrderList', True]  # 查询杠杆账户 OCO 挂单 (USER_DATA)
    get_myTrades = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/myTrades', True]  # 查询杠杆账户交易历史 (USER_DATA)
    get_maxBorrowable = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/maxBorrowable', True]  # 查询账户最大可借贷额度(USER_DATA)
    get_maxTransferable = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/maxTransferable', True]  # 查询最大可转出额 (USER_DATA)
    get_tradeCoeff = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/tradeCoeff', True]  # 查询Margin账户信息汇总 (USER_DATA)
    set_isolated_transfer = ['https://api.binance.com/', 'POST', '/sapi/v1/margin/isolated/transfer', True]  # 杠杆逐仓账户划转 (MARGIN)
    get_isolated_transfer = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/isolated/transfer', True]  # 获取杠杆逐仓划转历史 (USER_DATA)
    get_isolated_account = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/isolated/account', True]  # 查询杠杆逐仓账户信息 (USER_DATA)
    delete_isolated_account = ['https://api.binance.com/', 'DELETE', '/sapi/v1/margin/isolated/account', True]  # 杠杆逐仓账户停用 (TRADE)
    set_isolated_account = ['https://api.binance.com/', 'POST', '/sapi/v1/margin/isolated/account', True]  # 杠杆逐仓账户启用 (TRADE)
    get_isolated_accountLimit = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/isolated/accountLimit', True]  # 查询杠杆逐仓账户启用限制 (USER_DATA)
    get_isolated_pair = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/isolated/pair', True]  # 查询逐仓杠杆交易对 (USER_DATA)
    get_isolated_allPairs = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/isolated/allPairs', True]  # 获取所有逐仓杠杆交易对(USER_DATA)
    set_bnbBurn = ['https://api.binance.com/', 'POST', '/sapi/v1/bnbBurn', True]  # 现货交易和杠杆利息BNB抵扣开关(USER_DATA)
    get_bnbBurn = ['https://api.binance.com/', 'GET', '/sapi/v1/bnbBurn', True]  # 获取BNB抵扣开关状态 (USER_DATA)
    get_interestRateHistory = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/interestRateHistory', True]  # 获取杠杆利率历史 (USER_DATA)
    get_crossMarginData = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/crossMarginData', True]  # 获取全仓杠杆利率及限额 (USER_DATA)
    get_isolatedMarginData = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/isolatedMarginData', True]  # 获取逐仓杠杆利率及限额 (USER_DATA)
    get_isolatedMarginTier = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/isolatedMarginTier', True]  # 获取逐仓档位信息 (USER_DATA)
    get_rateLimit_order = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/rateLimit/order', False]  # 查询目前杠杆账户下单数 (TRADE)
    get_dribblet = ['https://api.binance.com/', 'GET', '/sapi/v1/margin/dribblet', True]  # 杠杆小额资产转换BNB历史 (USER_DATA


class MarginAccountTrade(Client):
    endpoints = _MarginAccountTradeEndpoints

    # 全仓杠杆账户划转 (MARGIN)
    def set_transfer(self, asset: str = '', amount: Union[float, int] = '', type: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#margin-5

        Name      	Type            	Mandatory	Description
        asset     	str             	YES      	被划转的资产, 比如, BTC
        amount    	Union[float,int]	YES      	划转数量
        type      	int             	YES      	1: 主账户向全仓杠杆账户划转 2: 全仓杠杆账户向主账户划转
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_transfer, **to_local(locals()))

    # 杠杆账户借贷 (MARGIN)
    def set_loan(self, asset: str = '', isIsolated: str = '', symbol: str = '', amount: Union[float, int] = '',
                 recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#margin-6

        Name      	Type            	Mandatory	Description
        asset     	str             	YES
        isIsolated	str             	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        symbol    	str             	NO       	逐仓交易对，配合逐仓使用
        amount    	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_loan, **to_local(locals()))

    # 杠杆账户归还借贷 (MARGIN)
    def set_repay(self, asset: str = '', isIsolated: str = '', symbol: str = '', amount: Union[float, int] = '',
                  recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#margin-7

        Name      	Type            	Mandatory	Description
        asset     	str             	YES
        isIsolated	str             	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        symbol    	str             	NO       	逐仓交易对，配合逐仓使用
        amount    	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_repay, **to_local(locals()))

    # 查询杠杆资产 (MARKET_DATA)
    def get_asset(self, asset: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#market_data-2

        Name 	Type	Mandatory	Description
        asset	str 	YES
        '''
        return self.send_request(*self.endpoints.get_asset, **to_local(locals()))

    # 查询全仓杠杆交易对 (MARKET_DATA)
    def get_pair(self, symbol: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#market_data-3

        Name  	Type	Mandatory	Description
        symbol	str 	YES
        '''
        return self.send_request(*self.endpoints.get_pair, **to_local(locals()))

    # 获取所有杠杆资产信息 (MARKET_DATA)
    def get_allAssets(self):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#market_data-4
        '''
        return self.send_request(*self.endpoints.get_allAssets, **to_local(locals()))

    # 获取所有全仓杠杆交易对(MARKET_DATA)
    def get_allPairs(self):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#market_data-5
        '''
        return self.send_request(*self.endpoints.get_allPairs, **to_local(locals()))

    # 查询杠杆价格指数 (MARKET_DATA)
    def get_priceIndex(self, symbol: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#market_data-6

        Name  	Type	Mandatory	Description
        symbol	str 	YES
        '''
        return self.send_request(*self.endpoints.get_priceIndex, **to_local(locals()))

    # 杠杆账户下单 (TRADE)
    def set_order(self, symbol: str = '', isIsolated: str = '', side: str = '', type: str = '',
                  quantity: Union[float, int] = '', quoteOrderQty: Union[float, int] = '',
                  price: Union[float, int] = '',
                  stopPrice: Union[float, int] = '', newClientOrderId: str = '', icebergQty: Union[float, int] = '',
                  newOrderRespType: str = '', sideEffectType: str = '', timeInForce: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-8

        Name            	Type            	Mandatory	Description
        symbol          	str             	YES
        isIsolated      	str             	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        side            	str             	YES
        type            	str             	YES      	详见枚举定义：订单类型
        quantity        	Union[float,int]	NO
        quoteOrderQty   	Union[float,int]	NO
        price           	Union[float,int]	NO
        stopPrice       	Union[float,int]	NO
        newClientOrderId	str             	NO       	客户自定义的唯一订单ID。若未发送自动生成。
        icebergQty      	Union[float,int]	NO
        newOrderRespType	str             	NO       	设置响应: JSON. ACK, RESULT, 或 FULL; MARKET 和 LIMIT 订单类型默认为 FULL, 所有其他订单默认为 ACK.
        sideEffectType  	str             	NO       	NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY;默认为 NO_SIDE_EFFECT.
        timeInForce     	str             	NO       	GTC,IOC,FOK
        recvWindow      	int             	NO
        '''
        return self.send_request(*self.endpoints.set_order, **to_local(locals()))

    # 杠杆账户撤销订单 (TRADE)
    def cancel_order(self, symbol: str = '', isIsolated: str = '', orderId: int = '', origClientOrderId: str = '',
                     newClientOrderId: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-9

        Name             	Type	Mandatory	Description
        symbol           	str 	YES
        isIsolated       	str 	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        orderId          	int 	NO
        origClientOrderId	str 	NO
        newClientOrderId 	str 	NO       	用于唯一识别此撤销订单，默认自动生成。
        recvWindow       	int 	NO
        '''
        return self.send_request(*self.endpoints.cancel_order, **to_local(locals()))

    # 杠杆账户撤销单一交易对的所有挂单 (TRADE)
    def cancel_openOrders(self, symbol: str = '', isIsolated: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-10

        Name      	Type	Mandatory	Description
        symbol    	str 	YES
        isIsolated	str 	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.cancel_openOrders, **to_local(locals()))

    # 获取全仓杠杆划转历史 (USER_DATA)
    def get_transfer(self, asset: str = '', type: str = '', startTime: int = '', endTime: int = '', current: int = '',
                     size: int = '', archived: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-25

        Name      	Type	Mandatory	Description
        asset     	str 	NO
        type      	str 	NO       	划转类型: ROLL_IN, ROLL_OUT
        startTime 	int 	NO
        endTime   	int 	NO
        current   	int 	NO       	当前查询页。 从 1开始。 默认:1
        size      	int 	NO       	默认:10 最大:100
        archived  	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_transfer, **to_local(locals()))

    # 查询借贷记录 (USER_DATA)
    def get_loan(self, asset: str = '', isolatedSymbol: str = '', txId: int = '', startTime: int = '',
                 endTime: int = '',
                 current: int = '', size: int = '', archived: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-26

        Name          	Type	Mandatory	Description
        asset         	str 	YES
        isolatedSymbol	str 	NO       	逐仓symbol
        txId          	int 	NO
        startTime     	int 	NO
        endTime       	int 	NO
        current       	int 	NO       	当前查询页。 开始值 1。 默认:1
        size          	int 	NO       	默认:10 最大:100
        archived      	str 	NO
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_loan, **to_local(locals()))

    # 查询还贷记录 (USER_DATA)
    def get_repay(self, asset: str = '', isolatedSymbol: str = '', txId: int = '', startTime: int = '',
                  endTime: int = '',
                  current: int = '', size: int = '', archived: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-27

        Name          	Type	Mandatory	Description
        asset         	str 	YES
        isolatedSymbol	str 	NO       	逐仓symbol
        txId          	int 	NO       	返回 /sapi/v1/margin/repay
        startTime     	int 	NO
        endTime       	int 	NO
        current       	int 	NO       	当前查询页。开始值 1. 默认:1
        size          	int 	NO       	默认:10 最大:100
        archived      	str 	NO
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_repay, **to_local(locals()))

    # 获取利息历史 (USER_DATA)
    def get_interestHistory(self, asset: str = '', isolatedSymbol: str = '', startTime: int = '', endTime: int = '',
                            current: int = '', size: int = '', archived: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-28

        Name          	Type	Mandatory	Description
        asset         	str 	NO
        isolatedSymbol	str 	NO       	逐仓symbol
        startTime     	int 	NO
        endTime       	int 	NO
        current       	int 	NO       	当前查询页。 开始值 1. 默认:1
        size          	int 	NO       	默认:10 最大:100
        archived      	str 	NO
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_interestHistory, **to_local(locals()))

    # 获取账户强制平仓记录(USER_DATA)
    def get_forceLiquidationRec(self, startTime: int = '', endTime: int = '', isolatedSymbol: str = '',
                                current: int = '',
                                size: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-29

        Name          	Type	Mandatory	Description
        startTime     	int 	NO
        endTime       	int 	NO
        isolatedSymbol	str 	NO
        current       	int 	NO       	当前查询页。 开始值 1. 默认:1
        size          	int 	NO       	默认:10 最大:100
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_forceLiquidationRec, **to_local(locals()))

    # 查询全仓杠杆账户详情 (USER_DATA)
    def get_cross_account(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-30

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_cross_account, **to_local(locals()))

    # 查询杠杆账户订单 (USER_DATA)
    def get_order(self, symbol: str = '', isIsolated: str = '', orderId: int = '', origClientOrderId: str = '',
                  recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-31

        Name             	Type	Mandatory	Description
        symbol           	str 	YES
        isIsolated       	str 	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        orderId          	int 	NO
        origClientOrderId	str 	NO
        recvWindow       	int 	NO
        '''
        return self.send_request(*self.endpoints.get_order, **to_local(locals()))

    # 查询杠杆账户挂单记录 (USER_DATA)
    def get_openOrders(self, symbol: str = '', isIsolated: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-32

        Name      	Type	Mandatory	Description
        symbol    	str 	NO
        isIsolated	str 	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_openOrders, **to_local(locals()))

    # 查询杠杆账户的所有订单 (USER_DATA)
    def get_allOrders(self, symbol: str = '', isIsolated: str = '', orderId: int = '', startTime: int = '',
                      endTime: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-33

        Name      	Type	Mandatory	Description
        symbol    	str 	YES
        isIsolated	str 	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        orderId   	int 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	默认 500;最大500.
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_allOrders, **to_local(locals()))

    # 杠杆账户 OCO 下单(TRADE)
    def set_order_oco(self, symbol: str = '', isIsolated: str = '', listClientOrderId: str = '', side: str = '',
                      quantity: Union[float, int] = '', limitClientOrderId: str = '', price: Union[float, int] = '',
                      limitIcebergQty: Union[float, int] = '', stopClientOrderId: str = '',
                      stopPrice: Union[float, int] = '', stopLimitPrice: Union[float, int] = '',
                      stopIcebergQty: Union[float, int] = '', stopLimitTimeInForce: str = '',
                      newOrderRespType: str = '',
                      sideEffectType: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#oco-trade-3

        Name                	Type            	Mandatory	Description
        symbol              	str             	YES
        isIsolated          	str             	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        listClientOrderId   	str             	NO       	整个orderList的唯一ID
        side                	str             	YES      	详见枚举定义：订单方向
        quantity            	Union[float,int]	YES
        limitClientOrderId  	str             	NO       	限价单的唯一ID
        price               	Union[float,int]	YES
        limitIcebergQty     	Union[float,int]	NO
        stopClientOrderId   	str             	NO       	止损/止损限价单的唯一ID
        stopPrice           	Union[float,int]	YES
        stopLimitPrice      	Union[float,int]	NO
        stopIcebergQty      	Union[float,int]	NO
        stopLimitTimeInForce	str             	NO
        newOrderRespType    	str             	NO       	详见枚举定义：订单返回类型
        sideEffectType      	str             	NO       	NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY; 默认为 NO_SIDE_EFFECT
        recvWindow          	int             	NO
        '''
        return self.send_request(*self.endpoints.set_order_oco, **to_local(locals()))

    # 取消杠杆账户 OCO 订单(TRADE)
    def cancel_orderList(self, symbol: str = '', isIsolated: str = '', orderListId: int = '',
                         listClientOrderId: str = '',
                         newClientOrderId: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#oco-trade-4

        Name             	Type	Mandatory	Description
        symbol           	str 	YES
        isIsolated       	str 	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        orderListId      	int 	NO
        listClientOrderId	str 	NO
        newClientOrderId 	str 	NO       	用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。
        recvWindow       	int 	NO
        '''
        return self.send_request(*self.endpoints.cancel_orderList, **to_local(locals()))

    # 查询杠杆账户 OCO (USER_DATA)
    def get_orderList(self, isIsolated: str = '', symbol: str = '', orderListId: int = '', origClientOrderId: str = '',
                      recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#oco-user_data-4

        Name             	Type	Mandatory	Description
        isIsolated       	str 	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        symbol           	str 	NO       	逐仓杠杆必填，全仓杠杆不支持该参数
        orderListId      	int 	NO
        origClientOrderId	str 	NO
        recvWindow       	int 	NO
        '''
        return self.send_request(*self.endpoints.get_orderList, **to_local(locals()))

    # 查询特定杠杆账户所有 OCO (USER_DATA)
    def get_allOrderList(self, isIsolated: str = '', symbol: str = '', fromId: int = '', startTime: int = '',
                         endTime: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#oco-user_data-5

        Name      	Type	Mandatory	Description
        isIsolated	str 	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        symbol    	str 	NO       	逐仓杠杆必填，全仓杠杆不支持该参数
        fromId    	int 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	默认值: 500; 最大值: 1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_allOrderList, **to_local(locals()))

    # 查询杠杆账户 OCO 挂单 (USER_DATA)
    def get_openOrderList(self, isIsolated: str = '', symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#oco-user_data-6

        Name      	Type	Mandatory	Description
        isIsolated	str 	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        symbol    	str 	NO       	逐仓杠杆必填，全仓杠杆不支持该参数
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_openOrderList, **to_local(locals()))

    # 查询杠杆账户交易历史 (USER_DATA)
    def get_myTrades(self, symbol: str = '', isIsolated: str = '', orderId: int = '', startTime: int = '',
                     endTime: int = '', fromId: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-34

        Name      	Type	Mandatory	Description
        symbol    	str 	YES
        isIsolated	str 	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        orderId   	int 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        fromId    	int 	NO       	获取TradeId，默认获取近期交易历史。
        limit     	int 	NO       	默认 500; 最大 1000.
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_myTrades, **to_local(locals()))

    # 查询账户最大可借贷额度(USER_DATA)
    def get_maxBorrowable(self, asset: str = '', isolatedSymbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-35

        Name          	Type	Mandatory	Description
        asset         	str 	YES
        isolatedSymbol	str 	NO       	逐仓交易对，适用于逐仓查询
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_maxBorrowable, **to_local(locals()))

    # 查询最大可转出额 (USER_DATA)
    def get_maxTransferable(self, asset: str = '', isolatedSymbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-36

        Name          	Type	Mandatory	Description
        asset         	str 	YES
        isolatedSymbol	str 	NO       	逐仓交易对，适用于逐仓查询
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_maxTransferable, **to_local(locals()))

    # 查询Margin账户信息汇总 (USER_DATA)
    def get_tradeCoeff(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#margin-user_data

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_tradeCoeff, **to_local(locals()))

    # 杠杆逐仓账户划转 (MARGIN)
    def set_isolated_transfer(self, asset: str = '', symbol: str = '', transFrom: str = '', transTo: str = '',
                              amount: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#margin-8

        Name      	Type            	Mandatory	Description
        asset     	str             	YES      	被划转的资产, 比如, BTC
        symbol    	str             	YES      	逐仓 symbol
        transFrom 	str             	YES      	"SPOT", "ISOLATED_MARGIN"
        transTo   	str             	YES      	"SPOT", "ISOLATED_MARGIN"
        amount    	Union[float,int]	YES      	划转数量
        recvWindow	int             	NO       	赋值不能大于 60000
        '''
        return self.send_request(*self.endpoints.set_isolated_transfer, **to_local(locals()))

    # 获取杠杆逐仓划转历史 (USER_DATA)
    def get_isolated_transfer(self, asset: str = '', symbol: str = '', transFrom: str = '', transTo: str = '',
                              startTime: int = '', endTime: int = '', current: int = '', size: int = '',
                              archived: str = '',
                              recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-37

        Name      	Type	Mandatory       	Description
        asset     	str 	NO
        symbol    	str 	YES             	逐仓 symbol
        transFrom 	str 	NO              	"SPOT", "ISOLATED_MARGIN"
        transTo   	str 	NO              	"SPOT", "ISOLATED_MARGIN"
        startTime 	int 	NO
        endTime   	int 	NO
        current   	int 	NO              	当前查询页。 从 1开始。 默认:1
        size      	int 	NO              	默认:10 最大:100
        archived  	str 	NO
        recvWindow	int 	NO  赋值不能大于 60000
        '''
        return self.send_request(*self.endpoints.get_isolated_transfer, **to_local(locals()))

    # 查询杠杆逐仓账户信息 (USER_DATA)
    def get_isolated_account(self, symbols: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-38

        Name      	Type	Mandatory	Description
        symbols   	str 	NO       	最多可以传5个symbol; 由","分隔的字符串表示. e.g. "BTCUSDT,BNBUSDT,ADAUSDT"
        recvWindow	int 	NO       	赋值不能大于 60000
        '''
        return self.send_request(*self.endpoints.get_isolated_account, **to_local(locals()))

    # 杠杆逐仓账户停用 (TRADE)
    def delete_isolated_account(self, symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-11

        Name      	Type	Mandatory	Description
        symbol    	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.delete_isolated_account, **to_local(locals()))

    # 杠杆逐仓账户启用 (TRADE)
    def set_isolated_account(self, symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-12

        Name      	Type	Mandatory	Description
        symbol    	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_isolated_account, **to_local(locals()))

    # 查询杠杆逐仓账户启用限制 (USER_DATA)
    def get_isolated_accountLimit(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-39

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_isolated_accountLimit, **to_local(locals()))

    # 查询逐仓杠杆交易对 (USER_DATA)
    def get_isolated_pair(self, symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-40

        Name      	Type	Mandatory	Description
        symbol    	str 	YES
        recvWindow	int 	NO       	赋值不能大于 60000
        '''
        return self.send_request(*self.endpoints.get_isolated_pair, **to_local(locals()))

    # 获取所有逐仓杠杆交易对(USER_DATA)
    def get_isolated_allPairs(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-41

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO       	赋值不能大于 60000
        '''
        return self.send_request(*self.endpoints.get_isolated_allPairs, **to_local(locals()))

    # 现货交易和杠杆利息BNB抵扣开关(USER_DATA)
    def set_bnbBurn(self, spotBNBBurn: str = '', interestBNBBurn: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#bnb-user_data-3

        Name           	Type	Mandatory	Description
        spotBNBBurn    	str 	NO       	"true" or "false", 是否使用BNB支付现货交易的手续费
        interestBNBBurn	str 	NO       	"true" or "false", 是否使用BNB支付杠杆贷款的利息
        recvWindow     	int 	NO       	赋值不能大于 60000
        '''
        return self.send_request(*self.endpoints.set_bnbBurn, **to_local(locals()))

    # 获取BNB抵扣开关状态 (USER_DATA)
    def get_bnbBurn(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#bnb-user_data-4

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO       	赋值不能大于 60000
        '''
        return self.send_request(*self.endpoints.get_bnbBurn, **to_local(locals()))

    # 获取杠杆利率历史 (USER_DATA)
    def get_interestRateHistory(self, asset: str = '', vipLevel: int = '', startTime: int = '', endTime: int = '',
                                recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-42

        Name      	Type	Mandatory	Description
        asset     	str 	YES
        vipLevel  	int 	NO       	默认用户当前等级
        startTime 	int 	NO       	默认7天前
        endTime   	int 	NO       	默认当天，时间间隔最大为1个月
        recvWindow	int 	NO       	赋值不能大于 60000
        '''
        return self.send_request(*self.endpoints.get_interestRateHistory, **to_local(locals()))

    # 获取全仓杠杆利率及限额 (USER_DATA)
    def get_crossMarginData(self, vipLevel: int = '', coin: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-43

        Name      	Type	Mandatory	Description
        vipLevel  	int 	NO       	默认为用户当前VIP等级
        coin      	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_crossMarginData, **to_local(locals()))

    # 获取逐仓杠杆利率及限额 (USER_DATA)
    def get_isolatedMarginData(self, vipLevel: int = '', symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-44

        Name      	Type	Mandatory	Description
        vipLevel  	int 	NO       	默认为用户当前VIP等级
        symbol    	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_isolatedMarginData, **to_local(locals()))

    # 获取逐仓档位信息 (USER_DATA)
    def get_isolatedMarginTier(self, symbol: str = '', tier: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-45

        Name      	Type	Mandatory	Description
        symbol    	str 	YES
        tier      	int 	NO       	不传则返回所有逐仓杠杆档位
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_isolatedMarginTier, **to_local(locals()))

    # 查询目前杠杆账户下单数 (TRADE)
    def get_rateLimit_order(self, isIsolated: str = '', symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-13

        Name      	Type	Mandatory	Description
        isIsolated	str 	NO       	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        symbol    	str 	NO       	逐仓交易对，查询逐仓杠杆账户必需
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_rateLimit_order, **to_local(locals()))

    # 杠杆小额资产转换BNB历史 (USER_DATA)
    def get_dribblet(self, startTime: int = '', endTime: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#bnb-user_data-5

        Name      	Type	Mandatory	Description
        startTime 	int 	NO
        endTime   	int 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_dribblet, **to_local(locals()))
