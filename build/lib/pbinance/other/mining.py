from finance_utils.component.local import to_local
from pbinance.client import Client
from typing import Union


# 矿池
class _MiningEndpoints():
    get_pub_algoList = ['https://api.binance.com/','GET', '/sapi/v1/mining/pub/algoList', True]  # 获取算法(MARKET_DATA)
    get_pub_coinList = ['https://api.binance.com/','GET', '/sapi/v1/mining/pub/coinList', True]  # 获取币种(MARKET_DATA)
    get_worker_detail = ['https://api.binance.com/','GET', '/sapi/v1/mining/worker/detail', True]  # 请求矿工列表明细 (USER_DATA)
    get_worker_list = ['https://api.binance.com/','GET', '/sapi/v1/mining/worker/list', True]  # 请求矿工列表 (USER_DATA)
    get_payment_list = ['https://api.binance.com/','GET', '/sapi/v1/mining/payment/list', True]  # 收益列表 (USER_DATA)
    get_payment_other = ['https://api.binance.com/','GET', '/sapi/v1/mining/payment/other', True]  # 其他收益列表 (USER_DATA)
    get_hash_transfer_config_details = ['https://api.binance.com/','GET', '/sapi/v1/mining/hash-transfer/config/details', True]  # 算力转让详情列表 (USER_DATA)
    get_hash_transfer_config_details_list = ['https://api.binance.com/','GET', '/sapi/v1/mining/hash-transfer/config/details/list', True]  # 算力转让列表 (USER_DATA)
    get_hash_transfer_profit_details = ['https://api.binance.com/','GET', '/sapi/v1/mining/hash-transfer/profit/details', True]  # 算力转让详情 (USER_DATA)
    set_hash_transfer_config = ['https://api.binance.com/','POST', '/sapi/v1/mining/hash-transfer/config', True]  # 算力转让请求 (USER_DATA)
    set_hash_transfer_config_cancel = ['https://api.binance.com/','POST', '/sapi/v1/mining/hash-transfer/config/cancel', True]  # 取消算力转让设置 (USER_DATA)
    get_statistics_user_status = ['https://api.binance.com/','GET', '/sapi/v1/mining/statistics/user/status', True]  # 统计列表 (USER_DATA)
    get_statistics_user_list = ['https://api.binance.com/','GET', '/sapi/v1/mining/statistics/user/list', True]  # 账号列表 (USER_DATA)
    get_payment_uid = ['https://api.binance.com/','GET', '/sapi/v1/mining/payment/uid', True]  # 矿池账户收益列表 (USER_DATA)


