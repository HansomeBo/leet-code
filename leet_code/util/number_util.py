# 十进制转二进制
def int_to_bin(n: int) -> str:
    res = '';
    while n:
        res += str(n % 2)
        n = n // 2
    return res


if __name__ == '__main__':
    print(int_to_bin(33))
