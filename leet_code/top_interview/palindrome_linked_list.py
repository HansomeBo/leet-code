# @Time : 2019/12/19 上午9:27
# @Author : HansomeBo
# @File : palindrome_linked_list.py
# @Software: PyCharm
# https://leetcode-cn.com/problems/palindrome-linked-list/
# 回文链表判断
from leet_code.model.list_node import ListNode, array_to_list, list_to_array


# 转化为数组后遍历
def is_palindrome(head: ListNode) -> bool:
    if head is None:
        return True
    array = list_to_array(head)
    end = array.__len__()
    mid = end // 2
    for i in range(0, mid + 1):
        if array[i] != array[end - i - 1]:
            return False
    return True


# 快指针慢指针
def is_palindrome_ii(head: ListNode) -> bool:
    if head is None or head.next is None:
        return True
    slow = head
    fast = head
    pre = head
    prepre = None
    """
      一次循环完成两件事情
      一、快指针移动到链表结尾，慢指针移动到链表中间节点
      二、前半部分链表反转
    """
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
        pre.next = prepre
        prepre = pre
    if fast is not None:
        slow = slow.next
    while slow and pre:
        if slow.val != pre.val:
            return False
        slow = slow.next
        pre = pre.next
    return True


if __name__ == '__main__':
    node = array_to_list([1, 2, 3, 4, 3, 2, 1])
    print(node)
    print(is_palindrome_ii(node))
