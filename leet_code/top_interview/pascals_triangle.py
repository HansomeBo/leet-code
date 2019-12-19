# @Software: PyCharm
# @Author : HansomeBo
# @Time : 2019/12/19 下午4:05
# @File : pascals_triangle.py
# https://leetcode-cn.com/problems/pascals-triangle/
# 杨辉三角
def generate(numRows: int) -> [[]]:
    res = []
    for i in range(0, numRows):
        row = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(res[i - 1][j - 1] + res[i - 1][j])
        res.append(row)
    return res


if __name__ == '__main__':
    print(generate(5))
