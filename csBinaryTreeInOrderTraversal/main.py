'''
You are given a binary tree. Write a function that returns the binary tree's node values using an in-order traversal.

In order: left, root, then right
At root go left. Nothing.
Up at root again, go right, then left to get 4.
Then we pick up 3

input: [2, none, 3, 4]
    2
     \
      3
    /
   4
output: [2, 4, 3]


'''
# 1
def binaryTreeInOrderTraversal(root):

    if root is None:
        return []

    return binaryTreeInOrderTraversal(root.left) + [root.value] + binaryTreeInOrderTraversal(root.right)


# 2 
'''
                8
              /   \
             9     10
            / \    /  \
          11  12  13  14

[11, 9, 12, 8, 13, 10, 14]
'''
def binaryTreeInOrderTraversal(root):

    stack = []
    result = []

    while root is not None or stack != []:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.value)
        root = root.right
    return result