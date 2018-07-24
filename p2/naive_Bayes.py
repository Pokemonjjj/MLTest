#!/usr/bin/env python
# encoding: utf-8

"""
@author: jzs
@file: naive_Bayes.py
@time: 2018/6/10 0010 下午 5:30
@description:
"""

from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt

# x1,x2的值域
X = [
    [1, 2, 3],
    ['S', 'M', "L"]
]

# y的值域
Y = [-1, 1]

# 测试用数据集合
T = [(1, 'S', -1),
     (1, 'M', -1),
     (1, 'M', 1),
     (1, 'S', 1),
     (1, 'S', -1),

     (2, 'S', -1),
     (2, 'M', -1),
     (2, 'M', 1),
     (2, 'L', 1),
     (2, 'L', 1),

     (3, 'L', 1),
     (3, 'M', 1),
     (3, 'M', 1),
     (3, 'L', 1),
     (3, 'L', -1)]  # type:list[]

# 训练集合的大小
N = len(T)


def get_py(k=0):
    """
    计算Y=ck的概率的最大似然估计
    :return:
    """
    ss = 0
    for d in T:
        if d[2] == Y[k]:
            ss += 1
    return float(ss) / N


def get_pxy_max_e(j=0, aj=0, k=0):
    """
    计算在Y=ck的条件下X=ajl的概率的最大似然估计
    :param j:
    :param l:
    :param k:
    :return:
    """
    s1 = 0
    s2 = 0
    for d in T:
        if d[j] == aj and d[2] == Y[k]:
            s1 += 1
        if d[2] == Y[k]:
            s2 += 1
    return float(s1) / float(s2)


def get_pxy_bayes_e(j=0, aj=0, k=0):
    """
    计算在Y=ck的条件下X=ajl的概率的最大似然估计
    :param j:
    :param l:
    :param k:
    :return:
    """
    s1 = 0
    s2 = 0
    for d in T:
        if d[j] == aj and d[2] == Y[k]:
            s1 += 1
        if d[2] == Y[k]:
            s2 += 1
    return float(s1) / float(s2)


def naive_bayes_run(x, lamd=0):

    pli = list()
    for k in range(0, len(Y)):
        py = get_py(k)
        pxy = 1
        for j in range(0, len(X)):
            pxy *= get_pxy_max_e(j, x[j], k)
        pli.append(py * pxy)

    return Y[argmax(pli)]


if __name__ == '__main__':
    x = (2, 'S')
    print naive_bayes_run(x)
    pass
