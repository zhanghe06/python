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