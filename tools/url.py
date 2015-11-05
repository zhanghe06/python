# encoding: utf-8
__author__ = 'zhanghe'

from urlparse import urlparse
from urlparse import urlunparse
from urlparse import urljoin


def get_next_url(current_url, path):
    """
    组装url
    :param current_url:
    :param path:
    :return:
    """
    if path is None or path == '':
        return ''
    if path.startswith('http'):
        return path
    if path.startswith('/'):
        url = urlparse(current_url)
        return urlunparse((url.scheme, url.netloc, path, url.params, url.query, url.fragment))
    return urljoin(current_url, path)


def test():
    print get_next_url('http://www.163.com/mail/index.htm', 'http://www.163.com/about.htm')
    print get_next_url('http://www.163.com/mail/index.htm', '/about.htm')
    print get_next_url('http://www.163.com/mail/index.htm', 'about.htm')


if __name__ == '__main__':
    test()