# @Software: PyCharm
# @Author : HansomeBo
# @Time : 2019/12/20 上午10:14
# @File : reverse_string.py
# https://leetcode-cn.com/problems/reverse-string/
# 反转字符串

def reverse_string(self, s: [str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    tmp = None
    length = len(s)
    for i in range(0, length // 2):
        tmp = s[i]
        s[i] = s[length - i - 1]
        s[length - i - 1] = tmp


if __name__ == '__main__':
    array = ['1', '2', '3', '4', '5']
    reverse_string(None, array)
    print(array)
