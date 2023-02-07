from paux.param import to_local
from pbinance.client import Client
from typing import Union


# 返佣
class _RebateEndpoints():
    get_taxQuery = ['https://api.binance.com/', 'GET', '/sapi/v1/rebate/taxQuery', True]  # 获取现货返佣历史记录 (USER_DATA)


class Rebate(Client):
    endpoints = _RebateEndpoints

    # 获取现货返佣历史记录 (USER_DATA)
    def get_taxQuery(self, startTime: int = '', endTime: int = '', page: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-117

        Name      	Type	Mandatory	Description
        startTime 	int 	NO
        endTime   	int 	NO
        page      	int 	NO       	默认 1
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_taxQuery, **to_local(locals()))
