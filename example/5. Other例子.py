from pbinance import Binance, Other
from pprint import pprint

if __name__ == '__main__':
    # 实例化other模块
    other = Other(key='****', secret='****')  # 等同于：other = Binance( key='****', secret='****').other
    # 获取混合保证金调整质押率历史

    result = other.future.get_loan_adjustCollateral_history()
    pprint(result)
