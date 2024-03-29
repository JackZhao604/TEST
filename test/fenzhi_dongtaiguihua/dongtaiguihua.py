#!/user/bin/python
# -*- coding=utf-8 -*-

# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
#
# 示例：
#
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 说明:
#
# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。


def countSubstrings(s):
    dp = [[False]*len(s)]*len(s)
    res =0
    for start in range(len(s)):
        for end in range(start+1):
            if start==end:
                dp[start][end] = True
                res+=1
            else:
                if s[start]==s[end] and (start-end<=1 or dp[start-1][end+1]):
                    res+=1
                    dp[start][end] = True
    return res

print countSubstrings('aaa')