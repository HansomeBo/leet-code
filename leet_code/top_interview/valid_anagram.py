# @Time : 2019/12/25 2:22 下午
# @Author : HansomeBo
# @File : valid_anagram.py
# @Software: PyCharm
# https://leetcode-cn.com/problems/valid-anagram/
# 有效的字母异位词

def is_anagram(self, s: str, t: str) -> bool:
    """
    Hash法
    :param self:
    :param s:
    :param t:
    :return:
    """
    dict_s = {}
    dict_t = {}
    length_s = len(s)
    length_t = len(t)
    if length_s != length_t:
        return False
    for i in range(0, length_s):
        if dict_s.get(s[i]):
            dict_s.update({s[i]: dict_s.get(s[i]) + 1})
        else:
            dict_s.setdefault(s[i], 1)
        if dict_t.get(t[i]):
            dict_t.update({t[i]: dict_t.get(t[i]) + 1})
        else:
            dict_t.setdefault(t[i], 1)
    for i in dict_s:
        if dict_s.get(i) != dict_t.get(i):
            return False
    return True


if __name__ == '__main__':
    print(is_anagram(None, "123", "331"))
