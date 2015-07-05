# encoding: utf-8
__author__ = 'zhanghe'

import re


def replace_html(input_html, reg_expression=r'', replace_text=''):
    """
    正则替换
    :param input_html:
    :param reg_expression:
    :param replace_text:
    :return:
    """
    p = re.compile(reg_expression)  # .*后面跟上? 非贪婪匹配
    output_html = p.sub(replace_text, input_html)
    return output_html


def strip_html(input_html):
    """
    去除html标签
    :param input_html:
    :return:
    """
    # p = re.compile('<[^>]+>')
    p = re.compile(r'<.*?>')  # .*后面跟上? 非贪婪匹配
    return p.sub("", input_html)


if __name__ == '__main__':
    test_html = '''<h2>多云</h2>  '''
    print replace_html(test_html)
    print replace_html(test_html, r'<.*?>')
    print strip_html(test_html)
