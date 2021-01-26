#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):

    queue = [t]
    values = []
    
    while queue != []:
        curNode = queue.pop(0)
        if curNode != None:
            values.append(curNode.value)
            if curNode.left != None:
                queue.append(curNode.left)
            if curNode.right != None:
                queue.append(curNode.right)
        
    return values