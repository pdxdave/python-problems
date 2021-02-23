'''
Given a binary tree of integers t, return its node values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
Etc.
'''
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



# PLUG INTO PYTHONTUTOR FOR WALKTHROUGH
'''
     1
   /   \
  2     4
   \   /
    3 5

[1, 2, 4, 3, 5]

1. Populate the tree with values.  They're in our queue.
2. Pop off the first value in the queue, which is 1.
3. 1 is the curNode.
4. Append currNode to values, gives us [1]
5. 
'''

class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
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
        
    print(values)
    
root = Tree(1) 
root.left = Tree(2) 
root.left.right = Tree(3)
root.right = Tree(4) 
root.right.left = Tree(5) 

traverseTree(root)
