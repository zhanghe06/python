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


"""
# python 打开文件的模式
r 以只读模式打开文件
w  以只写模式打开文件，且先把文件内容清空（truncate the file first）wb 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a   以添加模式打开文件，写文件的时候总是写到文件末尾，用seek也无用。打开的文件也是不能读的
r+  以读写方式打开文件，文件可读可写，可写到文件的任何位置
w+ 和r+不同的是，它会truncate the file first
a+ 和r+不同的是，它只能写到文件末尾

# 文件对象的方法
file.closed        返回true如果文件已被关闭，否则返回false。
file.mode        返回被打开文件的访问模式。
file.name        返回文件的名称。
file.softspace        如果用print输出后，必须跟一个空格符，则返回false。否则返回true。
"""
