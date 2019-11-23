#!/user/bin/python
# -*- coding=utf-8 -*-


# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。


def is_pipei(list_str):
    zhan = []
    for a in list_str:
        if zhan == []:
            zhan.append(a)
        elif a!=zhan[-1]:
            zhan.pop()
        else:
            zhan.append(a)
    if zhan==[]:
        return True
    return False


print is_pipei("()(((())))")



