from paux.param import to_local
from pbinance.client import Client
from typing import Union


# 行情信息
class _CMMarketEndpoints():
    get_ping = ['https://dapi.binance.com/','GET', '/dapi/v1/ping', False]  # 测试服务器连通性 PING
    get_time = ['https://dapi.binance.com/','GET', '/dapi/v1/time', False]  # 获取服务器时间
    get_exchangeInfo = ['https://dapi.binance.com/','GET', '/dapi/v1/exchangeInfo', False]  # 获取交易规则和交易对
    get_depth = ['https://dapi.binance.com/','GET', '/dapi/v1/depth', False]  # 深度信息
    get_trades = ['https://dapi.binance.com/','GET', '/dapi/v1/trades', False]  # 近期成交
    get_historicalTrades = ['https://dapi.binance.com/','GET', '/dapi/v1/historicalTrades', False]  # 查询历史成交 (MARKET_DATA)
    get_aggTrades = ['https://dapi.binance.com/','GET', '/dapi/v1/aggTrades', False]  # 近期成交(归集)
    get_premiumIndex = ['https://dapi.binance.com/','GET', '/dapi/v1/premiumIndex', False]  # 最新现货指数价格和Mark Price
    get_fundingRate = ['https://dapi.binance.com/','GET', '/dapi/v1/fundingRate', False]  # 查询永续合约资金费率历史
    get_klines = ['https://dapi.binance.com/','GET', '/dapi/v1/klines', False]  # K线数据
    get_continuousKlines = ['https://dapi.binance.com/','GET', '/dapi/v1/continuousKlines', False]  # 连续合约K线数据
    get_indexPriceKlines = ['https://dapi.binance.com/','GET', '/dapi/v1/indexPriceKlines', False]  # 价格指数K线数据
    get_markPriceKlines = ['https://dapi.binance.com/','GET', '/dapi/v1/markPriceKlines', False]  # 标记价格K线数据
    get_ticker_24hr = ['https://dapi.binance.com/','GET', '/dapi/v1/ticker/24hr', False]  # 24hr价格变动情况
    get_ticker_price = ['https://dapi.binance.com/','GET', '/dapi/v1/ticker/price', False]  # 最新价格
    get_ticker_bookTicker = ['https://dapi.binance.com/','GET', '/dapi/v1/ticker/bookTicker', False]  # 当前最优挂单
    get_openInterest = ['https://dapi.binance.com/','GET', '/dapi/v1/openInterest', False]  # 获取未平仓合约数
    get_openInterestHist = ['https://dapi.binance.com/','GET', '/futures/data/openInterestHist', False]  # 合约持仓量
    get_topLongShortAccountRatio = ['https://dapi.binance.com/','GET', '/futures/data/topLongShortAccountRatio', False]  # 大户账户数多空比
    get_topLongShortPositionRatio = ['https://dapi.binance.com/','GET', '/futures/data/topLongShortPositionRatio', False]  # 大户持仓量多空比
    get_globalLongShortAccountRatio = ['https://dapi.binance.com/','GET', '/futures/data/globalLongShortAccountRatio', False]  # 多空持仓人数比
    get_takerBuySellVol = ['https://dapi.binance.com/','GET', '/futures/data/takerBuySellVol', False]  # 合约主动买卖量
    get_basis = ['https://dapi.binance.com/','GET', '/futures/data/basis', False]  # 基差


