from finance_utils.component.local import to_local
from pbinance.client import Client
from typing import Union


# 币安宝
class _SavingsEndpoints():
    get_daily_product_list = ['https://api.binance.com/','GET', '/sapi/v1/lending/daily/product/list', True]  # 获取活期产品列表 (USER_DATA)
    get_daily_userLeftQuota = ['https://api.binance.com/','GET', '/sapi/v1/lending/daily/userLeftQuota', True]  # 获取用户当日剩余活期可申购余额 (USER_DATA)
    set_daily_purchase = ['https://api.binance.com/','POST', '/sapi/v1/lending/daily/purchase', True]  # 申购活期产品 (USER_DATA)
    get_daily_userRedemptionQuota = ['https://api.binance.com/','GET', '/sapi/v1/lending/daily/userRedemptionQuota', True]  # 获取用户当日活期可赎回余额 (USER_DATA)
    set_daily_redeem = ['https://api.binance.com/','POST', '/sapi/v1/lending/daily/redeem', True]  # 赎回活期产品 (USER_DATA)
    get_daily_token_position = ['https://api.binance.com/','GET', '/sapi/v1/lending/daily/token/position', True]  # 用户活期产品持仓 (USER_DATA)
    get_project_list = ['https://api.binance.com/','GET', '/sapi/v1/lending/project/list', True]  # 查询定期/活动产品列表 (USER_DATA)
    set_customizedFixed_purchase = ['https://api.binance.com/','POST', '/sapi/v1/lending/customizedFixed/purchase', True]  # 申购定期/活动产品 (USER_DATA)
    get_project_position_list = ['https://api.binance.com/','GET', '/sapi/v1/lending/project/position/list', True]  # 用户定期/活动持仓 (USER_DATA)
    get_union_account = ['https://api.binance.com/','GET', '/sapi/v1/lending/union/account', True]  # 币安宝账户信息 (USER_DATA)
    get_union_purchaseRecord = ['https://api.binance.com/','GET', '/sapi/v1/lending/union/purchaseRecord', True]  # 获取申购记录 (USER_DATA)
    get_union_redemptionRecord = ['https://api.binance.com/','GET', '/sapi/v1/lending/union/redemptionRecord', True]  # 获取赎回记录 (USER_DATA)
    get_union_interestHistory = ['https://api.binance.com/','GET', '/sapi/v1/lending/union/interestHistory', True]  # 获取利息历史 (USER_DATA)
    set_positionChanged = ['https://api.binance.com/','POST', '/sapi/v1/lending/positionChanged', True]  # 定期/活动持仓转活期持仓 (USER_DATA)


