# 分类模块
from pbinance import spot  # 币币
from pbinance import cm_future  # 币本位合约
from pbinance import um_future  # U本位合约
from pbinance import european_options  # 欧式期权
from pbinance import margin  # 币币杠杆
from pbinance import other  # 其他
# 类对象
from pbinance.spot import SPOT
from pbinance.cm_future import CM
from pbinance.um_future import UM
from pbinance.european_options import EO
from pbinance.margin import Margin
from pbinance.other import Other

# 别名
cm = cm_future
um = um_future
eo = european_options


class Binance():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.spot = SPOT(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.cm = CM(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.um = UM(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.eo = EO(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.margin = Margin(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.other = Other(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)


__version__ = '1.0.8'
