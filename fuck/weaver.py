#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: weaver.py
@time: 2019-02-19 17:50
"""

from __future__ import print_function
from __future__ import unicode_literals

import json
import time
import uuid
from urllib import urlencode

import requests

# from future.moves.urllib.parse import urlencode


REQUESTS_TIME_OUT = (30, 30)

s = requests.session()


class WeaverClient(object):
    """
    泛微打卡神器
    """
    headers = {
        'User-Agent': 'E-MobileE-Mobile 6.5.68 (iPhone; iOS 12.1.2; zh_CN)',
        'Host': '120.132.31.218:89',
        'Timezone': 'GMT+8',
        'Accept-Encoding': 'gzip',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
    }

    host = 'http://120.132.31.218:89'
    jession_id = ''
    session_key = ''
    udid = ''
    user_id = ''
    user_key = ''
    sign_status = 'checkin'  # 打卡类型: 默认签到（checkout 签退）

    token = '3eef8a67907788cbd45266ad4921d7d1802b1cd8fd4db00cd55516d8a5b38d13'
    client_user_id = '191e35f7e01b0dacefa'

    # 上海办公室坐标
    longitude = '31.30899441189236,121.5098819986979'  # 纬度,经度
    addr = '上海市杨浦区政立路靠近中航天盛广场'  # 地址

    login_status = False

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.udid = self.get_uuid()

    @staticmethod
    def get_uuid():
        return str(uuid.uuid4()).upper()

    def get_config(self):
        url = '%s/client.do' % self.host
        params = {
            "method": "getconfig",
            "clientver": "6.5.68",
            "clienttype": "iPhone",
            "language": "zh-Hans",
            "country": "CN",
        }
        request_headers = self.headers.copy()
        res = s.get(url, params=params, headers=request_headers, timeout=REQUESTS_TIME_OUT)
        print(res.status_code)
        print(json.dumps(res.json(), indent=4, ensure_ascii=False))
        self.jession_id = res.cookies.get('JESSIONID')

    def login(self):
        """
        登录
        错误消息
        {
            "errorno": "111",
            "error": "错误: 用户名或密码为空(111)"
        }
        """
        self.get_config()

        url = '%s/client.do' % self.host
        params = {
            "method": "login",
            "udid": self.udid,
            "token": self.token,
            "language": "zh-Hans",
            "country": "CN",
            "isneedmoulds": "1",
            "clienttype": "iPhone",
            "clientver": "6.5.68",
            "clientos": "iOS",
            "clientosver": "12.1.2",
            "authcode": "",
            "dynapass": "",
            "tokenpass": "",
            "clientChannelId": "",
            "clientuserid": self.client_user_id,
        }

        url = '?'.join([url, urlencode(params)])
        print(url)
        payload = {
            "loginid": self.username,
            "password": self.password,
            "isFromSunEmobile": 1,
        }
        print(payload)
        request_headers = self.headers.copy()
        request_headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=utf-8'

        res = s.post(url, data=payload, headers=request_headers, timeout=REQUESTS_TIME_OUT)
        if res.status_code == 200:
            data = res.json()
            print(json.dumps(data, indent=4, ensure_ascii=False))
            self.session_key = data['sessionkey']

            # 提取cookies
            self.user_id = res.cookies.get('userid')
            self.user_key = res.cookies.get('userKey')
            self.jession_id = res.cookies.get('JESSIONID')

            if data.get('error'):
                return False

            self.login_status = True
            return True
        else:
            print(res.status_code)
            print(res.content)
            return False

    def get_status(self):
        """
        检查打卡状况
        """
        url = '%s/client.do' % self.host
        params = {
            'method': 'checkin',
            'type': 'getStatus',
            'sessionkey': self.session_key,
        }
        request_headers = self.headers.copy()
        res = s.get(url, params=params, headers=request_headers, timeout=REQUESTS_TIME_OUT)
        data = res.json()
        print(json.dumps(data, indent=4, ensure_ascii=False))

    def fuck(self):
        """
        打卡
        正确消息
        {
            "msg": "如因工作原因迟到或早退请提交相应流程，签到（签退）时间：2019-02-19 18:15:28",
            "result": "success"
        }
        错误消息
        {
            "errorno": "005",
            "error": "错误: 当前用户信息无效，请重新登录(005)"
        }
        """
        url = '%s/client.do' % self.host

        request_headers = self.headers.copy()

        current_time = time.strftime("%H%M")
        self.sign_status = 'checkout' if current_time >= '1826' else self.sign_status

        params = {
            "method": "checkin",
            "type": self.sign_status,
            "latlng": self.longitude,  # 纬度,经度
            "addr": self.addr,  # 地址
            "sessionkey": self.session_key,
            "wifiMac": "",
        }

        res = s.get(url, params=params, headers=request_headers, timeout=REQUESTS_TIME_OUT)
        print(res.status_code)
        print(json.dumps(res.json(), indent=4, ensure_ascii=False))


if __name__ == '__main__':
    # 打卡
    weaver_client = WeaverClient(
        username='xxxxxx',
        password='xxxxxx',
    )
    weaver_client.login()
    weaver_client.fuck()
    weaver_client.get_status()
