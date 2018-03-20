#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: qianka.py
@time: 2018-03-20 17:29
"""

from __future__ import print_function
from __future__ import unicode_literals

import time
import requests
import json


REQUESTS_TIME_OUT = (30, 30)


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D100 Safari/604.1',
    'X-Requested-With': 'XMLHttpRequest',
}


class QianKa(object):
    task_process_status = {}

    def __init__(self, sid):
        self.sid = sid
        self.s = requests.session()
        self.cookies = {
            'DIS4': self.sid,
        }
        self.task_id_list = []

    @staticmethod
    def _get_tc():
        tc = str('%13d' % (time.time() * 1000))
        return tc

    def task_list(self):
        url = 'https://qianka.com/s4/lite.subtask.list'
        params = {
            't': self._get_tc(),
        }

        request_headers = HEADERS.copy()
        request_headers['Host'] = 'qianka.com'
        request_headers['Referer'] = 'https://qianka.com/v4/tasks/lite'
        request_headers['X-QK-DIS'] = self.sid

        res = self.s.get(
            url,
            params=params,
            headers=request_headers,
            cookies=self.cookies,
            timeout=REQUESTS_TIME_OUT,
            verify=False,
        )

        print(res.url)
        print(res.status_code)
        result = res.json()
        print(json.dumps(result, indent=4, ensure_ascii=False))
        self.task_id_list = [i['id'] for i in result['payload']['tasks']]

    def task_start(self, task_id):
        url = 'https://qianka.com/s4/lite.subtask.start'

        request_headers = HEADERS.copy()
        request_headers['Host'] = 'qianka.com'
        request_headers['Referer'] = 'https://qianka.com/v4/tasks/lite'
        request_headers['X-QK-DIS'] = self.sid

        params = {
            't': self._get_tc(),
            'task_id': task_id,
            'quality': 0,
        }

        res = self.s.get(
            url,
            params=params,
            headers=request_headers,
            cookies=self.cookies,
            timeout=REQUESTS_TIME_OUT,
            verify=False,
        )

        print(res.url)
        print(res.status_code)
        result = res.json()
        print(json.dumps(result, indent=4, ensure_ascii=False))
        self.task_process_status[task_id] = result['payload']['type']

    def check_task_process_status(self, task_id):
        while 1:
            if task_id not in self.task_process_status:
                self.task_start(task_id)
            elif self.task_process_status[task_id] != 2:
                time.sleep(2)
                self.task_start(task_id)
            else:
                break

    def task_detail(self, task_id):
        url = 'https://qianka.com/s4/lite.subtask.detail'

        params = {
            't': self._get_tc(),
            'task_id': task_id,
        }

        request_headers = HEADERS.copy()
        request_headers['Host'] = 'qianka.com'
        request_headers['Referer'] = 'https://qianka.com/v4/tasks/lite'
        request_headers['X-QK-DIS'] = self.sid

        res = self.s.get(
            url,
            params=params,
            headers=request_headers,
            cookies=self.cookies,
            timeout=REQUESTS_TIME_OUT,
            verify=False,
        )

        print(res.url)
        print(res.status_code)
        result = res.json()
        print(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    qk_client = QianKa(sid='06e1b64ca1244f00a1f394d05714d4c3')
    qk_client.task_list()
    for task_item_id in qk_client.task_id_list:
        qk_client.check_task_process_status(task_item_id)
        qk_client.task_detail(task_item_id)
