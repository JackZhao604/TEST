#!/user/bin/python
# -*- coding=utf-8 -*-


class node():
    def __init__(self,item):
        self.item = item
        self.next = None



def sortList(head):
    if not head or not head.next:
        return head
    slow,fast = head,head.next
    while fast and fast.next:
        fast,slow = fast.next.next,slow.next
    mid = slow.next
    slow.next = None
    left = sortList(head)
    right = sortList(mid)
    h = res = node(0)
    while left and right:
        if left.item < right.item:
            h.next = left
            left = left.next
        else:
            h.next = right
            right = right.next
        h = h.next
    h.next = left if left else right
    return res.next




def build_link_list(num_list):
    link_list = None
    cur = None
    for num in num_list:
        if link_list is None:
            link_list = node(num)
            cur= link_list
        else:
            cur.next = node(num)
            cur = cur.next
    return link_list


def print_Link(link_list):
    cur = link_list
    while cur:
        print cur.item
        cur = cur.next

l = build_link_list([5,4,1,2,6])
l_ = sortList(l)
print_Link(l_)