#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def minimumDepthBinaryTree(root):
    

    """
    This is similar to the previous solution. We can first check to see if there is a r         root.  If there isn't one, then we can return 0
    """
    if root is None:
        return 0
            
        
    """
    Check the leaf nodes
    """
    if root.left is None and root.right is None:
        return 1
    
    if root.left is None:
        return minimumDepthBinaryTree(root.right) + 1
    
    if root.right is None:
        return minimumDepthBinaryTree(root.left) + 1
    
    return min(minimumDepthBinaryTree(root.left), minimumDepthBinaryTree(root.right)) + 1