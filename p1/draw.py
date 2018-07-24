#!/usr/bin/env python
# encoding: utf-8

"""
@author: jzs
@file: draw.py
@time: 2018/6/9 0009 下午 3:44
@description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib



def func():
    # 定义数据
    x = np.arange(0, 10, 0.1)
    y = 0.05 * x ** 2

    # 绘制图像
    plt.plot(x, y)

    # 设置坐标轴
    plt.xlabel('x data')
    plt.ylabel('y data')

    # 默认保存为png格式
    plt.savefig('test')


if __name__ == '__main__':
    func()
    pass
