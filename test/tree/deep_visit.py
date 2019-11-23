#!/user/bin/python
# -*- coding=utf-8 -*-


class Node():

    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None




def creat_tree(alist):
    tree = None
    queue = []
    for item in alist:
        node = Node(item)
        if tree is None:
            tree = node
            queue.append(tree)
        else:
            if queue[0].left is None:
                queue[0].left = node
                queue.append(queue[0].left)
            elif queue[0].right is None:
                queue[0].right = node
                queue.append(queue[0].right)
                queue.pop(0)
    return tree



def cengci_visit(tree):
    queue = [tree]
    while len(queue)!=0:
        node = queue.pop(0)
        print node.item
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)




def deep_vist(tree):
    if tree is None:
        return 0
    print tree.item

    deep_left = 1+deep_vist(tree.left)
    deep_right = 1+deep_vist(tree.right)
    return deep_left if deep_left>deep_right else deep_right



tree = creat_tree([1,2,3,4,5,6])
cengci_visit(tree)
print '   '
deep = deep_vist(tree)
print 'deep:',deep





