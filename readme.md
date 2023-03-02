# pbinance 说明文档 v1.0.6

## 1 pbinance设计目的

pbinance是完全基于Python语言对Binance交易所REST API接口的封装，包括：现货、U本位合约、币本位合约、欧式期权等功能。

***本来想起名叫binance_api，但是这个名字被其他人已经申请了，就随手起名叫pbiance了***

之所以花了花几天的时间去写一个Binance交易所的底层Python SDK，有这么几点原因：

- 官方推荐的Python SDK目前主要支持SPOT现货交易
- GITHUB很多的开源框架是对官方API的高级封装，而非底层
- 量化交易有太多的框架，但是各个框架的函数名称调用方式等各不相同，这对于立足多平台的量化交易者有较大的学习成本，而且我个人对于非官方开源的SDK的安全性总抱有一个怀疑的态度（虽然他们写的也很好），也见过很多的的优秀项目停更，所以开发了一套量化交易的生态架构，由于各个交易所底层支持的接口类型和内容大多不相同，如果一个框架一个函数可以支持多个平台难免不能做到交易功能的精细化，但是我尽量让各个交易框架的结构相似、调用相似，这样可以极大的降低学习成本，例如如果你学会了binance_candle，仅需要几分钟的时间就可以上手okx_candle。


## 2 下载pbinance

```cmd
pip install pbinance
```

## 3 pbinance的例子

获取现货交易的挂单信息

```python
from pbinance import Binance
from pprint import pprint

if __name__ == '__main__':
    # 实例化Binance
    # 如果仅获取行情信息不需要key和secret，与账户交易相关的功能需要填写key和secret
    binance = Binance(
        key='****',
        secret='****',
    )
    # spot表示现货 get_ticker_bookTicker获取最优挂单价格
    result = binance.spot.market.get_ticker_bookTicker(
        symbol='BTCUSDT'
    )
    pprint(result)
```

输出：

```text
>> {'code': 200,
>>  'data': {'askPrice': '22886.87000000',
>>           'askQty': '0.05096000',
>>           'bidPrice': '22886.61000000',
>>           'bidQty': '0.00045000',
>>           'symbol': 'BTCUSDT'},
>>  'msg': ''}
```


限价单：以2美元的价格购买5个DOTUSDT

```python
from pbinance import Binance
from pprint import pprint

if __name__ == '__main__':
    # 账户与交易功能必须填写key和secret
    binance = Binance(
        key='****',
        secret='****'

    )
    result = binance.spot.accountTrade.set_order(
        symbol='DOTUSDT',  # 产品名称
        side='BUY',  # 订单方向
        type='LIMIT',  # 订单类型
        price='2',  # 价格
        quantity='5',  # 数量
        timeInForce='GTC',  # 订单的有效方式
    )
    pprint(result)
```

```text
>> {'code': 200,
>>  'data': {'clientOrderId': 'L8lQeRd15657si2u2zg1v6',
>>           'cummulativeQuoteQty': '0.00000000',
>>           'executedQty': '0.00000000',
>>           'fills': [],
>>           'orderId': 3258603953,
>>           'orderListId': -1,
>>           'origQty': '5.00000000',
>>           'price': '2.00000000',
>>           'selfTradePreventionMode': 'NONE',
>>           'side': 'BUY',
>>           'status': 'NEW',
>>           'symbol': 'DOTUSDT',
>>           'timeInForce': 'GTC',
>>           'transactTime': 1675654749477,
>>           'type': 'LIMIT',
>>           'workingTime': 1675654749477},
>>  'msg': ''}
```

关于请求的说明请参考Binance官方文档，或者使用PyTed开源的高级交易架构，可以省去繁琐的官方参数查阅。

## 4 pbinane的说明

请求参数名与官方一致，返回结果均采用字典类型：

- **{'code':<状态码:int>,'data':<主体数据:object>,'msg':<提示信息:str>}**

