from finance_utils.component.local import to_local
from pbinance.client import Client
from typing import Union


class _VIPLoansEndpoints():
    get_ongoing_orders = ['https://api.binance.com/','GET', '/sapi/v1/loan/vip/ongoing/orders', False]  # 查询VIP借币借款中订单 (USER_DATA)
    set_repay = ['https://api.binance.com/','POST', '/sapi/v1/loan/vip/repay', False]  # VIP借币还款 (TRADE)
    get_repay_history = ['https://api.binance.com/','GET', '/sapi/v1/loan/vip/repay/history', False]  # 查询VIP借币还款记录历史 (USER_DATA)


class VIPLoans(Client):
    endpoints = _VIPLoansEndpoints

    # 查询VIP借币借款中订单 (USER_DATA)
    def get_ongoing_orders(self, orderId: int = '', collateralAccountId: int = '', loanCoin: str = '',
                           collateralCoin: str = '', current: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#vip-user_data

        Name               	Type	Mandatory	Description
        orderId            	int 	NO
        collateralAccountId	int 	NO
        loanCoin           	str 	NO
        collateralCoin     	str 	NO
        current            	int 	NO       	当前查询页数，从1开始。默认值：1，最大：1000
        limit              	int 	NO       	默认值：10，最大：100
        recvWindow         	int 	NO
        '''
        return self.send_request(*self.endpoints.get_ongoing_orders, **to_local(locals()))

    # VIP借币还款 (TRADE)
    def set_repay(self, orderId: int = '', amount: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#vip-trade

        Name      	Type            	Mandatory	Description
        orderId   	int             	YES
        amount    	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_repay, **to_local(locals()))

    # 查询VIP借币还款记录历史 (USER_DATA)
    def get_repay_history(self, orderId: int = '', loanCoin: str = '', startTime: int = '', endTime: int = '',
                          current: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#vip-user_data-2

        Name      	Type	Mandatory	Description
        orderId   	int 	NO
        loanCoin  	str 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        current   	int 	NO       	当前查询页数，从1开始。默认值：1，最大：1000
        limit     	int 	NO       	默认值：10，最大：100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_repay_history, **to_local(locals()))
