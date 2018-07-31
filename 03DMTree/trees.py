#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2018/7/21 15:40
@Author     : PokemonJ
@File       : trees.py
@Software   : PyCharm
@Description: 决策树测试类
"""

import math

import operator


def createDataSet():
    """
    创建数据集
    :return:
    """
    X = [[1, 1, 'yes'],
         [1, 1, 'yes'],
         [1, 0, 'no'],
         [0, 1, 'no'],
         [0, 1, 'no']]

    labels = ['no surfacing', 'flippers']
    return X, labels


def calcShannonEntropy(X):
    """
    计算给定数据集的香农熵
    :param X: 数据集
    :return:
    """
    N = len(X)
    count = dict()
    for x in X:
        lab = x[-1]
        if lab not in count.keys():
            count[lab] = 0
        count[lab] += 1
    ent = 0.0
    for key in count:
        pr = float(count[key]) / N  # 以频率作为计算的概率
        ent -= pr * math.log(pr, 2)
    return ent


def splitDataSet(X, axis, value):
    """
    按照给定特征划分数据集
    :param X: 待划分的数据集
    :param axis: 划分数据集的特征的下标
    :param value: 需要返回特征的值
    :return:
    """
    retX = list()
    for x in X:
        if x[axis] == value:
            xt = x[:axis]  # type:list
            xt.extend(x[axis + 1:])
            retX.append(xt)
    return retX


def getBestFeatureToSplit(X):
    """
    利用香农熵计算信息增益，选择最好的数据集划分方式
    :param X:
    :return:
    """
    featureNum = len(X[0]) - 1
    baseEnt = calcShannonEntropy(X)
    bestInfoGain = 0.0
    bestFeature = 0
    for i in range(featureNum):
        featList = set([e[i] for e in X])  # 创建唯一的分类标签列表
        newEnt = 0.0
        for value in featList:
            subX = splitDataSet(X, i, value)
            pr = len(subX) / float(len(X))
            newEnt += pr * calcShannonEntropy(X)
        infoGain = bestInfoGain - newEnt
        if infoGain > bestInfoGain:
            bestFeature = i
            bestInfoGain = infoGain
    return bestFeature


def majorityCnt(classList):
    count = dict()
    for v in classList:
        if v not in count.keys():
            count[v] = 0
        count[v] += 1
    sortedCount = sorted()
    pass


def createTree(X, labels):
    """
    递归创建树,以多重嵌套字典作为树数据结构
    :param X:
    :param labels:
    :return:
    """
    yList = [e[-1] for e in X]
    # 递归出口条件：当类别完全相同，停止继续划分
    if yList.count(yList[0]) == len(yList):
        return yList[0]
    # 遍历完所有特征时返回出现次数最多的类别
    if len(X[0]) == 1:
        return majorityCnt(yList)

    bestFeat = getBestFeatureToSplit(X)
    bestFeatLabel = labels[bestFeat]

    # 以字典作为树数据结构
    tree = {bestFeatLabel: dict()}
    del (labels[bestFeat])
    featValues = set([e[bestFeat] for e in X])
    for value in featValues:
        subLabels = labels[:]
        tree[bestFeatLabel][value] = createTree(splitDataSet(X, bestFeat, value), subLabels)
    return tree


if __name__ == "__main__":
    X, labels = createDataSet()
    print createTree(X, labels)

    # print splitDataSet(X, 0, 0)
    # print calcShannonEntropy(X)

    # X[0][-1] = 'maybe'
    # print X
    # print calcShannonEntropy(X)

    pass
