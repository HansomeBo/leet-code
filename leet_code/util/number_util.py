def int_to_bin(n: int) -> str:
    """
    十进制转二进制字符串
    :param n:
    :return:
    """
    res = '';
    while n:
        res += str(n % 2)
        n = n // 2
    return res


def int_to_bin_array(n: int) -> []:
    """
    十进制转二进制数组
    :param n:
    :return:
    """
    res = []
    while n:
        res.append(n % 2)
        n = n // 2
    return res





def bin_to_int(bin: str) -> int:
    """
    二进制字符串转化为十进制
    :param bin:
    :return:
    """
    res = 0
    length = len(bin)
    for i in range(0, length):
        if bin[i] == "1":
            res += 2 ** (length - 1 - i)
    return res


if __name__ == '__main__':
    print(int_to_bin(33))
