# encoding: utf-8
__author__ = 'zhanghe'

import sys
sys.path.append('..')
from tools.url import get_next_url

print get_next_url('http://www.163.com/mail/index.htm', 'http://www.163.com/about.htm')
print get_next_url('http://www.163.com/mail/index.htm', '/about.htm')
print get_next_url('http://www.163.com/mail/index.htm', 'about.htm')