# encoding: utf-8
__author__ = 'zhanghe'

import urllib2
from multiprocessing.dummy import Pool as ThreadPool
from tools import time_log

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
    # etc..
    ]


@time_log.time_log
def work(num=2):
    # Make the Pool of workers
    pool = ThreadPool(num)
    # Open the urls in their own threads
    # and return the results
    results = pool.map(urllib2.urlopen, urls)
    # close the pool and wait for the work to finish
    pool.close()
    pool.join()


@time_log.time_log
def work2(num=2):
    p = ThreadPool(num)
    for i in urls:
        p.apply_async(urllib2.urlopen, args=(i,))
    p.close()
    p.join()

if __name__ == '__main__':
    work(1)
    work(2)
    work(4)
    work(8)
    work2(1)
    work2(2)
    work2(4)
    work2(8)

# 测试结果：
# 方法work开始时间：Thu Apr 30 00:26:21 2015
# 方法work结束时间：Thu Apr 30 00:26:46 2015
# 方法work运行时间：25.28S
# 方法work开始时间：Thu Apr 30 00:26:46 2015
# 方法work结束时间：Thu Apr 30 00:27:04 2015
# 方法work运行时间：18.25S
# 方法work开始时间：Thu Apr 30 00:27:04 2015
# 方法work结束时间：Thu Apr 30 00:27:10 2015
# 方法work运行时间：5.47S
# 方法work开始时间：Thu Apr 30 00:27:10 2015
# 方法work结束时间：Thu Apr 30 00:27:15 2015
# 方法work运行时间：5.16S
# 方法work2开始时间：Thu Apr 30 00:33:56 2015
# 方法work2结束时间：Thu Apr 30 00:34:24 2015
# 方法work2运行时间：27.42S
# 方法work2开始时间：Thu Apr 30 00:34:24 2015
# 方法work2结束时间：Thu Apr 30 00:34:35 2015
# 方法work2运行时间：11.62S
# 方法work2开始时间：Thu Apr 30 00:34:35 2015
# 方法work2结束时间：Thu Apr 30 00:34:42 2015
# 方法work2运行时间：6.87S
# 方法work2开始时间：Thu Apr 30 00:34:42 2015
# 方法work2结束时间：Thu Apr 30 00:34:53 2015
# 方法work2运行时间：11.10S