from pbinance import Binance, UM
from pprint import pprint

if __name__ == '__main__':
    # 实例化UM模块
    um = UM(key='****', secret='****')  # 等同于：um = Binance( key='****', secret='****').um
    # 查询持仓模式
    result = um.accountTrade.get_positionSide_dual()
    pprint(result)
