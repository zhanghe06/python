# encoding: utf-8
__author__ = 'zhanghe'

from sklearn import svm
clf = svm.SVC()


def learn(x, y):
    """
    学习
    """
    clf.fit(x, y)


def predict(x):
    """
    预测
    """
    result = clf.predict(x)
    return result


def test():
    """
    测试
    """
    x = [[0, 0], [1, 1]]
    y = [0, 1]
    learn(x, y)  # 学习
    test_x = [[2., 2.], [.2, .2]]
    print predict(test_x)  # 预测


if __name__ == '__main__':
    test()  # [1 0]
