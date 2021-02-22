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
        # hale marry search. get it on first pass
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

    # 3rd print option
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