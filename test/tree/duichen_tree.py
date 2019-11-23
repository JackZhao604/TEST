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
        if item is None:
            node = None
        else:
            node = Node(item)
        if tree is None:
            tree = node
            if tree is not None:
                queue.append(tree)
        else:
            if queue[0].left is None:
                queue[0].left = node
                if queue[0].left:
                    queue.append(queue[0].left)
            elif queue[0].right is None:
                queue[0].right = node
                if queue[0].right:
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


def check_duichen(tree):
    if tree is None:
        return True
    left_duichen = check_duichen(tree.left)
    right_duichen = check_duichen(tree.right)
    if (tree.left == tree.right==None or tree.left.item == tree.right.item)  and left_duichen and right_duichen:
        return True
    else:
        return False


def check_duichen_(tree1,tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False

    if tree1.item == tree2.item and check_duichen_(tree1.left,tree2.right) and check_duichen_(tree1.right,tree2.left):
        return True
    else:
        return False






tree = creat_tree( [1,2,2,None,3,None,3])
cengci_visit(tree)
print '   '
deep = deep_vist(tree)
print 'deep:',deep

print check_duichen_(tree.left,tree.right)



