#!/user/bin/python
# -*- coding=utf-8 -*-

#
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
# 说明:
#
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:
#
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。



def get_dum(alist,target):
    for i in range(0,len(alist)):
        num = target - alist[i]
        k = binary_find(alist,i+1,len(alist)-1,num)
        if k:
            return i+1,k+1





def binary_find(alist,left,right,num):
    while left<right:
        k = (left+right)/2
        if alist[k]<num:
            left = k+1
        elif alist[k]>num:
            right = k-1
        else:
            return k
    if alist[left] !=num:
        return None
    else:
        return left


print get_dum([2, 7, 11, 15],9)