#!/usr/bin/env python
# encoding: utf-8

"""
@author: jzs
@file: perceptron.py
@time: 2018/6/5 0005 下午 9:25
@description:
感知器学习算法的原始形式
"""

from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt

# 常量：负实例点的y值
neg_y = -1

# 常量：正实例点的y值
pos_y = 1

# 测试用数据集合DATA_SET = {(x,y)|x∈Rd, y∈{-1，1}}
T = [(array([3, 3]), pos_y),
     (array([4, 3]), pos_y),
     (array([1, 1]), neg_y)]  # type:list[]

# 数据集合的大小
N = len(T)

# 测试用数据x向量的维度
dimension = 2  # type: int

# 权值向量
w = array([0 for i in range(0, dimension)])  # type: array

# 偏置
b = 0  # type: int

# 权值向量增量系数
alpha = array([0 for i in range(0, N)])  # type: array

# Gram矩阵
G = mat([[dot(T[i][0], T[j][0]) for j in range(0, N)] for i in range(0, N)])


def perceptron_run(step=1):
    """
    感知机学习算法的原始形式
    :param step: 学习率（步长）
    :return: w ,b
    """
    global w, b
    w = array([0 for i in range(0, dimension)])
    b = 0
    i = 0
    while i < N:
        xi = T[i][0]
        yi = T[i][1]
        # print yi * (dot(w, xi) + b)
        if yi * (dot(w, xi) + b) <= 0:
            w = w + step * yi * xi
            b = b + step * yi
            i = 0
        else:
            i += 1
    return w, b


def perceptron_run_a(step=1):
    """
    感知机学习算法的对偶形式
    :param step: 学习率（步长）
    :return: w ,b
    """
    global alpha, b
    alpha = array([0 for i in range(0, N)])
    b = 0
    i = 0
    while i < N:
        yi = T[i][1]
        ss = sum([alpha[j] * T[j][1] * G[j, i] for j in range(0, N)])
        # print yi * (ss + b)
        if yi * (ss + b) <= 0:
            alpha[i] += step
            b += yi
            i = 0
        else:
            i += 1
    return alpha, b


def f_sign(x):
    """
    感知机模型函数
    :param x:
    :return: {-1 ,1}
    """
    ret = sign(dot(w, x) + b)
    return ret if ret != 0 else 0


def f_sign_a(x):
    """
    感知机模型函数，对偶形式
    :param x:
    :return: {-1 ,1}
    """
    ss = sum([alpha[j] * T[j][1] * G[j, i] for j in range(0, N)])
    ret = sign(ss + b)
    return ret if ret != 0 else 0


def draw_pic():
    x1 = list()
    x2 = list()
    t = list()
    for x in T:
        x1.append(x[0][0])
        x2.append(x[0][1])
        t.append('r' if x[1] > 0 else 'b')

    plt.scatter(x1, x2, s=75, c=t, alpha=0.5)  # s为size，按每个点的坐标绘制，alpha为透明度
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.savefig('test')
    plt.show()
    pass


if __name__ == '__main__':
    print "感知机学习算法的原始形式："
    w, b = perceptron_run()
    print "w=", w, ", b=", b
    print "f(x)=sign(w·x+b)=", f_sign(array([1, 4]))

    print "感知机学习算法的对偶形式："
    a, b = perceptron_run_a()
    print "a=", a, ", b=", b
    print "f(x)=sign(Σajyjxj·x+b)=", f_sign(array([1, 4]))

    draw_pic()