状态码200表示成功，官方原始的返回结果类型有差异，有的时候仅仅是主体数据内容，有的时候是包括状态码的字典，pbinance对官方的不规整结果做了优化，统一格式字典类型。

pbinance在遇到这些状态码时，会自动延时重试多次，避免由于单次网络问题丢失请求：

- -1001  DISCONNECTED
- -1003 TOO_MANY_REQUESTS
- -1004 SERVER_BUSY
- -1007 TIMEOUT
- -1008 SERVER_BUSY
- -1016 SERVICE_SHUTTING_DOWN

## 5 现货模块 SPOT

### 5.1 接口总览

#### 5.1.1 账户与交易 AccountTrade

|接口名称|函数名称|
|:---|:---|
|测试下单 |set_order_test|
|下单 |set_order|
|撤销订单 |cancel_order|
|撤销单一交易对的所有挂单 |cancel_openOrders|
|撤消挂单再下单 |order_cancelReplace|
|查询订单 |get_order|
|当前挂单 |get_openOrders|
|查询所有订单 |get_allOrders|
|OCO下单|set_order_oco|
|取消 OCO 订单|cancel_orderList|
|查询 OCO |get_orderList|
|查询所有 OCO |get_allOrderList|
|查询 OCO 挂单 |get_openOrderList|
|账户信息 |get_account|
|账户成交历史 |get_myTrades|
|查询目前下单数 |get_rateLimit_order|


#### 5.1.2 行情信息 Market

|接口名称|函数名称|
|:---|:---|
|测试服务器连通性|get_ping|
|获取服务器时间|get_time|
|交易规范信息|get_exchangeInfo|
|深度信息|get_depth|
|近期成交列表|get_trades|
|查询历史成交 |get_historicalTrades|
|近期成交|get_aggTrades|
|K线数据|get_klines|
|当前平均价格|get_avgPrice|
|UIK线数据|get_uiKlines|
|24hr 价格变动情况|get_ticker_24hr|
|最新价格|get_ticker_price|
|当前最优挂单|get_ticker_bookTicker|
|滚动窗口价格变动统计|get_ticker|

#### 5.1.3 统一账户 PortfolioMargin

|接口名称|函数名称|
|:---|:---|
|查询统一账户信息 |portfolio_account|
|统一账户资产质押率 |portfolio_collateralRate|
|查询统一账户穿仓借贷金额 |portfolio_pmLoan|
|偿还统一账户穿仓负债|portfolio_repay|


#### 5.1.4 钱包接口 Wallet


|接口名称|函数名称|
|:---|:---|
|系统状态|get_system_status|
|获取所有币信息 |get_capital_config_getall|
|查询每日资产快照 |get_accountSnapshot|
|关闭站内划转 |set_account_disableFastWithdrawSwitch|
|开启站内划转 |set_account_enableFastWithdrawSwitch|
|提币 |set_capital_withdraw_apply|
|获取充值历史|get_capital_deposit_hisrec|
|获取提币历史 |get_capital_withdraw_history|
|获取充值地址 |get_capital_deposit_address|
|账户状态 |get_account_status|
|账户API交易状态|get_account_apiTradingStatus|
|小额资产转换BNB历史 |get_asset_dribblet|
|获取可以转换成BNB的小额资产 |set_asset_dust_btc|
|小额资产转换 |set_asset_dust|
|资产利息记录 |get_asset_assetDividend|
|上架资产详情 |get_asset_assetDetail|
|交易手续费率查询 |get_asset_tradeFee|
|用户万向划转 |set_set_asset_transfer|
|查询用户万向划转历史 |get_get_asset_transfer|
|资金账户 |set_asset_get_funding_asset|
|用户持仓 |set_asset_getUserAsset|
|稳定币自动兑换划转 |set_asset_convert_transfer|
|稳定币自动兑换划转查询 |get_asset_convert_transfer_queryByPage|
|云算力历史记录分页查询 |get_asset_ledger_transfer_cloud_mining_queryByPage|
|查询用户API Key权限 |get_account_apiRestrictions|

