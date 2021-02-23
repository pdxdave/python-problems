'''
            8
          /   \
         5    12
        / \   / \
       n   7 11  n
          /\ /\
         n n 9 n
            / \
           n   n

Depth first traversals make their way down a branch until     
it has reached the end.    
The in-order, pre-order and post-order examples are DFT
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

    #### DFT examples using recursion #####
    # Numbers end up in ascending order: In Order Traversal
    # [5,7,8,9,11,12]
    def print_tree(self):

        if self.left is not None:
            self.left.print_tree()

        print(self.value)

        if self.right is not None:
            self.right.print_tree()

    # prints branches in physical order: Pre-order Traversal
    # [8,5,7,12,11,9]
    def print_tree(self):

        print(self.value)

        if self.left is not None:
            self.left.print_tree()

        if self.right is not None:
            self.right.print_tree()

    
    # prints branches in physical order: Post-order Traversal
    # [7,5,9,11,12,8]
    def print_tree(self):

        if self.left is not None:
            self.left.print_tree()

        if self.right is not None:
            self.right.print_tree()

        print(self.value)
    #### End of DFT examples #####


    #### DFT iterative examples #####
    def print_tree_iter(self):
        stack = [] # need
        stack.append(self) # need, add first item to stack. here it's 8

        while len(stack) > 0:
            top_item = stack.pop() # need, always pop curr item

            print(top_item.value) # the thing that changes

            if top_item.right:  # need
                stack.append(top_item.right)
            if top_item.left:   # need
                stack.append(top_item.left)
    # [8,5,4,7,12,11,9]
    #### End of DFT iterative examples #####

    #### BFT iterative examples #####
    def print_tree_iter(self):
        stack = [] # need
        stack.append(self) # need, add first item to stack. here it's 8

        while len(stack) > 0:
            top_item = stack.pop() # need, always pop curr item

            print(top_item.value) # the thing that changes

            if top_item.right:  # need
                stack.append(top_item.right)
            if top_item.left:   # need
                stack.append(top_item.left)
    # [8,5,12,4,7,11,9]
    #### End of BFT iterative examples #####


# populate BST
root = BSTNode(8)
root.insert(5)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(9)

root.print_tree()
print("break")
root.print_tree_iter()