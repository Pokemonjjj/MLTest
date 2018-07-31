#!/usr/bin/env python
# encoding: utf-8

"""
@Time       : 2018/7/30 0030 下午 11:28
@Author     : PokemonJ
@Email      : 
@File       : __init__.py.py
@Software   : PyCharm
@Description:
"""


class Man(object):

    @property
    def num(self):
        return 0

    @num.setter
    def num(self, v):
        return v

    def __init__(self):
        pass


if __name__ == '__main__':
    a1 = Man()

    pass
