# @Software: PyCharm
# @Author : HansomeBo
# @Time : 2019/12/19 下午4:58
# @File : reverse_bits.py
# https://leetcode-cn.com/problems/reverse-bits/
# 颠倒二进制位

def reverse_bits(n: int) -> int:
    bin = int_to_bin_array(n)
    return reverse_bin_array_to_int(bin)


def reverse_bin_array_to_int(array: []) -> int:
    """
    二进制数组反着转十进制
    :param array:
    :return:
    """
    res = 0
    length = len(array)
    for i in range(0, length):
        if array[i] == 1:
            res += 2 ** (length - i - 1)
    return res


def int_to_bin_array(n: int) -> []:
    """
    十进制转二进制数组
    :param n:
    :return:
    """
    res = [0] * 32
    index = 0
    while n:
        res[index] = n % 2
        index += 1
        n = n // 2
    return res


if __name__ == '__main__':
    print(reverse_bits(345));