class Savings(Client):
    endpoints = _SavingsEndpoints

    # 获取活期产品列表 (USER_DATA)
    def get_daily_product_list(self, status: str = '', featured: str = '', current: int = '', size: int = '',
                               recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-46

        Name      	Type	Mandatory	Description
        status    	str 	NO       	"ALL", "SUBSCRIBABLE", "UNSUBSCRIBABLE";  默认: "ALL"
        featured  	str 	NO       	"ALL", "TRUE";  默认: "ALL"
        current   	int 	NO       	当前页面. 默认: 1, 最小: 1
        size      	int 	NO       	默认: 50, 最大: 100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_daily_product_list, **to_local(locals()))

    # 获取用户当日剩余活期可申购余额 (USER_DATA)
    def get_daily_userLeftQuota(self, productId: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-47

        Name      	Type	Mandatory	Description
        productId 	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_daily_userLeftQuota, **to_local(locals()))

    # 申购活期产品 (USER_DATA)
    def set_daily_purchase(self, productId: str = '', amount: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-48

        Name      	Type            	Mandatory	Description
        productId 	str             	YES
        amount    	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_daily_purchase, **to_local(locals()))

    # 获取用户当日活期可赎回余额 (USER_DATA)
    def get_daily_userRedemptionQuota(self, productId: str = '', type: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-49

        Name      	Type	Mandatory	Description
        productId 	str 	YES
        type      	str 	YES      	"FAST", "NORMAL"
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_daily_userRedemptionQuota, **to_local(locals()))

    # 赎回活期产品 (USER_DATA)
    def set_daily_redeem(self, productId: str = '', amount: Union[float, int] = '', type: str = '',
                         recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-50

        Name      	Type            	Mandatory	Description
        productId 	str             	YES
        amount    	Union[float,int]	YES
        type      	str             	YES      	"FAST", "NORMAL"
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_daily_redeem, **to_local(locals()))

    # 用户活期产品持仓 (USER_DATA)
    def get_daily_token_position(self, asset: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-51

        Name      	Type	Mandatory	Description
        asset     	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_daily_token_position, **to_local(locals()))

    # 查询定期/活动产品列表 (USER_DATA)
    def get_project_list(self, asset: str = '', type: str = '', status: str = '', isSortAsc: bool = '',
                         sortBy: str = '',
                         current: int = '', size: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-52

        Name      	Type	Mandatory	Description
        asset     	str 	NO
        type      	str 	YES      	"CUSTOMIZED_FIXED"定期 , "ACTIVITY" 活动
        status    	str 	NO       	"ALL", "SUBSCRIBABLE", "UNSUBSCRIBABLE"; 默认 "ALL"
        isSortAsc 	bool	NO       	默认 "true"
        sortBy    	str 	NO       	"START_TIME", "LOT_SIZE", "INTEREST_RATE", "DURATION"; 默认 "START_TIME"
        current   	int 	NO       	分页页码. 默认:1
        size      	int 	NO       	单页显示条数，默认:10 最大:100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_project_list, **to_local(locals()))

    # 申购定期/活动产品 (USER_DATA)
    def set_customizedFixed_purchase(self, projectId: str = '', lot: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-53

        Name      	Type	Mandatory	Description
        projectId 	str 	YES
        lot       	int 	YES      	申购手数
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_customizedFixed_purchase, **to_local(locals()))

    # 用户定期/活动持仓 (USER_DATA)
    def get_project_position_list(self, asset: str = '', projectId: str = '', status: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-54

        Name      	Type	Mandatory	Description
        asset     	str 	NO
        projectId 	str 	NO
        status    	str 	NO       	"HOLDING", "REDEEMED"
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_project_position_list, **to_local(locals()))

    # 币安宝账户信息 (USER_DATA)
    def get_union_account(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-55

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_union_account, **to_local(locals()))

    # 获取申购记录 (USER_DATA)
    def get_union_purchaseRecord(self, lendingType: str = '', asset: str = '', startTime: int = '', endTime: int = '',
                                 current: int = '', size: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-56

        Name       	Type	Mandatory	Description
        lendingType	str 	YES      	"DAILY" 表示活期, "ACTIVITI" 表示活动, "CUSTOMIZED_FIXED" 表示定期
        asset      	str 	NO
        startTime  	int 	NO
        endTime    	int 	NO
        current    	int 	NO       	Currently querying page. Start from 1. Default:1
        size       	int 	NO       	Default:10, Max:100
        recvWindow 	int 	NO
        '''
        return self.send_request(*self.endpoints.get_union_purchaseRecord, **to_local(locals()))

    # 获取赎回记录 (USER_DATA)
    def get_union_redemptionRecord(self, lendingType: str = '', asset: str = '', startTime: int = '', endTime: int = '',
                                   current: int = '', size: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-57

        Name       	Type	Mandatory	Description
        lendingType	str 	YES      	"DAILY" 表示活期, "ACTIVITY" 表示活动, "CUSTOMIZED_FIXED" 表示定期
        asset      	str 	NO
        startTime  	int 	NO
        endTime    	int 	NO
        current    	int 	NO       	Currently querying page. Start from 1. Default:1
        size       	int 	NO       	Default:10, Max:100
        recvWindow 	int 	NO
        '''
        return self.send_request(*self.endpoints.get_union_redemptionRecord, **to_local(locals()))

    # 获取利息历史 (USER_DATA)
    def get_union_interestHistory(self, lendingType: str = '', asset: str = '', startTime: int = '', endTime: int = '',
                                  current: int = '', size: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-58

        Name       	Type	Mandatory	Description
        lendingType	str 	YES      	"DAILY" 表示活期, "ACTIVITY" 表示活动, "CUSTOMIZED_FIXED" 表示定期
        asset      	str 	NO
        startTime  	int 	NO
        endTime    	int 	NO
        current    	int 	NO       	Currently querying page. Start from 1. Default:1
        size       	int 	NO       	Default:10, Max:100
        recvWindow 	int 	NO
        '''
        return self.send_request(*self.endpoints.get_union_interestHistory, **to_local(locals()))

    # 定期/活动持仓转活期持仓 (USER_DATA)
    def set_positionChanged(self, projectId: str = '', lot: int = '', positionId: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-59

        Name      	Type	Mandatory	Description
        projectId 	str 	YES
        lot       	int 	YES
        positionId	int 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_positionChanged, **to_local(locals()))