### 5.2 例子

获取BTCUSDT的最新成交价

```python
from pbinance import Binance, SPOT
from pprint import pprint

if __name__ == '__main__':
    # 实例化现货模块
    spot = SPOT(key='****', secret='****')  # 等同于：spot = Binance( key='****', secret='****').spot
    # 获取BTCUSDT的最新成交价
    result = spot.market.get_ticker_price(
        symbol='BTCUSDT'
    )
    pprint(result)
```

输出：

```text
>> {'code': 200,
>>  'data': {'price': '22902.27000000', 'symbol': 'BTCUSDT'},
>>  'msg': ''}
```

## 6 U本位合约模块 UM

### 6.1 接口总览

#### 6.1.1 账户与交易 AccountTrade

|接口名称|函数名称|
|:---|:---|
|更改持仓模式|set_positionSide_dual|
|查询持仓模式|get_positionSide_dual|
|更改联合保证金模式|set_multiAssetsMargin|
|查询联合保证金模式|get_multiAssetsMargin|
|下单 |set_order|
|测试下单接口 |set_order_test|
|批量下单 |set_batchOrders|
|查询订单 |get_order|
|撤销订单 |cancel_order|
|撤销全部订单 |cancel_allOpenOrders|
|批量撤销订单 |cancel_batchOrders|
|倒计时撤销所有订单 |set_countdownCancelAll|
|查询当前挂单 |get_openOrder|
|查看当前全部挂单 |get_openOrders|
|查询所有订单|get_allOrders|
|账户余额V2 |get_balance|
|账户信息V2 |get_account|
|调整开仓杠杆 |set_leverage|
|变换逐全仓模式 |set_marginType|
|调整逐仓保证金 |set_positionMargin|
|逐仓保证金变动历史 |get_positionMargin_history|
|用户持仓风险V2 |get_positionRisk|
|账户成交历史 |get_userTrades|
|获取账户损益资金流水 |get_income|
|杠杆分层标准 |get_leverageBracket|
|持仓ADL队列估算 |get_adlQuantile|
|用户强平单历史 |get_forceOrders|
|合约交易量化规则指标 |get_apiTradingStatus|
|用户手续费率 |get_commissionRate|
|获取合约资金流水下载Id |get_income_asyn|
|通过下载Id获取合约资金流水下载链接 |get_income_asyn_id|

#### 6.1.2 行情信息 Market

|接口名称|函数名称|
|:---|:---|
|测试服务器连通性 PING|get_ping|
|获取服务器时间|get_time|
|获取交易规则和交易对|get_exchangeInfo|
|深度信息|get_depth|
|近期成交|get_trades|
|查询历史成交|get_historicalTrades|
|近期成交|get_aggTrades|
|K线数据|get_klines|
|连续合约K线数据|get_continuousKlines|
|价格指数K线数据|get_indexPriceKlines|
|标记价格K线数据|get_markPriceKlines|
|最新标记价格和资金费率|get_premiumIndex|
|查询资金费率历史|get_fundingRate|
|24hr价格变动情况|get_ticker_24hr|
|最新价格|get_ticker_price|
|当前最优挂单|get_ticker_bookTicker|
|获取未平仓合约数|get_openInterest|
|合约持仓量|get_openInterestHist|
|大户账户数多空比|get_topLongShortAccountRatio|
|大户持仓量多空比|get_topLongShortPositionRatio|
|多空持仓人数比|get_globalLongShortAccountRatio|
|合约主动买卖量|get_takerlongshortRatio|
|杠杆代币历史净值K线|get_lvtKlines|
|综合指数交易对信息|get_indexInfo|
|多资产模式资产汇率指数|get_assetIndex|

#### 6.1.3 统一账户 PortfolioMargin

|接口名称|函数名称|
|:---|:---|
|获取统一账户交易规则|get_pmExchangeInfo|
|查询统一账户账户信息 |get_pmAccountInfo|

