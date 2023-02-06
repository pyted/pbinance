from finance_utils.component.local import to_local
from pbinance.client import Client
from typing import Union


# 统一账户
class _CMPortfolioMarginEndpoints():
    get_pmExchangeInfo = ['https://dapi.binance.com/','GET', '/dapi/v1/pmExchangeInfo', False]  # 获取统一账户交易规则
    get_pmAccountInfo = ['https://dapi.binance.com/','GET', '/dapi/v1/pmAccountInfo', False]  # 查询统一账户账户信息 (USER_DATA)


class CMPortfolioMargin(Client):
    endpoints = _CMPortfolioMarginEndpoints

    # 获取统一账户交易规则
    def get_pmExchangeInfo(self, symbol: str = '', pair: str = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#72815f42fe

        Name  	Type	Mandatory	Description
        symbol	str 	NO       	交易对
        pair  	str 	NO       	标的交易对
        '''
        return self.send_request(*self.endpoints.get_pmExchangeInfo, **to_local(locals()))

    # 查询统一账户账户信息 (USER_DATA)
    def get_pmAccountInfo(self, asset: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-15

        Name      	Type	Mandatory	Description
        asset     	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_pmAccountInfo, **to_local(locals()))
