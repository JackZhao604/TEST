#!/user/bin/python
#-*- coding=utf-8 -*-
#
#
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
# 说明：
#
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
#



def get_peat(alist):
    p = 0
    q = len(alist)-1
    while p< q:
        k = (p+q)/2
        if alist[k-1]<alist[k] and alist[k]<alist[k+1]:
            p = k+1
        elif alist[k-1]>alist[k] and list[k]> alist[k+1]:
            q = k-1
        else:
            return k
    return p


print get_peat([1,2,3,4,5,6,5,4,3,2,1])