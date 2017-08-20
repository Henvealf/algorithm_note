# coding=utf-8
"""
使用动态规划计算编辑距离的算法
"""
from HeneUtil import Array


def getEditLengthBasic(str1, str2):
    """
    编辑距离最基础的求解方式
    输入参数：两个要比较的字符串
    返回值： 两个字符串的编辑距离
    """

    i = len(str1)
    j = len(str2)

    # 定义数组
    dArray = Array.get(i + 1, j + 1)

    for j in range(j + 1):
        dArray[0][j] = j

    for i in range(1, i + 1):
        dArray[i][0] = i
        for j in range(1, j + 1):
            if str1[i - 1] is str2[j - 1]:
                dArray[i][j] = dArray[i - 1][j - 1]
            else:
                dArray[i][j] = min(dArray[i][j - 1], dArray[i - 1][j], dArray[i - 1][j - 1]) + 1

    return dArray[i][j]


def getEditLengthScrollArray(str1, str2):
    """
    计算两个字符串之间的编辑距离。并进行滚动数组优化，降低空间复杂度。
    :param str1:
    :param str2:
    :return: 编辑距离
    """
    i = len(str1)
    j = len(str2)

    dOldArray = [j for j in range(j + 1)]
    dNewArray = [0 for j in range(j + 1)]
    for i in range(1, i + 1):
        dNewArray[0] = i
        for j in range(1, j + 1):
            if str1[i - 1] is str2[j - 1]:
                dNewArray[j] = dOldArray[j - 1]
            else:
                dNewArray[j] = min(dNewArray[j - 1], dOldArray[j - 1], dOldArray[j]) + 1

        dTmpArray = dOldArray
        dOldArray = dNewArray
        dNewArray = dTmpArray
    # 因为最后交换了，所以返回老的
    return dOldArray[j]


if __name__ == '__main__':
    #print getEditLengthBasic('math', 'mouth')
    print getEditLengthScrollArray('math', 'mouth')
    # print range(1, 10)
