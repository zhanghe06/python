# encoding: utf-8
__author__ = 'zhanghe'

from urlparse import urlparse
from urlparse import urlunparse
from urlparse import urljoin


def get_next_url(current_url, next_url):
    """
    组装url
    protocol :// hostname[:port] / path / [;parameters][?query]#fragment
    :param current_url:
    :param next_url:
    :return:
    """
    if next_url is None or next_url == '':
        return ''
    if next_url.startswith('http'):
        return next_url
    if next_url.startswith('/'):
        current_url_parse = urlparse(current_url)
        next_url_parse = urlparse(next_url)
        return urlunparse((current_url_parse.scheme, current_url_parse.netloc, next_url_parse.path, next_url_parse.params, next_url_parse.query, next_url_parse.fragment))
    return urljoin(current_url, next_url)


def test():
    print get_next_url('http://www.163.com/mail/index.htm', 'http://www.163.com/about.htm')
    print urljoin('http://www.163.com/mail/index.htm', 'http://www.163.com/about.htm')
    print '\n',
    print get_next_url('http://www.163.com/mail/index.htm', '/about.htm')
    print urljoin('http://www.163.com/mail/index.htm', '/about.htm')
    print '\n',
    print get_next_url('http://www.163.com/mail/index.htm', 'about.htm')
    print urljoin('http://www.163.com/mail/index.htm', 'about.htm')
    print '\n',
    print get_next_url('http://sh.58.com/banjia/?sort=pingfen', '/banjia/pn2/?sort=pingfen')
    print urljoin('http://sh.58.com/banjia/?sort=pingfen', '/banjia/pn2/?sort=pingfen')


if __name__ == '__main__':
    test()
    test_url = 'http://suining.58.com/zhongdiangong/?sort=pingfen'
    print urlparse(test_url).hostname.rstrip('.58.com')
    print urlparse(test_url).path.strip('/')


"""
以上测试结果可以看出
一个urljoin就搞定了
"""