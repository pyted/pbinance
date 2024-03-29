'''
币币交易
https://binance-docs.github.io/apidocs/spot/cn/#185368440e
'''

from .spot_market import SPOTMarket  # 行情信息
from .spot_account_trade import SPOTAccountTrade  # 账户与交易
from .spot_portfolio_margin import SPOTPortfolioMargin  # 统一账户
from .wallet import Wallet

Market = SPOTMarket
AccountTrade = SPOTAccountTrade
PortfolioMargin = SPOTPortfolioMargin


class SPOT():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.accountTrade = AccountTrade(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.market = Market(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.portfolioMargin = PortfolioMargin(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.wallet = Wallet(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
