'''
欧式期权
https://binance-docs.github.io/apidocs/voptions/cn/#185368440e
'''

from .eo_market import EOMarket  # 行情信息
from .eo_account_trade import EOAccountTrade  # 账户与交易
from .eo_market_maker import EOMarketMaker  # 市场接口

Market = EOMarket
AccountTrade = EOAccountTrade
MarketMaker = EOMarketMaker

class EO():
    def __init__(self, key='', secret=''):
        self.market = Market(key=key, secret=secret)
        self.accountTrade = AccountTrade(key=key, secret=secret)
        self.marketMaker = MarketMaker(key=key, secret=secret)
