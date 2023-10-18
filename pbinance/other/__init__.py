'''
其他接口
https://binance-docs.github.io/apidocs/spot/cn/#185368440e
'''
from .sub_account import SubAccount  # 子母账户
from .savings import Savings  # 币安宝
from .staking import Staking  # Staking
from .mining import Mining  # 矿池
from .futures import Future  # 合约
from .futures_algo import FuturesAlgo  # 合约策略交易
from .blvt import Blvt  # 杠杆代币
from .bs_wap import Bswap  # 币安挖矿
from .fiat import Fiat  # 法币
from .c2c import C2c  # C2C
from .vip_loans import VIPLoans  # VIP借币
from .crypto_loans import CryptoLoans  # 质押借币
from .pay import Pay  # Pay
from .convert import Convert  # 闪兑
from .rebate import Rebate  # 返佣
from .nft import Nft  # NFT
from .giftcard import GiftCard  # 币安码


class Other():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.subAccount = SubAccount(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.savings = Savings(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.staking = Staking(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.mining = Mining(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.future = Future(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.futuresAlgo = FuturesAlgo(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.blvt = Blvt(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.bswap = Bswap(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.fiat = Fiat(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.c2c = C2c(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.vipLoans = VIPLoans(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.cryptoLoans = CryptoLoans(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.pay = Pay(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.convert = Convert(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.rebate = Rebate(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.nft = Nft(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.giftCard = GiftCard(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
