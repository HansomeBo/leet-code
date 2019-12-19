from leet_code.util import number_util

# https://leetcode-cn.com/problems/number-of-1-bits/
def hammingWeight(n: int) -> int:
    return bin(n).count('1')


def hammingWeightII(n: int) -> int:
    res = ""
    count = 0
    while n:
        res += str(n % 2)
        if res == "1":
            count += 1
        n = n // 2
    return count


if __name__ == '__main__':
    print(number_util.intToBin(33))
