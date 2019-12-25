# @Time : 2019/12/25 10:13 上午
# @Author : HansomeBo
# @File : valid_palindrome.py
# @Software: PyCharm
# https://leetcode-cn.com/problems/valid-palindrome/
def is_palindrome(self, s: str) -> bool:
    length = len(s)
    i = 0
    j = length - 1
    while i <= j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


if __name__ == '__main__':
    print(is_palindrome(None, "`l;`` 1o1 ??;l`"))
