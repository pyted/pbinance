from paux.param import to_local
from pbinance.client import Client
from typing import Union


# 钱包接口
class _WalletEndpoints():
    get_system_status = ['https://api.binance.com/', 'GET', '/sapi/v1/system/status', False]  # 系统状态(System)
    get_capital_config_getall = ['https://api.binance.com/', 'GET', '/sapi/v1/capital/config/getall', True]  # 获取所有币信息 (USER_DATA)
    get_accountSnapshot = ['https://api.binance.com/', 'GET', '/sapi/v1/accountSnapshot', True]  # 查询每日资产快照 (USER_DATA)
    set_account_disableFastWithdrawSwitch = ['https://api.binance.com/', 'POST', '/sapi/v1/account/disableFastWithdrawSwitch', True]  # 关闭站内划转 (USER_DATA)
    set_account_enableFastWithdrawSwitch = ['https://api.binance.com/', 'POST', '/sapi/v1/account/enableFastWithdrawSwitch', True]  # 开启站内划转 (USER_DATA)
    set_capital_withdraw_apply = ['https://api.binance.com/', 'POST', '/sapi/v1/capital/withdraw/apply', True]  # 提币 (USER_DATA)
    get_capital_deposit_hisrec = ['https://api.binance.com/', 'GET', '/sapi/v1/capital/deposit/hisrec', True]  # 获取充值历史(支持多网络) (USER_DATA)
    get_capital_withdraw_history = ['https://api.binance.com/', 'GET', '/sapi/v1/capital/withdraw/history', True]  # 获取提币历史 (支持多网络) (USER_DATA)
    get_capital_deposit_address = ['https://api.binance.com/', 'GET', '/sapi/v1/capital/deposit/address', True]  # 获取充值地址 (支持多网络) (USER_DATA)
    get_account_status = ['https://api.binance.com/', 'GET', '/sapi/v1/account/status', False]  # 账户状态 (USER_DATA)
    get_account_apiTradingStatus = ['https://api.binance.com/', 'GET', '/sapi/v1/account/apiTradingStatus', True]  # 账户API交易状态(USER_DATA)
    get_asset_dribblet = ['https://api.binance.com/', 'GET', '/sapi/v1/asset/dribblet', True]  # 小额资产转换BNB历史 (USER_DATA)
    set_asset_dust_btc = ['https://api.binance.com/', 'POST', '/sapi/v1/asset/dust-btc', True]  # 获取可以转换成BNB的小额资产 (USER_DATA)
    set_asset_dust = ['https://api.binance.com/', 'POST', '/sapi/v1/asset/dust', True]  # 小额资产转换 (USER_DATA)
    get_asset_assetDividend = ['https://api.binance.com/', 'GET', '/sapi/v1/asset/assetDividend', True]  # 资产利息记录 (USER_DATA)
    get_asset_assetDetail = ['https://api.binance.com/', 'GET', '/sapi/v1/asset/assetDetail', True]  # 上架资产详情 (USER_DATA)
    get_asset_tradeFee = ['https://api.binance.com/', 'GET', '/sapi/v1/asset/tradeFee', True]  # 交易手续费率查询 (USER_DATA)
    set_set_asset_transfer = ['https://api.binance.com/', 'POST', '/sapi/v1/asset/transfer', True]  # 用户万向划转 (USER_DATA)
    get_get_asset_transfer = ['https://api.binance.com/', 'GET', '/sapi/v1/asset/transfer', True]  # 查询用户万向划转历史 (USER_DATA)
    set_asset_get_funding_asset = ['https://api.binance.com/', 'POST', '/sapi/v1/asset/get-funding-asset', True]  # 资金账户 (USER_DATA)
    set_asset_getUserAsset = ['https://api.binance.com/', 'POST', '/sapi/v3/asset/getUserAsset', False]  # 用户持仓 (USER_DATA)
    set_asset_convert_transfer = ['https://api.binance.com/', 'POST', '/sapi/v1/asset/convert-transfer', False]  # 稳定币自动兑换划转 (TRADE)
    get_asset_convert_transfer_queryByPage = ['https://api.binance.com/', 'GET', '/sapi/v1/asset/convert-transfer/queryByPage', False]  # # 稳定币自动兑换划转查询 (USER_DATA)
    get_asset_ledger_transfer_cloud_mining_queryByPage = ['https://api.binance.com/', 'GET', '/sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage', False]  # 云算力历史记录分页查询 (USER_DATA)
    get_account_apiRestrictions = ['https://api.binance.com/', 'GET', '/sapi/v1/account/apiRestrictions', True]  # 查询用户API Key权限 (USER_DATA)

