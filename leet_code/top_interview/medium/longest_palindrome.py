# @Time : 2019/12/31 10:20 上午
# @Author : HansomeBo
# @File : longest_palindrome.py
# @Software: PyCharm
# https://leetcode-cn.com/problems/longest-palindromic-substring/
# 最长回文子串


def longest_palindrome(self, s: str) -> str:
    """
    特征利用：对称
    1、选取中间一点或者中间两点
    2、得出左右双指针，左右指针和中间点偏移量一致
    3、遍历选出最大数组
    """
    length = len(s)
    max_pa = ''

    left = 0
    right = 0
    offset = 0
    while right < length:
        if left - offset >= 0 and right + offset < length and s[left - offset] == s[right + offset]:
            tmp = s[left - offset:right + offset + 1]
            if len(max_pa) < len(tmp):
                max_pa = tmp
            offset += 1
        else:
            offset = 0
            if left == right:
                right += 1
            else:
                left += 1
    return max_pa


def is_palindrome(s: str) -> bool:
    length = len(s)
    for i in range(0, length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True


if __name__ == '__main__':
    print(longest_palindrome(None, "12123456"))
