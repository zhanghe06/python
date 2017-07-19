#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_paramiko.py
@time: 2017/6/16 上午9:11
"""

import paramiko

ip = '192.168.64.216'
username = 'zhanghe'
password = '123456'
port = 22
# 设置记录日志
paramiko.util.log_to_file('ssh.log')
# 生成ssh客户端实例
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print "Starting"
s.connect(ip, port, username, password)
stdin, stdout, stderr = s.exec_command('free -m')
print stdout.read()
s.close()

if __name__ == '__main__':
    pass
