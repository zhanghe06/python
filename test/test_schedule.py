#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_schedule.py
@time: 2016/10/20 下午5:17
"""


import schedule
import time


def job():
    print("I'm working...")


def run():
    schedule.every(10).minutes.do(job)
    schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    run()

"""
$ pip install schedule

python 版本的定时调度
"""