class Mining(Client):
    endpoints = _MiningEndpoints

    # 获取算法(MARKET_DATA)
    def get_pub_algoList(self):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#market_data-7
        '''
        return self.send_request(*self.endpoints.get_pub_algoList, **to_local(locals()))

    # 获取币种(MARKET_DATA)
    def get_pub_coinList(self):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#market_data-8
        '''
        return self.send_request(*self.endpoints.get_pub_coinList, **to_local(locals()))

    # 请求矿工列表明细 (USER_DATA)
    def get_worker_detail(self, algo: str = '', userName: str = '', workerName: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-64

        Name      	Type	Mandatory	Description
        algo      	str 	YES
        userName  	str 	YES
        workerName	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_worker_detail, **to_local(locals()))

    # 请求矿工列表 (USER_DATA)
    def get_worker_list(self, algo: str = '', userName: str = '', pageIndex: int = '', sort: int = '',
                        sortColumn: int = '',
                        workerStatus: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-65

        Name        	Type	Mandatory	Description
        algo        	str 	YES
        userName    	str 	YES
        pageIndex   	int 	NO       	页码，为空默认第一页，从1开始
        sort        	int 	NO       	排序方向(为空默认为0): 0 正序，1 倒序
        sortColumn  	int 	NO
        workerStatus	int 	NO       	矿机状态(默认为0)：0 全部，1 有效， 2 无效， 3 失效
        recvWindow  	int 	NO
        '''
        return self.send_request(*self.endpoints.get_worker_list, **to_local(locals()))

    # 收益列表 (USER_DATA)
    def get_payment_list(self, algo: str = '', userName: str = '', coin: str = '', startDate: int = '',
                         endDate: int = '',
                         pageIndex: int = '', pageSize: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-66

        Name      	Type	Mandatory	Description
        algo      	str 	YES
        userName  	str 	YES
        coin      	str 	NO       	币种名称
        startDate 	int 	NO       	搜索日期 毫秒时间戳，同时为空查询所有
        endDate   	int 	NO       	搜索日期 毫秒时间戳，同时为空查询所有
        pageIndex 	int 	NO       	页码，为空默认第一页，从1开始
        pageSize  	int 	NO       	分页数量,最小10,最大200
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_payment_list, **to_local(locals()))

    # 其他收益列表 (USER_DATA)
    def get_payment_other(self, algo: str = '', userName: str = '', coin: str = '', startDate: int = '',
                          endDate: int = '',
                          pageIndex: int = '', pageSize: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-67

        Name      	Type	Mandatory	Description
        algo      	str 	YES
        userName  	str 	YES
        coin      	str 	NO       	币种名称
        startDate 	int 	NO       	搜索日期 毫秒时间戳，同时为空查询所有
        endDate   	int 	NO       	搜索日期 毫秒时间戳，同时为空查询所有
        pageIndex 	int 	NO       	页码，为空默认第一页，从1开始
        pageSize  	int 	NO       	分页数量,最小10,最大200
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_payment_other, **to_local(locals()))

    # 算力转让详情列表 (USER_DATA)
    def get_hash_transfer_config_details(self, pageIndex: int = '', pageSize: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-68

        Name      	Type	Mandatory	Description
        pageIndex 	int 	NO       	页码，为空默认第一页，从1开始
        pageSize  	int 	NO       	分页数量,最小10,最大200
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_hash_transfer_config_details, **to_local(locals()))

    # 算力转让列表 (USER_DATA)
    def get_hash_transfer_config_details_list(self, pageIndex: int = '', pageSize: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-69

        Name      	Type	Mandatory	Description
        pageIndex 	int 	NO       	页码，为空默认第一页，从1开始
        pageSize  	int 	NO       	分页数量,最小10,最大200
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_hash_transfer_config_details_list, **to_local(locals()))

    # 算力转让详情 (USER_DATA)
    def get_hash_transfer_profit_details(self, configId: int = '', pageIndex: int = '', pageSize: int = '',
                                         recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-70

        Name      	Type	Mandatory	Description
        configId  	int 	YES
        pageIndex 	int 	NO       	页码，为空默认第一页，从1开始
        pageSize  	int 	NO       	分页数量,最小10,最大200
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_hash_transfer_profit_details, **to_local(locals()))

    # 算力转让请求 (USER_DATA)
    def set_hash_transfer_config(self, userName: str = '', algo: str = '', endDate: int = '', startDate: int = '',
                                 toPoolUser: str = '', hashRate: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-71

        Name      	Type	Mandatory	Description
        userName  	str 	YES
        algo      	str 	YES
        endDate   	int 	YES
        startDate 	int 	YES
        toPoolUser	str 	YES
        hashRate  	int 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_hash_transfer_config, **to_local(locals()))

    # 取消算力转让设置 (USER_DATA)
    def set_hash_transfer_config_cancel(self, configId: int = '', userName: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-72

        Name      	Type	Mandatory	Description
        configId  	int 	YES
        userName  	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.set_hash_transfer_config_cancel, **to_local(locals()))

    # 统计列表 (USER_DATA)
    def get_statistics_user_status(self, algo: str = '', userName: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-73

        Name      	Type	Mandatory	Description
        algo      	str 	YES
        userName  	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_statistics_user_status, **to_local(locals()))

    # 账号列表 (USER_DATA)
    def get_statistics_user_list(self, algo: str = '', userName: str = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-74

        Name      	Type	Mandatory	Description
        algo      	str 	YES
        userName  	str 	YES
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_statistics_user_list, **to_local(locals()))

    # 矿池账户收益列表 (USER_DATA)
    def get_payment_uid(self, algo: str = '', startDate: int = '', endDate: int = '', pageIndex: int = '',
                        pageSize: int = '', recvWindow: int = ''):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-75

        Name      	Type	Mandatory	Description
        algo      	str 	YES
        startDate 	int 	NO       	搜索日期 毫秒时间戳，同时为空查询所有
        endDate   	int 	NO       	搜索日期 毫秒时间戳，同时为空查询所有
        pageIndex 	int 	NO       	页码，为空默认第一页，从1开始
        pageSize  	int 	NO       	分页数量,最小10,最大200
        recvWindow	int 	NO
        '''
        return self.send_request(*self.endpoints.get_payment_uid, **to_local(locals()))
