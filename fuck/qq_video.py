#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: qq_video.py
@time: 2018-03-22 16:45
"""


from __future__ import print_function
from __future__ import unicode_literals

import time
import requests


REQUESTS_TIME_OUT = (30, 30)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
}


class QQVideo(object):
    def __init__(self, vid):
        self.vid = vid
        self.s = requests.session()
        self.cookies = {}

    @staticmethod
    def _get_tc():
        tc = str('%10d' % time.time())
        return tc

    def a(self):
        url = 'https://v.qq.com/iframe/preview.html'
        params = {
            'vid': self.vid,
            'width': 500,
            'height': 375,
            'auto': 0,
        }
        request_headers = HEADERS.copy()
        # request_headers['Host'] = 'pphongbao.com'
        # request_headers['Referer'] = 'http://pphongbao.com/'

        request_cookie = self.cookies.copy()
        res = self.s.get(
            url,
            params=params,
            headers=request_headers,
            cookies=request_cookie,
            timeout=REQUESTS_TIME_OUT,
        )
        print(res.status_code)
        print(res.content)

    def getinfo(self):
        url = 'https://h5vv.video.qq.com/getinfo'
        params = {
            'callback': 'tvp_request_getinfo_callback_41129',
            'platform': 11001,
            'charge': 0,
            'otype': 'json',
            'ehost': 'https://v.qq.com',
            'sphls': 0,
            'sb': 1,
            'nocache': 0,
            '_rnd': self._get_tc(),
            'guid': 'a30b9989e977cba7534ae35f968152f2',
            'appVer': 'V2.0Build9496',
            'vids': 'a0566mb7a7o',
            'defaultfmt': 'auto',
            '_qv_rmt': 'y1mmy6reA12797AGf=',
            '_qv_rmt2': 'IpHx2z2m151097kWg=',
            'sdtfrom': 'v1010',
        }

        request_headers = HEADERS.copy()

        request_cookie = self.cookies.copy()
        res = self.s.get(
            url,
            params=params,
            headers=request_headers,
            cookies=request_cookie,
            timeout=REQUESTS_TIME_OUT,
        )
        print(res.status_code)
        print(res.content)

    def b(self):
        url = 'http://ugcydzd.qq.com/a0566mb7a7o.mp4'
        params = {
            'vkey': '4E2E338D054D1168796D7C2DDDC3952E98BADB5E937E196BA7B8C79FAC0E71CEF22B5E67048213A97FC2D8118BE7184AC5782CA935C05B70673C27D581BAAEAA3430E438B434AFE8FFAA9393E9CC18E4A024D19A2578EC6A6FA4379451620F5E116623C6462662C917D8AE186F22B1865D422902AF8E7140',
            'br': 91,
            'platform': 2,
            'fmt': 'auto',
            'level': 0,
            'sdtfrom': 'v1010',
            'guid': 'a30b9989e977cba7534ae35f968152f2',
        }
        request_headers = HEADERS.copy()

        request_cookie = self.cookies.copy()
        res = self.s.get(
            url,
            params=params,
            headers=request_headers,
            cookies=request_cookie,
            timeout=REQUESTS_TIME_OUT,
        )
        print(res.status_code)
        print(res.content)


if __name__ == '__main__':
    video_url = 'https://v.qq.com/iframe/preview.html?vid=a0566mb7a7o&amp;width=500&amp;height=375&amp;auto=0'
    item_vid = 'a0566mb7a7o'
    qq_video = QQVideo(item_vid)
    qq_video.a()
