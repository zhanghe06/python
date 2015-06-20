# encoding: utf-8
__author__ = 'zhanghe'

import os

# 获取当前脚本的相对路径
print __file__  # /home/zhanghe/code/python/tools/file.py 在当前目录下执行则返回file.py

# 返回文件名
print os.path.basename(__file__)  # file.py

# 返回文件所在目录
print os.path.dirname(__file__)  # /home/zhanghe/code/python/tools

# 连接目录与文件名或目录
print os.path.join('/home/zhanghe/code/python/tools', 'file.py')

# 返回一个路径的目录名和文件名
print os.path.split(__file__)  # ('/home/zhanghe/code/python/tools', 'file.py') 在当前目录下执行则返回('', 'file.py')

# 分离文件名与扩展名
print os.path.splitext('file.py')  # ('file', '.py')

# 检验给出的路径是否真地存在
print os.path.exists('/home/zhanghe/code/python/tools/file.py')  # True

# 获得文件的绝对路径
print os.path.abspath('file.py')  # /home/zhanghe/code/python/tools/file.py

# 输出字符串指示正在使用的平台。如果是window 则用'nt'表示，对于Linux/Unix用户，它是'posix'。
print os.name  # posix

# 获取当前工作目录，即当前Python脚本工作的目录路径。
print os.getcwd()  # /home/zhanghe/code/python/tools

# 获取指定目录下的所有文件和目录名，列表形式
print os.listdir(os.getcwd())

# 删除一个文件
print os.remove('delete.txt')  # 删除成功 返回None，否则报错 OSError: [Errno 2] No such file or directory: 'delete.txt'
