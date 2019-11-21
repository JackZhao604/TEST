#!/user/bin/python
# -*- coding=utf-8 -*-


class node():
    def __init__(self,item):
        self.item =item
        self.next = None


def build_two_links(item,list1,n1,list2,n2):
    l1 = cur1 = node(0)
    l2 = cur2 = node(0)
    for i in range(n1):
        cur1.next = node(list1[i])
        cur1 = cur1.next
    for i in range(n2):
        cur2.next = node(list2[i])
        cur2 = cur2.next
    l1 = l1.next
    l2 = l2.next
    for i in range(n1,len(list1)):
        Node = node(list1[i])
        cur1.next =Node
        cur2.next = Node
        cur1,cur2 = cur1.next,cur2.next
    return l1,l2



def get_same_node(l1,l2):

    dict_hash = {}

    cur = l1
    while cur:
        dict_hash[cur] = cur.item
        cur = cur.next

    cur = l2
    while cur:
        if cur in dict_hash:
            return cur.item
        cur = cur.next
    return -1


l1,l2 = build_two_links(8,[1,2,3,8,7,9],3,[2,4,6,9,8,7,9],4)
print get_same_node(l1,l2)
