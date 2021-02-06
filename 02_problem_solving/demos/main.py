"""
U.P.E.R.
- Understand
- Plan
- Execute
- Reflect
"""

"""
Effectively ask for help
- giving the expected vs experienced behavior
- explaing what specific actions they taken so far
- providing all relevant info and code
"""

# challenge 1
'''
Write a function that retrieves the last n elements from a list
Examples
- last ([1,2,3,4,5], 1) -> [5]
- last ([4,3,9,9,7,6], 3) -> [9,7,6]
- last ([1,2,3,4,5], 7) -> "invalid"
- last ([1,2,3,4,5], 0) -> []

Notes:
- Return 'invalid' if n exceeds the length of the list
- Return an empty list if n == 0
- Given the examples, we are asked to take a slice of the array (e.g., [9,7,6])
- We know that a slice is [start inclusive: end exclusive]
'''
def last(a, n):

    if n == 0:
        return []
    
    elif n > len(a):
        return("invalid")

    else:
        return a[-n: ]
        

print(last([1,2,3,4,5], 1))
print(last([4,3,9,9,7,6], 3))
print(last([1,2,3,4,5], 7))
print(last([1,2,3,4,5], 0)) 

# Challenge 2
"""
Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.
- 
"""


def add_indexes(numbers):
    # Your code here
    newList = []

    for i, item in enumerate(numbers, start=0):
        newList.append(i + item)
    print(newList)

    # or
    # for i in range(len(numbers)):
        # newList.append(i + numbers[i])
    # print(newList)



add_indexes([0, 0, 0, 0, 0])
add_indexes([1, 2, 3, 4, 5])
add_indexes([5, 4, 3, 2, 1])
