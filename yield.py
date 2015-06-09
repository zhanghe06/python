# encoding: utf-8
__author__ = 'zhanghe'

import time
import requests
import re

root_url = 'http://www.ycit.cn/'  # 爬虫入口
web_host = 'http://www.ycit.cn/'
web_domain = 'ycit.cn'
url_list = [root_url]  # 爬虫待访问url列表
url_visited_list = []  # 爬虫已访问url列表


def url_join(url_str, host):
    """
    url拼接
    :param url_str:
    :param host:
    :return:
    """
    if url_str is not None:
        if url_str.startswith(host) or url_str.startswith('http://'):
            return url_str
        return host.rstrip('/') + '/' + url_str.lstrip('/')


def url_filter(url_str, domain):
    """
    过滤其它域名
    :param url_str:
    :param domain:
    :return:
    """
    if url_str is not None:
        if domain in url_str:
            return url_str


def routine(func):
    def ret():
        f = func()
        f.next()
        return f
    return ret


@routine
def hit():
    while 1:
        url_node = (yield)
        if url_node is None:
            print '待抓取列表为空'
        response = requests.get(url_node)
        html = response.text
        reg = '<a .*?href="(.+?)".*?>'
        tags = re.compile(reg, re.I).findall(html)
        for tag in tags:
            if tag != '#' and tag is not None:  # 过滤掉错误地址
                url = url_filter(url_join(tag, web_host), web_domain)
                if url is not None and url not in url_list and url not in url_visited_list:  # 去重
                    url_list.append(url.rstrip('/'))
        # print "访问 %s" % url_node
        print "待访问节点：%s" % len(url_list)
        url_visited_list.append(url_node)
        print "已访问节点：%s" % len(url_visited_list)
        end_time = time.time()
        print "耗时：%0.2f S" % (end_time - start_time)
        print '--------------'


def get():
    c = hit()
    while len(url_list) > 0:
        c.send(url_list.pop(0))


if __name__ == "__main__":
    start_time = time.time()
    get()