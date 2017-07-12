#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_blinker.py
@time: 2017/6/6 下午10:48
"""


from blinker import signal

started = signal('round-started')


def each(round):
    print "Round %s!" % round


started.connect(each)


def round_two(round):
    print "This is round two."


started.connect(round_two, sender=2)


for r in range(1, 4):
    started.send(r)


# https://pypi.python.org/pypi/blinker
# http://pythonhosted.org/blinker/
# https://github.com/jek/blinker
