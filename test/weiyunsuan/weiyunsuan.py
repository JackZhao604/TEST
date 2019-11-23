#!/user/bin/python
# -*- coding=utf-8 -*-


# 给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。
#
# 示例 1:
#
# 输入: 5
# 输出: True
# 解释:
# 5的二进制数是: 101
import numpy as np
binary = lambda n: '' if n==0 else binary(n/2) + str(n%2)


def check_jiaoti(num):
    a= binary(num)
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            return False
    return True
print check_jiaoti(5)
print check_jiaoti(7)