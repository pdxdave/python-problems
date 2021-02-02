'''
You are given a non-empty array of integers.

One element appears exactly once, with every other element appearing at least twice, perhaps more.

Write a function that can find and return the element that appears exactly once.

Example 1:

Input: [1,1,2,1]
Output: 2
Example 2:

Input: [1,2,1,2,1,2,80]
Output: 80
'''

def csFindTheSingleNumber(nums):
    # store numbers in a dictionary
    res = {}
    for num in nums:
        if num not in res:
            # take number and assign it to a value of one
            res[num] = 1
            # {0: 3, 1: 3, 99: 1}
        else:
            # else, take that number and add one to it
            res[num] += 1
    # look for the item with only one of them
    for key, val in res.items():
        if val == 1:
            return key
    
    
nums = [0, 1, 0, 1, 0, 1, 99]
print(csFindTheSingleNumber(nums))