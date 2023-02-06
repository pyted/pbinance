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
    # 获取BTCUSDT的最新成交价
    result = binance.spot.market.get_ticker_price(
        symbol='BTCUSDT'
    )
    pprint(result)
    # 账户与交易功能必须填写key和secret
    # 限价单：以2美元单价购买5个DOTUSDT
    result = binance.spot.accountTrade.set_order(
        symbol='DOTUSDT',  # 产品名称
        side='BUY',  # 订单方向
        type='LIMIT',  # 订单类型
        price='2',  # 价格
        quantity='5',  # 数量
        timeInForce='GTC',  # 订单的有效方式
    )
    pprint(result)

