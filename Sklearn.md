## scikit-learn

安装
```
$ sudo apt-get install build-essential python-dev python-setuptools python-numpy python-scipy libatlas-dev libatlas3gf-base
$ sudo apt-get install python-matplotlib
$ sudo apt-get install python-sklearn
```

最新版安装(推荐)
```
$ cd ~
$ git clone https://github.com/scikit-learn/scikit-learn.git
$ cd scikit-learn/
$ sudo pip install Cython
$ sudo python setup.py install
```

pip方式安装scikit-learn（适用虚拟环境）
```
$ pip install numpy
$ pip install scipy  # 这个安装时间有点长，差点不耐烦了
$ pip install -U scikit-learn
```

pip方式安装matplotlib（安装成功，但是虚拟环境运行没有图像出来）
```
$ sudo apt-get install libpng-dev
$ sudo apt-get install libfreetype6-dev
$ pip install matplotlib
```

Matplotlib的官网地址[http://matplotlib.org/](http://matplotlib.org/)

Matplotlib绘图示例[http://matplotlib.org/1.2.1/examples/index.html](http://matplotlib.org/1.2.1/examples/index.html)

测试
```
$ nosetests -v sklearn
```

参考文档：

官网[http://scikit-learn.org](http://scikit-learn.org)

Support vector machines (SVMs)
[http://scikit-learn.org/stable/modules/svm.html](http://scikit-learn.org/stable/modules/svm.html)


Matplotlib是一个Python的图形框架
[http://matplotlib.org/](http://matplotlib.org/)