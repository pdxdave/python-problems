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

    def print_tree_iterative(self)


# populate BST
root = BSTNode(8)
root.insert(5)
root.insert(7)
root.insert(12)
root.insert(11)

root.print_tree()