#!/user/bin/python
# -*- coding=utf-8 -*-

# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？


class Node():
    def __init__(self,item):
        self.item = item
        self.next = None


def build_link_list(alist):
    linklist = cur = None
    for item in alist:
        if linklist is None:
            linklist = cur = Node(item)
        else:
            cur.next = Node(item)
            cur = cur.next
    return linklist

def delete(n,link_list):
    use = cur = link_list
    for i in range(n):
        cur = cur.next
    if cur is None:
        link_list = link_list.next
        return link_list
    while cur and cur.next is not None:
        cur = cur.next
        use = use.next

    use.next = use.next.next
    return link_list



def print_Link(link_list):
    cur = link_list
    while cur:
        print cur.item
        cur = cur.next


link_list = build_link_list([1,2,3,4,5])
link_list = delete(5,link_list)
print_Link(link_list)





