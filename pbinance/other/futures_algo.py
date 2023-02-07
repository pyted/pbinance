from paux.param import to_local
from pbinance.client import Client
from typing import Union


# 合约策略
class _FuturesAlgoEndpoints():
    set_newOrderVp = ['https://api.binance.com/','POST', '/sapi/v1/algo/futures/newOrderVp', True]  # 成交量份额参与算法(VP)下单 (TRADE)
    set_newOrderTwap = ['https://api.binance.com/','POST', '/sapi/v1/algo/futures/newOrderTwap', True]  # 时间加权平均价格策略(Twap)下单 (TRADE)
    delete_order = ['https://api.binance.com/','DELETE', '/sapi/v1/algo/futures/order', True]  # 取消策略订单 (TRADE)
    get_openOrders = ['https://api.binance.com/','GET', '/sapi/v1/algo/futures/openOrders', True]  # 查询当前策略订单挂单 (USER_DATA)
    get_historicalOrders = ['https://api.binance.com/','GET', '/sapi/v1/algo/futures/historicalOrders', True]  # 查询历史策略订单 (USER_DATA)
    get_subOrders = ['https://api.binance.com/','GET', '/sapi/v1/algo/futures/subOrders', True]  # 查询执行子订单 (USER_DATA)


class FuturesAlgo(Client):
    endpoints = _FuturesAlgoEndpoints

    # 成交量份额参与算法(VP)下单 (TRADE)
    def set_newOrderVp(self, symbol: str = '', side: str = '', positionSide: str = '', quantity: Union[float, int] = '',
                       urgency: str = '', clientAlgoId: str = '', reduceOnly: bool = '',
                       limitPrice: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#vp-trade

        Name        	Type            	Mandatory	Description
        symbol      	str             	YES      	交易对 eg. BTCUSDT
        side        	str             	YES      	买卖方向 ( BUY or SELL )
        positionSide	str             	NO       	持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择 LONG 或 SHORT
        quantity    	Union[float,int]	YES
        urgency     	str             	YES      	代表当前执行的相对速率; ENUM: LOW（慢）, MEDIUM（中等）, HIGH（快）
        clientAlgoId	str             	NO       	必须传入32位，如果未发送，则自动生成
        reduceOnly  	bool            	NO       	true, false; 非双开模式下默认false；双开模式下不接受此参数； 开仓不接受此参数
        limitPrice  	Union[float,int]	NO       	限价单价格; 若未发送，则以市场价下单
        recvWindow  	int             	NO
        '''
        return self.send_request(*self.endpoints.set_newOrderVp, **to_local(locals()))

    # 时间加权平均价格策略(Twap)下单 (TRADE)
    def set_newOrderTwap(self, symbol: str = '', side: str = '', positionSide: str = '',
                         quantity: Union[float, int] = '', duration: int = '', clientAlgoId: str = '',
                         reduceOnly: bool = '', limitPrice: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#twap-trade

        Name        	Type            	Mandatory	Description
        symbol      	str             	YES      	交易对 eg. BTCUSDT
        side        	str             	YES      	买卖方向 ( BUY or SELL )
        positionSide	str             	NO       	持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择 LONG 或 SHORT
        quantity    	Union[float,int]	YES
        duration    	int             	YES      	请以秒为单位发送[300,86400]；少于 5 分钟 => 默认为 5 分钟；大于 24h => 默认为 24h
        clientAlgoId	str             	NO       	必须传入32位，如果未发送，则自动生成
        reduceOnly  	bool            	NO       	true, false; 非双开模式下默认false；双开模式下不接受此参数； 开仓不接受此参数
        limitPrice  	Union[float,int]	NO       	限价单价格; 若未发送，则以市场价下单
        recvWindow  	int             	NO
        '''
        return self.send_request(*self.endpoints.set_newOrderTwap, **to_local(locals()))

    # 取消策略订单 (TRADE)
    def delete_order(self, algoId: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-14

        Name      	Type	Mandatory	Description
        algoId    	int 	YES      	eg. 14511
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.delete_order, **to_local(locals()))

    # 查询当前策略订单挂单 (USER_DATA)
    def get_openOrders(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-83

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_openOrders, **to_local(locals()))

    # 查询历史策略订单 (USER_DATA)
    def get_historicalOrders(self, symbol: str = '', side: str = '', startTime: int = '', endTime: int = '',
                             page: int = '', pageSize: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-84

        Name      	Type	Mandatory	Description
        symbol    	str 	NO       	交易对 eg. BTCUSDT
        side      	str 	NO       	BUY 或者 SELL
        startTime 	int 	NO       	毫秒级时间戳  eg.1641522717552
        endTime   	int 	NO       	毫秒级时间戳  eg.1641522526562
        page      	int 	NO       	默认 1
        pageSize  	int 	NO       	最小 1, 最大 100; 默认 100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_historicalOrders, **to_local(locals()))

    # 查询执行子订单 (USER_DATA)
    def get_subOrders(self, algoId: int = '', page: int = '', pageSize: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-85

        Name      	Type	Mandatory	Description
        algoId    	int 	YES
        page      	int 	NO       	默认1
        pageSize  	int 	NO       	最小 1， 最大 100; 默认 100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_subOrders, **to_local(locals()))
