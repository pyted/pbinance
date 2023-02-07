from paux.param import to_local
from pbinance.client import Client
from typing import Union

# 行情信息
class _EOMarketEndpoints():
    get_ping = ['https://eapi.binance.com/','GET', '/eapi/v1/ping', False]  # 测试服务器连通性 PING
    get_time = ['https://eapi.binance.com/','GET', '/eapi/v1/time', False]  # 获取服务器时间
    get_exchangeInfo = ['https://eapi.binance.com/','GET', '/eapi/v1/exchangeInfo', False]  # 获取交易规则和交易对
    get_depth = ['https://eapi.binance.com/','GET', '/eapi/v1/depth', False]  # 深度信息
    get_trades = ['https://eapi.binance.com/','GET', '/eapi/v1/trades', False]  # 近期成交
    get_historicalTrades = ['https://eapi.binance.com/','GET', '/eapi/v1/historicalTrades', False]  # 查询历史成交(MARKET_DATA)
    get_klines = ['https://eapi.binance.com/','GET', '/eapi/v1/klines', False]  # K线数据
    get_mark = ['https://eapi.binance.com/','GET', '/eapi/v1/mark', False]  # 查询期权标记价格
    get_ticker = ['https://eapi.binance.com/','GET', '/eapi/v1/ticker', False]  # 24hr价格变动情况
    get_index = ['https://eapi.binance.com/','GET', '/eapi/v1/index', False]  # 标的最新价格
    get_exerciseHistory = ['https://eapi.binance.com/','GET', '/eapi/v1/exerciseHistory', False]  # 历史行权记录
    get_openInterest = ['https://eapi.binance.com/','GET', '/eapi/v1/openInterest', False]  # 合约持仓量

class EOMarket(Client):
    endpoints = _EOMarketEndpoints

    # 测试服务器连通性 PING
    def get_ping(self):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#ping
        '''
        return self.send_request(*self.endpoints.get_ping, **to_local(locals()))

    # 获取服务器时间
    def get_time(self):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#3f1907847c
        '''
        return self.send_request(*self.endpoints.get_time, **to_local(locals()))

    # 获取交易规则和交易对
    def get_exchangeInfo(self):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#0f3f2d5ee7
        '''
        return self.send_request(*self.endpoints.get_exchangeInfo, **to_local(locals()))

    # 深度信息
    def get_depth(self, symbol: str = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#38a975b802

        Name  	Type	Mandatory	Description
        symbol	str 	YES      	交易对
        limit 	int 	NO       	默认 100; 可选值:[10, 20, 50, 100, 500, 1000]
        '''
        return self.send_request(*self.endpoints.get_depth, **to_local(locals()))

    # 近期成交
    def get_trades(self, symbol: str = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#404aacd9b3

        Name  	Type	Mandatory	Description
        symbol	str 	YES      	交易对
        limit 	int 	NO       	默认:100，最大500
        '''
        return self.send_request(*self.endpoints.get_trades, **to_local(locals()))

    # 查询历史成交(MARKET_DATA)
    def get_historicalTrades(self, symbol: str = '', limit: int = '', fromId: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#market_data

        Name  	Type	Mandatory	Description
        symbol	str 	YES      	交易对
        limit 	int 	NO       	默认值:100 最大值:500.
        fromId	int 	NO       	从哪一条成交id开始返回. 缺省返回最近的成交记录
        '''
        return self.send_request(*self.endpoints.get_historicalTrades, **to_local(locals()))

    # K线数据
    def get_klines(self, symbol: str = '', interval: str = '', startTime: int = '', endTime: int = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#k

        Name     	Type	Mandatory	Description
        symbol   	str 	YES      	交易对
        interval 	str 	YES      	时间间隔
        startTime	int 	NO       	起始时间
        endTime  	int 	NO       	结束时间
        limit    	int 	NO       	默认值:500 最大值:1500.
        '''
        return self.send_request(*self.endpoints.get_klines, **to_local(locals()))

    # 查询期权标记价格
    def get_mark(self, symbol: str = '', startTime: int = '', endTime: int = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#d49aa3823d

        Name     	Type	Mandatory	Description
        symbol   	str 	NO       	交易对
        startTime	int 	NO       	起始时间
        endTime  	int 	NO       	结束时间
        limit    	int 	NO       	默认值:100 最大值:1000
        '''
        return self.send_request(*self.endpoints.get_mark, **to_local(locals()))

    # 24hr价格变动情况
    def get_ticker(self, symbol: str = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#24hr

        Name  	Type	Mandatory	Description
        symbol	str 	NO       	交易对
        '''
        return self.send_request(*self.endpoints.get_ticker, **to_local(locals()))

    # 标的最新价格
    def get_index(self, underlying: str = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#2b0691658e

        Name      	Type	Mandatory	Description
        underlying	str 	YES      	现货交易对如BTCUSDT
        '''
        return self.send_request(*self.endpoints.get_index, **to_local(locals()))

    # 历史行权记录
    def get_exerciseHistory(self, startTime: int = '', endTime: int = '', limit: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#c7c743e6ce

        Name     	Type	Mandatory	Description
        startTime	int 	NO       	开始时间
        endTime  	int 	NO       	结束时间
        limit    	int 	NO       	默认值:100 最大值:100.
        '''
        return self.send_request(*self.endpoints.get_exerciseHistory, **to_local(locals()))

    # 合约持仓量
    def get_openInterest(self, underlyingAsset: str = '', expiration: str = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#c1c9193984

        Name           	Type	Mandatory	Description
        underlyingAsset	str 	YES      	标的资产，如ETH或BTC
        expiration     	str 	YES      	到期日，如221225
        '''
        return self.send_request(*self.endpoints.get_openInterest, **to_local(locals()))

