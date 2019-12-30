# @Time : 2019/12/26 6:20 下午
# @Author : HansomeBo
# @File : four_sum_count.py
# @Software: PyCharm
# https://leetcode-cn.com/problems/4sum-ii/
# 四数相加
"""
1、四个集合长度相同
2、集合长度小于500
"""
from typing import List
import requests


def fou_sum_count(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    """
    最差复杂度O(n^4) = 500^4 = 62500000000
    如果将三个数的组合进行Hash，复杂度O(n^3) = 500^3 = 125000000
    将四组数分两组，进行两次Hash，复杂度为O(n^2)
    :param self:
    :param A:
    :param B:
    :param C:
    :param D:
    :return:
    """
    tmp = None
    count = 0
    dictAB = {}
    C.sort()
    D.sort()
    for i in A:
        for j in B:
            tmp = i + j
            if dictAB.get(tmp):
                dictAB.update({tmp: dictAB.get(tmp) + 1})
            else:
                dictAB.setdefault(tmp, 1)
    print(dictAB)
    for i in C:
        for j in D:
            tmp = i + j
            if dictAB.get(-tmp):
                count = count + dictAB.get(-tmp)
    return count


if __name__ == '__main__':
    print(requests.get("https://baidu.com").text);
