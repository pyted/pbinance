from paux.param import to_local
from pbinance.client import Client
from typing import Union

# staking接口
class _StakingEndpoints():
    get_productList = ['https://api.binance.com/','GET', '/sapi/v1/staking/productList', True]  # 查询Staking产品列表(USER_DATA)
    set_purchase = ['https://api.binance.com/','POST', '/sapi/v1/staking/purchase', True]  # 申购锁仓产品(USER_DATA)
    set_redeem = ['https://api.binance.com/','POST', '/sapi/v1/staking/redeem', True]  # 赎回锁仓产品(USER_DATA)
    get_position = ['https://api.binance.com/','GET', '/sapi/v1/staking/position', True]  # 查看个人持仓(USER_DATA)
    get_stakingRecord = ['https://api.binance.com/','GET', '/sapi/v1/staking/stakingRecord', True]  # 查看Staking历史记录(USER_DATA)
    set_setAutoStaking = ['https://api.binance.com/','POST', '/sapi/v1/staking/setAutoStaking', True]  # 设置自动续期(USER_DATA)
    get_personalLeftQuota = ['https://api.binance.com/','GET', '/sapi/v1/staking/personalLeftQuota', True]  # 查询Staking个人剩余额度(USER_DATA)A


class Staking(Client):
    endpoints = _StakingEndpoints

    # 查询Staking产品列表(USER_DATA)
    def get_productList(self, product: str = '', asset: str = '', current: int = '', size: int = '',
                        recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#staking-user_data

        Name      	Type	Mandatory	Description
        product   	str 	YES      	"STAKING" 是Staking, "F_DEFI" 是DeFi活期挖矿, "L_DEFI" 是DeFi定期挖矿
        asset     	str 	NO
        current   	int 	NO       	当前查询页。 开始值 1，默认:1
        size      	int 	NO       	默认：10，最大：100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_productList, **to_local(locals()))

    # 申购锁仓产品(USER_DATA)
    def set_purchase(self, product: str = '', productId: str = '', amount: Union[float, int] = '', renewable: str = '',
                     recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-60

        Name      	Type            	Mandatory	Description
        product   	str             	YES      	"STAKING" 是Staking, "F_DEFI" 是DeFi活期挖矿, "L_DEFI" 是DeFi定期挖矿
        productId 	str             	YES
        amount    	Union[float,int]	YES
        renewable 	str             	NO       	true或者false，默认为false。仅在产品为 "STAKING" 或 "L_DEFI"时生效
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_purchase, **to_local(locals()))

    # 赎回锁仓产品(USER_DATA)
    def set_redeem(self, product: str = '', positionId: str = '', productId: str = '', amount: Union[float, int] = '',
                   recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-61

        Name      	Type            	Mandatory	Description
        product   	str             	YES      	"STAKING" 是Staking, "F_DEFI" 是DeFi活期挖矿, "L_DEFI" 是DeFi定期挖矿
        positionId	str             	NO       	"1234", 当产品为"STAKING" 或 "L_DEFI"时为必填项
        productId 	str             	YES
        amount    	Union[float,int]	NO       	当产品为"F_DEFI" 时为必填项
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_redeem, **to_local(locals()))

    # 查看个人持仓(USER_DATA)
    def get_position(self, product: str = '', productId: str = '', asset: str = '', current: int = '', size: int = '',
                     recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-62

        Name      	Type	Mandatory	Description
        product   	str 	YES      	"STAKING" 是Staking, "F_DEFI" 是DeFi活期挖矿, "L_DEFI" 是DeFi定期挖矿
        productId 	str 	NO
        asset     	str 	NO
        current   	int 	NO       	当前查询页。 开始值 1， 默认:1
        size      	int 	NO       	默认：10，最大：100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_position, **to_local(locals()))

    # 查看Staking历史记录(USER_DATA)
    def get_stakingRecord(self, product: str = '', txnType: str = '', asset: str = '', startTime: int = '',
                          endTime: int = '', current: int = '', size: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#staking-user_data-2

        Name      	Type	Mandatory	Description
        product   	str 	YES      	"STAKING" 是Staking, "F_DEFI" 是DeFi活期挖矿, "L_DEFI" 是DeFi定期挖矿
        txnType   	str 	YES      	申购："SUBSCRIPTION", 赎回："REDEMPTION", 利息："INTEREST"
        asset     	str 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        current   	int 	NO       	当前查询页。 开始值 1, 默认:1
        size      	int 	NO       	默认：10，最大：100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_stakingRecord, **to_local(locals()))

    # 设置自动续期(USER_DATA)
    def set_setAutoStaking(self, product: str = '', positionId: str = '', renewable: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-63

        Name      	Type	Mandatory	Description
        product   	str 	YES      	"STAKING" 是Staking, "L_DEFI" 是DeFi定期挖矿
        positionId	str 	YES
        renewable 	str 	YES      	true 或者 false
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_setAutoStaking, **to_local(locals()))

    def get_personalLeftQuota(self, product: str = '', productId: str = '', recvWindow: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#staking-user_data-3

        Name      	Type	Mandatory	Description
        product   	str 	YES      	"STAKING" 是Staking, "F_DEFI" 是DeFi活期挖矿, "L_DEFI" 是DeFi定期挖矿
        productId	str 	YES
        recvWindow 	str 	YES
        '''
        return self.send_request(*self.endpoints.get_personalLeftQuota, **to_local(locals()))
