#!/user/bin/python
# -*- coding=utf-8 -*-

# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
#
# 要求返回这个链表的深拷贝。 
#
#  
#
# 示例：
#
#
#
# 输入：
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
#
# 解释：
# 节点 1 的值是 1，它的下一个指针和随机指针都指向节点 2 。
# 节点 2 的值是 2，它的下一个指针指向 null，随机指针指向它自己。


class Node():
    def __init__(self,item,next,random):
        self.item = item
        self.next = next
        self.random = random


def build_link_list(alist):
    pass



visited_hash = {}
head = None
cur = head

def deep_copy(head):
    if head is None:
        return None
    if head in visited_hash:
        return visited_hash[head]


    node = Node(head.item,None,None)
    visited_hash[head] = node

    node.next = deep_copy(head.next)
    node.random = deep_copy(head.random)
    return head





