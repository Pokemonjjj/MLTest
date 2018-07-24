#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2018/7/21 13:28
@Author     : PokemonJ
@File       : DatingTest.py
@Software   : PyCharm
@Description: ......
"""
from numpy import *
import kNN


def datingClassTest():
    """
    分类器测试：约会分类网站的用户数据分类的测试
    :return:
    """
    hoRet = 0.10
    x, y = kNN.file2matrix("datingTestSet.txt")
    normX, rage, minV = kNN.autoNorm(x)
    m = normX.shape[0]
    errorCount = 0
    testNum = int(hoRet * m)
    for i in range(testNum):
        yr = kNN.classify0(normX[i, :], normX[testNum:m, :], y, 3)
        print "第%d个分类为%s，原来分类为%s" % (i, yr, y[i])
        if yr != y[i]:
            errorCount += 1
    print "错误数为：%d，数错误率为：%f%% " % (errorCount, float(errorCount) * 100 / m)
    return


def classifyPerson():
    """
    根据提示输入数据
    :return:
    """
    ll = ["不喜欢的人", "魅力一般的人", "具有魅力的人"]
    x1 = float(raw_input("玩视频游戏所耗时间的百分比？"))
    x2 = float(raw_input("每年获得的飞行常客里程数为？"))
    x3 = float(raw_input("每周消费的冰淇淋的功升数为？"))

    x, y = kNN.file2matrix("datingTestSet2.txt")
    normX, rage, minV = kNN.autoNorm(x)

    inX = (array([x1, x2, x3]) - minV) / rage

    ret = kNN.classify0(inX, x, y, 3)

    print "你对的喜欢程度可能是：", ll[int(ret) - 1]


if __name__ == "__main__":
    classifyPerson()
    pass
