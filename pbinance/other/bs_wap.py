from paux.param import to_local
from pbinance.client import Client
from typing import Union


class _BSwapEndpoints():
    get_pools = ['https://api.binance.com/','GET', '/sapi/v1/bswap/pools', False]  # 获取所有流动资金池 (MARKET_DATA)
    get_liquidity = ['https://api.binance.com/','GET', '/sapi/v1/bswap/liquidity', True]  # 获取流动资金池具体信息 (USER_DATA)
    set_liquidityAdd = ['https://api.binance.com/','POST', '/sapi/v1/bswap/liquidityAdd', True]  # 添加流动性 (TRADE)
    set_liquidityRemove = ['https://api.binance.com/','POST', '/sapi/v1/bswap/liquidityRemove', True]  # 移除流动性 (TRADE)
    get_liquidityOps = ['https://api.binance.com/','GET', '/sapi/v1/bswap/liquidityOps', True]  # 获取流动性操作记录 (USER_DATA)
    get_quote = ['https://api.binance.com/','GET', '/sapi/v1/bswap/quote', True]  # 获取报价 (USER_DATA)
    set_swap = ['https://api.binance.com/','POST', '/sapi/v1/bswap/swap', True]  # 交易 (TRADE)
    get_swap = ['https://api.binance.com/','GET', '/sapi/v1/bswap/swap', True]  # 获取交易记录 (USER_DATA)
    get_poolConfigure = ['https://api.binance.com/','GET', '/sapi/v1/bswap/poolConfigure', True]  # 获取币对池的配置信息 (USER_DATA)
    get_addLiquidityPreview = ['https://api.binance.com/','GET', '/sapi/v1/bswap/addLiquidityPreview', True]  # 添加流动性的试算 (USER_DATA)
    get_removeLiquidityPreview = ['https://api.binance.com/','GET', '/sapi/v1/bswap/removeLiquidityPreview', True]  # 移除流动性的试算 (USER_DATA)
    get_unclaimedRewards = ['https://api.binance.com/','GET', '/sapi/v1/bswap/unclaimedRewards', True]  # 查询未领取的奖励数量 (USER_DATA)
    set_claimRewards = ['https://api.binance.com/','POST', '/sapi/v1/bswap/claimRewards', True]  # 领取奖励 (TRADE)
    set_claimedHistory = ['https://api.binance.com/','GET', '/sapi/v1/bswap/claimedHistory', True]  # 获取已领取奖励记录 (USER_DATA)


