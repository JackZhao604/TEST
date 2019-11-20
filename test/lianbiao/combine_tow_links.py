#!/user/bin/pytho
# -*- coding=utf-8 -*-



# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Node():
    def __init__(self,item):
        self.item =item
        self.next = None


def build_link_list(alist):
    link_list = cur = None
    for item in alist:
        if link_list is None:
            link_list =cur = Node(item)
        else:
            cur.next = Node(item)
            cur = cur.next
    return link_list


def combind_two_link(l1,l2):
    link_list = cur = Node(l1.item)
    l1 = l1.next
    while l1 or l2:
        if l2 is not None:
            cur.next = Node(l2.item)
            cur = cur.next
            l2 = l2.next
        if l1 is not None:
            cur.next = Node(l1.item)
            cur = cur.next
            l1 = l1.next
    return link_list



def print_Link(link_list):
    cur = link_list
    while cur:
        print cur.item
        cur = cur.next


l1 = build_link_list([1,3,5,7,9])
l2 = build_link_list([2,4,6])
l = combind_two_link(l1,l2)
print_Link(l)