class CMMarket(Client):
    endpoints = _CMMarketEndpoints

    # 测试服务器连通性 PING
    def get_ping(self):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#ping
        '''
        return self.send_request(*self.endpoints.get_ping, **to_local(locals()))

    # 获取服务器时间
    def get_time(self):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#3f1907847c
        '''
        return self.send_request(*self.endpoints.get_time, **to_local(locals()))

    # 获取交易规则和交易对
    def get_exchangeInfo(self):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#0f3f2d5ee7
        '''
        return self.send_request(*self.endpoints.get_exchangeInfo, **to_local(locals()))

    # 深度信息
    def get_depth(self, symbol: str = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#38a975b802

        Name  	Type	Mandatory	Description
        symbol	str 	YES      	交易对
        limit 	int 	NO       	默认 500; 可选值:[5, 10, 20, 50, 100, 500, 1000]
        '''
        return self.send_request(*self.endpoints.get_depth, **to_local(locals()))

    # 近期成交
    def get_trades(self, symbol: str = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#404aacd9b3

        Name  	Type	Mandatory	Description
        symbol	str 	YES      	交易对
        limit 	int 	NO       	默认值:500 最大值:1000.
        '''
        return self.send_request(*self.endpoints.get_trades, **to_local(locals()))

    # 查询历史成交 (MARKET_DATA)
    def get_historicalTrades(self, symbol: str = '', limit: int = '', fromId: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#market_data

        Name  	Type	Mandatory	Description
        symbol	str 	YES      	交易对
        limit 	int 	NO       	默认值:500 最大值:1000.
        fromId	int 	NO       	从哪一条成交id开始返回. 缺省返回最近的成交记录
        '''
        return self.send_request(*self.endpoints.get_historicalTrades, **to_local(locals()))

    # 近期成交(归集)
    def get_aggTrades(self, symbol: str = '', fromId: int = '', startTime: int = '', endTime: int = '',
                      limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#c59e471e81

        Name     	Type	Mandatory	Description
        symbol   	str 	YES      	交易对
        fromId   	int 	NO       	从包含fromID的成交开始返回结果
        startTime	int 	NO       	从该时刻之后的成交记录开始返回结果
        endTime  	int 	NO       	返回该时刻为止的成交记录
        limit    	int 	NO       	默认 500; 最大 1000.
        '''
        return self.send_request(*self.endpoints.get_aggTrades, **to_local(locals()))

    # 最新现货指数价格和Mark Price
    def get_premiumIndex(self, symbol: str = '', pair: str = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#mark-price

        Name  	Type	Mandatory	Description
        symbol	str 	NO       	交易对
        pair  	str 	NO       	标的交易对
        '''
        return self.send_request(*self.endpoints.get_premiumIndex, **to_local(locals()))

    # 查询永续合约资金费率历史
    def get_fundingRate(self, symbol: str = '', startTime: int = '', endTime: int = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#bb3cc57bdf

        Name     	Type	Mandatory	Description
        symbol   	str 	YES      	交易对
        startTime	int 	NO       	起始时间
        endTime  	int 	NO       	结束时间
        limit    	int 	NO       	默认值:100 最大值:1000
        '''
        return self.send_request(*self.endpoints.get_fundingRate, **to_local(locals()))

    # K线数据
    def get_klines(self, symbol: str = '', interval: str = '', startTime: int = '', endTime: int = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#k

        Name     	Type	Mandatory	Description
        symbol   	str 	YES      	交易对
        interval 	str 	YES      	时间间隔
        startTime	int 	NO       	起始时间
        endTime  	int 	NO       	结束时间
        limit    	int 	NO       	默认值:500 最大值:1500
        '''
        return self.send_request(*self.endpoints.get_klines, **to_local(locals()))

    # 连续合约K线数据
    def get_continuousKlines(self, pair: str = '', contractType: str = '', interval: str = '', startTime: int = '',
                             endTime: int = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#k-2

        Name        	Type	Mandatory	Description
        pair        	str 	YES      	标的交易对
        contractType	str 	YES      	合约类型
        interval    	str 	YES      	时间间隔
        startTime   	int 	NO       	起始时间
        endTime     	int 	NO       	结束时间
        limit       	int 	NO       	默认值:500 最大值:1500
        '''
        return self.send_request(*self.endpoints.get_continuousKlines, **to_local(locals()))

    # 价格指数K线数据
    def get_indexPriceKlines(self, pair: str = '', interval: str = '', startTime: int = '', endTime: int = '',
                             limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#k-3

        Name     	Type	Mandatory	Description
        pair     	str 	YES      	标的交易对
        interval 	str 	YES      	时间间隔
        startTime	int 	NO       	起始时间
        endTime  	int 	NO       	结束时间
        limit    	int 	NO       	默认值:500 最大值:1500
        '''
        return self.send_request(*self.endpoints.get_indexPriceKlines, **to_local(locals()))

    # 标记价格K线数据
    def get_markPriceKlines(self, symbol: str = '', interval: str = '', startTime: int = '', endTime: int = '',
                            limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#k-4

        Name     	Type	Mandatory	Description
        symbol   	str 	YES      	交易对
        interval 	str 	YES      	时间间隔
        startTime	int 	NO       	起始时间
        endTime  	int 	NO       	结束时间
        limit    	int 	NO       	默认值:500 最大值:1500
        '''
        return self.send_request(*self.endpoints.get_markPriceKlines, **to_local(locals()))

    # 24hr价格变动情况
    def get_ticker_24hr(self, symbol: str = '', pair: str = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#24hr

        Name  	Type	Mandatory	Description
        symbol	str 	NO       	交易对
        pair  	str 	NO       	标的交易对
        '''
        return self.send_request(*self.endpoints.get_ticker_24hr, **to_local(locals()))

    # 最新价格
    def get_ticker_price(self, symbol: str = '', pair: str = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#8ff46b58de

        Name  	Type	Mandatory	Description
        symbol	str 	NO       	交易对
        pair  	str 	NO       	标的交易对
        '''
        return self.send_request(*self.endpoints.get_ticker_price, **to_local(locals()))

    # 当前最优挂单
    def get_ticker_bookTicker(self, symbol: str = '', pair: str = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#5393cd07b4

        Name  	Type	Mandatory	Description
        symbol	str 	NO       	交易对
        pair  	str 	NO       	标的交易对
        '''
        return self.send_request(*self.endpoints.get_ticker_bookTicker, **to_local(locals()))

    # 获取未平仓合约数
    def get_openInterest(self, symbol: str = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#f6cc22e496

        Name  	Type	Mandatory	Description
        symbol	str 	YES      	交易对
        '''
        return self.send_request(*self.endpoints.get_openInterest, **to_local(locals()))

    # 合约持仓量
    def get_openInterestHist(self, pair: str = '', contractType: str = '', period: str = '', limit: int = '',
                             startTime: int = '', endTime: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#c1c9193984

        Name        	Type	Mandatory	Description
        pair        	str 	YES      	BTCUSD
        contractType	str 	YES      	ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL
        period      	str 	YES      	"5m","15m","30m","1h","2h","4h","6h","12h","1d"
        limit       	int 	NO       	Default 30,Max 500
        startTime   	int 	NO
        endTime     	int 	NO
        '''
        return self.send_request(*self.endpoints.get_openInterestHist, **to_local(locals()))

    # 大户账户数多空比
    def get_topLongShortAccountRatio(self, pair: str = '', period: str = '', limit: int = '', startTime: int = '',
                                     endTime: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#4d050dd845

        Name     	Type	Mandatory	Description
        pair     	str 	YES      	BTCUSD
        period   	str 	YES      	"5m","15m","30m","1h","2h","4h","6h","12h","1d"
        limit    	int 	NO       	Default 30,Max 500
        startTime	int 	NO
        endTime  	int 	NO
        '''
        return self.send_request(*self.endpoints.get_topLongShortAccountRatio, **to_local(locals()))

    # 大户持仓量多空比
    def get_topLongShortPositionRatio(self, pair: str = '', period: str = '', limit: int = '', startTime: int = '',
                                      endTime: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#269e531011

        Name     	Type	Mandatory	Description
        pair     	str 	YES      	BTCUSD
        period   	str 	YES      	"5m","15m","30m","1h","2h","4h","6h","12h","1d"
        limit    	int 	NO       	Default 30,Max 500
        startTime	int 	NO
        endTime  	int 	NO
        '''
        return self.send_request(*self.endpoints.get_topLongShortPositionRatio, **to_local(locals()))

    # 多空持仓人数比
    def get_globalLongShortAccountRatio(self, pair: str = '', period: str = '', limit: int = '', startTime: int = '',
                                        endTime: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#4d55ab5a20

        Name     	Type	Mandatory	Description
        pair     	str 	YES      	BTCUSD
        period   	str 	YES      	"5m","15m","30m","1h","2h","4h","6h","12h","1d"
        limit    	int 	NO       	Default 30,Max 500
        startTime	int 	NO
        endTime  	int 	NO
        '''
        return self.send_request(*self.endpoints.get_globalLongShortAccountRatio, **to_local(locals()))

    # 合约主动买卖量
    def get_takerBuySellVol(self, pair: str = '', contractType: str = '', period: str = '', limit: int = '',
                            startTime: int = '', endTime: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#249be3ac39

        Name        	Type	Mandatory	Description
        pair        	str 	YES      	BTCUSD
        contractType	str 	YES      	ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL
        period      	str 	YES      	"5m","15m","30m","1h","2h","4h","6h","12h","1d"
        limit       	int 	NO       	Default 30,Max 500
        startTime   	int 	NO
        endTime     	int 	NO
        '''
        return self.send_request(*self.endpoints.get_takerBuySellVol, **to_local(locals()))

    # 基差
    def get_basis(self, pair: str = '', contractType: str = '', period: str = '', limit: int = '', startTime: int = '',
                  endTime: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#282fdb520f

        Name        	Type	Mandatory	Description
        pair        	str 	YES      	BTCUSD
        contractType	str 	YES      	CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL
        period      	str 	YES      	"5m","15m","30m","1h","2h","4h","6h","12h","1d"
        limit       	int 	NO       	Default 30,Max 500
        startTime   	int 	NO
        endTime     	int 	NO
        '''
        return self.send_request(*self.endpoints.get_basis, **to_local(locals()))