### 6.2 例子

查询U本位合约持仓模式

```python
from pbinance import Binance, UM
from pprint import pprint

if __name__ == '__main__':
    # 实例化UM模块
    um = UM(key='****', secret='****')  # 等同于：um = Binance( key='****', secret='****').um
    # 查询持仓模式
    result = um.accountTrade.get_positionSide_dual()
    pprint(result)
```

输出：

```text
>> {'code': 200, 'data': {'dualSidePosition': True}, 'msg': ''}
```



## 7 币本位合约模块 CM

### 7.1 接口总览

#### 7.1.1 账户与交易 AccountTrade

|接口名称|函数名称|
|:---|:---|
|更改持仓模式|set_positionSide_dual|
|查询持仓模式|get_positionSide_dual|
|下单 |set_order|
|测试下单接口 |set_order_test|
|修改订单 |alter_order|
|批量下单 |set_batchOrders|
|批量修改订单 |alter_batchOrders|
|查询订单修改历史 |get_orderAmendment|
|查询订单 |get_order|
|撤销订单 |cancel_order|
|撤销全部订单 |cancel_allOpenOrders|
|批量撤销订单 |cancel_batchOrders|
|倒计时撤销所有订单 |set_countdownCancelAll|
|查询当前挂单 |get_openOrder|
|查看当前全部挂单 |get_openOrders|
|查询所有订单|get_allOrders|
|账户余额 |get_balance|
|账户信息 |get_account|
|调整开仓杠杆 |set_leverage|
|变换逐全仓模式 |set_marginType|
|调整逐仓保证金 |set_positionMargin|
|逐仓保证金变动历史 |get_positionMargin_history|
|用户持仓风险|get_positionRisk|
|账户成交历史 |get_userTrades|
|获取账户损益资金流水|get_income|
|交易对杠杆分层标准 |get_leverageBracket|
|用户强平单历史 |get_forceOrders|
|持仓ADL队列估算 |get_adlQuantile|
|用户手续费率 |get_commissionRate|

#### 7.1.2 行情信息 Market

|接口名称|函数名称|
|:---|:---|
|测试服务器连通性 PING|get_ping|
|获取服务器时间|get_time|
|获取交易规则和交易对|get_exchangeInfo|
|深度信息|get_depth|
|近期成交|get_trades|
|查询历史成交 |get_historicalTrades|
|近期成交|get_aggTrades|
|最新现货指数价格和Mark Price|get_premiumIndex|
|查询永续合约资金费率历史|get_fundingRate|
|K线数据|get_klines|
|连续合约K线数据|get_continuousKlines|
|价格指数K线数据|get_indexPriceKlines|
|标记价格K线数据|get_markPriceKlines|
|24hr价格变动情况|get_ticker_24hr|
|最新价格|get_ticker_price|
|当前最优挂单|get_ticker_bookTicker|
|获取未平仓合约数|get_openInterest|
|合约持仓量|get_openInterestHist|
|大户账户数多空比|get_topLongShortAccountRatio|
|大户持仓量多空比|get_topLongShortPositionRatio|
|多空持仓人数比|get_globalLongShortAccountRatio|
|合约主动买卖量|get_takerBuySellVol|
|基差|get_basis|

#### 7.1.3 统一账户 PortfolioMargin

|接口名称|函数名称|
|:---|:---|
|获取统一账户交易规则|get_pmExchangeInfo|
|查询统一账户账户信息 |get_pmAccountInfo|


### 7.2 例子

查询全部当前挂单

```python
from pbinance import Binance, CM
from pprint import pprint

if __name__ == '__main__':
    # 实例化CM模块
    cm = CM(key='****', secret='****')  # 等同于：cm = Binance( key='****', secret='****').cm
    # 查询全部当前挂单
    result = cm.accountTrade.get_openOrders()
    pprint(result)
```

输出：

