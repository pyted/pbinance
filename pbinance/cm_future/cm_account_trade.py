from paux.param import to_local
from pbinance.client import Client
from typing import Union


# 账户与交易
class _CMAccountTradeEndpoints():
    set_positionSide_dual = ['https://dapi.binance.com/','POST', '/dapi/v1/positionSide/dual', True]  # 更改持仓模式(TRADE)
    get_positionSide_dual = ['https://dapi.binance.com/','GET', '/dapi/v1/positionSide/dual', True]  # 查询持仓模式(USER_DATA)
    set_order = ['https://dapi.binance.com/','POST', '/dapi/v1/order', True]  # 下单 (TRADE)
    set_order_test = ['https://dapi.binance.com/','POST', '/dapi/v1/order/test', True]  # 测试下单接口 (TRADE)
    alter_order = ['https://dapi.binance.com/','PUT', '/dapi/v1/order', True]  # 修改订单 (TRADE)
    set_batchOrders = ['https://dapi.binance.com/','POST', '/dapi/v1/batchOrders', True]  # 批量下单 (TRADE)
    alter_batchOrders = ['https://dapi.binance.com/','PUT', '/dapi/v1/batchOrders', True]  # 批量修改订单 (TRADE)
    get_orderAmendment = ['https://dapi.binance.com/','GET', '/dapi/v1/orderAmendment', True]  # 查询订单修改历史 (USER_DATA)
    get_order = ['https://dapi.binance.com/','GET', '/dapi/v1/order', True]  # 查询订单 (USER_DATA)
    cancel_order = ['https://dapi.binance.com/','DELETE', '/dapi/v1/order', True]  # 撤销订单 (TRADE)
    cancel_allOpenOrders = ['https://dapi.binance.com/','DELETE', '/dapi/v1/allOpenOrders', True]  # 撤销全部订单 (TRADE)
    cancel_batchOrders = ['https://dapi.binance.com/','DELETE', '/dapi/v1/batchOrders', True]  # 批量撤销订单 (TRADE)
    set_countdownCancelAll = ['https://dapi.binance.com/','POST', '/dapi/v1/countdownCancelAll', True]  # 倒计时撤销所有订单 (TRADE)
    get_openOrder = ['https://dapi.binance.com/','GET', '/dapi/v1/openOrder', True]  # 查询当前挂单 (USER_DATA)
    get_openOrders = ['https://dapi.binance.com/','GET', '/dapi/v1/openOrders', True]  # 查看当前全部挂单 (USER_DATA)
    get_allOrders = ['https://dapi.binance.com/','GET', '/dapi/v1/allOrders', True]  # 查询所有订单(包括历史订单) (USER_DATA)
    get_balance = ['https://dapi.binance.com/','GET', '/dapi/v1/balance', True]  # 账户余额 (USER_DATA)
    get_account = ['https://dapi.binance.com/','GET', '/dapi/v1/account', True]  # 账户信息 (USER_DATA)
    set_leverage = ['https://dapi.binance.com/','POST', '/dapi/v1/leverage', True]  # 调整开仓杠杆 (TRADE)
    set_marginType = ['https://dapi.binance.com/','POST', '/dapi/v1/marginType', True]  # 变换逐全仓模式 (TRADE)
    set_positionMargin = ['https://dapi.binance.com/','POST', '/dapi/v1/positionMargin', True]  # 调整逐仓保证金 (TRADE)
    get_positionMargin_history = ['https://dapi.binance.com/','GET', '/dapi/v1/positionMargin/history', True]  # 逐仓保证金变动历史 (TRADE)
    get_positionRisk = ['https://dapi.binance.com/','GET', '/dapi/v1/positionRisk', True]  # 用户持仓风险
    get_userTrades = ['https://dapi.binance.com/','GET', '/dapi/v1/userTrades', True]  # 账户成交历史 (USER_DATA)
    get_income = ['https://dapi.binance.com/','GET', '/dapi/v1/income', True]  # 获取账户损益资金流水(USER_DATA)
    get_leverageBracket = ['https://dapi.binance.com/','GET', '/dapi/v2/leverageBracket', False]  # 交易对杠杆分层标准 (USER_DATA)
    get_forceOrders = ['https://dapi.binance.com/','GET', '/dapi/v1/forceOrders', False]  # 用户强平单历史 (USER_DATA)
    get_adlQuantile = ['https://dapi.binance.com/','GET', '/dapi/v1/adlQuantile', False]  # 持仓ADL队列估算 (USER_DATA)
    get_commissionRate = ['https://dapi.binance.com/','GET', '/dapi/v1/commissionRate', True]  # 用户手续费率 (USER_DATA)


