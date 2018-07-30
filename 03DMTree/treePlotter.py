#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2018/7/30 19:12
@Author     : Jiang Zesheng
@File       : treePlotter.py
@Software   : PyCharm
@Description: ......
"""

import matplotlib.pyplot as plt

# 定义文本框和箭头
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


def createPlot():
    """
    创建点
    :return:
    """
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode('decisionNode', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('leafNode', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()
    pass


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    """
    绘制带箭头的注解
    :param nodeTxt: 文本
    :param centerPt: 中心点
    :param parentPt: 父节点
    :param nodeType: 结点类型
    :return:
    """
    createPlot.ax1.annotate(nodeTxt,
                            xy=parentPt,
                            xycoords='axes fraction',
                            xytext=centerPt,
                            textcoords='axes fraction',
                            va="center",
                            ha="center",
                            bbox=nodeType,
                            arrowprops=arrow_args)

    pass

if __name__ == '__main__':
    print "测试图"
    createPlot()