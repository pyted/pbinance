from paux.param import to_local
from pbinance.client import Client


# 统一账户
class _SPOTPortfolioMarginEndpoints():
    portfolio_account = ['https://api.binance.com/','GET', '/sapi/v1/portfolio/account', True]  # 查询统一账户信息 (USER_DATA)
    portfolio_collateralRate = ['https://api.binance.com/','GET', '/sapi/v1/portfolio/collateralRate', False]  # 统一账户资产质押率 (MARKET_DATA)
    portfolio_pmLoan = ['https://api.binance.com/','GET', '/sapi/v1/portfolio/pmLoan', False]  # 查询统一账户穿仓借贷金额 (USER_DATA)
    portfolio_repay = ['https://api.binance.com/','POST', '/sapi/v1/portfolio/repay', False]  # 偿还统一账户穿仓负债


class SPOTPortfolioMargin(Client):
    endpoints = _SPOTPortfolioMarginEndpoints

    # 查询统一账户信息 (USER_DATA)
    def portfolio_account(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-86

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.portfolio_account, **to_local(locals()))

    # 统一账户资产质押率 (MARKET_DATA)
    def portfolio_collateralRate(self):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#market_data-9
        '''
        return self.send_request(*self.endpoints.portfolio_collateralRate, **to_local(locals()))

    # 查询统一账户穿仓借贷金额 (USER_DATA)
    def portfolio_pmLoan(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-87

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.portfolio_pmLoan, **to_local(locals()))

    # 偿还统一账户穿仓负债
    def portfolio_repay(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#eb9fb28dd5

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.portfolio_repay, **to_local(locals()))
