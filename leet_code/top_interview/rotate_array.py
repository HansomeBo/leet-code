# @Software: PyCharm
# @Author : HansomeBo
# @Time : 2019/12/20 下午2:43
# @File : rotate_array.py
# https://leetcode-cn.com/problems/rotate-array/
# 旋转数组

def rotate(self, nums: [int], k: int) -> None:
    """
    两层循环，超时
    :param self:
    :param nums:
    :param k:
    :return:
    """
    tmp = None
    length = len(nums)
    for i in range(0, k):
        tmp = nums[length - 1]
        for j in range(length - 1, 0, -1):
            nums[j] = nums[j - 1]
        nums[0] = tmp


def rotate_ii(self, nums: [int], k: int) -> None:
    """

    :param self:
    :param nums:
    :param k:
    :return:
    """
    pre = None
    cur = None
    index = None
    length = len(nums)
    for i in range(0, k):
        pre = nums[i]
        for j in range(i + k, length, k):
            cur = nums[j]
            nums[j] = pre
            # print(str(j) + "," + str(pre))
            print(nums)
            pre = cur
            index = j
        nums[index + k - length] = cur

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]
    rotate_ii(None, array, 2)
    print(array)
