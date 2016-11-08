## pycharm相关设置

### 一、修改头部模板定义

1、设置PyCharm工具的编码格式：
```
File -->> setting -->> File Encodings -->> IDE encoding：utf-8 
```

2、设置Pycharm文件模板：
```
File -->> Setting -->> Editor -->> File and Code Templates -->> Python Script
```

在模块里顶部加入下面语句

```
#!/usr/bin/env python
# encoding: utf-8

"""
@author: ${USER}
@software: ${PRODUCT_NAME}
@file: ${NAME}.py
@time: ${DATE} ${TIME}
"""

def func():
    pass


class Main(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    pass
```



### 二、设置python标准编码风格（PEP8）
```
file -->> setting -->> inspections -->> PEP 8 coding style violation
```



### 三、PyCharm设置显示行号

1、临时设置。
```
右键单击行号处，勾选 Show Line Numbers。
```

2、临时设置。
```
View -->> Active Editor，勾选 Show Line Numbers。
```

3、永久设置。
```
File -->> Settings -->> Editor -->> Appearance ，勾选 Show Line Numbers。
```


### 四、插件安装
```
Preferences -->> Plugins, 搜索，选择，安装
```
