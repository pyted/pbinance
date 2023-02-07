from paux.param import to_local
from pbinance.client import Client
from typing import Union


class _BlvtEndpoints():
    get_tokenInfo = ['https://api.binance.com/','GET', '/sapi/v1/blvt/tokenInfo', False]  # 杠杆代币信息 (MARKET_DATA)
    set_subscribe = ['https://api.binance.com/','POST', '/sapi/v1/blvt/subscribe', True]  # 申购代币 (USER_DATA)
    get_subscribe_record = ['https://api.binance.com/','GET', '/sapi/v1/blvt/subscribe/record', True]  # 查询申购记录 (USER_DATA)
    set_redeem = ['https://api.binance.com/','POST', '/sapi/v1/blvt/redeem', True]  # 赎回代币 (USER_DATA)
    get_redeem_record = ['https://api.binance.com/','GET', '/sapi/v1/blvt/redeem/record', True]  # 查询赎回记录 (USER_DATA)
    get_userLimit = ['https://api.binance.com/','GET', '/sapi/v1/blvt/userLimit', True]  # 查询用户每日申购赎回限额 (USER_DATA)


class Blvt(Client):
    endpoints = _BlvtEndpoints

    # 杠杆代币信息 (MARKET_DATA)
    def get_tokenInfo(self, tokenName: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#market_data-10

        Name     	Type	Mandatory	Description
        tokenName	str 	NO       	BTCDOWN, BTCUP
        '''
        return self.send_request(*self.endpoints.get_tokenInfo, **to_local(locals()))

    # 申购代币 (USER_DATA)
    def set_subscribe(self, tokenName: str = '', cost: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-88

        Name      	Type            	Mandatory	Description
        tokenName 	str             	YES      	BTCDOWN, BTCUP
        cost      	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_subscribe, **to_local(locals()))

    # 查询申购记录 (USER_DATA)
    def get_subscribe_record(self, tokenName: str = '', id: int = '', startTime: int = '', endTime: int = '',
                             limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-89

        Name      	Type	Mandatory	Description
        tokenName 	str 	NO       	BTCDOWN, BTCUP
        id        	int 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	默认 1000, 最大 1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_subscribe_record, **to_local(locals()))

    # 赎回代币 (USER_DATA)
    def set_redeem(self, tokenName: str = '', amount: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-90

        Name      	Type            	Mandatory	Description
        tokenName 	str             	YES      	BTCDOWN, BTCUP
        amount    	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_redeem, **to_local(locals()))

    # 查询赎回记录 (USER_DATA)
    def get_redeem_record(self, tokenName: str = '', id: int = '', startTime: int = '', endTime: int = '',
                          limit: int = '',
                          recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-91

        Name      	Type	Mandatory	Description
        tokenName 	str 	NO       	BTCDOWN, BTCUP
        id        	int 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	默认 1000, 最大 1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_redeem_record, **to_local(locals()))

    # 查询用户每日申购赎回限额 (USER_DATA)
    def get_userLimit(self, tokenName: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-92

        Name      	Type	Mandatory	Description
        tokenName 	str 	NO       	BTCDOWN, BTCUP
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_userLimit, **to_local(locals()))
