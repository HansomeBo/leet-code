# @Time : 2019/12/19 上午9:27
# @Author : HansomeBo
# @File : list_node.py
# @Software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def listToArray(node : ListNode) -> []:
    array = []
    while node :
        array.append(node.val)
        node = node.next
    return array