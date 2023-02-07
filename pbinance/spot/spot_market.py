from paux.param import to_local
from pbinance.client import Client
from typing import Union

# 行情信息
class _SPOTMarketEndpoints():
    get_ping = ['https://api.binance.com/', 'GET', '/api/v3/ping', False]  # 测试服务器连通性
    get_time = ['https://api.binance.com/', 'GET', '/api/v3/time', False]  # 获取服务器时间
    get_exchangeInfo = ['https://api.binance.com/', 'GET', '/api/v3/exchangeInfo', False]  # 交易规范信息
    get_depth = ['https://api.binance.com/', 'GET', '/api/v3/depth', False]  # 深度信息
    get_trades = ['https://api.binance.com/', 'GET', '/api/v3/trades', False]  # 近期成交列表
    get_historicalTrades = ['https://api.binance.com/', 'GET', '/api/v3/historicalTrades', False]  # 查询历史成交 (MARKET_DATA)
    get_aggTrades = ['https://api.binance.com/', 'GET', '/api/v3/aggTrades', False]  # 近期成交(归集)
    get_klines = ['https://api.binance.com/', 'GET', '/api/v3/klines', False]  # K线数据
    get_avgPrice = ['https://api.binance.com/', 'GET', '/api/v3/avgPrice', False]  # 当前平均价格
    get_uiKlines = ['https://api.binance.com/', 'GET', '/api/v3/uiKlines', False]  # UIK线数据
    get_ticker_24hr = ['https://api.binance.com/', 'GET', '/api/v3/ticker/24hr', False]  # 24hr 价格变动情况
    get_ticker_price = ['https://api.binance.com/', 'GET', '/api/v3/ticker/price', False]  # 最新价格
    get_ticker_bookTicker = ['https://api.binance.com/', 'GET', '/api/v3/ticker/bookTicker', False]  # 当前最优挂单
    get_ticker = ['https://api.binance.com/', 'GET', '/api/v3/ticker', False]  # 滚动窗口价格变动统计


class SPOTMarket(Client):
    endpoints = _SPOTMarketEndpoints

    # 测试服务器连通性
    def get_ping(self):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#16073bbcf1
        '''
        return self.send_request(*self.endpoints.get_ping, **to_local(locals()))

    # 获取服务器时间
    def get_time(self):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#3f1907847c
        '''
        return self.send_request(*self.endpoints.get_time, **to_local(locals()))

    # 交易规范信息
    def get_exchangeInfo(self, symbol: str = '', symbols: list = [], permissions: Union[list, str] = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#e7746f7d60
        Name     	Type	Mandatory	Description
        symbol   	str 	YES         单个交易对
        symbols   	list 	NO          多个交易对
        permissions	int 	NO          交易权限
        '''
        return self.send_request(*self.endpoints.get_exchangeInfo, **to_local(locals()))

    # 深度信息
    def get_depth(self, symbol: str = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#38a975b802

        Name  	Type	Mandatory	Description
        symbol	str 	YES
        limit 	int 	NO
        '''
        return self.send_request(*self.endpoints.get_depth, **to_local(locals()))

    # 近期成交列表
    def get_trades(self, symbol: str = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#2c5e424c25

        Name  	Type	Mandatory	Description
        symbol	str 	YES
        limit 	int 	NO       	默认 500; 最大值 1000.
        '''
        return self.send_request(*self.endpoints.get_trades, **to_local(locals()))

    # 查询历史成交 (MARKET_DATA)
    def get_historicalTrades(self, symbol: str = '', limit: int = '', fromId: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#market_data

        Name  	Type	Mandatory	Description
        symbol	str 	YES
        limit 	int 	NO       	默认 500; 最大值 1000.
        fromId	int 	NO       	从哪一条成交id开始返回. 缺省返回最近的成交记录。
        '''
        return self.send_request(*self.endpoints.get_historicalTrades, **to_local(locals()))

    # 近期成交(归集)
    def get_aggTrades(self, symbol: str = '', fromId: int = '', startTime: int = '', endTime: int = '',
                      limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#c59e471e81

        Name     	Type	Mandatory	Description
        symbol   	str 	YES
        fromId   	int 	NO       	从包含fromId的成交id开始返回结果
        startTime	int 	NO       	从该时刻之后的成交记录开始返回结果
        endTime  	int 	NO       	返回该时刻为止的成交记录
        limit    	int 	NO       	默认 500; 最大 1000.
        '''
        return self.send_request(*self.endpoints.get_aggTrades, **to_local(locals()))

    # K线数据
    def get_klines(self, symbol: str = '', interval: str = '', startTime: int = '', endTime: int = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#k

        Name     	Type	Mandatory	Description
        symbol   	str 	YES
        interval 	str 	YES      	详见枚举定义：K线间隔
        startTime	int 	NO
        endTime  	int 	NO
        limit    	int 	NO       	默认 500; 最大 1000.
        '''
        return self.send_request(*self.endpoints.get_klines, **to_local(locals()))

    # 当前平均价格
    def get_avgPrice(self, symbol: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#3b4f48cdbb

        Name  	Type	Mandatory	Description
        symbol	str 	YES
        '''
        return self.send_request(*self.endpoints.get_avgPrice, **to_local(locals()))

    # UIK线数据
    def get_uiKlines(self, symbol: str = '', interval: str = '', startTime: int = '', endTime: int = '',
                     limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#uik

        Name     	Type	Mandatory	Description
        symbol   	str 	YES
        interval 	str 	YES
        startTime	int 	NO
        endTime  	int 	NO
        limit    	int 	NO       	默认 500; 最大 1000.
        '''
        return self.send_request(*self.endpoints.get_uiKlines, **to_local(locals()))

    # 24hr 价格变动情况
    def get_ticker_24hr(self, symbol: str = '', symbols: str = '', type: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#24hr

        Name   	Type	Mandatory	Description
        symbol 	str 	NO
        symbols	str 	NO
        type   	str 	NO
        '''
        return self.send_request(*self.endpoints.get_ticker_24hr, **to_local(locals()))

    # 最新价格
    def get_ticker_price(self, symbol: str = '', symbols: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#8ff46b58de

        Name   	Type	Mandatory	Description
        symbol 	str 	NO
        symbols	str 	NO
        '''
        return self.send_request(*self.endpoints.get_ticker_price, **to_local(locals()))

    # 当前最优挂单
    def get_ticker_bookTicker(self, symbol: str = '', symbols: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#5393cd07b4

        Name   	Type	Mandatory	Description
        symbol 	str 	NO
        symbols	str 	NO
        '''
        return self.send_request(*self.endpoints.get_ticker_bookTicker, **to_local(locals()))

    # 滚动窗口价格变动统计
    def get_ticker(self, symbol: str = '', symbols: list = [], windowSize: str = '', type: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#4175e32579
        Name   	    Type	Mandatory	Description
        symbol 	    str 	YES         提供 symbol或者symbols 其中之一 symbols 可以传入的格式: ["BTCUSDT","BNBUSDT"] or %5B%22BTCUSDT%22,%22BNBUSDT%22%5D
        symbols	    str
        windowSize  str     NO          默认为 1d windowSize 支持的值: 如果是分钟: 1m,2m....59m 如果是小时: 1h, 2h....23h 如果是天: 1d...7d
        type        str     NO          可接受的参数: FULL or MINI. 如果不提供, 默认值为 FULL
        '''
        return self.send_request(*self.endpoints.get_ticker, **to_local(locals()))