class Wallet(Client):
    endpoints = _WalletEndpoints

    # 系统状态(System)
    def get_system_status(self):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#system
        '''
        return self.send_request(*self.endpoints.get_system_status, **to_local(locals()))

    # 获取所有币信息 (USER_DATA)
    def get_capital_config_getall(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_capital_config_getall, **to_local(locals()))

    # 查询每日资产快照 (USER_DATA)
    def get_accountSnapshot(self, type: str = '', startTime: int = '', endTime: int = '', limit: int = '',
                            recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-2

        Name      	Type	Mandatory	Description
        type      	str 	YES      	"SPOT", "MARGIN", "FUTURES"
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	min 7, max 30, default 7
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_accountSnapshot, **to_local(locals()))

    # 关闭站内划转 (USER_DATA)
    def set_account_disableFastWithdrawSwitch(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-3

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_account_disableFastWithdrawSwitch, **to_local(locals()))

    # 开启站内划转 (USER_DATA)
    def set_account_enableFastWithdrawSwitch(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-4

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_account_enableFastWithdrawSwitch, **to_local(locals()))

    # 提币 (USER_DATA)
    def set_capital_withdraw_apply(self, coin: str = '', withdrawOrderId: str = '', network: str = '',
                                   address: str = '', addressTag: str = '', amount: Union[float, int] = '',
                                   transactionFeeFlag: bool = '', name: str = '', walletType: int = '',
                                   recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-5

        Name              	Type            	Mandatory	Description
        coin              	str             	YES
        withdrawOrderId   	str             	NO       	自定义提币ID
        network           	str             	NO       	提币网络
        address           	str             	YES      	提币地址
        addressTag        	str             	NO       	某些币种例如 XRP,XMR 允许填写次级地址标签
        amount            	Union[float,int]	YES      	数量
        transactionFeeFlag	bool            	NO
        name              	str             	NO
        walletType        	int             	NO       	表示出金使用的钱包，0为现货钱包，1为资金钱包。默认walletType为"充币账户"是您设置在钱包->现货账户或资金账户->充值。
        recvWindow        	int             	NO
        '''
        return self.send_request(*self.endpoints.set_capital_withdraw_apply, **to_local(locals()))

    # 获取充值历史(支持多网络) (USER_DATA)
    def get_capital_deposit_hisrec(self, coin: str = '', status: int = '', startTime: int = '', endTime: int = '',
                                   offset: int = '', limit: int = '', recvWindow: int = '', txId: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-6

        Name      	Type	Mandatory	Description
        coin      	str 	NO
        status    	int 	NO       	0(0:pending,6: credited but cannot withdraw, 1:success)
        startTime 	int 	NO       	默认当前时间90天前的时间戳
        endTime   	int 	NO       	默认当前时间戳
        offset    	int 	NO       	默认:0
        limit     	int 	NO       	默认：1000，最大1000
        recvWindow	int 	NO
        txId      	str 	NO
        '''
        return self.send_request(*self.endpoints.get_capital_deposit_hisrec, **to_local(locals()))

    # 获取提币历史 (支持多网络)  (USER_DATA)
    def get_capital_withdraw_history(self, coin: str = '', withdrawOrderId: str = '', status: int = '',
                                     offset: int = '', limit: int = '', startTime: int = '', endTime: int = '',
                                     recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-7

        Name           	Type	Mandatory	Description
        coin           	str 	NO
        withdrawOrderId	str 	NO
        status         	int 	NO       	0(0:已发送确认Email,1:已被用户取消 2:等待确认 3:被拒绝 4:处理中 5:提现交易失败 6 提现完成)
        offset         	int 	NO
        limit          	int 	NO       	默认：1000， 最大：1000
        startTime      	int 	NO       	默认当前时间90天前的时间戳
        endTime        	int 	NO       	默认当前时间戳
        recvWindow     	int 	NO
        '''
        return self.send_request(*self.endpoints.get_capital_withdraw_history, **to_local(locals()))

    # 获取充值地址 (支持多网络) (USER_DATA)
    def get_capital_deposit_address(self, coin: str = '', network: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-8

        Name      	Type	Mandatory	Description
        coin      	str 	YES
        network   	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_capital_deposit_address, **to_local(locals()))

    # 账户状态 (USER_DATA)
    def get_account_status(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-9

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_account_status, **to_local(locals()))

    # 账户API交易状态(USER_DATA)
    def get_account_apiTradingStatus(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#api-user_data

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_account_apiTradingStatus, **to_local(locals()))

    # 小额资产转换BNB历史 (USER_DATA)
    def get_asset_dribblet(self, startTime: int = '', endTime: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#bnb-user_data

        Name      	Type	Mandatory	Description
        startTime 	int 	NO
        endTime   	int 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_asset_dribblet, **to_local(locals()))

    # 获取可以转换成BNB的小额资产 (USER_DATA)
    def set_asset_dust_btc(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#bnb-user_data-2

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_asset_dust_btc, **to_local(locals()))

    # 小额资产转换 (USER_DATA)
    def set_asset_dust(self, asset: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-10

        Name      	Type	Mandatory	Description
        asset     	str 	YES      	正在转换的资产。 例如：asset = BTC＆asset = USDT
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_asset_dust, **to_local(locals()))

    # 资产利息记录 (USER_DATA)
    def get_asset_assetDividend(self, asset: str = '', startTime: int = '', endTime: int = '', limit: int = '',
                                recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-11

        Name      	Type	Mandatory	Description
        asset     	str 	NO
        startTime 	int 	NO
        endTime   	int 	NO
        limit     	int 	NO       	Default 20, max 500
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_asset_assetDividend, **to_local(locals()))

    # 上架资产详情 (USER_DATA)
    def get_asset_assetDetail(self, asset: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-12

        Name      	Type	Mandatory	Description
        asset     	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_asset_assetDetail, **to_local(locals()))

    # 交易手续费率查询 (USER_DATA)
    def get_asset_tradeFee(self, symbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-13

        Name      	Type	Mandatory	Description
        symbol    	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_asset_tradeFee, **to_local(locals()))

    # 用户万向划转 (USER_DATA)
    def set_set_asset_transfer(self, type: str = '', asset: str = '', amount: Union[float, int] = '',
                               fromSymbol: str = '', toSymbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-14

        Name      	Type            	Mandatory	Description
        type      	str             	YES
        asset     	str             	YES
        amount    	Union[float,int]	YES
        fromSymbol	str             	NO
        toSymbol  	str             	NO
        recvWindow	int             	NO
        '''
        return self.send_request(*self.endpoints.set_set_asset_transfer, **to_local(locals()))

    # 查询用户万向划转历史 (USER_DATA)
    def get_get_asset_transfer(self, type: str = '', startTime: int = '', endTime: int = '', current: int = '',
                               size: int = '', fromSymbol: str = '', toSymbol: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-15

        Name      	Type	Mandatory	Description
        type      	str 	YES
        startTime 	int 	NO
        endTime   	int 	NO
        current   	int 	NO       	默认 1
        size      	int 	NO       	默认 10, 最大 100
        fromSymbol	str 	NO
        toSymbol  	str 	NO
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_get_asset_transfer, **to_local(locals()))

    # 资金账户 (USER_DATA)
    def set_asset_get_funding_asset(self, asset: str = '', needBtcValuation: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-16

        Name            	Type	Mandatory	Description
        asset           	str 	NO
        needBtcValuation	str 	NO       	true or false
        recvWindow      	int 	NO
        '''
        return self.send_request(*self.endpoints.set_asset_get_funding_asset, **to_local(locals()))

    # 用户持仓 (USER_DATA)
    def set_asset_getUserAsset(self, asset: str = '', needBtcValuation: bool = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-17

        Name            	Type	Mandatory	Description
        asset           	str 	NO       	如果资产为空，则查询用户所有的正资产。
        needBtcValuation	bool	NO       	是否需要返回兑换成BTC的估值
        recvWindow      	int 	NO
        '''
        return self.send_request(*self.endpoints.set_asset_getUserAsset, **to_local(locals()))

    # 稳定币自动兑换划转 (TRADE)
    def set_asset_convert_transfer(self, clientTranId: str = '', asset: str = '', amount: Union[float, int] = '',
                                   targetAsset: str = '', accountType: str = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade

        Name        	Type            	Mandatory	Description
        clientTranId	str             	YES      	用户自定义流水号，唯一标志，限制最短长度为20
        asset       	str             	YES      	当前资产
        amount      	Union[float,int]	YES      	数量必须为正数
        targetAsset 	str             	YES      	目标资产
        accountType 	str             	NO       	仅支持MAIN和CARD，如果为空，默认查询主账户MAIN
        '''
        return self.send_request(*self.endpoints.set_asset_convert_transfer, **to_local(locals()))

    # 稳定币自动兑换划转查询 (USER_DATA)
    def get_asset_convert_transfer_queryByPage(self, tranId: int = '', clientTranId: str = '', asset: str = '',
                                               startTime: int = '', endTime: int = '', accountType: str = '',
                                               current: int = '', size: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-18

        Name        	Type	Mandatory	Description
        tranId      	int 	NO       	流水号
        clientTranId	str 	NO       	用户自定义流水号
        asset       	str 	NO       	不传或者空字符串查全部, 匹配扣除币种和目标币种
        startTime   	int 	YES      	开始时间（包含），单位：毫秒
        endTime     	int 	YES      	结束时间（不包含），单位：毫秒
        accountType 	str 	NO       	账户类型: MAIN-主账户。CARD-资金账户。如果传入则仅返回对应wallet的记录，不传或者传null则返回该用户spot和card钱包的记录。
        current     	int 	NO       	当前页面，默认1，最小值为1
        size        	int 	NO       	页面大小，默认10，最大值为100
        '''
        return self.send_request(*self.endpoints.get_asset_convert_transfer_queryByPage, **to_local(locals()))

    # 云算力历史记录分页查询 (USER_DATA)
    def get_asset_ledger_transfer_cloud_mining_queryByPage(self, tranId: int = '', clientTranId: str = '',
                                                           asset: str = '', startTime: int = '', endTime: int = '',
                                                           current: int = '', size: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-19

        Name        	Type	Mandatory	Description
        tranId      	int 	NO       	流水号
        clientTranId	str 	NO       	外部唯一流水号
        asset       	str 	NO       	不传或者空字符串查全部
        startTime   	int 	YES      	开始时间（包含），单位：毫秒
        endTime     	int 	YES      	结束时间（不包含），单位：毫秒
        current     	int 	NO       	当前页面，默认1，最小值为1
        size        	int 	NO       	页面大小，默认10，最大值为100
        '''
        return self.send_request(*self.endpoints.get_asset_ledger_transfer_cloud_mining_queryByPage, **to_local(locals()))

    # 查询用户API Key权限 (USER_DATA)
    def get_account_apiRestrictions(self, recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#api-key-user_data

        Name      	Type	Mandatory	Description
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_account_apiRestrictions, **to_local(locals()))
