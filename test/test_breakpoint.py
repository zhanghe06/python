#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_breakpoint.py
@time: 2017/10/22 下午11:02
"""


class Base(object):
    def __init__(self):
        self.info = 'Base class'
        print '%s init from Base' % self.info

    def show(self):
        print '%s show from Base' % self.info


class Child(Base):
    def __init__(self):
        self.info = 'Child class 01'    # 子类先赋值再初始化父类, 子类其它方法里使用的这个同名变量是父类中赋的值（非期望，未覆盖）
        print '%s init from Child' % self.info
        # Base.__init__(self)           # 普通继承
        super(Child, self).__init__()   # super 继承
        self.info = 'Child class 02'    # 先初始化父类子类再赋值, 子类其它方法里使用的这个同名变量是子类中赋的值

    def show(self):
        print '%s show 01 from Child' % self.info
        super(Child, self).show()
        print '%s show 02 from Child' % self.info


if __name__ == '__main__':
    child = Child()
    child.show()


"""
Child class 01 init from Child
Base class init from Base
Child class 02 show 01 from Child
Child class 02 show from Base
Child class 02 show 02 from Child
"""
