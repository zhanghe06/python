#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_cpus.py
@time: 2017/6/15 下午11:29
"""


import multiprocessing

bind = "127.0.0.1:8000"

workers = multiprocessing.cpu_count() * 2 + 1


if __name__ == '__main__':
    print workers
