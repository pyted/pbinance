from finance_utils.component.local import to_local
from pbinance.client import Client
from typing import Union


# 合约
class _FuturesEndpoints():
    set_transfer = ['https://api.binance.com/','POST', '/sapi/v1/futures/transfer', True]  # 合约资金划转 (USER_DATA)
    get_transfer = ['https://api.binance.com/','GET', '/sapi/v1/futures/transfer', True]  # 获取合约资金划转历史 (USER_DATA)
    get_loan_borrow_history = ['https://api.binance.com/','GET', '/sapi/v1/futures/loan/borrow/history', True]  # 混合保证金借款历史 (USER_DATA)
    get_loan_repay_history = ['https://api.binance.com/','GET', '/sapi/v1/futures/loan/repay/history', True]  # 混合保证金还款历史 (USER_DATA)
    get_loan_wallet = ['https://api.binance.com/','GET', '/sapi/v2/futures/loan/wallet', True]  # 混合保证金钱包V2 (USER_DATA)
    get_loan_adjustCollateral_history = ['https://api.binance.com/','GET', '/sapi/v1/futures/loan/adjustCollateral/history', True]  # 混合保证金调整质押率历史 (USER_DATA)
    get_loan_liquidationHistory = ['https://api.binance.com/','GET', '/sapi/v1/futures/loan/liquidationHistory', True]  # 混合保证金强平历史 (USER_DATA)
    get_loan_interestHistory = ['https://api.binance.com/','GET', '/sapi/v1/futures/loan/interestHistory', True]  # 混合保证金利息收取历史 (USER_DATA)


class Future(Client):
    endpoints = _FuturesEndpoints

    # 合约资金划转 (USER_DATA)
    def set_transfer(self, asset: str = '', amount: Union[float, int] = '', type: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-76

        Name      	Type            	Mandatory	Description
        asset     	str             	YES      	The asset being transferred, e.g., USDT
        amount    	Union[float,int]	YES      	The amount to be transferred
        type      	int             	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_transfer, **to_local(locals()))

    # 获取合约资金划转历史 (USER_DATA)
    def get_transfer(self, asset: str = '', startTime: int = '', endTime: int = '', current: int = '', size: int = '',
                     recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-77

        Name      	Type	Mandatory	Description
        asset     	str 	YES
        startTime 	int 	YES
        endTime   	int 	NO
        current   	int 	NO       	当前页面. 起始计数为1. 默认值1
        size      	int 	NO       	单页数据条目数，默认:10 最大:100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_transfer, **to_local(locals()))

    # 混合保证金借款历史 (USER_DATA)
    def get_loan_borrow_history(self, coin: str = '', startTime: int = '', endTime: int = '', limit: int = '',
                                recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-78

        Name      	Type	Mandatory	Description
        coin      	str 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	default 500, max 1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_loan_borrow_history, **to_local(locals()))

    # 混合保证金还款历史 (USER_DATA)
    def get_loan_repay_history(self, coin: str = '', startTime: int = '', endTime: int = '', limit: int = '',
                               recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-79

        Name      	Type	Mandatory	Description
        coin      	str 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	default 500, max 1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_loan_repay_history, **to_local(locals()))

    # 混合保证金钱包V2 (USER_DATA)
    def get_loan_wallet(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#v2-user_data

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_loan_wallet, **to_local(locals()))

    # 混合保证金调整质押率历史 (USER_DATA)
    def get_loan_adjustCollateral_history(self, loanCoin: str = '', collateralCoin: str = '', startTime: int = '',
                                          endTime: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-80

        Name          	Type	Mandatory	Description
        loanCoin      	str 	NO
        collateralCoin	str 	NO
        startTime     	int 	NO
        endTime       	int 	NO
        limit         	int 	NO       	default 500, max 1000
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_loan_adjustCollateral_history, **to_local(locals()))

    # 混合保证金强平历史 (USER_DATA)
    def get_loan_liquidationHistory(self, loanCoin: str = '', collateralCoin: str = '', startTime: int = '',
                                    endTime: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-81

        Name          	Type	Mandatory	Description
        loanCoin      	str 	NO
        collateralCoin	str 	NO
        startTime     	int 	NO
        endTime       	int 	NO
        limit         	int 	NO       	default 500, max 1000
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_loan_liquidationHistory, **to_local(locals()))

    # 混合保证金利息收取历史 (USER_DATA)
    def get_loan_interestHistory(self, collateralCoin: str = '', startTime: int = '', endTime: int = '',
                                 current: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-82

        Name          	Type	Mandatory	Description
        collateralCoin	str 	NO
        startTime     	int 	NO
        endTime       	int 	NO
        current       	int 	NO       	当前查询页。 开始值 1。 默认:1
        limit         	int 	NO       	默认 500，最大 1000
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_loan_interestHistory, **to_local(locals()))
