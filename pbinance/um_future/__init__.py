'''
U本位合约
https://binance-docs.github.io/apidocs/futures/cn/#185368440e
'''

from .um_market import UMMarket  # 行情信息
from .um_account_trade import UMAccountTrade  # 账户与交易
from .um_portfolio_margin import UMPortfolioMargin  # 统一账户

Market = UMMarket
AccountTrade = UMAccountTrade
PortfolioMargin = UMPortfolioMargin


class UM():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.market = Market(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.accountTrade = AccountTrade(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.portfolioMargin = PortfolioMargin(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
