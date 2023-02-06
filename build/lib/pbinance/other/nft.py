from finance_utils.component.local import to_local
from pbinance.client import Client
from typing import Union


# NFT
class _NFTEndpoints():
    get_history_transactions = ['https://api.binance.com/', 'GET', '/sapi/v1/nft/history/transactions', True]  # 获取 NFT 资金流水记录 (USER_DATA)
    get_history_deposit = ['https://api.binance.com/', 'GET', '/sapi/v1/nft/history/deposit', True]  # 获取 NFT 充值记录 (USER_DATA)
    get_history_withdraw = ['https://api.binance.com/', 'GET', '/sapi/v1/nft/history/withdraw', True]  # 获取 NFT 提现记录 (USER_DATA)
    get_user_getAsset = ['https://api.binance.com/', 'GET', '/sapi/v1/nft/user/getAsset', True]  # 获取 NFT 资产 (USER_DATA)


class Nft(Client):
    endpoints = _NFTEndpoints

    # 获取 NFT 资金流水记录 (USER_DATA)
    def get_history_transactions(self, orderType: int = '', startTime: int = '', endTime: int = '', limit: int = '',
                                 page: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#nft-user_data

        Name      	Type	Mandatory	Description
        orderType 	int 	YES      	0:买单，1:卖单，2:版税收入，3:一级市场买单，4:mint 费用
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	默认 50, 最大 50
        page      	int 	NO       	默认 1
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_history_transactions, **to_local(locals()))

    # 获取 NFT 充值记录 (USER_DATA)
    def get_history_deposit(self, startTime: int = '', endTime: int = '', limit: int = '', page: int = '',
                            recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#nft-user_data-2

        Name      	Type	Mandatory	Description
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	默认 50, 最大 50
        page      	int 	NO       	默认 1
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_history_deposit, **to_local(locals()))

    # 获取 NFT 提现记录 (USER_DATA)
    def get_history_withdraw(self, startTime: int = '', endTime: int = '', limit: int = '', page: int = '',
                             recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#nft-user_data-3

        Name      	Type	Mandatory	Description
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	默认 50, 最大 50
        page      	int 	NO       	默认 1
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_history_withdraw, **to_local(locals()))

    # 获取 NFT 资产 (USER_DATA)
    def get_user_getAsset(self, limit: int = '', page: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#nft-user_data-4

        Name      	Type	Mandatory	Description
        limit     	int 	NO       	默认 50, 最大 50
        page      	int 	NO       	默认 1
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_user_getAsset, **to_local(locals()))
