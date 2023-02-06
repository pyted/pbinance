from finance_utils.component.local import to_local
from pbinance.client import Client
from typing import Union


# 子母账户
class _SubAccountEndpoints():
    set_virtualSubAccount = ['https://api.binance.com/','POST', '/sapi/v1/sub-account/virtualSubAccount', True]  # 创建虚拟子账户（适用主账户）
    get_list = ['https://api.binance.com/','GET', '/sapi/v1/sub-account/list', True]  # 查询子账户列表（适用主账户）
    get_transfer_history = ['https://api.binance.com/','GET', '/sapi/v1/sub-account/sub/transfer/history', True]  # 查询子账户现货资金划转历史 (适用主账户)
    get_futures_internalTransfer = ['https://api.binance.com/','GET', '/sapi/v1/sub-account/futures/internalTransfer', True]  # 查询子账户合约资金划转历史 (适用主账户)
    set_futures_internalTransfer = ['https://api.binance.com/','POST', '/sapi/v1/sub-account/futures/internalTransfer', True]  # 执行子账户合约资金划转 (适用主账户)
    get_assets = ['https://api.binance.com/','GET', '/sapi/v3/sub-account/assets', True]  # 查询子账户资产 (适用主账户)
    get_spotSummary = ['https://api.binance.com/','GET', '/sapi/v1/sub-account/spotSummary', True]  # 查询子账户现货资产汇总 (适用主账户)
    get_capital_deposit_subAddress = ['https://api.binance.com/','GET', '/sapi/v1/capital/deposit/subAddress', True]  # 获取子账户充值地址 (适用主账户)
    get_capital_deposit_subHisrec = ['https://api.binance.com/','GET', '/sapi/v1/capital/deposit/subHisrec', True]  # 获取子账户充值记录 (适用主账户)
    get_status = ['https://api.binance.com/','GET', '/sapi/v1/sub-account/status', True]  # 查询子账户Margin/Futures状态 (适用主账户)
    set_margin_enable = ['https://api.binance.com/','POST', '/sapi/v1/sub-account/margin/enable', True]  # 为子账户开通Margin (适用主账户)
    get_margin_account = ['https://api.binance.com/','GET', '/sapi/v1/sub-account/margin/account', True]  # 查询子账户Margin账户详情 (适用主账户)
    get_margin_accountSummary = ['https://api.binance.com/','GET', '/sapi/v1/sub-account/margin/accountSummary', True]  # 查询子账户Margin账户汇总 (适用主账户)
    set_futures_enable = ['https://api.binance.com/','POST', '/sapi/v1/sub-account/futures/enable', True]  # 为子账户开通Futures (适用主账户)
    set_futures_transfer = ['https://api.binance.com/','POST', '/sapi/v1/sub-account/futures/transfer', True]  # 子账户Futures划转 (仅适用主账户)
    set_margin_transfer = ['https://api.binance.com/','POST', '/sapi/v1/sub-account/margin/transfer', True]  # 子账户Margin划转 (仅适用主账户)
    set_transfer_subToSub = ['https://api.binance.com/','POST', '/sapi/v1/sub-account/transfer/subToSub', True]  # 向共同主账户下的子账户主动划转 (仅适用子账户)
    set_transfer_subToMaster = ['https://api.binance.com/','POST', '/sapi/v1/sub-account/transfer/subToMaster', True]  # 向主账户主动划转 (仅适用子账户)
    get_transfer_subUserHistory = ['https://api.binance.com/','GET', '/sapi/v1/sub-account/transfer/subUserHistory', True]  # 查询子账户划转历史 (仅适用子账户)
    set_universalTransfer = ['https://api.binance.com/','POST', '/sapi/v1/sub-account/universalTransfer', True]  # 子母账户万能划转 (适用主账户)
    get_universalTransfer = ['https://api.binance.com/','GET', '/sapi/v1/sub-account/universalTransfer', True]  # 查询子母账户万能划转历史 (适用主账户)
    get_futures_account = ['https://api.binance.com/','GET', '/sapi/v2/sub-account/futures/account', True]  # 查询子账户Futures账户详情V2 (适用主账户)
    get_futures_accountSummary = ['https://api.binance.com/','GET', '/sapi/v2/sub-account/futures/accountSummary', True]  # 查询子账户Futures账户汇总V2 (适用主账户)
    get_futures_positionRisk = ['https://api.binance.com/','GET', '/sapi/v2/sub-account/futures/positionRisk', True]  # 查询子账户合约持仓信息V2 (仅适用主账户)
    set_blvt_enable = ['https://api.binance.com/','POST', '/sapi/v1/sub-account/blvt/enable', True]  # 为子账户开通杠杆代币 (适用母账户)
    sert_subAccountApi_ipRestriction = ['','POST','/sapi/v1/sub-account/subAccountApi/ipRestriction',True]  #为子账户API Key开启/关闭IP白名单 (适用母账户)
    set_subAccountApi_ipRestriction_ipList = ['https://api.binance.com/','POST', '/sapi/v1/sub-account/subAccountApi/ipRestriction/ipList', True]  # 为子账户API Key添加IP白名单 (适用母账户)
    get_subAccountApi_ipRestriction = ['https://api.binance.com/','GET', '/sapi/v1/sub-account/subAccountApi/ipRestriction', True]  # 查询子账户API Key IP白名单 (适用母账户)
    delete_subAccountApi_ipRestriction_ipList = ['https://api.binance.com/','DELETE', '/sapi/v1/sub-account/subAccountApi/ipRestriction/ipList', True]  # 删除子账户API Key IP白名单 (适用母账户)
    get_apiRestrictions_ipRestriction_thirdPartyList = ['https://api.binance.com/','GET', '/sapi/v1/sub-account/apiRestrictions/ipRestriction/thirdPartyList', False]  # 取得子帳戶API key IP三方名單 (适用母账户)
    set_subAccountApi_ipRestriction = ['https://api.binance.com/','POST', '/sapi/v2/sub-account/subAccountApi/ipRestriction', True]  # 为子账户API Key更新IP白名单 (适用母账户)
    set_managed_subaccount_deposit = ['https://api.binance.com/','POST', '/sapi/v1/managed-subaccount/deposit', True]  # 投资人账户为托管子账户充值资产 (适用投资人母账户)
    get_managed_subaccount_asset = ['https://api.binance.com/','GET', '/sapi/v1/managed-subaccount/asset', True]  # 投资人账户查询托管子账户资产 (适用投资人母账户)
    set_managed_subaccount_withdraw = ['https://api.binance.com/','POST', '/sapi/v1/managed-subaccount/withdraw', True]  # 投资人账户为托管子账户提币资产 (适用投资人母账户)
    get_managed_subaccount_accountSnapshot = ['https://api.binance.com/','GET', '/sapi/v1/managed-subaccount/accountSnapshot', True]  # 查询托管子账户资产快照 (适用投资人母账户)


