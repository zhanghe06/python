#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_file.py
@time: 16-1-9 上午11:24
"""

import os
import os.path

root_dir = '/tmp'  # 指明被遍历的文件夹

for dir_parent, dir_names, file_names in os.walk(root_dir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for dir_name in dir_names:  # 输出文件夹信息
        print "dir_parent is:" + dir_parent
        print "dir_name is" + dir_name

    for file_name in file_names:  # 输出文件信息
        print "dir_parent is:" + dir_parent
        print "file_name is:" + file_name
        print "the full name of the file is:" + os.path.join(dir_parent, file_name)  # 输出文件路径信息

# 获取指定目录下的所有文件和目录名，列表形式
print os.listdir(root_dir)

root_dir = '/tmp'
for file_name in [item for item in os.listdir(root_dir) if item.startswith('resume-') and item.endswith('.html')]:
    file_path = os.path.join(root_dir, file_name)
    print file_path
    with open(file_path, 'rb') as f:
        html = f.read().decode('utf-8')
        print html


if __name__ == '__main__':
    pass
