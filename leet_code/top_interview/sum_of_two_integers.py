# @Time : 2019/12/25 3:10 下午
# @Author : HansomeBo
# @File : sum_of_two_integers.py
# @Software: PyCharm
# https://leetcode-cn.com/problems/sum-of-two-integers/
#  两整数之和
"""
转化成二进制，使用二进制的加减法
二进制加法 ：与或（非进位计算）+ 与（进位计算）
"""


def get_sum(self, a: int, b: int) -> int:
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    # 2^32
    MASK = 0x100000000
    MAX_INT = 0x7FFFFFFF
    MIN_INT = MAX_INT + 1
    while b != 0:
        # 计算进位
        carry = (a & b) << 1
        # 取余范围限制在 [0, 2^32-1] 范围内
        a = (a ^ b) % MASK
        b = carry % MASK
    return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


if __name__ == '__main__':
    print(get_sum(None, -1, -1))
