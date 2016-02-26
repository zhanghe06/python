#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_resume.py
@time: 16-2-26 下午5:19
"""


import json


class Base(object):
    """
    数据结构基类
    """
    # 定义构造方法
    def __init__(self, **kwargs):
        # 初始化简历数据
        for key, value in kwargs.iteritems():
            if not hasattr(self, key):
                raise Exception(u'存在不允许的属性')
            self.__setattr__(key, value)

    # 字典方式获取元素
    def __getitem__(self, key):
        return self.__dict__.get(key)

    # 字典方式设置元素
    def __setitem__(self, key, value):
        self.__setattr__(key, value)


class Resume(Base):
    """
    简历基本信息
    """
    def __init__(self, **kwargs):
        # 定义基本属性
        self.intent = ResumeIntent()
        self.edu_list = []
        self.work_list = []
        self.train_list = []
        self.project_list = []
        self.skill_list = []
        self.cert_list = []
        self.opus_list = []
        # 初始化超类
        super(Resume, self).__init__(**kwargs)


class ResumeIntent(Base):
    """
    简历-求职意向
    """
    def __init__(self, **kwargs):
        self.city = []  # 期望城市
        self.duty = []  # 期望职能
        self.industry = []  # 期望行业
        self.salary = ''  # 期望月薪
        # 初始化超类
        super(ResumeIntent, self).__init__(**kwargs)


class ResumeEdu(Base):
    """
    简历-教育经历
    """
    def __init__(self, **kwargs):
        self.school = ''  # 学校
        self.degree = ''  # 学历
        self.major = ''  # 专业
        self.start_date = ''  # 开始日期
        self.end_date = ''  # 结束日期
        # 初始化超类
        super(ResumeEdu, self).__init__(**kwargs)


class ResumeWork(Base):
    """
    简历-工作经验
    """
    def __init__(self, **kwargs):
        self.company = ''  # 公司
        self.industry = ''  # 行业
        self.duty = ''  # 岗位
        self.salary = ''  # 薪资
        self.start_date = ''  # 开始日期
        self.end_date = ''  # 结束日期
        # 初始化超类
        super(ResumeWork, self).__init__(**kwargs)


class ResumeTrain(Base):
    """
    简历-培训经历
    """
    def __init__(self, **kwargs):
        self.name = ''  # 名称
        self.institute = ''  # 机构
        self.content = ''  # 内容
        self.start_date = ''  # 开始日期
        self.end_date = ''  # 结束日期
        # 初始化超类
        super(ResumeTrain, self).__init__(**kwargs)


class ResumeProject(Base):
    """
    简历-项目经验
    """
    def __init__(self, **kwargs):
        self.name = ''  # 名称
        self.content = ''  # 内容
        self.start_date = ''  # 开始日期
        self.end_date = ''  # 结束日期
        # 初始化超类
        super(ResumeProject, self).__init__(**kwargs)


class ResumeSkill(Base):
    """
    简历-职业技能
    """
    def __init__(self, **kwargs):
        self.name = ''  # 名称
        self.grade = ''  # 程度
        self.use_time = ''  # 使用时间
        # 初始化超类
        super(ResumeSkill, self).__init__(**kwargs)


class ResumeCert(Base):
    """
    简历-荣誉证书
    """
    def __init__(self, **kwargs):
        self.name = ''  # 名称
        # 初始化超类
        super(ResumeCert, self).__init__(**kwargs)


class ResumeOpus(Base):
    """
    简历-个人作品
    """
    def __init__(self, **kwargs):
        self.name = ''  # 名称
        self.url = ''  # 链接
        self.type = ''  # 类型
        # 初始化超类
        super(ResumeOpus, self).__init__(**kwargs)


def obj_to_dict(obj):
    """
    :param obj:
    简历对象转字典
    """
    data = {}
    for key, items in obj.__dict__.iteritems():
        if isinstance(items, list):
            for index, item in enumerate(items):
                if isinstance(item, Base):
                    items[index] = item.__dict__
            data[key] = items
        elif isinstance(items, dict):
            data[key] = items
        elif isinstance(items, Base):
            data[key] = items.__dict__
    return data


def test_resume():
    """
    测试简历
    """
    # 实例化简历对象
    resume = Resume()
    print obj_to_dict(resume)

    # 教育经历
    # 方式一
    edu_item = ResumeEdu()
    edu_item.school = u'校园1'
    edu_item.degree = u'本科1'
    edu_item.major = u'软件1'
    edu_item.start_date = u'2016-09-01'
    edu_item.end_date = u'2018-06-21'
    resume.edu_list.append(edu_item)
    # 方式二
    edu_item = ResumeEdu()
    edu_item['school'] = u'校园2'
    edu_item['degree'] = u'本科2'
    edu_item['major'] = u'软件2'
    edu_item['start_date'] = u'2016-09-02'
    edu_item['end_date'] = u'2018-06-22'
    resume.edu_list.append(edu_item)

    # 工作经历
    work_data = {
        'company': u'公司中国',
        'duty': u'清洁',
        'salary': '19000',
        'start_date': '2012-06-02',
        'end_date': '2014-06-05',
    }
    work_item = ResumeWork(**work_data)
    resume.work_list.append(work_item)
    print json.dumps(obj_to_dict(resume), indent=4, ensure_ascii=False)


if __name__ == '__main__':
    test_resume()
