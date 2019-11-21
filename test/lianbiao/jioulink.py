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




def print_Link(link_list):
    cur = link_list
    while cur:
        print cur.item
        cur = cur.next



def make_jioulink(l):
    lj = l
    lo = l.next
    ji,ou = l,l.next
    while ou and ou.next :
        ji.next = ji.next.next
        ou.next = ou.next.next
        ji = ji.next
        ou = ou.next
    ji.next = lo
    return lj


l = build_link_list([1,2,3,4,5,6,7,8])

lj = make_jioulink(l)
print_Link(lj)