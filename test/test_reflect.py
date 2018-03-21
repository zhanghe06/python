#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_reflect.py
@time: 2018-07-27 14:07
"""


# 假设有以下结构的包
"""
├── abcd
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── ff.py
│   └── ff.pyc
"""

# ff.py
"""
#!/usr/bin/env python
# encoding: utf-8

class Gg(object):
    def __init__(self):
        pass

    def cc(self):
        return 1
"""

s = 'abcd.ff'


# 方式一
# c = __import__(s)

# print(c)
# print(type(c))
#
# print('')
# print(c.ff.Gg)
# print(getattr(getattr(c, 'ff'), 'Gg'))
# print(c.ff.Gg == getattr(c.ff, 'Gg'))
#
# print('')
# print(c.ff.Gg().cc)
# print(c.ff.Gg().cc())

# 方式二
c = __import__(s, fromlist=True)

print(c)
print(type(c))

print('')
print(c.Gg)
print(getattr(c, 'Gg'))
print(c.Gg == getattr(c, 'Gg'))

print('')
print(c.Gg().cc)
print(c.Gg().cc())


# https://www.cnblogs.com/yyyg/p/5554111.html
