#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: hongbaodaren.py
@time: 2018-03-20 16:52
"""

from __future__ import print_function
from __future__ import unicode_literals

import time
import requests
import json


REQUESTS_TIME_OUT = (30, 30)


def _get_tc():
    tc = str('%13d' % (time.time() * 1000))
    return tc


s = requests.session()


headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D100 Safari/604.1',
    'X-Requested-With': 'XMLHttpRequest',
}

url = 'http://m.hongbaodaren.com/ajax/task/GetOnLineTask'
params = {
    'type': 'currenttask',
    'timmetamp': _get_tc(),
}

cookies = {
    # 'token': 'AD7932D8E813DA170E1B4C5F8759EAF5CF9A020119A2274678FBE3064B8B2B75BCFB5DD695C710F77E368E704CB6B717B3A6C51D09E2E84CB66C2AAF4E37CCB5CA43945271F0249BCED26A688047456171311700CC485A9583FFD8C1C58EAAAB6983D631C11885C0EA9FA637D2421B4D',
    'token': 'AD7932D8E813DA17D44ACD3676AD96E6F6AF4B3E456340CE6415B923898C2C74ABC5E18A4C010786C118021CB36638F91F1ACDCC68A532AE53E6B627182405A29938FCCA6340BB0A5887A846E90A8A27B86AB79D559AF635F9C9AE1166EA39167B0604EEB66D221F42317BF1842664DE',
}

request_headers = headers.copy()
request_headers['Host'] = 'm.hongbaodaren.com'
request_headers['Referer'] = 'http://m.hongbaodaren.com/tasklist'

request_cookie = cookies.copy()

res = s.get(
    url,
    params=params,
    headers=request_headers,
    cookies=request_cookie,
    timeout=REQUESTS_TIME_OUT,
)

print(res.url)
print(res.status_code)
result = res.json()
print(json.dumps(result, indent=4, ensure_ascii=False))
