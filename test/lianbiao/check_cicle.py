#!/user/bin/python
# -*- coding=utf-8 -*-

# 给定一个链表，判断链表中是否有环。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
#  
#
# 示例 1：
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。

class Node():
    def __init__(self,item):
        self.item = item
        self.next = None


def build_links(alist,n):
    dict_hash = {}
    cur = link_list = None
    for i in range(0,len(alist)):
        if link_list is None:
            node = Node(alist[i])
            cur = link_list = node
            dict_hash[i] = node
        else:
            node = Node(alist[i])
            cur.next = node
            cur = cur.next
            dict_hash[i] = node

    cur.next = dict_hash[n]
    return link_list

def check_cicle(l):
    dict_hash = {}
    cur = l
    num = 0
    while cur:
        if cur in dict_hash:
            return dict_hash[cur]
        dict_hash[cur] = num
        num+=1
        cur = cur.next
    return -1



l = build_links([1,2,3,4,5],3)
print check_cicle(l)
