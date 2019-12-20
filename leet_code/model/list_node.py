# @Time : 2019/12/19 上午9:27
# @Author : HansomeBo
# @File : list_node.py
# @Software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        """
        重写后的toString方法，方便查看链表结构
        :return:
        """
        if self.next is None:
            return str(self.val)
        return str(self.val) + "->" + self.next.__str__()


def list_to_array(node: ListNode) -> []:
    """
    将链表转化为数组
    :param node:
    :return:
    """
    array = []
    while node:
        array.append(node.val)
        node = node.next
    return array


def array_to_list(array: []) -> ListNode:
    """
    寄存法，将数组转化为链表
    :param array:
    :return:
    """
    pre = None
    for i in range(len(array) - 1, -1, -1):
        node = ListNode(array[i])
        node.next = pre
        pre = node
    return pre


def array_to_list_ii(array: []) -> ListNode:
    """
    递归法，将数组转化为链表
    :param array:
    :return:
    """
    return get_next_node(array, 0)


def get_next_node(array: [], index: int) -> ListNode:
    if index >= len(array):
        return None
    node = ListNode(array[index])
    node.next = get_next_node(array, index + 1)
    return node


def reversal_list(head: ListNode) -> ListNode:
    pre = None
    prepre = None
    while head:
        pre = head
        head = head.next
        pre.next = prepre
        prepre = pre
    return pre


if __name__ == '__main__':
    print(reversal_list(array_to_list([1, 2, 3, 4, 5, 6])))
