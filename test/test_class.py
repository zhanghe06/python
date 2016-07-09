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
        self.data = kwargs
        for key, value in kwargs.iteritems():
            if not hasattr(self, key):
                raise Exception(u'存在不允许的属性')
            self.__setattr__(key, value)

    # 字典方式获取元素
    def __getitem__(self, key):
        return self.data.get(key)

    # 字典方式设置元素
    def __setitem__(self, key, value):
        self.data[key] = value


class DetailResume(object):
    """
    简历详细信息
    """
    # 定义基本属性
    edu_list = []   # 教育经历
    work_list = []  # 工作经历
    project_list = []   # 项目经历
    train_list = []     # 培训经历
    cert_list = []      # 证书
    skill_list = []     # 技能

    # 定义构造方法
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            self.__setattr__(key, value)


def test_01():
    print '--------测试 01'
    user_info = {
        'name': 'Tom',
        'age': 20
    }
    # base_resume = BaseResume(name='Tom', age=20)  # 方式一
    base_resume = BaseResume(**user_info)  # 方式二
    print base_resume.name, base_resume['name']
    print base_resume.age, base_resume['age']
    # print base_resume.ff
    print isinstance(base_resume, BaseResume)  # True
    print isinstance(base_resume, DetailResume)  # False


def test_02():
    print '--------测试 02'
    try:
        base_resume = BaseResume(name='Tom', age=20, ff=33)  # 方式一 塞入错误的key
        print base_resume.name
        print base_resume.age
        print base_resume.ff
        print isinstance(base_resume, BaseResume)  # True
        print isinstance(base_resume, DetailResume)  # False
    except Exception, e:
        print e.message


def test_03():
    print '--------测试 03'
    try:
        data = {
            'base': {
                'uid': 100,
                'name': 'Tom',
                'sex': 'M'
            },
            'edu_list': [
                {
                    'school': 'S-ABC',
                    'degree': u'学历1',
                    'major': u'专业1'
                },
                {
                    'school': 'S-DEF',
                    'degree': u'学历2',
                    'major': u'专业2'
                }
            ],
            'work_list': [
                {
                    'company': 'C-DGG',
                    'job': 'J-DGG'
                },
                {
                    'company': 'C-FGG',
                    'job': 'J-FGG'
                },
            ]
        }
        detail_resume = DetailResume(**data)
        print isinstance(detail_resume, DetailResume)
        print type(detail_resume.work_list), detail_resume.work_list
    except Exception, e:
        print e.message


if __name__ == '__main__':
    test_01()
    test_02()
    test_03()


"""
测试结果：
--------测试 01
Tom
20
True
False
--------测试 02
存在不允许的属性
--------测试 03
True
<type 'list'> [{'company': 'C-DGG', 'job': 'J-DGG'}, {'company': 'C-FGG', 'job': 'J-FGG'}]
"""