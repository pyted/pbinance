from finance_utils.component.local import to_local
from pbinance.client import Client


# 法币
class _FiatEndpoints():
    get_orders = ['https://api.binance.com/','GET', '/sapi/v1/fiat/orders', True]  # 获取法币充值/提现历史记录 (USER_DATA)
    get_payments = ['https://api.binance.com/','GET', '/sapi/v1/fiat/payments', True]  # 获取法币支付历史记录 (USER_DATA)


class Fiat(Client):
    endpoints = _FiatEndpoints

    # 获取法币充值/提现历史记录 (USER_DATA)
    def get_orders(self, transactionType: str = '', beginTime: int = '', endTime: int = '', page: int = '',
                   rows: int = '',
                   recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-102

        Name           	Type	Mandatory	Description
        transactionType	str 	YES      	0-deposit,1-withdraw
        beginTime      	int 	NO
        endTime        	int 	NO
        page           	int 	NO       	默认 1
        rows           	int 	NO       	默认 100, 最大 500
        recvWindow     	int 	NO
        '''
        return self.send_request(*self.endpoints.get_orders, **to_local(locals()))

    # 获取法币支付历史记录 (USER_DATA)
    def get_payments(self, transactionType: str = '', beginTime: int = '', endTime: int = '', page: int = '',
                     rows: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-103

        Name           	Type	Mandatory	Description
        transactionType	str 	YES      	0-buy,1-sell
        beginTime      	int 	NO
        endTime        	int 	NO
        page           	int 	NO       	默认 1
        rows           	int 	NO       	默认 100, 最大 500
        recvWindow     	int 	NO
        '''
        return self.send_request(*self.endpoints.get_payments, **to_local(locals()))
