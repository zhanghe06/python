# encoding: utf-8
"""
循环测试
"""
__author__ = 'zhanghe'


import time


friend_dict = {
    # 'QQ号': '姓名',
    'A_f': 'info_a',
    'B_f': 'info_b',
    'C_f': 'info_c',
    'D_f': 'info_d'
}

group_dict = {
    # '群号': '群名',
    'A_g': 'info_a',
    'B_g': 'info_b',
    'C_g': 'info_c',
    'D_g': 'info_d'
}


def show_list(dict_info):
    for key, value in dict_info.iteritems():
        print key, value


def get_msg():
    print '最新消息[%s]' % time.ctime()
    time.sleep(2)


msg_type = None
while 1:
    try:
        if msg_type == '0':  # 接收最新消息
            get_msg()
            continue
        if msg_type == '1':
            show_list(friend_dict)  # 显示好友列表
            raw_input_msg = raw_input("输入好友消息: \n")
            if raw_input_msg == '#':
                msg_type = '#'
            else:
                print raw_input_msg
            continue
        if msg_type == '2':
            show_list(group_dict)  # 显示群组列表
            raw_input_msg = raw_input("输入群组消息: \n")
            if raw_input_msg == '#':
                msg_type = '#'
            else:
                print raw_input_msg
            continue
        if msg_type == 'q':
            print '确认退出（Y）'
            print '取消操作（N）'
            raw_input_msg = raw_input("程序即将退出: \n")
            if raw_input_msg in ['y', 'Y']:
                print '程序已退出'
                break
            else:
                msg_type = ''
                continue
        else:  # ? 直接回车 回到菜单 初始进入 显示帮助
            print '\n-------------'
            print '0、接收最新消息'
            print '1、发送好友消息'
            print '2、发送群组消息'
            print 'q、退出程序'
            msg_type = raw_input('请选择类型: \n')
            continue
    except KeyboardInterrupt:
        print '程序已退出'
        break
