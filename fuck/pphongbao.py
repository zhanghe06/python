#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: pphongbao.py
@time: 2018-03-20 17:45
"""

from __future__ import print_function
from __future__ import unicode_literals

import time
import requests
import json
from scrapy.selector import Selector

REQUESTS_TIME_OUT = (30, 30)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D100 Safari/604.1',
    'X-Requested-With': 'XMLHttpRequest',
}


class PPHB(object):
    def __init__(self, session_id):
        self.s = requests.session()
        self.cookies = {
            'PHPSESSID': session_id,
            '_cb': '1',
            'Hm_lpvt_e91800291a5741f043ef7d78a2580f0b': '1521613708',
            'Hm_lvt_e91800291a5741f043ef7d78a2580f0b': '1521604913,1521604974,1521605859,1521606583',
            'ppport': '10091',
            'fast_s_n': '1',
            'USERINFO': '3lHu6GDZT3cLDA90NDk6wFbDzb3dvkj%2F6UQII%2FN1RVHlRLwrFP2dI3EfT6SFOsq4wPuZmI3CW%2BysJrCMJs4qzVwQZBwjwlsnA%2FMIOd4DD3yihrOJH4qmNnR7VGBRsh7U7s%2BGkrh%2BLSp7wH%2B8OLlSlY7B17SliI1OTr0igTiH31UVnGmO8iDAfVcZZw%2F0AuzRebb3eKdKGSKvUC3RfnWziJJTTDkqxxOxYViVKkDN66KfLFa4h4Tz1NfQbQizMgY4xRPXyJa%2Fm5Vw3Rl1KkJGhZ%2FBzNISHRQkcOY7e2NN32Q2P6WloGKneQDzJzrJvyq0DNl9eGmZS34%3D',
            '1c6abf7a3ce9f84965344760d015a2ae': '1',
            'scheme': 'com.sport.aerobico',
        }

    @staticmethod
    def _get_tc():
        tc = str('%13d' % (time.time() * 1000))
        return tc

    task_list = []

    def get_list(self):
        url = 'http://pphongbao.com/index.php/fasttask/index'
        params = {}

        request_headers = HEADERS.copy()
        request_headers['Host'] = 'pphongbao.com'
        request_headers['Referer'] = 'http://pphongbao.com/'

        request_cookie = self.cookies.copy()

        res = self.s.get(
            url,
            params=params,
            headers=request_headers,
            cookies=request_cookie,
            timeout=REQUESTS_TIME_OUT,
        )

        print(res.url)
        print(res.status_code)

        self.cookies.update(res.cookies)
        # print(res.content)
        # result = res.json()
        # print(json.dumps(result, indent=4))

        response = Selector(res)

        # 进行中任务
        xpath_list_process = '//ul[@class="type-reserved"]/li[@class!="item-divider pp-flex"]'
        res_list_process = response.xpath(xpath_list_process)

        process_result = []
        for item in res_list_process:
            data_item = {
                'data_index': item.xpath('./@data-index').extract_first(),
                'data_id': item.xpath('./a/@data-id').extract_first(),
                'data_righttime': item.xpath('./a/@data-righttime').extract_first(),
                'data_amount': item.xpath('./a/@data-amount').extract_first(),
                'item_title': item.xpath('.//div[@class="item-title"]/text()').extract_first(default='').lstrip(
                    '搜索: '),
            }
            process_result.append(data_item)
        print('进行中的任务')
        print(json.dumps(process_result, indent=4, ensure_ascii=False))
        # 任务列表
        xpath_list = '//ul[@class="type-fast"]/li[@class!="item-divider pp-flex"]'

        res_list = response.xpath(xpath_list)

        task_result = []
        for item in res_list:
            data_item = {
                'data_index': item.xpath('./@data-index').extract_first(),
                'data_id': item.xpath('./a/@data-id').extract_first(),
                'data_righttime': item.xpath('./a/@data-righttime').extract_first(),
                'data_amount': item.xpath('./a/@data-amount').extract_first(),
                'item_title': item.xpath('.//div[@class="item-title"]/text()').extract_first(default='').lstrip('搜索: '),
            }
            task_result.append(data_item)
        print('新任务')
        print(json.dumps(task_result, indent=4, ensure_ascii=False))
        return task_result

    def start_task(self, task_id):
        url = 'http://pphongbao.com/index.php/fasttask/startTask'

        sign_task = ''
        # TODO

        request_headers = HEADERS.copy()
        request_headers['Host'] = 'pphongbao.com'
        request_headers['Referer'] = 'http://pphongbao.com/'
        request_headers['sign'] = sign_task

        request_cookie = self.cookies.copy()

        form_data = {
            'fast_id':	task_id,
            '_sysversion':	'11.2.6',
            '_mobile':	'15D100',
            '_width':	'320',
            'sign':	sign_task,
        }

        res = self.s.post(
            url,
            data=form_data,
            headers=request_headers,
            cookies=request_cookie,
            timeout=REQUESTS_TIME_OUT,
        )
        print(res.status_code)
        print(res.content)
        self.cookies.update(res.cookies)

    def get_detail(self, task_id):
        url = 'http://pphongbao.com/index.php/fasttask/detail'
        params = {
            'fast_id': task_id,
        }

        request_headers = HEADERS.copy()
        request_headers['Host'] = 'pphongbao.com'
        request_headers['Referer'] = 'http://pphongbao.com/'

        request_cookie = self.cookies.copy()

        res = self.s.get(
            url,
            params=params,
            headers=request_headers,
            cookies=request_cookie,
            timeout=REQUESTS_TIME_OUT,
        )

        print(res.url)
        print(res.status_code)
        print(res.content)

    def gave_up_task(self, task_id):
        url = 'http://pphongbao.com/index.php/fasttask/giveupTask'
        request_headers = HEADERS.copy()
        request_headers['Host'] = 'pphongbao.com'
        request_headers['Referer'] = 'http://pphongbao.com/'

        request_cookie = self.cookies.copy()

        form_data = {
            'fast_id': task_id,
        }

        res = self.s.post(
            url,
            data=form_data,
            headers=request_headers,
            cookies=request_cookie,
            timeout=REQUESTS_TIME_OUT,
        )
        print(res.status_code)
        print(res.content)
        self.cookies.update(res.cookies)

if __name__ == '__main__':
    pphb = PPHB('pg5g7t33ogh0pbvn3n37t54g25')
    task_list = pphb.get_list()
    for i, task_item in enumerate(task_list):
        if i == 0:
            # 第一个是收徒，忽略
            continue
        pphb_task_id = task_item['data_id']
        print(task_item)
        # pphb.start_task(pphb_task_id)
        pphb.get_detail(pphb_task_id)
        # pphb.gave_up_task(pphb_task_id)
        break
