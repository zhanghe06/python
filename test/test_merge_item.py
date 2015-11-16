# encoding: utf-8
"""
测试列表、字典值合并
"""
__author__ = 'zhanghe'


gg = {'1': 'a', '2': 'b', '3': 'c'}

ff = [{'id': "12", 'name': "绩效奖金"}, {'id': "15", 'name': "通讯津贴"}, {'id': "26", 'name': "探亲假"}, {'id': "9", 'name': "员工培训"}]

print ','.join([i for i in gg.values()])

print ','.join([i['name'] for i in ff])

print '第一条；第二条；第三条'.count('；')  # 分号的个数


# 求两个字典的乘积和
dict_a = {'a': 40, 'b': 20}
dict_b = {'a': 30, 'b': 50}
# total = 0
# for x, y in dict_a.items():
#     for p, q in dict_b.items():
#         if x == p:
#             total += y*q
# print total

print sum(y*n for x, y in dict_a.items() for m, n in dict_b.items() if x == m)