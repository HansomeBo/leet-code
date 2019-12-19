from leet_code.util import number_util


# https://leetcode-cn.com/problems/number-of-1-bits/

def hamming_weight(n: int) -> int:
    return bin(n).count('1')


def hamming_weight_ii(n: int) -> int:
    res = ""
    count = 0
    while n:
        res += str(n % 2)
        if res == "1":
            count += 1
        n = n // 2
    return count


if __name__ == '__main__':
    print(number_util.int_to_bin(33))
