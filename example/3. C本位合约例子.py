from pbinance import Binance, CM
from pprint import pprint

if __name__ == '__main__':
    # 实例化CM模块
    cm = CM(key='****', secret='****')  # 等同于：cm = Binance( key='****', secret='****').cm
    # 查询全部当前挂单
    result = cm.accountTrade.get_openOrders()
    pprint(result)
