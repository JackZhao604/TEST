#!/user/bin/python
# -*- coding=utf-8 -*-


class Node():
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None





def creat_tree(alist):
    if len(alist)==0:
        return None
    item = alist.pop()
    node = Node(item)
    node.left = creat_tree(alist)
    node.right = creat_tree(alist)
    return node


def creat_tree_cengci(alist):
    queue = []
    tree = None
    for item in alist:
        node = Node(item)
        if len(queue)==0:
            tree = node
            queue.append(node)
        else:
            cur = queue[0]
            if cur.left is None:
                cur.left = node
                queue.append(cur.left)
            elif cur.right is None:
                cur.right = node
                queue.append(cur.right)
                queue.pop(0)

    return tree



tree = creat_tree_cengci([1,2,3,4,5,6])


def cengci_visit(tree):
    queue = []
    cur = tree
    queue.append(cur)
    while len(queue)!=0:
        a = queue.pop(0)
        print a.item
        if a.left is not None:
            queue.append(a.left)
        if a.right is not None:
            queue.append(a.right)

cengci_visit(tree)



