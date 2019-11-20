#!/user/bin/python
# -*- coding=utf-8 -*-


def heapfi(alist,n,i):
    lagest = i
    l = 2*i+1
    r = 2*i+2
    if l<n and alist[lagest]<alist[l]:
        lagest = l

    if r<n and alist[lagest]<alist[r]:
        lagest = r

    if lagest!=i:
        alist[i],alist[lagest] = alist[lagest],alist[i]
        heapfi(alist,n,lagest)

def heap_sort(alist):
    n = len(alist)
    for i in range(0,n):
        heapfi(alist,n,i)

    for i in range(n-1,0,-1):
        alist[i],alist[0] = alist[0],alist[i]
        heapfi(alist,i,0)




alist = [9,3,2,4,5]

heap_sort(alist)

print alist

























