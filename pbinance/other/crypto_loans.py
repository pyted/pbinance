from finance_utils.component.local import to_local
from pbinance.client import Client
from typing import Union


# 质押借币
class _CryptoLoansEndpoints():
    get_income = ['https://api.binance.com/','GET', '/sapi/v1/loan/income', True]  # 获取质押借币资金流水 (USER_DATA)
    set_borrow = ['https://api.binance.com/','POST', '/sapi/v1/loan/borrow', False]  # 借币 - 质押借币借贷 (TRADE)
    get_borrow_history = ['https://api.binance.com/','GET', '/sapi/v1/loan/borrow/history', False]  # 借币 - 查询质押借币历史记录 (USER_DATA)
    get_ongoing_orders = ['https://api.binance.com/','GET', '/sapi/v1/loan/ongoing/orders', False]  # 借币 - 查询借款中订单列表 (USER_DATA)
    set_repay = ['https://api.binance.com/','POST', '/sapi/v1/loan/repay', False]  # 还款 - 质押借币还款 (TRADE)
    get_repay_history = ['https://api.binance.com/','GET', '/sapi/v1/loan/repay/history', False]  # 还款 - 查询还款记录历史 (USER_DATA)
    set_adjust_ltv = ['https://api.binance.com/','POST', '/sapi/v1/loan/adjust/ltv', False]  # 调整质押率 - 质押借币调整质押率 (TRADE)
    get_ltv_adjustment_history = ['https://api.binance.com/','GET', '/sapi/v1/loan/ltv/adjustment/history', False]  # 调整质押率 - 查询质押率调整历史 (USER_DATA)
    get_loanable_data = ['https://api.binance.com/','GET', '/sapi/v1/loan/loanable/data', False]  # 查询可借币种数据 (USER_DATA)
    get_collateral_data = ['https://api.binance.com/','GET', '/sapi/v1/loan/collateral/data', False]  # 查询抵押币种数据 (USER_DATA)
    get_repay_collateral_rate = ['https://api.binance.com/','GET', '/sapi/v1/loan/repay/collateral/rate', False]  # 查询抵押币种还款汇率 (USER_DATA)
    set_customize_margin_call = ['https://api.binance.com/','POST', '/sapi/v1/loan/customize/margin_call', False]  # 质押借币自定义补仓质押率 (TRADE)