class CMAccountTrade(Client):
    endpoints = _CMAccountTradeEndpoints

    # 更改持仓模式(TRADE)
    def set_positionSide_dual(self, dualSidePosition: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade

        Name            	Type	Mandatory	Description
        dualSidePosition	str 	YES      	"true": 双向持仓模式；"false": 单向持仓模式
        recvWindow      	int 	NO
        '''
        return self.send_request(*self.endpoints.set_positionSide_dual, **to_local(locals()))

    # 查询持仓模式(USER_DATA)
    def get_positionSide_dual(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_positionSide_dual, **to_local(locals()))

    # 下单 (TRADE)
    def set_order(self, symbol: str = '', side: str = '', positionSide: str = '', type: str = '', reduceOnly: str = '',
                  quantity: Union[float, int] = '', price: Union[float, int] = '', newClientOrderId: str = '',
                  stopPrice: Union[float, int] = '', closePosition: str = '', activationPrice: Union[float, int] = '',
                  callbackRate: Union[float, int] = '', timeInForce: str = '', workingType: str = '',
                  priceProtect: str = '', newOrderRespType: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-2

        Name            	Type            	Mandatory	Description
        symbol          	str             	YES      	交易对
        side            	str             	YES
        positionSide    	str             	NO
        type            	str             	YES
        reduceOnly      	str             	NO
        quantity        	Union[float,int]	NO
        price           	Union[float,int]	NO       	委托价格
        newClientOrderId	str             	NO
        stopPrice       	Union[float,int]	NO
        closePosition   	str             	NO
        activationPrice 	Union[float,int]	NO
        callbackRate    	Union[float,int]	NO
        timeInForce     	str             	NO       	有效方法
        workingType     	str             	NO
        priceProtect    	str             	NO
        newOrderRespType	str             	NO       	"ACK", "RESULT", 默认 "ACK"
        recvWindow      	int             	NO
        '''
        return self.send_request(*self.endpoints.set_order, **to_local(locals()))

    # 测试下单接口 (TRADE)
    def set_order_test(self, symbol: str = '', side: str = '', positionSide: str = '', type: str = '', reduceOnly: str = '',
                  quantity: Union[float, int] = '', price: Union[float, int] = '', newClientOrderId: str = '',
                  stopPrice: Union[float, int] = '', closePosition: str = '', activationPrice: Union[float, int] = '',
                  callbackRate: Union[float, int] = '', timeInForce: str = '', workingType: str = '',
                  priceProtect: str = '', newOrderRespType: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-3

        Name            	Type            	Mandatory	Description
        symbol          	str             	YES      	交易对
        side            	str             	YES
        positionSide    	str             	NO
        type            	str             	YES
        reduceOnly      	str             	NO
        quantity        	Union[float,int]	NO
        price           	Union[float,int]	NO       	委托价格
        newClientOrderId	str             	NO
        stopPrice       	Union[float,int]	NO
        closePosition   	str             	NO
        activationPrice 	Union[float,int]	NO
        callbackRate    	Union[float,int]	NO
        timeInForce     	str             	NO       	有效方法
        workingType     	str             	NO
        priceProtect    	str             	NO
        newOrderRespType	str             	NO       	"ACK", "RESULT", 默认 "ACK"
        recvWindow      	int             	NO
        '''
        return self.send_request(*self.endpoints.set_order_test, **to_local(locals()))

    # 修改订单 (TRADE)
    def alter_order(self, orderId: int = '', origClientOrderId: str = '', symbol: str = '', side: str = '',
                    quantity: Union[float, int] = '', price: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-4

        Name             	Type            	Mandatory	Description
        orderId          	int             	NO       	系统订单号
        origClientOrderId	str             	NO       	用户自定义的订单号
        symbol           	str             	YES      	交易对
        side             	str             	YES
        quantity         	Union[float,int]	NO
        price            	Union[float,int]	NO       	委托价格
        recvWindow       	int             	NO
        '''
        return self.send_request(*self.endpoints.alter_order, **to_local(locals()))

    # 批量下单 (TRADE)
    def set_batchOrders(self, batchOrders: list = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-5

        Name            	Type            	Mandatory	Description
        batchOrders     	list            	YES      	订单列表,最多支持5个订单
        recvWindow      	int             	NO
        '''
        return self.send_request(*self.endpoints.set_batchOrders, **to_local(locals()))

    # 批量修改订单 (TRADE)
    def alter_batchOrders(self, batchOrders: list = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-6

        Name             	Type            	Mandatory	Description
        batchOrders      	list            	YES      	订单列表,最多支持5个订单
        recvWindow       	int             	NO
        '''
        return self.send_request(*self.endpoints.alter_batchOrders, **to_local(locals()))

    # 查询订单修改历史 (USER_DATA)
    def get_orderAmendment(self, symbol: str = '', orderId: int = '', origClientOrderId: str = '', startTime: int = '',
                           endTime: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-2

        Name             	Type	Mandatory	Description
        symbol           	str 	YES      	交易对
        orderId          	int 	NO       	系统订单号
        origClientOrderId	str 	NO       	用户自定义的订单号
        startTime        	int 	NO       	起始时间
        endTime          	int 	NO       	结束时间
        limit            	int 	NO       	返回的结果集数量 默认值:50 最大值:100
        recvWindow       	int 	NO
        '''
        return self.send_request(*self.endpoints.get_orderAmendment, **to_local(locals()))

    # 查询订单 (USER_DATA)
    def get_order(self, symbol: str = '', orderId: int = '', origClientOrderId: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-3

        Name             	Type	Mandatory	Description
        symbol           	str 	YES      	交易对
        orderId          	int 	NO       	系统订单号
        origClientOrderId	str 	NO       	用户自定义的订单号
        recvWindow       	int 	NO
        '''
        return self.send_request(*self.endpoints.get_order, **to_local(locals()))

    # 撤销订单 (TRADE)
    def cancel_order(self, symbol: str = '', orderId: int = '', origClientOrderId: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-7

        Name             	Type	Mandatory	Description
        symbol           	str 	YES      	交易对
        orderId          	int 	NO       	系统订单号
        origClientOrderId	str 	NO       	用户自定义的订单号
        recvWindow       	int 	NO
        '''
        return self.send_request(*self.endpoints.cancel_order, **to_local(locals()))

    # 撤销全部订单 (TRADE)
    def cancel_allOpenOrders(self, symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-8

        Name      	Type	Mandatory	Description
        symbol    	str 	YES      	交易对
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.cancel_allOpenOrders, **to_local(locals()))

    # 批量撤销订单 (TRADE)
    def cancel_batchOrders(self, symbol: str = '', orderIdList: list = '',
                           origClientOrderIdList: list = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-9

        Name                 	Type        	Mandatory	Description
        symbol               	str         	YES      	交易对
        orderIdList          	LIST<LONG>  	NO
        origClientOrderIdList	LIST<STRING>	NO
        recvWindow           	int         	NO
        '''
        return self.send_request(*self.endpoints.cancel_batchOrders, **to_local(locals()))

    # 倒计时撤销所有订单 (TRADE)
    def set_countdownCancelAll(self, symbol: str = '', countdownTime: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-10

        Name         	Type	Mandatory	Description
        symbol       	str 	YES
        countdownTime	int 	YES      	倒计时。 1000 表示 1 秒； 0 表示取消倒计时撤单功能。
        recvWindow   	int 	NO
        '''
        return self.send_request(*self.endpoints.set_countdownCancelAll, **to_local(locals()))

    # 查询当前挂单 (USER_DATA)
    def get_openOrder(self, symbol: str = '', orderId: int = '', origClientOrderId: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-4

        Name             	Type	Mandatory	Description
        symbol           	str 	YES      	交易对
        orderId          	int 	NO       	系统订单号
        origClientOrderId	str 	NO       	用户自定义的订单号
        recvWindow       	int 	NO
        '''
        return self.send_request(*self.endpoints.get_openOrder, **to_local(locals()))

    # 查看当前全部挂单 (USER_DATA)
    def get_openOrders(self, symbol: str = '', pair: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-5

        Name      	Type	Mandatory	Description
        symbol    	str 	NO       	交易对
        pair      	str 	NO       	标的交易对
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_openOrders, **to_local(locals()))

    # 查询所有订单(包括历史订单) (USER_DATA)
    def get_allOrders(self, symbol: str = '', pair: str = '', orderId: int = '', startTime: int = '', endTime: int = '',
                      limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-6

        Name      	Type	Mandatory	Description
        symbol    	str 	NO       	交易对
        pair      	str 	NO       	标的交易对
        orderId   	int 	NO       	只返回此orderID及之后的订单,缺省返回最近的订单, 仅支持配合symbol使用
        startTime 	int 	NO       	起始时间
        endTime   	int 	NO       	结束时间
        limit     	int 	NO       	返回的结果集数量 默认值:50 最大值:100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_allOrders, **to_local(locals()))

    # 账户余额 (USER_DATA)
    def get_balance(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-7

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_balance, **to_local(locals()))

    # 账户信息 (USER_DATA)
    def get_account(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-8

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_account, **to_local(locals()))

    # 调整开仓杠杆 (TRADE)
    def set_leverage(self, symbol: str = '', leverage: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-11

        Name      	Type	Mandatory	Description
        symbol    	str 	YES      	交易对
        leverage  	int 	YES      	目标杠杆倍数
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_leverage, **to_local(locals()))

    # 变换逐全仓模式 (TRADE)
    def set_marginType(self, symbol: str = '', marginType: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-12

        Name      	Type	Mandatory	Description
        symbol    	str 	YES      	交易对
        marginType	str 	YES      	保证金模式 ISOLATED(逐仓), CROSSED(全仓)
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_marginType, **to_local(locals()))

    # 调整逐仓保证金 (TRADE)
    def set_positionMargin(self, symbol: str = '', positionSide: str = '', amount: Union[float, int] = '',
                           type: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-13

        Name        	Type            	Mandatory	Description
        symbol      	str             	YES      	交易对
        positionSide	str             	NO
        amount      	Union[float,int]	YES      	保证金资金
        type        	int             	YES      	调整方向 1: 增加逐仓保证金,2: 减少逐仓保证金
        recvWindow  	int             	NO
        '''
        return self.send_request(*self.endpoints.set_positionMargin, **to_local(locals()))

    # 逐仓保证金变动历史 (TRADE)
    def get_positionMargin_history(self, symbol: str = '', type: int = '', startTime: int = '', endTime: int = '',
                                   limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-14

        Name      	Type	Mandatory	Description
        symbol    	str 	YES      	交易对
        type      	int 	NO       	调整方向 1: 增加逐仓保证金,2: 减少逐仓保证金
        startTime 	int 	NO       	起始时间
        endTime   	int 	NO       	结束时间
        limit     	int 	NO       	返回的结果集数量 默认值: 50
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_positionMargin_history, **to_local(locals()))

    # 用户持仓风险
    def get_positionRisk(self, marginAsset: str = '', pair: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#479ce129f6

        Name       	Type	Mandatory	Description
        marginAsset	str 	NO
        pair       	str 	NO
        recvWindow 	int 	NO
        '''
        return self.send_request(*self.endpoints.get_positionRisk, **to_local(locals()))

    # 账户成交历史 (USER_DATA)
    def get_userTrades(self, symbol: str = '', pair: str = '', startTime: int = '', endTime: int = '', fromId: int = '',
                       limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-9

        Name      	Type	Mandatory	Description
        symbol    	str 	NO       	交易对
        pair      	str 	NO       	标的交易对
        startTime 	int 	NO       	起始时间
        endTime   	int 	NO       	结束时间
        fromId    	int 	NO       	返回该fromId及之后的成交,缺省返回最近的成交,仅支持配合symbol使用
        limit     	int 	NO       	返回的结果集数量 默认值:50 最大值:1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_userTrades, **to_local(locals()))

    # 获取账户损益资金流水(USER_DATA)
    def get_income(self, symbol: str = '', incomeType: str = '', startTime: int = '', endTime: int = '',
                   limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-10

        Name      	Type	Mandatory	Description
        symbol    	str 	NO       	交易对
        incomeType	str 	NO       	收益类型 "TRANSFER","WELCOME_BONUS", "FUNDING_FEE", "REALIZED_PNL", "COMMISSION", "INSURANCE_CLEAR", "DELIVERED_SETTELMENT"
        startTime 	int 	NO       	起始时间
        endTime   	int 	NO       	结束时间
        limit     	int 	NO       	返回的结果集数量 默认值:100 最大值:1000
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_income, **to_local(locals()))

    # 标的交易对默认杠杆分层标准 (USER_DATA)
    def get_leverageBracket(self, pair: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-11

        Name      	Type	Mandatory	Description
        pair      	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_leverageBracket, **to_local(locals()))

    # 交易对杠杆分层标准 (USER_DATA)
    def get_leverageBracket(self, symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-12

        Name      	Type	Mandatory	Description
        symbol    	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_leverageBracket, **to_local(locals()))

    # 用户强平单历史 (USER_DATA)
    def get_forceOrders(self, symbol: str = '', autoCloseType: str = '', startTime: int = '', endTime: int = '',
                        limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-13

        Name         	Type	Mandatory	Description
        symbol       	str 	NO
        autoCloseType	str 	NO       	"LIQUIDATION": 强平单, "ADL": ADL减仓单.
        startTime    	int 	NO
        endTime      	int 	NO
        limit        	int 	NO       	Default 50; max 100.
        recvWindow   	int 	NO
        '''
        return self.send_request(*self.endpoints.get_forceOrders, **to_local(locals()))

    # 持仓ADL队列估算 (USER_DATA)
    def get_adlQuantile(self, symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#adl-user_data

        Name      	Type	Mandatory	Description
        symbol    	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_adlQuantile, **to_local(locals()))

    # 用户手续费率 (USER_DATA)
    def get_commissionRate(self, symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-14

        Name      	Type	Mandatory	Description
        symbol    	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_commissionRate, **to_local(locals()))
