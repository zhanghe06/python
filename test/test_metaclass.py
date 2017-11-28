#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_metaclass.py
@time: 2017/10/26 下午3:49
@desc: 通过编写自定义 ORM 框架, 学习元类
@link: https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820064557c69858840b4c48d2b8411bc2ea9099ba000
"""


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        """
        :param cls: 当前准备创建的类的对象(非实例)
        :param name: 类的名称
        :param bases: 继承的父类集合
        :param attrs: 类的方法集合
        :return:
        """
        print('cls: %s' % cls)
        print('name: %r\nbases: %r\nattrs: %r' % (name, bases, attrs))

        for base in bases:
            print('base.__dict__: %r' % base.__dict__)
            print('base.__dict__.keys(): %r' % base.__dict__.keys())

        # 排除掉对 Model 类的修改
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)  # 创建类
        # 核心部分:
        # 1、动态收集所需类型属性: attrs 中所有 Field 类型的属性
        # 2、动态创建所需类型属性: __table__, __mappings__
        # 3、其它属性和方法保持不变
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        # 除掉类的所有类属性（避免实例的属性缺失, 意外调用类的属性; 实例属性优先级比类属性高，默认调用实例属性）
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name.lower()  # 假设表名和类名一致
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)  # 创建修改后的类


class Model(dict):
    # 指示使用 ModelMetaclass 来定制类, 通过 ModelMetaclass.__new__() 动态创建类
    # 因为只有使用者才能根据表的结构定义出对应的类来, 所有的类都只能动态定义
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

    def delete(self):
        pass

    def find(self):
        pass


def run():
    """
    测试创建用户类
    :return:
    """
    class User(Model):
        """
        User Class
        Python解释器首先在当前类User的定义中查找 __metaclass__，如果没有找到，就继续在父类Model中查找__metaclass__
        """
        id = IntegerField('id')
        name = StringField('username')
        email = StringField('email')
        password = StringField('password')

    print('User.__dict__: %s' % User.__dict__)
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    u.save()


if __name__ == '__main__':
    run()

"""
类就是一组用来描述如何生成一个对象的代码段

type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

这里，type 有一种完全不同的能力，它也能动态的创建类。
type 可以接受一个类的描述作为参数，然后返回一个类。
根据传入参数的不同，同一个函数拥有两种完全不同的用法是一件很傻的事情，但这在Python中是为了保持向后兼容性

元类的本质
1)   拦截类的创建
2)   修改类
3)   返回修改之后的类

“元类就是深度的魔法，99%的用户应该根本不必为此操心。
如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。
那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。”
  —— Python界的领袖 Tim Peters
"""
