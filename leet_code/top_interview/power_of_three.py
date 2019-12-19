# @Software: PyCharm
# @Author : HansomeBo
# @Time : 2019/12/19 下午4:31
# @File : power_of_three.py
# https://leetcode-cn.com/problems/power-of-three/
# 3的幂
def is_power_of_three(n: int) -> bool:
    if n < 1:
        return False
    while n > 1:
        n = n / 3
        if n % 1 > 0:
            return False
    return True


if __name__ == '__main__':
    print(is_power_of_three(8))