class SubAccount(Client):
    endpoints = _SubAccountEndpoints

    # 创建虚拟子账户（适用主账户）
    def set_virtualSubAccount(self, subAccountString: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#85bc268690

        Name            	Type	Mandatory	Description
        subAccountString	str 	YES      	请输入字符串，我们将为您创建一个虚拟邮箱进行注册
        recvWindow      	int 	NO
        '''
        return self.send_request(*self.endpoints.set_virtualSubAccount, **to_local(locals()))

    # 查询子账户列表（适用主账户）
    def get_list(self, email: str = '', isFreeze: str = '', page: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#bd2019e819

        Name      	Type	Mandatory	Description
        email     	str 	NO       	Sub-account email
        isFreeze  	str 	NO       	true or false
        page      	int 	NO       	默认: 1
        limit     	int 	NO       	默认: 1, 最大: 200
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_list, **to_local(locals()))

    # 查询子账户现货资金划转历史 (适用主账户)
    def get_transfer_history(self, fromEmail: str = '', toEmail: str = '', startTime: int = '', endTime: int = '',
                             page: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#13801cd07b

        Name      	Type	Mandatory	Description
        fromEmail 	str 	NO
        toEmail   	str 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        page      	int 	NO       	默认: 1
        limit     	int 	NO       	默认: 500
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_transfer_history, **to_local(locals()))

    # 查询子账户合约资金划转历史 (适用主账户)
    def get_futures_internalTransfer(self, email: str = '', futuresType: int = '', startTime: int = '',
                                     endTime: int = '', page: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#c144d4d678

        Name       	Type	Mandatory	Description
        email      	str 	YES
        futuresType	int 	YES      	1:USDT合约，2: 币本位合约
        startTime  	int 	NO       	默认返回100天内历史记录
        endTime    	int 	NO       	默认返回100天内历史记录
        page       	int 	NO       	默认值: 1
        limit      	int 	NO       	默认值: 50, 最大值：500
        recvWindow 	int 	NO
        '''
        return self.send_request(*self.endpoints.get_futures_internalTransfer, **to_local(locals()))

    # 执行子账户合约资金划转 (适用主账户)
    def set_futures_internalTransfer(self, fromEmail: str = '', toEmail: str = '', futuresType: int = '',
                                     asset: str = '', amount: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#b410330a48

        Name       	Type            	Mandatory	Description
        fromEmail  	str             	YES
        toEmail    	str             	YES
        futuresType	int             	YES      	1:USDT合约， 2: 币本位合约
        asset      	str             	YES
        amount     	Union[float,int]	YES
        recvWindow 	int             	NO
        '''
        return self.send_request(*self.endpoints.set_futures_internalTransfer, **to_local(locals()))

    # 查询子账户资产 (适用主账户)
    def get_assets(self, email: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#46f686d3aa

        Name      	Type	Mandatory	Description
        email     	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_assets, **to_local(locals()))

    # 查询子账户现货资产汇总 (适用主账户)
    def get_spotSummary(self, email: str = '', page: int = '', size: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#52f120c8f6

        Name      	Type	Mandatory	Description
        email     	str 	NO       	子账户邮箱
        page      	int 	NO       	分页，默认 1
        size      	int 	NO       	单页条目数, 默认 10, 最大 20
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_spotSummary, **to_local(locals()))

    # 获取子账户充值地址 (适用主账户)
    def get_capital_deposit_subAddress(self, email: str = '', coin: str = '', network: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#7c015974a6

        Name      	Type	Mandatory	Description
        email     	str 	YES
        coin      	str 	YES
        network   	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_capital_deposit_subAddress, **to_local(locals()))

    # 获取子账户充值记录 (适用主账户)
    def get_capital_deposit_subHisrec(self, email: str = '', coin: str = '', status: int = '', startTime: int = '',
                                      endTime: int = '', limit: int = '', offset: int = '', recvWindow: int = '',
                                      txId: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#0baad7eee0

        Name      	Type	Mandatory	Description
        email     	str 	YES
        coin      	str 	NO
        status    	int 	NO       	0(0:pending,6: credited but cannot withdraw, 1:success)
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO
        offset    	int 	NO       	default:0
        recvWindow	int 	NO
        txId      	str 	NO
        '''
        return self.send_request(*self.endpoints.get_capital_deposit_subHisrec, **to_local(locals()))

    # 查询子账户Margin/Futures状态 (适用主账户)
    def get_status(self, email: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#margin-futures

        Name      	Type	Mandatory	Description
        email     	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_status, **to_local(locals()))

    # 为子账户开通Margin (适用主账户)
    def set_margin_enable(self, email: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#margin

        Name      	Type	Mandatory	Description
        email     	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_margin_enable, **to_local(locals()))

    # 查询子账户Margin账户详情 (适用主账户)
    def get_margin_account(self, email: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#margin-2

        Name      	Type	Mandatory	Description
        email     	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_margin_account, **to_local(locals()))

    # 查询子账户Margin账户汇总 (适用主账户)
    def get_margin_accountSummary(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#margin-3

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_margin_accountSummary, **to_local(locals()))

    # 为子账户开通Futures (适用主账户)
    def set_futures_enable(self, email: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#futures

        Name      	Type	Mandatory	Description
        email     	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_futures_enable, **to_local(locals()))

    # 子账户Futures划转 (仅适用主账户)
    def set_futures_transfer(self, email: str = '', asset: str = '', amount: Union[float, int] = '', type: int = '',
                             recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#futures-4

        Name      	Type            	Mandatory	Description
        email     	str             	YES
        asset     	str             	YES      	划转资产, e.g., USDT
        amount    	Union[float,int]	YES      	划转数量
        type      	int             	YES      	1: 由子账户的现货账户划转至其USDT本位合约账户; 2: 由子账户的USDT本位合约账户划转至其现货账户； 3:由子账户现货账户划转至其COIN本位合约账户；4: 由子账户COIN本位合约账户划转至其现货账户
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_futures_transfer, **to_local(locals()))

    # 子账户Margin划转 (仅适用主账户)
    def set_margin_transfer(self, email: str = '', asset: str = '', amount: Union[float, int] = '', type: int = '',
                            recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#margin-4

        Name      	Type            	Mandatory	Description
        email     	str             	YES
        asset     	str             	YES      	划转资产, e.g., USDT
        amount    	Union[float,int]	YES      	划转数量
        type      	int             	YES      	1: 由子账户的现货账户划转至其杠杆账户; 2: 由子账户的杠杆账户划转至其现货账户
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_margin_transfer, **to_local(locals()))

    # 向共同主账户下的子账户主动划转 (仅适用子账户)
    def set_transfer_subToSub(self, toEmail: str = '', asset: str = '', amount: Union[float, int] = '',
                              recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#84d71c39a1

        Name      	Type            	Mandatory	Description
        toEmail   	str             	YES
        asset     	str             	YES
        amount    	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_transfer_subToSub, **to_local(locals()))

    # 向主账户主动划转 (仅适用子账户)
    def set_transfer_subToMaster(self, asset: str = '', amount: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#19a57905df

        Name      	Type            	Mandatory	Description
        asset     	str             	YES
        amount    	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_transfer_subToMaster, **to_local(locals()))

    # 查询子账户划转历史 (仅适用子账户)
    def get_transfer_subUserHistory(self, asset: str = '', type: int = '', startTime: int = '', endTime: int = '',
                                    limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#f38ebd8fc2

        Name      	Type	Mandatory	Description
        asset     	str 	NO       	如不提供，返回所有asset 划转记录
        type      	int 	NO       	1: transfer in, 2: transfer out; 如不提供，返回transfer out方向划转记录
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	默认值: 500
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_transfer_subUserHistory, **to_local(locals()))

    # 子母账户万能划转 (适用主账户)
    def set_universalTransfer(self, fromEmail: str = '', toEmail: str = '', fromAccountType: str = '',
                              toAccountType: str = '', clientTranId: str = '', symbol: str = '', asset: str = '',
                              amount: Union[float, int] = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#c2d564529d

        Name           	Type            	Mandatory	Description
        fromEmail      	str             	NO
        toEmail        	str             	NO
        fromAccountType	str             	YES      	"SPOT","USDT_FUTURE","COIN_FUTURE","MARGIN"(Cross),"ISOLATED_MARGIN"
        toAccountType  	str             	YES      	"SPOT","USDT_FUTURE","COIN_FUTURE","MARGIN"(Cross),"ISOLATED_MARGIN"
        clientTranId   	str             	NO       	不可重复
        symbol         	str             	NO       	仅在ISOLATED_MARGIN类型下使用
        asset          	str             	YES
        amount         	Union[float,int]	YES
        recvWindow     	int             	NO
        '''
        return self.send_request(*self.endpoints.set_universalTransfer, **to_local(locals()))

    # 查询子母账户万能划转历史 (适用主账户)
    def get_universalTransfer(self, fromEmail: str = '', toEmail: str = '', clientTranId: str = '', startTime: int = '',
                              endTime: int = '', page: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#5f274ef2c2

        Name        	Type	Mandatory	Description
        fromEmail   	str 	NO
        toEmail     	str 	NO
        clientTranId	str 	NO
        startTime   	int 	NO
        endTime     	int 	NO
        page        	int 	NO       	默认 1
        limit       	int 	NO       	默认 500, 最大 500
        recvWindow  	int 	NO
        '''
        return self.send_request(*self.endpoints.get_universalTransfer, **to_local(locals()))

    # 查询子账户Futures账户详情V2 (适用主账户)
    def get_futures_account(self, email: str = '', futuresType: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#futures-v2

        Name       	Type	Mandatory	Description
        email      	str 	YES
        futuresType	int 	YES      	1:USDT Margined Futures, 2:COIN Margined Futures
        recvWindow 	int 	NO
        '''
        return self.send_request(*self.endpoints.get_futures_account, **to_local(locals()))

    # 查询子账户Futures账户汇总V2 (适用主账户)
    def get_futures_accountSummary(self, futuresType: int = '', page: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#futures-v2-2

        Name       	Type	Mandatory	Description
        futuresType	int 	YES      	1:USDT Margined Futures, 2:COIN Margined Futures
        page       	int 	NO       	default:1
        limit      	int 	NO       	default:10, max:20
        recvWindow 	int 	NO
        '''
        return self.send_request(*self.endpoints.get_futures_accountSummary, **to_local(locals()))

    # 查询子账户合约持仓信息V2 (仅适用主账户)
    def get_futures_positionRisk(self, email: str = '', futuresType: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#v2

        Name       	Type	Mandatory	Description
        email      	str 	YES
        futuresType	int 	YES      	1:USDT Margined Futures, 2:COIN Margined Futures
        recvWindow 	int 	NO
        '''
        return self.send_request(*self.endpoints.get_futures_positionRisk, **to_local(locals()))

    # 为子账户开通杠杆代币 (适用母账户)
    def set_blvt_enable(self, email: str = '', enableBlvt: bool = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#60e8efdca2

        Name      	Type	Mandatory	Description
        email     	str 	YES      	Sub-account email
        enableBlvt	bool	YES      	Only true for now
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_blvt_enable, **to_local(locals()))

    # 为子账户API Key开启/关闭IP白名单 (适用母账户)
    def sert_subAccountApi_ipRestriction(self, email: str = '', subAccountApiKey: str = '', ipRestrict: bool = '',
                                         recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#api-key-ip

        Name            	Type	Mandatory	Description
        email           	str 	YES      	Sub-account email
        subAccountApiKey	str 	YES
        ipRestrict      	bool	YES      	true or false
        recvWindow      	int 	NO
        '''
        return self.send_request(*self.endpoints.sert_subAccountApi_ipRestriction, **to_local(locals()))

    # 为子账户API Key添加IP白名单 (适用母账户)
    def set_subAccountApi_ipRestriction_ipList(self, email: str = '', subAccountApiKey: str = '', ipAddress: str = '',
                                               recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#api-key-ip-2

        Name            	Type	Mandatory	Description
        email           	str 	YES      	Sub-account email
        subAccountApiKey	str 	YES
        ipAddress       	str 	NO       	可批量添加，用逗号分隔。单API Key最多可添加30个
        recvWindow      	int 	NO
        '''
        return self.send_request(*self.endpoints.set_subAccountApi_ipRestriction_ipList, **to_local(locals()))

    # 查询子账户API Key IP白名单 (适用母账户)
    def get_subAccountApi_ipRestriction(self, email: str = '', subAccountApiKey: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#api-key-ip-3

        Name            	Type	Mandatory	Description
        email           	str 	YES      	Sub-account email
        subAccountApiKey	str 	YES
        recvWindow      	int 	NO
        '''
        return self.send_request(*self.endpoints.get_subAccountApi_ipRestriction, **to_local(locals()))

    # 删除子账户API Key IP白名单 (适用母账户)
    def delete_subAccountApi_ipRestriction_ipList(self, email: str = '', subAccountApiKey: str = '',
                                                  ipAddress: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#api-key-ip-4

        Name            	Type	Mandatory	Description
        email           	str 	YES      	Sub-account email
        subAccountApiKey	str 	YES
        ipAddress       	str 	NO       	可批量删除，用逗号分隔
        recvWindow      	int 	NO
        '''
        return self.send_request(*self.endpoints.delete_subAccountApi_ipRestriction_ipList, **to_local(locals()))

    # 取得子帳戶API key IP三方名單 (适用母账户)
    def get_apiRestrictions_ipRestriction_thirdPartyList(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#api-key-ip-5

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_apiRestrictions_ipRestriction_thirdPartyList, **to_local(locals()))

    # 为子账户API Key更新IP白名单 (适用母账户)
    def set_subAccountApi_ipRestriction(self, email: str = '', subAccountApiKey: str = '', status: str = '',
                                        thirdPartyName: str = '', ipAddress: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#api-key-ip-6

        Name            	Type	Mandatory	Description
        email           	str 	YES      	Sub-account email
        subAccountApiKey	str 	YES
        status          	str 	YES      	IP限制状态。1或不填入(null) = IP未受限。2 = 仅限受信任IP访问。3 = 仅限受信任三方IP访问。
        thirdPartyName  	str 	NO       	填入三方名称
        ipAddress       	str 	NO       	可批量填入IP，以逗号区隔
        recvWindow      	int 	NO
        '''
        return self.send_request(*self.endpoints.set_subAccountApi_ipRestriction, **to_local(locals()))

    # 投资人账户为托管子账户充值资产 (适用投资人母账户)
    def set_managed_subaccount_deposit(self, toEmail: str = '', asset: str = '', amount: Union[float, int] = '',
                                       recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#6b06e66554

        Name      	Type            	Mandatory	Description
        toEmail   	str             	YES
        asset     	str             	YES
        amount    	Union[float,int]	YES
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_managed_subaccount_deposit, **to_local(locals()))

    # 投资人账户查询托管子账户资产 (适用投资人母账户)
    def get_managed_subaccount_asset(self, email: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#55063e46dd

        Name      	Type	Mandatory	Description
        email     	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_managed_subaccount_asset, **to_local(locals()))

    # 投资人账户为托管子账户提币资产 (适用投资人母账户)
    def set_managed_subaccount_withdraw(self, fromEmail: str = '', asset: str = '', amount: Union[float, int] = '',
                                        transferDate: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#6105aa08c4

        Name        	Type            	Mandatory	Description
        fromEmail   	str             	YES
        asset       	str             	YES
        amount      	Union[float,int]	YES
        transferDate	int             	NO       	提币会自动发生在选择的日期(UTC0)，如果没有选择日期，提币会立即生效
        recvWindow  	int             	NO
        '''
        return self.send_request(*self.endpoints.set_managed_subaccount_withdraw, **to_local(locals()))

    # 查询托管子账户资产快照 (适用投资人母账户)
    def get_managed_subaccount_accountSnapshot(self, email: str = '', type: str = '', startTime: int = '',
                                               endTime: int = '', limit: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#2c2c5f3fa7

        Name      	Type	Mandatory	Description
        email     	str 	YES
        type      	str 	YES      	"SPOT"（现货）, "MARGIN"（全仓）, "FUTURES"（U本位合约）
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	min 7, max 30, default 7
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_managed_subaccount_accountSnapshot, **to_local(locals()))
