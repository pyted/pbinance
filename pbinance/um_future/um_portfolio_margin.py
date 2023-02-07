from paux.param import to_local
from pbinance.client import Client
from typing import Union


# 统一账户
class _UMPortfolioMarginEndpoints():
    get_pmExchangeInfo = ['https://fapi.binance.com/', 'GET', '/fapi/v1/pmExchangeInfo', False]  # 获取统一账户交易规则
    get_pmAccountInfo = ['https://fapi.binance.com/', 'GET', '/fapi/v1/pmAccountInfo', False]  # 查询统一账户账户信息 (USER_DATA)


class UMPortfolioMargin(Client):
    endpoints = _UMPortfolioMarginEndpoints

    # 获取统一账户交易规则
    def get_pmExchangeInfo(self, symbol: str = ''):
        '''
        https://binance-docs.github.io/apidocs/futures/cn/#72815f42fe

        Name  	Type	Mandatory	Description
        symbol	str 	NO       	交易对
        '''
        return self.send_request(*self.endpoints.get_pmExchangeInfo, **to_local(locals()))

    # 查询统一账户账户信息 (USER_DATA)
    def get_pmAccountInfo(self, asset: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/futures/cn/#user_data-13

        Name      	Type	Mandatory	Description
        asset     	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_pmAccountInfo, **to_local(locals()))