```text
>> {'code': 200, 'data': [], 'msg': ''}
```

## 8 欧式期权 EO

### 8.1 接口总览

#### 8.1.1 账户与交易 AccountTrade

|接口名称|函数名称|
|:---|:---|
|账户信息 |get_account|
|资金划转 |set_transfer|
|下单 |set_order|
|批量下单 |set_batchOrders|
|撤销订单 |cancel_order|
|批量撤销订单 |cancel_batchOrders|
|撤销单交易对全部订单 |cancel_allOpenOrders|
|撤销特定标的全部订单 |cancel_allOpenOrdersByUnderlying|
|查询当前挂单 |get_openOrders|
|查询历史订单 |get_historyOrders|
|仓位信息 |get_position|
|账户成交历史 |get_userTrades|
|用户行权历史|get_exerciseRecord|
|获取账户资金流水|get_bill|


#### 8.1.2 行情信息 Market

|接口名称|函数名称|
|:---|:---|
|测试服务器连通性 PING|get_ping|
|获取服务器时间|get_time|
|获取交易规则和交易对|get_exchangeInfo|
|深度信息|get_depth|
|近期成交|get_trades|
|查询历史成交|get_historicalTrades|
|K线数据|get_klines|
|查询期权标记价格|get_mark|
|24hr价格变动情况|get_ticker|
|标的最新价格|get_index|
|历史行权记录|get_exerciseHistory|
|合约持仓量|get_openInterest|


#### 8.1.3 市商 MarketMaker

|接口名称|函数名称|
|:---|:---|
|保证金账户信息|get_marginAccount|
|设置MMP规则|set_mmpSet|
|获取MMP规则|get_mmpSet|
|重置MMP状态|set_mmpReset|
|设置倒计时取消所有订单配置 |set_countdownCancelAll|
|获得倒计时自动取消所有订单配置 |get_countdownCancelAll|
|重置倒计时取消所有订单心跳 |set_countdownCancelAllHeartBeat|

### 8.2 例子

获取交易规则和交易对

```python
from pbinance import Binance, EO
from pprint import pprint

if __name__ == '__main__':
    # 实例化EO模块
    eo = EO(key='****', secret='****')  # 等同于：eo = Binance( key='****', secret='****').eo
    # 获取交易规则和交易对
    result = eo.market.get_exchangeInfo()
    pprint(result)
```

输出：

```text
>> {'code': 200,
>>  'data': {'optionAssets': [{'id': 1, 'name': 'USDT'}],
>>           'optionContracts': [{'baseAsset': 'SOL',
>>                                'id': 1,
>>                                'quoteAsset': 'USDT',
>>                                'settleAsset': 'USDT',
>>                                'underlying': 'SOLUSDT'},
>>                               {'baseAsset': 'BTC',
>>                                'id': 2,
>>                                'quoteAsset': 'USDT',
>>                                'settleAsset': 'USDT',
>>                                'underlying': 'BTCUSDT'},
>>                               {'baseAsset': 'ETH',
>>                                'id': 3,
>>                                'quoteAsset': 'USDT',
>>                                'settleAsset': 'USDT',
>>                                'underlying': 'ETHUSDT'},
>>                               {'baseAsset': 'BNB',
>>                                'id': 4,
>>                                'quoteAsset': 'USDT',
>>                                'settleAsset': 'USDT',
>>                                'underlying': 'BNBUSDT'}],
>>           'optionSymbols': [{'contractId': 3,
>>                              'expiryDate': 1677225600000,
>>                              'filters': [{'filterType': 'PRICE_FILTER',
>>                                           'maxPrice': '923.9',
>>                                           'minPrice': '728.9',
>>                                           'tickSize': '0.1'},
>>                                          {'filterType': 'LOT_SIZE',
>>                                           'maxQty': '1000',
>>                                           'minQty': '0.01',
>>                                           'stepSize': '0.01'}],
>>                              'id': 2474,
>>                              'initialMargin': '0.15000000',
>>                              'maintenanceMargin': '0.07500000',
>>                              'makerFeeRate': '0.00020000',
>>                              'maxQty': '1000',
>>                              'minInitialMargin': '0.10000000',
>>                              'minMaintenanceMargin': '0.05000000',
>>                              'minQty': '0.01',
>>                              'priceScale': 1,
>>                              'quantityScale': 2,
>>                              'quoteAsset': 'USDT',
>>                              'side': 'CALL',
>>                              'strikePrice': '800.00000000',
>>                              'symbol': 'ETH-230224-800-C',
>>                              'takerFeeRate': '0.00020000',
>>                              'underlying': 'ETHUSDT',
>>                              'unit': 1},
>>                              ... ... 
>>                             ],
>>           'rateLimits': [{'interval': 'MINUTE',
>>                           'intervalNum': 1,
>>                           'limit': 400,
>>                           'rateLimitType': 'REQUEST_WEIGHT'},
>>                          {'interval': 'MINUTE',
>>                           'intervalNum': 1,
>>                           'limit': 100,
>>                           'rateLimitType': 'ORDERS'},
>>                          {'interval': 'SECOND',
>>                           'intervalNum': 10,
>>                           'limit': 30,
>>                           'rateLimitType': 'ORDERS'}],
>>           'serverTime': 1675657383732,
>>           'timezone': 'UTC'},
>>  'msg': ''}
```