class CryptoLoans(Client):
    endpoints = _CryptoLoansEndpoints

    # 获取质押借币资金流水 (USER_DATA)
    def get_income(self, asset: str = '', type: str = '', startTime: int = '', endTime: int = '', limit: int = '',
                   recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-104

        Name      	Type	Mandatory	Description
        asset     	str 	NO
        type      	str 	NO          默认返回所有类型 枚举值：借入 borrowIn,抵押金使用collateralSpent, 还款金额repayAmount, 抵押物返还collateralReturn, 增加抵押物addCollateral, 减少抵押物removeCollateral, 强平后返还抵押物collateralReturnAfterLiquidation
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	默认 20, 最大 100
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_income, **to_local(locals()))

    # 借币 - 质押借币借贷 (TRADE)
    def set_borrow(self, loanCoin: str = '', loanAmount: Union[float, int] = '', collateralCoin: str = '',
                   collateralAmount: Union[float, int] = '', loanTerm: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-19

        Name            	Type            	Mandatory	Description
        loanCoin        	str             	YES
        loanAmount      	Union[float,int]	NO       	当collateralAmount为空时，需必填
        collateralCoin  	str             	YES
        collateralAmount	Union[float,int]	NO       	当loanAmount为空时，需必填
        loanTerm        	int             	YES      	7/14/30/90/180 天
        recvWindow      	int             	NO
        '''
        return self.send_request(*self.endpoints.set_borrow, **to_local(locals()))

    # 借币 - 查询质押借币历史记录 (USER_DATA)
    def get_borrow_history(self, orderId: int = '', loanCoin: str = '', collateralCoin: str = '', startTime: int = '',
                           endTime: int = '', current: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-105

        Name          	Type	Mandatory	Description
        orderId       	int 	NO          POST /sapi/v1/loan/borrow 中的 orderId
        loanCoin      	str 	NO
        collateralCoin	str 	NO
        startTime     	int 	NO
        endTime       	int 	NO
        current       	int 	NO       	当前查询页数，从1开始。默认值：1；最大：1000。
        limit         	int 	NO       	默认值：10；最大：100。
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_borrow_history, **to_local(locals()))

    # 借币 - 查询借款中订单列表 (USER_DATA)
    def get_ongoing_orders(self, orderId: int = '', loanCoin: str = '', collateralCoin: str = '', current: int = '',
                           limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-106

        Name          	Type	Mandatory	Description
        orderId       	int 	NO
        loanCoin      	str 	NO
        collateralCoin	str 	NO
        current       	int 	NO       	当前查询页数，从1开始。默认值：1；最大：1000。
        limit         	int 	NO       	默认值：10；最大：100。
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_ongoing_orders, **to_local(locals()))

    # 还款 - 质押借币还款 (TRADE)
    def set_repay(self, orderId: int = '', amount: Union[float, int] = '', type: int = '', collateralReturn: bool = '',
                  recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-20

        Name            	Type            	Mandatory	Description
        orderId         	int             	YES
        amount          	Union[float,int]	YES
        type            	int             	NO       	默认值：1。 1：用借贷币还款；2：用抵押币还款。
        collateralReturn	bool            	NO       	默认值：TRUE。TRUE：多余的抵押金退回现货钱包；FALSE: 多余的抵押金保留在原订单里。
        recvWindow      	int             	NO
        '''
        return self.send_request(*self.endpoints.set_repay, **to_local(locals()))

    # 还款 - 查询还款记录历史 (USER_DATA)
    def get_repay_history(self, orderId: int = '', loanCoin: str = '', collateralCoin: str = '', startTime: int = '',
                          endTime: int = '', current: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-107

        Name          	Type	Mandatory	Description
        orderId       	int 	NO
        loanCoin      	str 	NO
        collateralCoin	str 	NO
        startTime     	int 	NO
        endTime       	int 	NO
        current       	int 	NO       	当前查询页数，从1开始。默认值：1；最大：1000。
        limit         	int 	NO       	默认值：10；最大：100。
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_repay_history, **to_local(locals()))

    # 调整质押率 - 质押借币调整质押率 (TRADE)
    def set_adjust_ltv(self, orderId: int = '', amount: Union[float, int] = '', direction: str = '',
                       recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-21

        Name      	Type            	Mandatory	Description
        orderId   	int             	YES
        amount    	Union[float,int]	YES
        direction 	str             	YES      	"ADDITIONAL", "REDUCED"
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_adjust_ltv, **to_local(locals()))

    # 调整质押率 - 查询质押率调整历史 (USER_DATA)
    def get_ltv_adjustment_history(self, orderId: int = '', loanCoin: str = '', collateralCoin: str = '',
                                   startTime: int = '', endTime: int = '', current: int = '', limit: int = '',
                                   recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-108

        Name          	Type	Mandatory	Description
        orderId       	int 	NO
        loanCoin      	str 	NO
        collateralCoin	str 	NO
        startTime     	int 	NO
        endTime       	int 	NO
        current       	int 	NO       	当前查询页数，从1开始。默认值：1；最大：1000。
        limit         	int 	NO       	默认值：10；最大：100。
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_ltv_adjustment_history, **to_local(locals()))

    # 查询可借币种数据 (USER_DATA)
    def get_loanable_data(self, loanCoin: str = '', vipLevel: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-109

        Name      	Type	Mandatory	Description
        loanCoin  	str 	NO
        vipLevel  	int 	NO       	默认：用户当前VIP登记。如有特殊配置，则填“-1”查询
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_loanable_data, **to_local(locals()))

    # 查询抵押币种数据 (USER_DATA)
    def get_collateral_data(self, collateralCoin: str = '', vipLevel: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-110

        Name          	Type	Mandatory	Description
        collateralCoin	str 	NO
        vipLevel      	int 	NO       	默认：用户当前VIP登记。如有特殊配置，则填“-1”查询
        recvWindow    	int 	NO
        '''
        return self.send_request(*self.endpoints.get_collateral_data, **to_local(locals()))

    # 查询抵押币种还款汇率 (USER_DATA)
    def get_repay_collateral_rate(self, loanCoin: str = '', collateralCoin: str = '',
                                  repayAmount: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-111

        Name          	Type            	Mandatory	Description
        loanCoin      	str             	YES
        collateralCoin	str             	YES
        repayAmount   	Union[float,int]	YES      	以借贷币种为单位的还款金额
        recvWindow    	int             	NO
        '''
        return self.send_request(*self.endpoints.get_repay_collateral_rate, **to_local(locals()))

    # 质押借币自定义补仓质押率 (TRADE)
    def set_customize_margin_call(self, orderId: int = '', collateralCoin: str = '', marginCall: Union[float, int] = '',
                                  recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-22

        Name          	Type            	Mandatory	Description
        orderId       	int             	NO       	当collateralCoin为空时，需必填。orderId或collateralCoin只需传一个，如果两个参数同时传，以orderId为准。
        collateralCoin	str             	NO       	当orderID为空时，需必填。orderId或collateralCoin只需传一个，如果两个参数同时传，以orderId为准。
        marginCall    	Union[float,int]	YES
        recvWindow    	int             	NO
        '''
        return self.send_request(*self.endpoints.set_customize_margin_call, **to_local(locals()))