class Bswap(Client):
    endpoints = _BSwapEndpoints

    # 获取所有流动资金池 (MARKET_DATA)
    def get_pools(self):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#market_data-11
        '''
        return self.send_request(*self.endpoints.get_pools, **to_local(locals()))

    # 获取流动资金池具体信息 (USER_DATA)
    def get_liquidity(self, poolId: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-93

        Name      	Type	Mandatory	Description
        poolId    	int 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_liquidity, **to_local(locals()))

    # 添加流动性 (TRADE)
    def set_liquidityAdd(self, poolId: int = '', type: str = '', asset: str = '', quantity: Union[float, int] = '',
                         recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-15

        Name      	Type            	Mandatory	Description
        poolId    	int             	YES
        type      	str             	NO       	"SINGLE" 为单币添加资产; "COMBINATION" 为双币添加资产。 默认 "SINGLE"
        asset     	str             	YES
        quantity  	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_liquidityAdd, **to_local(locals()))

    # 移除流动性 (TRADE)
    def set_liquidityRemove(self, poolId: int = '', type: str = '', asset: list = '',
                            shareAmount: Union[float, int] = '',
                            recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-16

        Name       	Type            	Mandatory	Description
        poolId     	int             	YES
        type       	str             	YES
        asset      	list            	NO
        shareAmount	Union[float,int]	YES
        recvWindow 	int             	NO
        '''
        return self.send_request(*self.endpoints.set_liquidityRemove, **to_local(locals()))

    # 获取流动性操作记录 (USER_DATA)
    def get_liquidityOps(self, operationId: int = '', poolId: int = '', operation: str = '', startTime: int = '',
                         endTime: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-94

        Name       	Type	Mandatory	Description
        operationId	int 	NO
        poolId     	int 	NO
        operation  	str 	NO
        startTime  	int 	NO
        endTime    	int 	NO
        limit      	int 	NO       	默认 3, 最大 100
        recvWindow 	int 	NO
        '''
        return self.send_request(*self.endpoints.get_liquidityOps, **to_local(locals()))

    # 获取报价 (USER_DATA)
    def get_quote(self, quoteAsset: str = '', baseAsset: str = '', quoteQty: Union[float, int] = '',
                  recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-95

        Name      	Type            	Mandatory	Description
        quoteAsset	str             	YES
        baseAsset 	str             	YES
        quoteQty  	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.get_quote, **to_local(locals()))

    # 交易 (TRADE)
    def set_swap(self, quoteAsset: str = '', baseAsset: str = '', quoteQty: Union[float, int] = '',
                 recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-17

        Name      	Type            	Mandatory	Description
        quoteAsset	str             	YES
        baseAsset 	str             	YES
        quoteQty  	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_swap, **to_local(locals()))

    # 获取交易记录 (USER_DATA)
    def get_swap(self, swapId: int = '', startTime: int = '', endTime: int = '', status: int = '', quoteAsset: str = '',
                 baseAsset: str = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-96

        Name      	Type	Mandatory	Description
        swapId    	int 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        status    	int 	NO       	0: 交易中, 1: 交易成功, 2: 交易失败
        quoteAsset	str 	NO
        baseAsset 	str 	NO
        limit     	int 	NO       	默认 3, 最大 100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_swap, **to_local(locals()))

    # 获取币对池的配置信息 (USER_DATA)
    def get_poolConfigure(self, poolId: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-97

        Name      	Type	Mandatory	Description
        poolId    	int 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_poolConfigure, **to_local(locals()))

    # 添加流动性的试算 (USER_DATA)
    def get_addLiquidityPreview(self, poolId: int = '', type: str = '', quoteAsset: str = '',
                                quoteQty: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-98

        Name      	Type            	Mandatory	Description
        poolId    	int             	YES
        type      	str             	YES      	类型为"SINGLE"意思为单币添加;类型为"COMBINATION"意思为双币添加
        quoteAsset	str             	YES
        quoteQty  	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.get_addLiquidityPreview, **to_local(locals()))

    # 移除流动性的试算 (USER_DATA)
    def get_removeLiquidityPreview(self, poolId: int = '', type: str = '', quoteAsset: str = '',
                                   shareAmount: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-99

        Name       	Type            	Mandatory	Description
        poolId     	int             	YES
        type       	str             	YES      	类型为"SINGLE"意思为移除获得单币；类型为"COMBINATION"意思为移除获得双币
        quoteAsset 	str             	YES
        shareAmount	Union[float,int]	YES
        recvWindow 	int             	NO
        '''
        return self.send_request(*self.endpoints.get_removeLiquidityPreview, **to_local(locals()))

    # 查询未领取的奖励数量  (USER_DATA)
    def get_unclaimedRewards(self, type: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-100

        Name      	Type	Mandatory	Description
        type      	int 	NO       	0:交易挖矿奖励，1:流动性挖矿奖励，默认为0
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_unclaimedRewards, **to_local(locals()))

    # 领取奖励 (TRADE)
    def set_claimRewards(self, type: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-18

        Name      	Type	Mandatory	Description
        type      	int 	NO       	0:交易挖矿奖励，1:流动性挖矿奖励，默认为0
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_claimRewards, **to_local(locals()))

    # 获取已领取奖励记录 (USER_DATA)
    def set_claimedHistory(self, poolId: int = '', assetRewards: str = '', type: int = '', startTime: int = '',
                           endTime: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-101

        Name        	Type	Mandatory	Description
        poolId      	int 	NO
        assetRewards	str 	NO
        type        	int 	NO       	0:交易挖矿奖励，1:流动性挖矿奖励，默认为0
        startTime   	int 	NO
        endTime     	int 	NO
        limit       	int 	NO       	Default 3, max 100
        recvWindow  	int 	NO
        '''
        return self.send_request(*self.endpoints.set_claimedHistory, **to_local(locals()))