## 9 其他 Other

### 9.1 接口总览


#### 9.1.1 子母账户 SubAccount

|接口名称|函数名称|
|:---|:---|
|创建虚拟子账户（适用主账户）|set_virtualSubAccount|
|查询子账户列表（适用主账户）|get_list|
|查询子账户现货资金划转历史 |get_transfer_history|
|查询子账户合约资金划转历史 |get_futures_internalTransfer|
|执行子账户合约资金划转 |set_futures_internalTransfer|
|查询子账户资产 |get_assets|
|查询子账户现货资产汇总 |get_spotSummary|
|获取子账户充值地址 |get_capital_deposit_subAddress|
|获取子账户充值记录 |get_capital_deposit_subHisrec|
|查询子账户Margin/Futures状态 |get_status|
|为子账户开通Margin |set_margin_enable|
|查询子账户Margin账户详情 |get_margin_account|
|查询子账户Margin账户汇总 |get_margin_accountSummary|
|为子账户开通Futures |set_futures_enable|
|子账户Futures划转 |set_futures_transfer|
|子账户Margin划转 |set_margin_transfer|
|向共同主账户下的子账户主动划转 |set_transfer_subToSub|
|向主账户主动划转 |set_transfer_subToMaster|
|查询子账户划转历史 |get_transfer_subUserHistory|
|子母账户万能划转 |set_universalTransfer|
|查询子母账户万能划转历史 |get_universalTransfer|
|查询子账户Futures账户详情V2 |get_futures_account|
|查询子账户Futures账户汇总V2 |get_futures_accountSummary|
|查询子账户合约持仓信息V2 |get_futures_positionRisk|
|为子账户开通杠杆代币 |set_blvt_enable|
|为子账户API Key开启/关闭IP白名单 |sert_subAccountApi_ipRestriction|
|为子账户API Key添加IP白名单 |set_subAccountApi_ipRestriction_ipList|
|查询子账户API Key IP白名单 |get_subAccountApi_ipRestriction|
|删除子账户API Key IP白名单 |delete_subAccountApi_ipRestriction_ipList|
|取得子帳戶API key IP三方名單 |get_apiRestrictions_ipRestriction_thirdPartyList|
|为子账户API Key更新IP白名单 |set_subAccountApi_ipRestriction|
|投资人账户为托管子账户充值资产 |set_managed_subaccount_deposit|
|投资人账户查询托管子账户资产 |get_managed_subaccount_asset|
|投资人账户为托管子账户提币资产 |set_managed_subaccount_withdraw|
|查询托管子账户资产快照 |get_managed_subaccount_accountSnapshot|

