import hmac
import hashlib
import requests
import urllib.parse as up
import time


def request_retry_wrapper(retry_num=50, retry_delay=0.1):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            for i in range(retry_num - 1):
                result = func(*args, **kwargs)
                if result['code'] == 200:
                    return result
                elif result['code'] in [-1001, -1003, -1004, -1007, -1008, -1016]:
                    time.sleep(retry_delay)
                    continue
                else:
                    return result
            result = func(*args, **kwargs)
            return result

        return wrapper2

    return wrapper1


class Client():
    def __init__(self, key='', secret=''):
        self.key = key
        self.secret = secret
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json;charset=utf-8",
                "User-Agent": "binance-api",
                "X-MBX-APIKEY": key,
            }
        )

    @request_retry_wrapper()
    def send_request(self, api_url, method, path, sign=True, **kwargs):
        params_no_empty = {}
        for key, v in kwargs.items():
            if not (v == '' or v == None):
                params_no_empty[key] = v
        if sign:
            params_no_empty["timestamp"] = int(time.time() * 1000)
            query_string = up.urlencode(params_no_empty, True).replace("%40", "@")
            signature = self._get_sign(query_string)
            params_no_empty["signature"] = signature
        url = up.urljoin(api_url, path)


        response = getattr(self.session, method.lower())(
            url=url,
            params=up.urlencode(params_no_empty, True).replace("%40", "@")
        )
        data = response.json()
        # 如果有code
        if type(data) == dict and 'code' in data.keys():
            result = data
        else:
            result = {
                'code': 200,
                'data': data,
                'msg': '',
            }
        return result

    def _get_sign(self, data):
        m = hmac.new(self.secret.encode("utf-8"), data.encode("utf-8"), hashlib.sha256)
        return m.hexdigest()
