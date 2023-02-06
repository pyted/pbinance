from finance_utils.component.local import to_local
from pbinance.client import Client


class _C2CEndpoints():
    get_orderMatch_listUserOrderHistory = ['https://api.binance.com/','GET', '/sapi/v1/c2c/orderMatch/listUserOrderHistory', True]  # 获取 C2C 交易历史记录 (USER_DATA)


class C2c(Client):
    endpoints = _C2CEndpoints

    # 获取 C2C 交易历史记录 (USER_DATA)
    def get_orderMatch_listUserOrderHistory(self, tradeType: str = '', startTimestamp: int = '', endTimestamp: int = '',
                                            page: int = '', rows: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#c2c-user_data

        Name          	Type	Mandatory	Description
        tradeType     	str 	YES      	BUY, SEll
        startTimestamp	int 	NO
        endTimestamp  	int 	NO
        page          	int 	NO       	default 1
        rows          	int 	NO       	default 100, max 100
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_orderMatch_listUserOrderHistory, **to_local(locals()))
