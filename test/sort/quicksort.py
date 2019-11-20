#!/user/bin/python
# -*- coding=utf-8 -*-

test_list = [1,6,7,2,3,9,0]


def quick_sort(alist,start,end):
    if start>=end:
        return
    mid = alist[start]
    left = start
    right = end

    while left<right:
        while left<right and alist[right]>=mid:
            right-=1
        alist[left] = alist[right]

        while left<right and alist[left]<mid:
            left+=1
        alist[right] = alist[left]

        alist[left] = mid
    quick_sort(alist,start,left-1)
    quick_sort(alist,left+1,end)



quick_sort(test_list,0,len(test_list)-1)
print test_list

