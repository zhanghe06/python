# encoding: utf-8
__author__ = 'zhanghe'


list_a = ['a', 'b', 'c', 'd', 'e']
list_b = ['a', 'd', 'f', 'g', 'p']

# 交集
print list(set(list_a).intersection(set(list_b)))
print len(set(list_a).intersection(set(list_b)))

# 并集
print list(set(list_a).union(set(list_b)))
print len(set(list_a).union(set(list_b)))

# 差集
print list(set(list_b).difference(set(list_a)))  # list_b中有而list_a中没有的
print len(set(list_b).difference(set(list_a)))


"""
['a', 'd']
2
['a', 'c', 'b', 'e', 'd', 'g', 'f', 'p']
8
['p', 'g', 'f']
3
"""