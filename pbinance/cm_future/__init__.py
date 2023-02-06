'''
币本位合约
https://binance-docs.github.io/apidocs/delivery/cn/#185368440e
'''

from .cm_market import CMMarket  # 行情信息
from .cm_account_trade import CMAccountTrade  # 账户与交易
from .cm_portfolio_margin import CMPortfolioMargin  # 统一账户

Market = CMMarket
AccountTrade = CMAccountTrade
PortfolioMargin = CMPortfolioMargin


class CM():
    def __init__(self, key='', secret=''):
        self.market = Market(key=key, secret=secret)
        self.accountTrade = AccountTrade(key=key, secret=secret)
        self.portfolioMargin = PortfolioMargin(key=key, secret=secret)
