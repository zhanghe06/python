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
    print time.strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(80)


def run():
    # schedule.every(10).minutes.do(job)
    # schedule.every().hour.do(job)
    # schedule.every().day.at("10:30").do(job)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(job)
    schedule.every().day.at("15:14").do(job)
    schedule.every().day.at("15:15").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    run()

"""
$ pip install schedule

python 版本的定时调度

注意：
schedule.every().hour.do(job)
调度器开始工作后1个小时开始执行 job

测试执行顺序
设置任务处理时间超过调度间隔：
schedule.every().day.at("15:14").do(job)
schedule.every().day.at("15:15").do(job)
结果：
I'm working...
2017-04-13 15:14:00
I'm working...
2017-04-13 15:15:21
可以看出schedule任务调度是顺序执行，不是并行
"""
