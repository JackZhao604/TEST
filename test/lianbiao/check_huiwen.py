#!/user/bin/python
#-*- coding=utf-8 -*-

class Node():
    item = None
    next = None
    def __init__(self,item):
        self.item = item
        self.next = None


def build_link_list(num_list):
    link_list = None
    cur = None
    for num in num_list:
        if link_list is None:
            link_list = Node(num)
            cur= link_list
        else:
            cur.next = Node(num)
            cur = cur.next
    return link_list


def reverse_link(l):
    l2 = Node(l.item)
    cur = l.next
    while cur:
        node = Node(cur.item)
        cur = cur.next
        node.next = l2
        l2 = node
    return l2


def check_huiwen(l1):
    l2 = reverse_link(l1)
    cur1 = l1
    cur2 = l2

    while cur1 and cur2:
        if cur1.item != cur2.item:
            return False
        cur1,cur2 = cur1.next,cur2.next

    return True



def print_Link(link_list):
    cur = link_list
    while cur:
        print cur.item
        cur = cur.next


l = build_link_list([1,2,3,4,4,3,2,1])

print check_huiwen(l)