#### 9.1.2 币安宝 Savings

|接口名称|函数名称|
|:---|:---|
|获取活期产品列表 |get_daily_product_list|
|获取用户当日剩余活期可申购余额 |get_daily_userLeftQuota|
|申购活期产品 |set_daily_purchase|
|获取用户当日活期可赎回余额 |get_daily_userRedemptionQuota|
|赎回活期产品 |set_daily_redeem|
|用户活期产品持仓 |get_daily_token_position|
|查询定期/活动产品列表 |get_project_list|
|申购定期/活动产品 |set_customizedFixed_purchase|
|用户定期/活动持仓 |get_project_position_list|
|币安宝账户信息 |get_union_account|
|获取申购记录 |get_union_purchaseRecord|
|获取赎回记录 |get_union_redemptionRecord|
|获取利息历史 |get_union_interestHistory|
|定期/活动持仓转活期持仓 |set_positionChanged|

#### 9.1.3 Staking产品 Staking

|接口名称|函数名称|
|:---|:---|
|查询Staking产品列表|get_productList|
|申购锁仓产品|set_purchase|
|赎回锁仓产品|set_redeem|
|查看个人持仓|get_position|
|查看Staking历史记录|get_stakingRecord|
|设置自动续期|set_setAutoStaking|
|查询Staking个人剩余额度A|get_personalLeftQuota|


#### 9.1.4 矿池 Mining

|接口名称|函数名称|
|:---|:---|
|获取算法|get_pub_algoList|
|获取币种|get_pub_coinList|
|请求矿工列表明细 |get_worker_detail|
|请求矿工列表 |get_worker_list|
|收益列表 |get_payment_list|
|其他收益列表 |get_payment_other|
|算力转让详情列表 |get_hash_transfer_config_details|
|算力转让列表 |get_hash_transfer_config_details_list|
|算力转让详情 |get_hash_transfer_profit_details|
|算力转让请求 |set_hash_transfer_config|
|取消算力转让设置 |set_hash_transfer_config_cancel|
|统计列表 |get_statistics_user_status|
|账号列表 |get_statistics_user_list|
|矿池账户收益列表 |get_payment_uid|

#### 9.1.5 合约 Future

|接口名称|函数名称|
|:---|:---|
|合约资金划转 |set_transfer|
|获取合约资金划转历史 |get_transfer|
|混合保证金借款历史 |get_loan_borrow_history|
|混合保证金还款历史 |get_loan_repay_history|
|混合保证金钱包V2 |get_loan_wallet|
|混合保证金调整质押率历史 |get_loan_adjustCollateral_history|
|混合保证金强平历史 |get_loan_liquidationHistory|
|混合保证金利息收取历史 |get_loan_interestHistory|

#### 9.1.6 合约策略交易 FuturesAlgo

|接口名称|函数名称|
|:---|:---|
|成交量份额参与算法|set_newOrderVp|
|时间加权平均价格策略|set_newOrderTwap|
|取消策略订单 |delete_order|
|查询当前策略订单挂单 |get_openOrders|
|查询历史策略订单 |get_historicalOrders|
|查询执行子订单 |get_subOrders|

#### 9.1.7 杠杆代币 Blvt

|接口名称|函数名称|
|:---|:---|
|杠杆代币信息 |get_tokenInfo|
|申购代币 |set_subscribe|
|查询申购记录 |get_subscribe_record|
|赎回代币 |set_redeem|
|查询赎回记录 |get_redeem_record|
|查询用户每日申购赎回限额 |get_userLimit|

#### 9.1.8 币安挖矿 Bswap

