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
    p = re.compile(reg_expression, re.I)  # .*后面跟上? 非贪婪匹配 re.I大小写不敏感
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


def read_file(file_path):
    """
    一次读取全文件
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as f:
        return f.read()


def read_file_each_line(file_path):
    """
    逐行读取文件
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as f:
        for each_line in f:
            yield each_line


def save_file(file_path, text, save_type='w'):
    """
    保存文件
    :param file_path:
    :param text:
    :return:
    """
    with open(file_path, save_type) as f:
        f.write(text)


def replace_file_html(file_path, reg_rule=None):
    """
    html文件内容替换
    :param file_path:
    :param reg_rule:
    示例：
    reg_rule = [
        (r'<a href="http://(.*?).shtml"', '<a href="#"'),
        (r' onClick="analytical((.*?))"', '')
        ]
    :return:
    """
    if not reg_rule:
        reg_rule = []
    content = read_file(file_path)
    for rule in reg_rule:
        content = replace_html(content, rule[0], rule[1])
    save_file(file_path, content)


if __name__ == '__main__':
    test_html = '''<h2>多云</h2>  '''
    print replace_html(test_html)
    print replace_html(test_html, r'<.*?>')
    print strip_html(test_html)
    # read_file_text = read_file('/home/zhanghe/code/php/secoo/app/views/partials/container/floor.volt')
    # print read_file_text
    # save_file('/home/zhanghe/code/php/secoo/app/views/partials/container/floor2.volt', read_file_text)
    reg_rule_html = [
        (r'<a href="http://(.*?)"', '<a href="#"'),
        (r'<a target="_blank" href="http://(.*?)"', '<a target="_blank" href="#"'),
        (r'<a style="width:56px;" href="http://(.*?).shtml"', '<a style="width:56px;" href="#"'),
        (r'(\s*)onClick="analytical((.*?))"', ''),
        # (r'(\n){2,}', '\n'),  # 这种不能去除空格组成的行
        (r'(\n[\s|\r]*\n)', '\n'),  # 贪婪匹配，去除多余换行和无意义空行
        ]
    # test_file_path = '/home/zhanghe/code/php/secoo/app/views/partials/container/slider.volt'
    test_file_path = '/home/zhanghe/code/php/secoo/app/views/partials/head.volt'
    replace_file_html(test_file_path, reg_rule_html)


'''
这个工具可以做为仿站辅助工具
下一步做个获取页面图片的辅助工具配合使用
'''