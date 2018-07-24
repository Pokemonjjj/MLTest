#!/usr/bin/env python
# encoding: utf-8

"""
@author: jzs
@file: kNN.py
@time: 2018/7/8 0008 上午 11:12
@description:
"""

from numpy import *
import operator

import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
    """
    创建数据集合
    :return:
    """
    return array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]]), ['A', 'A', 'B', 'B']


def classify0(inX, X, Y, k):
    """
    执行k-邻近算法做一个分类器
    :param inX: 输入的向量
    :param X: 数据集：特征向量集合X
    :param Y: 数据集：结果集Y
    :param k: k-NN中的k值
    :return:
    """
    # 计算距离,欧式距离
    # tile()
    tmp = (tile(inX, (len(X), 1)) - X) ** 2
    # TODO tile()函数
    # 在列方向上重复[0,0]1次，行1次

    dist = tmp.sum(axis=1) ** 0.5

    # 排序并选择最小的k个点
    index = dist.argsort()
    count = dict()
    for i in range(k):
        y = Y[index[i]]
        count[y] = count.get(y, 0) + 1  # get(key, 默认值)，如果key的值不存在，则赋默认值
    sortCount = sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)
    # TODO 笔记2：sorted()函数
    # sorted对由字典排序 ，返回由tuple组成的List,不再是字典
    # print sortCount
    return sortCount[0][0]


def file2matrix(fileName):
    """
    将文本记录转换NumPy的解析解析
    :param fileName:
    :return:
    """
    fr = open(fileName)
    lines = fr.readlines()
    X = zeros([len(lines), 3])  # 新建特征向量数据集
    Y = list()  # 新建特征向量类别集
    i = 0
    for line in lines:
        args = line.strip().split("\t")
        X[i, :] = args[0:3]
        Y.append(args[-1])
        i += 1
    fr.close()
    return X, Y


def autoNorm(X):
    """
    对数据集合X的数据，进行归一化处理，进行归一化
    公式：对每个数据的每一个分量，newValue = (oldValue - min)/(max - min)
    :param X:
    :return:
    """
    minV = X.min(0)
    maxV = X.max(0)

    m = X.shape[0]

    normX = (X - tile(minV, (m, 1))) / tile(maxV - minV, (m, 1))

    return normX, maxV - minV, minV


def drawPicture(X, Y):
    """
    绘制关于X,Y数据集合的散点图
    :param X:
    :return:
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(X[:, 1], X[:, 2], 15.0 * array(Y), 15.0 * array(Y))
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("y=f(x1,x2)")
    plt.show()
    return


def knnTest():
    # x, y = file2matrix("D:\机器学习实战 数据以及源码\Ch02\datingTestSet2.txt")
    x, y = file2matrix("datingTestSet.txt")
    # print x
    # print y[0:20]
    normX, rage, minV = autoNorm(x)
    # print normX
    # print rage
    # print minV
    # drawPicture(x, y)
    return





