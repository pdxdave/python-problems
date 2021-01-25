#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def maxDepth(root):
    '''
    This will get the maxDepth height for both the left and right sides.
    It will then forward them to the balancedBinaryTree method

    First, we need to see if there is anything in the root.  If not, return 0
    '''
    if root is None:
        return 0
        
    return max(maxDepth(root.left), maxDepth(root.right)) + 1
    

def balancedBinaryTree(root):
    '''
    First we need to see if there's anything in the root.  If not, then the tree would be
    balanced at a 0 height
    '''
    if root is None:
        return True 
        
    '''
    Call the maxDepth method to get the maxDepth results for the left and right sides
    '''
    l = maxDepth(root.left)
    r = maxDepth(root.right)

    '''
    We have three conditions to be met. 1) is the diff between the left and right less than or equal to one. 2)
    is there a left root, and 3) is there a right root.  If all conditions are True, then the result is true
    '''
    
    if ((l - r) <= 1) and balancedBinaryTree(root.left) is True and balancedBinaryTree(root.right) is True:
        return True
    
    return False


# 2

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def balancedBinaryTree(root):

    # If there is no root, return true
    if not root:
        return True 
        
    # Get the right and lefth depth
    r = getDepth(root.right)
    l = getDepth(root.left)
    
    if(l - r) <= 1:
        return balancedBinaryTree(root.left) and balancedBinaryTree(root.right)
    else:
        return False
        
def getDepth(root):
    if root == None:
        return 0
    return 1 + max(getDepth(root.left), getDepth(root.right))