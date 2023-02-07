from paux.param import to_local
from pbinance.client import Client


class _PayEndpoints():
    get_transactions = ['https://api.binance.com/','GET', '/sapi/v1/pay/transactions', True]  # 获取 Pay 交易历史记录 (USER_DATA)


class Pay(Client):
    endpoints = _PayEndpoints

    # 获取 Pay 交易历史记录 (USER_DATA)
    def get_transactions(self, startTime: int = '', endTime: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#pay-user_data

        Name      	Type	Mandatory	Description
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	默认 100, 最大 100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_transactions, **to_local(locals()))
