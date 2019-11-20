#!/user/bin/python
# -*- coding=utf-8 -*-

# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

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


l1 = build_link_list([1,9,3])
l2 = build_link_list([9,9])

def add(l1,l2):
    length_l1 = 0
    length_l2 = 0
    cur = l1
    while cur:
        cur = cur.next
        length_l1+=1
    cur=l2
    while cur:
        cur = cur.next
        length_l2+=1

    result = None
    cur_result = None
    cur_1 = l1
    cur_2 = l2
    if length_l1>=length_l2:
        for i in range(length_l1-length_l2):
            if result is None:
                result = Node(cur_1.item)
                cur_result = result
                cur_1 = cur_1.next
            else:
                cur_result.next = Node(cur_1.item)
                cur_result = cur_result.next
                cur_1 = cur_1.next
    else:
        for i in range(length_l2-length_l1):
            if result is None:
                result = Node(cur_2.item)
                cur_result = result
                cur_2 = cur_2.next
            else:
                cur_result.next = Node(cur_2.item)
                cur_result = cur_result.next
                cur_2 = cur_2.next
    carry = 0
    while cur_2 and cur_1:
        sum = cur_1.item+cur_2.item+carry
        if result is None:
            result = Node(sum%10)
            cur_result = result
        else:
            cur_result.next = Node(sum%10)
            cur_result = cur_result.next

        carry = sum / 10
        cur_1 = cur_1.next
        cur_2 = cur_2.next
    if carry!=0:
        cur_result.next = Node(carry)
        cur_result = cur_result.next
    return result

result = add(l1,l2)

def echo_num(result):
    result_ = None
    cur = result
    while cur:
        temp = Node(cur.item)
        temp.next = result_
        result_ = temp
        cur = cur.next

    cur = result_
    while cur:
        print cur.item
        cur = cur.next



echo_num(result)






