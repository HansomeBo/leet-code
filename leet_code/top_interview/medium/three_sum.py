# @Time : 2019/12/25 6:04 下午
# @Author : HansomeBo
# @File : three_sum.py
# @Software: PyCharm
# https://leetcode-cn.com/problems/3sum/
# 三数之和
"""
1、三层遍历，遍历所有三人组合
2、先遍历两人的组合，然后寻找第三人
3、排序后，寻找组合
"""
from typing import List


def three_sum(self, nums: List[int]) -> List[List[int]]:
    """
    先确定两边的边界，作为两位数，寻找第三位数的方式
    两位数的情况遍历有些复杂。。。暂时没想出好的解决办法
    :param self:
    :param nums:
    :return:
    """
    nums.sort()
    print("sort array:", nums)
    i = 0
    j = len(nums) - 1
    res = []
    while i < j:
        tmp = nums[i] + nums[j]
        start = i + 1
        end = j
        print("start:", nums[i], ",end:", nums[j], ",need :", -tmp)
        for s in range(start, end):
            print("search third number :", nums[s])
            if nums[s] == -tmp:
                res.append([nums[i], nums[s], nums[j]])
                print("add result:", nums[i], nums[s], nums[j])
                break
        while i + 1 < len(nums) and nums[i + 1] == nums[i]:
            i = i + 1
        while j - 1 >= 0 and nums[j - 1] == nums[j]:
            j = j - 1
        if i + 1 < len(nums) and nums[i + 1] <= 0:
            i = i + 1
        elif j - 1 >= 0:
            j = j - 1
    return res


def three_sum_ii(self, nums: List[int]) -> List[List[int]]:
    """
    先确定一位数，通过双指针寻找其他两位数
    超出时间限制，需要再想办法缩小范围
    :param self:
    :param nums:
    :return:
    """
    nums.sort()
    length = len(nums)
    res = []
    for i in range(0, length):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = length - 1
        while left < right:
            if nums[left] + nums[right] + nums[i] == 0:
                res.append([nums[left], nums[right], nums[i]])

                """为了去除重复数据进行的循环判断"""
                while left < right and nums[left] == nums[left + 1]:
                    left = left + 1
                while left < right and nums[right] == nums[right - 1]:
                    right = right - 1
                """判定成功后，左右指针各自位移一位"""
                left = left + 1
                right = right - 1
            elif nums[left] + nums[right] + nums[i] < 0:
                left = left + 1
            elif nums[left] + nums[right] + nums[i] > 0:
                right = right - 1
    return res


if __name__ == '__main__':
    print(three_sum_ii(None, [-1,0,1]))
