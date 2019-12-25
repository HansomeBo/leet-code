# @Time : 2019/12/25 11:11 上午
# @Author : HansomeBo
# @File : single_number.py
# @Software: PyCharm
# https://leetcode-cn.com/problems/single-number/

def single_number(self, nums: [int]) -> int:
    """
    与或运算方式
    :param self:
    :param nums:
    :return:
    """
    res = 0
    for i in nums:
        res ^= i
    return res


if __name__ == '__main__':
    print(single_number(None, [1, 2, 3, 1, 2]))
