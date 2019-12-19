# @Time : 2019/12/19 上午9:27
# @Author : HansomeBo
# @File : palindrome_linked_list.py
# @Software: PyCharm
# https://leetcode-cn.com/problems/palindrome-linked-list/
# 回文链表
from leet_code.model.list_node import ListNode, listToArray


#转化为数组后遍历
def isPalindrome(head: ListNode) -> bool:
    if head is None:
        return True
    array = listToArray(head);
    end = array.__len__();
    mid = end // 2;
    for i in range(0, mid + 1):
        if array[i] != array[end - i - 1]:
            return False
    return True

#快指针慢指针
def isPalindromeII(head: ListNode) -> bool:

    return True

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    # node2.next = node3
    # node1.next = node2
    print(isPalindrome(None))
