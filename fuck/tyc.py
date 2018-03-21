#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: tyc.py
@time: 2018-09-20 14:18
"""


from fontTools.ttLib import TTFont
font1 = TTFont('/Users/zhanghe/code/bearing_project/tyc-num.woff')
font1.saveXML('./tyc-num.xml')

cmap=font1['cmap']
cdict=cmap.getBestCmap()
# acs=ord('3')
# print (acs)
print(cdict)
