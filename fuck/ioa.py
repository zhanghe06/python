#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: ioa.py
@time: 2018-01-02 19:55
"""


from __future__ import unicode_literals
from __future__ import print_function

import json
import time
import requests
from base64 import b64decode
from requests.auth import HTTPBasicAuth


REQUESTS_TIME_OUT = (30, 30)


s = requests.session()


class IoaClient(object):
    """
    爱办公打卡神器（接口参数未校验，此漏洞可利用）

    方式一（每次都要登录）:
    ioa_client = IoaClient(
        username='13800000000',
        password='123456',
    )
    ioa_client.check_security_token()

    方式二（token校验通过免登陆）:
    ioa_client = IoaClient(
        username='13800000000',
        password='123456',
        security_token='MTM4MTg3MzI1OTNAYWNjb3VudGxvZ2luODY6MTUxNzU3MTU0Njg1ODpiOWJhYWJmNWMzZmZmZDhmMjZiYzFmMWU5MDc4MzdmOA',
        staff_id='e9490f62c45d45278ffac841a6d892b8',  # 员工编号
        org_id='40b30cfa9f2145b1810e02f953a5b27b',    # 组织编号
    )
    ioa_client.check_security_token()
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153',
        'Host': 'i.ioa.cn',
        'Origin': 'http://i.ioa.cn',
        'Accept-Language': 'zh-cn',
        'Content-Type': 'application/json;charset=UTF-8',
    }

    auth_username = 'usermobile'
    auth_password = 't8kevs1CpGwHB6v8'

    # 上海办公室坐标
    longitude = '121.516476'            # 经度
    latitude = '31.311131'              # 纬度
    place = '上海市 杨浦区 三门路36号'    # 地址(百度坐标有偏移)

    login_status = False

    def __init__(self, username, password, security_token=None, staff_id=None, org_id=None):
        self.username = username
        self.password = password
        self.security_token = security_token
        self.staff_id = staff_id
        self.org_id = org_id

        if (security_token or staff_id or org_id) and not (security_token and staff_id and org_id):
            raise Exception('缺少参数'.encode('utf-8'))

    def check_security_token(self):
        """
        校验 security_token 是否过期
        :return:
        """
        if not self.security_token:
            return False
        security_token_str = b64decode(self.security_token + '=' * (-len(self.security_token) % 4))
        print(security_token_str)
        security_token_arr = security_token_str.split(':')
        expiration_time = security_token_arr[1]
        status = expiration_time > time.time()*1000
        print('check_security_token: %s' % status)
        return status

    def login(self):
        url = 'https://i.ioa.cn/rs/m/security/login'
        payload = {
            "username": self.username,
            "password": self.password,
            "phoneZone": "86",
            "accessSource": "ios"
        }
        request_headers = self.headers.copy()
        base_auth = HTTPBasicAuth(self.auth_username, self.auth_password)
        res = s.post(url, json=payload, auth=base_auth, headers=request_headers, timeout=REQUESTS_TIME_OUT)
        if res.status_code == 200:
            data = res.json()
            print(json.dumps(data, indent=4, ensure_ascii=False))
            if data['resultCode'] != "0000":
                # 登录失败
                print(data['msg'])
                return False

            self.staff_id = data['data']['attributes']['staffId']
            self.org_id = data['data']['attributes']['orgId']
            self.security_token = data['data']['attributes']['securityToken']
            self.login_status = True
            return True
        else:
            print(res.status_code)
            print(res.content)
            return False

    def fuck(self):
        """
        打卡

        正确结果:
        {
            "resultCode": "0000",
            "data": {
                "clockHistoryId": "b9bfa5c3e24a4a9f8b1407851f842c7b",
                "primaryOrgId": "40b30cfa9f2145b1810e02f953a5b27b",
                "staffId": "d91d9f3fbc9744848894308e72cb6f4b",
                "clockDate": 1514895802029,
                "clockTime": "20:23",
                "clockType": 1,
                "remark": null,
                "longitude": "121.516476",
                "latitude": "31.311131",
                "place": "上海市 杨浦区 三门路36号",
                "signType": 0,
                "createTime": 1514895802088,
                "attIds": null,
                "caseId": null
            },
            "msg": null
        }

        错误结果:
        {
            "msg": "服务异常",
            "resultCode": "1111",
            "data": null
        }
        :return:
        """
        if not self.login_status and not self.check_security_token():
            self.login()
        url = 'http://i.ioa.cn/hr/h/clockJsonController/addClockHistory'

        request_headers = self.headers.copy()
        request_headers['securityToken'] = self.security_token

        payload = {
            "longitude": self.longitude,    # 经度
            "latitude": self.latitude,      # 纬度
            "place": self.place,            # 地址
            "clockType": 1,
            "signType": 0,
            "staffId": self.staff_id,       # 员工编号
            "primaryOrgId": self.org_id     # 组织编号
        }
        res = s.post(url, json=payload, headers=request_headers, timeout=REQUESTS_TIME_OUT)
        print(res.status_code)
        print(json.dumps(res.json(), indent=4, ensure_ascii=False))


if __name__ == '__main__':
    # 打卡
    ioa_client = IoaClient(
        username='13800000000',
        password='123456',
    )
    ioa_client.fuck()
