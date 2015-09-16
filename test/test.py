# coding:utf-8
__author__ = 'zhanghe'

import requests, sys

#for cid in open('/tmp/all.cids.txt'):
for cid in [12345, 354545, 43676, 6767, 7686, 45632, 397320]:
    url = 'http://www.wealink.com/gongsi/shouye/%s/' % cid
    res = requests.get(url)
    res.encoding = 'utf-8'
    if u'<li><label for="shortname">' in res.text:
        print 'error', cid, url
    else:
        pass

