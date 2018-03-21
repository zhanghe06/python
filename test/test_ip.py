#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_ip.py
@time: 2018-02-08 18:53
"""


import netaddr


def check_allocation_pools(allocation_pools):
    print(allocation_pools)
    # 开始IP 必须小于 结束IP 校验可用IP数量
    for ip_pool in allocation_pools:
        print(ip_pool)
        ip_start = netaddr.IPAddress(ip_pool['start']).__int__()
        ip_end = netaddr.IPAddress(ip_pool['end']).__int__()
        print(ip_start)
        print(ip_end)
        print(ip_end - ip_start)
        if ip_start > ip_end or (ip_end - ip_start) < 2:
            print('error')
    print('-'*20)


if __name__ == '__main__':
    allocation_pools_f = [{'start': '192.168.0.1', 'end': '192.168.0.2'}]
    allocation_pools_t = [{'start': '192.168.0.1', 'end': '192.168.0.20'}]
    check_allocation_pools(allocation_pools_f)
    check_allocation_pools(allocation_pools_t)