|接口名称|函数名称|
|:---|:---|
|获取所有流动资金池 |get_pools|
|获取流动资金池具体信息 |get_liquidity|
|添加流动性 |set_liquidityAdd|
|移除流动性 |set_liquidityRemove|
|获取流动性操作记录 |get_liquidityOps|
|获取报价 |get_quote|
|交易 |set_swap|
|获取交易记录 |get_swap|
|获取币对池的配置信息 |get_poolConfigure|
|添加流动性的试算 |get_addLiquidityPreview|
|移除流动性的试算 |get_removeLiquidityPreview|
|查询未领取的奖励数量 |get_unclaimedRewards|
|领取奖励 |set_claimRewards|
|获取已领取奖励记录 |set_claimedHistory|

#### 9.1.9 法币 Fiat

|接口名称|函数名称|
|:---|:---|
|获取法币充值/提现历史记录 |get_orders|
|获取法币支付历史记录 |get_payments|


#### 9.1.10 C2C接口 C2c

|接口名称|函数名称|
|:---|:---|
|获取 C2C 交易历史记录 |get_orderMatch_listUserOrderHistory|


#### 9.1.11 VIP借币 VIPLoans

|接口名称|函数名称|
|:---|:---|
|查询VIP借币借款中订单 |get_ongoing_orders|
|VIP借币还款 |set_repay|
|查询VIP借币还款记录历史 |get_repay_history|

#### 9.1.12 质押借币 CryptoLoans

|接口名称|函数名称|
|:---|:---|
|获取质押借币资金流水 |get_income|
|借币 - 质押借币借贷 |set_borrow|
|借币 - 查询质押借币历史记录 |get_borrow_history|
|借币 - 查询借款中订单列表 |get_ongoing_orders|
|还款 - 质押借币还款 |set_repay|
|还款 - 查询还款记录历史 |get_repay_history|
|调整质押率 - 质押借币调整质押率 |set_adjust_ltv|
|调整质押率 - 查询质押率调整历史 |get_ltv_adjustment_history|
|查询可借币种数据 |get_loanable_data|
|查询抵押币种数据 |get_collateral_data|
|查询抵押币种还款汇率 |get_repay_collateral_rate|
|质押借币自定义补仓质押率 |set_customize_margin_call|

#### 9.1.13 Pay接口 Pay

|接口名称|函数名称|
|:---|:---|
|获取 Pay 交易历史记录 |get_transactions|

#### 9.1.14 闪兑 Convert

|接口名称|函数名称|
|:---|:---|
|查询可交易币对信息 |get_exchangeInfo|
|查询可交易币种精度 |get_assetInfo|
|发送获取报价请求 |set_getQuote|
|接受报价 |set_acceptQuote|
|查询订单状态 |get_orderStatus|
|获取闪兑交易记录 |get_tradeFlow|


#### 9.1.15 返佣 Rebate


|接口名称|函数名称|
|:---|:---|
|获取现货返佣历史记录 |get_taxQuery|


#### 9.1.16 NFT接口 Nft


|接口名称|函数名称|
|:---|:---|
|获取 NFT 资金流水记录 |get_history_transactions|
|获取 NFT 充值记录 |get_history_deposit|
|获取 NFT 提现记录 |get_history_withdraw|
|获取 NFT 资产 |get_user_getAsset|

#### 9.1.17 币安码 GiftCard

|接口名称|函数名称|
|:---|:---|
|创建币安码 |set_createCode|
|兑现币安码 |set_redeemCode|
|验证币安码 |get_verify|
|获取RSA Public Key |get_cryptography_rsa_public_key|
|购买币安码 |set_buyCode|
|获取货币使用限制 |get_buyCode_token_limit|

### 9.2 例子

获取混合保证金调整质押率历史

```python
from pbinance import Binance, Other
from pprint import pprint

if __name__ == '__main__':
    # 实例化other模块
    other = Other(key='****', secret='****')  # 等同于：other = Binance( key='****', secret='****').other
    # 获取混合保证金调整质押率历史

    result = other.future.get_loan_adjustCollateral_history()
    pprint(result)
```

输出：

```text
>> {'code': 200, 'data': {'rows': [], 'total': 0}, 'msg': ''}
```