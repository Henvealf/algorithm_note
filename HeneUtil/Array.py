# coding=utf-8
"""
一个数组,使用 get 方法获取
"""


def get(x, y = 0):

    if x < 1 or y < 0:
        raise ValueError("args error! the args [x] must great than 0, [y] must great than -1 ")

    if y == 1:
        return [0 for i in x]
    else:
        return [[ 0 for i in range(y)] for i in range(x)]


