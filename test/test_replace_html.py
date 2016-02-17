#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_replace_html.py
@time: 16-1-20 下午3:08
"""

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


def replace_file_html(content, reg_rule=None):
    """
    html文件内容替换
    :param content:
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
    for rule in reg_rule:
        content = replace_html(content, rule[0], rule[1])
    return content


def test_replace_html():
    """
    批量清理 html 标签
    """
    html = '''<div style=\"min-height: 16px; \"><h3 style=\"margin: 0px; padding: 0px; \"><strong><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">岗位职责：</span><br style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; white-space: normal; widows: auto; background-color: rgb(255, 255, 255);\"/><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">1.负责互联网产品的视觉交互界面设计及图形设计；</span><br style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; white-space: normal; widows: auto; background-color: rgb(255, 255, 255);\"/><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">2.负责为日常运营活动、功能改进及维护提供美术支持；</span><br style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; white-space: normal; widows: auto; background-color: rgb(255, 255, 255);\"/><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">3.负责新产品与新功能提供创意策划并提供用户界面的设计方案；</span><br style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; white-space: normal; widows: auto; background-color: rgb(255, 255, 255);\"/><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">4.参与产品设计优化工作，提出视觉设计优化方案；</span><br style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; white-space: normal; widows: auto; background-color: rgb(255, 255, 255);\"/><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">5.参与用户体验计划，通过研究用户心理、分析数据，改进视觉设计；</span><br style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; white-space: normal; widows: auto; background-color: rgb(255, 255, 255);\"/><br style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; white-space: normal; widows: auto; background-color: rgb(255, 255, 255);\"/><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">任职要求：</span><br style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; white-space: normal; widows: auto; background-color: rgb(255, 255, 255);\"/><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">1.爱生活爱分享，爱设计爱前端，正确的审美和深刻的用户体验认知；</span><br style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; white-space: normal; widows: auto; background-color: rgb(255, 255, 255);\"/><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">2.有扎实的美术功底、良好色彩审美观及优秀的创意设计能力；</span><br style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; white-space: normal; widows: auto; background-color: rgb(255, 255, 255);\"/><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">3.有移动平台/网站相关的界面设计经验；</span><br style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; white-space: normal; widows: auto; background-color: rgb(255, 255, 255);\"/><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">3.熟练使用图像处理或网页制作相关软件；</span><br style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; white-space: normal; widows: auto; background-color: rgb(255, 255, 255);\"/><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">4.能独立完成项目；</span><span style=\"font-family:宋体\"><span style=\"font-size: 14px;\"></span></span></strong></h3><h3 style=\"font-family: 宋体; font-size: 12px; margin: 0px; padding: 0px; \"><br/></h3><p><strong><span style=\"font-family: 微软雅黑; font-size: 14px; line-height: 21px; widows: auto; background-color: rgb(255, 255, 255);\">&nbsp;(请附带近期设计作品)</span></strong></p></div>'''
    reg_rule_html = [
        (r'<[/]*div(.*?)>', ''),
        (r'<[/]*span(.*?)>', ''),
        (r'<[/]*h(.*?)>', ''),
        (r'<[/]*strong(.*?)>', ''),
        (r'<[/]*br(.*?)>', '<br/>'),
        (r'(\n[\s|\r]*\n)', '\n'),  # 贪婪匹配，去除多余换行和无意义空行
        ]
    html = replace_file_html(html, reg_rule_html)
    print html


if __name__ == '__main__':
    test_replace_html()
