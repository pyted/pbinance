'''
币币杠杆(除账户与交易外，币币杠杆交易中很多接口与SPOT公用)
https://binance-docs.github.io/apidocs/spot/cn/#185368440e
'''

from .margin_account_trade import MarginAccountTrade  # 账户与交易

AccountTrade = MarginAccountTrade


class Margin():
    def __init__(self, key='', secret=''):
        from pbinance.spot.spot_market import SPOTMarket as Market
        from pbinance.spot.spot_portfolio_margin import SPOTPortfolioMargin as PortfolioMargin
        from pbinance.spot.wallet import Wallet

        self.accountTrade = AccountTrade(key=key, secret=secret)  # 币币杠杆账户与交易
        # *******************************************************
        self.market = Market(key=key, secret=secret)  # 使用币币交易行情信息
        self.portfolioMargin = PortfolioMargin(key=key, secret=secret)  # 使用币币交易的统一账户
        self.wallet = Wallet(key=key, secret=secret)  # 钱包
