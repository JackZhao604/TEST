
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



max_sum = float('-inf')
def maxPathSum(root):
    def max_gain(node):
        global max_sum
        if not node:
            return 0

        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        price_newpath = node.item + left_gain + right_gain
        max_sum = max(max_sum, price_newpath)
        return node.item + max(left_gain, right_gain)


    max_gain(root)
    return max_sum




tree = creat_tree([1,2,3])

print maxPathSum(tree)
