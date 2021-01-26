'''
Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, where root is the value stored in the root and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes in the path respectively (noden representing the leaf).

t = {
    "value": 5,
    "left": {
        "value": 2,
        "left": {
            "value": 10,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": -3,
        "left": null,
        "right": null
    }
}

he output should be
treePaths(t) = ["5->2->10", "5->2->4", "5->-3"].
'''

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def treePaths(t):
    
    if t is None:
        return []
        
    output = []
    dft(t, output, [])
    return output 
    
def is_leaf(node):
    return node.left is None and node.right is None
    
def dft(root, output, path):
    
    if root is None:
        return
        
    path.append(f'{root.value}')
    
    if is_leaf(root):
        output.append("->" .join(path[:]))
        
    dft(root.left, output, path)
    dft(root.right, output, path)
    
    path.pop()