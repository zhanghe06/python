#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_class.py
@time: 16-1-9 下午3:54
"""


class BaseResume(object):
    """
    简历基本信息
    USAGE:
    user_info = {
        'name': 'Tom',
        'age': 20
    }
    base_resume = BaseResume(name='Tom', age=20)  # 方式一
    base_resume = BaseResume(**user_info)  # 方式二
    """
    # 定义基本属性
    link = ''  # 简历详情链接
    name = ''  # 姓名
    uid = ''  # 用户ID
    email = ''  # 用户邮箱
    phone = ''  # 用户电话
    apply_id = ''  # 应聘ID
    sex = ''  # 性别
    age = ''  # 年龄
    education = ''  # 学历（教育背景）
    resume_id = ''  # 简历ID
    major_name = ''  # 专业名称
    p_id = ''  # 职位ID
    work_years = ''  # 工作年限
    living_city = ''  # 现居住地

    # 定义构造方法
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            self.__setattr__(key, value)


if __name__ == '__main__':
    user_info = {
        'name': 'Tom',
        'age': 20
    }
    # base_resume = BaseResume(name='Tom', age=20)  # 方式一
    base_resume = BaseResume(**user_info)  # 方式二
    print base_resume.name
    print base_resume.age
