# encoding: utf-8
"""
循环测试
"""
__author__ = 'zhanghe'

friend_dict = {
    'A_f': 'info_a',
    'B_f': 'info_b',
    'C_f': 'info_c',
    'D_f': 'info_d'
}

group_dict = {
    'A_g': 'info_a',
    'B_g': 'info_b',
    'C_g': 'info_c',
    'D_g': 'info_d'
}


def show_list(dict_info):
    for i in dict_info:
        print i, dict_info[i]

send_type = None
while 1:
    print '\n-------------'
    print '1、发送好友消息'
    print '2、发送群组消息'
    send_type = raw_input("请输入类型: ")
    if send_type == '1':
        show_list(friend_dict)  # 显示好友列表
        raw_input_msg = raw_input("输入好友消息: ")
        print raw_input_msg
        continue
    if send_type == '2':
        show_list(group_dict)  # 显示群组列表
        raw_input_msg = raw_input("输入群组消息: ")
        print raw_input_msg
        continue
