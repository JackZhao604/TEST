#!/user/bin/python
# -*- coding=utf-8 -*-

test_list = [0,3,5,2,7,8,9,1]


def bubble_sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(0,n-i-1):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]


bubble_sort(test_list)
print test_list

























