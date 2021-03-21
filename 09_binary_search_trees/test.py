'''
            8
          /   \
         5    12
        / \   / \
       n   7 11  n
          /\ /\
         n n n n
'''

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None

    def insert(self, value):
        if value < self.value:
            # new node goes left
            if self.left is None:
                # create new node if left is none
                self.left = BSTNode(value)
            else: 
                # otherwise let existing left node figure it out
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, target):
        # hail mary search. get it on first pass
        if target == self.value:
            return True

        if target < self.value:
            if self.left is None:
                return False
            # if a node exists to the left, call search on that. RECURSIVE
            return self.left.search(target)

        else:
            if self.right is None:
                return False
            return self.right.search(target)


    # 1st print option
    # def print(self):

    # 2nd print option
    # def print_tree(self):
    #     print(self.value)
    #     if self.left is not None:
    #         self.left.print_tree()
    #     if self.right is not None:
    #         self.right.print_tree()

    # 3rd print option / In order traversal
    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()

        print(self.value)

        if self.right is not None:
            self.right.print_tree()


# populate BST
root = BSTNode(8)
root.insert(5)
root.insert(7)
root.insert(12)
root.insert(11)

# 1st print option
# print(root.search(7)) 
# print(root.search(15))

# 2nd & 3rd print option
root.print_tree()


# NEW PROBLEM. FIND MAX DEPTH OF BINARY TREE

class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value 
        self.left = left 
        self.right = right 

    def maxDepth(self, root):
        # if no left or right after root node, return 1
        right_height = 0
        left_height = 0

        if self.right:
            right_height = self.maxDepth(self.right)

        if self.left:
            left_height = self.maxDepth(self.left)

        largest_height = max(right_height, left_height)

        return 1 + largest_height

'''
post-order printing
    go left
    go right
    print

pre-order printing
    print
    go left
    go right

in-order printing
    go left
    print
    go right
'''
# InOrder Traversal
'''
        1
      /   \
     2     3
          /  \
         4    5

#[2,1,4,3,5]
'''
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(value)
            else:
                self.right.insert(value)
                
    def inorder(self):

        if self.value == None:
            return
        
        if self.left is not None:
            self.left.inorder()
            
        print(self.value)
        
        if self.right is not None:
            self.right.inorder()
            
b1 = BinaryTreeNode(1)
b1.left = BinaryTreeNode(2)
b1.right = BinaryTreeNode(3)
b1.right.left = BinaryTreeNode(4)
b1.right.right = BinaryTreeNode(5)
b1.inorder() 





# PreOrder Traversal
'''
        1
      /   \
     2     3
          /  \
         4    5

#[1,2,3,4,5]
'''
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(value)
            else:
                self.right.insert(value)
                
    def pre_order(self):
        if self.value == None:
            return 

        print(self.value)

        if self.left is not None:
            self.left.pre_order()

        if self.right is not None:
            self.right.pre_order()
            
b1 = BinaryTreeNode(1)
b1.left = BinaryTreeNode(2)
b1.right = BinaryTreeNode(3)
b1.right.left = BinaryTreeNode(4)
b1.right.right = BinaryTreeNode(5)
b1.pre_order()

# Post-Order Traversal
'''
        1
      /   \
     2     3
          /  \
         4    5

#[2,4,5,3,1]
'''
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(value)
            else:
                self.right.insert(value)
                
    def post_order(self):
        if self.value == None:
            return 
        
        if self.left is not None:
            self.left.post_order()
            
        if self.right is not None:
            self.right.post_order()
            
        print(self.value)
            
        
            
     
b1 = BinaryTreeNode(1)
b1.left = BinaryTreeNode(2)
b1.right = BinaryTreeNode(3)
b1.right.left = BinaryTreeNode(4)
b1.right.right = BinaryTreeNode(5)
b1.post_order()