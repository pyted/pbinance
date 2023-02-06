from pbinance import Binance, EO
from pprint import pprint

if __name__ == '__main__':
    # 实例化EO模块
    eo = EO(key='****', secret='****')  # 等同于：eo = Binance( key='****', secret='****').eo
    # 获取交易规则和交易对
    result = eo.market.get_exchangeInfo()
    pprint(result)
