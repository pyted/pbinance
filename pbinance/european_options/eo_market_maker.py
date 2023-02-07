from paux.param import to_local
from pbinance.client import Client
from typing import Union


# 市商
class _EOMarketMakerEndpoints():
    get_marginAccount = ['https://eapi.binance.com/','GET', '/eapi/v1/marginAccount', True]  # 保证金账户信息
    set_mmpSet = ['https://eapi.binance.com/','POST', '/eapi/v1/mmpSet', True]  # 设置MMP规则
    get_mmpSet = ['https://eapi.binance.com/','GET', '/eapi/v1/mmpSet', True]  # 获取MMP规则
    set_mmpReset = ['https://eapi.binance.com/','POST', '/eapi/v1/mmpReset', True]  # 重置MMP状态
    set_countdownCancelAll = ['https://eapi.binance.com/','POST', '/eapi/v1/countdownCancelAll', True]  # 设置倒计时取消所有订单配置 (TRADE)
    get_countdownCancelAll = ['https://eapi.binance.com/','GET', '/eapi/v1/countdownCancelAll', True]  # 获得倒计时自动取消所有订单配置 (TRADE)
    set_countdownCancelAllHeartBeat = ['https://eapi.binance.com/','POST', '/eapi/v1/countdownCancelAllHeartBeat', True]  #重置倒计时取消所有订单心跳 (TRADE)


class EOMarketMaker(Client):
    endpoints = _EOMarketMakerEndpoints

    # 保证金账户信息
    def get_marginAccount(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#f5972c1906

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_marginAccount, **to_local(locals()))

    # 设置MMP规则
    def set_mmpSet(self, underlying: str = '', windowTimeInMilliseconds: int = '', frozenTimeInMilliseconds: int = '',
                   qtyLimit: Union[float, int] = '', deltaLimit: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#mmp

        Name                    	Type            	Mandatory	Description
        underlying              	str             	YES      	标的资产如BTCUSDT
        windowTimeInMilliseconds	int             	YES      	MMP监控时间窗口（毫秒），在(0,5000]之间
        frozenTimeInMilliseconds	int             	NO       	MMP冻结时间（毫秒），设置为0后代表账号为冻结状态，需要手动重置
        qtyLimit                	Union[float,int]	NO       	数量限制
        deltaLimit              	Union[float,int]	NO       	净delta限制
        recvWindow              	int             	NO
        '''
        return self.send_request(*self.endpoints.set_mmpSet, **to_local(locals()))

    # 获取MMP规则
    def get_mmpSet(self, underlying: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#mmp-2

        Name      	Type	Mandatory	Description
        underlying	str 	YES      	标的资产如BTCUSDT
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_mmpSet, **to_local(locals()))

    # 重置MMP状态
    def set_mmpReset(self, underlying: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#mmp-3

        Name      	Type	Mandatory	Description
        underlying	str 	YES      	标的资产如BTCUSDT
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_mmpReset, **to_local(locals()))

    # 设置倒计时取消所有订单配置 (TRADE)
    def set_countdownCancelAll(self, underlying: str = '', countdownTime: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#trade-9

        Name         	Type	Mandatory	Description
        underlying   	str 	YES      	期权标的资产， 如 BTCUSDT
        countdownTime	int 	YES      	以毫秒计量倒计时长 (1000代表1秒)。 设为0时关闭倒计时。最小设为5000（负值无效）
        recvWindow   	int 	NO
        '''
        return self.send_request(*self.endpoints.set_countdownCancelAll, **to_local(locals()))

    # 获得倒计时自动取消所有订单配置 (TRADE)
    def get_countdownCancelAll(self, underlying: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#trade-10

        Name      	Type	Mandatory	Description
        underlying	str 	YES      	期权标的资产， 如BTCUSDT
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_countdownCancelAll, **to_local(locals()))

    # 重置倒计时取消所有订单心跳 (TRADE)
    def set_countdownCancelAllHeartBeat(self, underlyings: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/voptions/cn/#trade-11

        Name       	Type	Mandatory	Description
        underlyings	str 	YES      	期权标的资产， 如BTCUSDT
        recvWindow 	int 	NO
        '''
        return self.send_request(*self.endpoints.set_countdownCancelAllHeartBeat, **to_local(locals()))
