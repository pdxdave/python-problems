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
    res = {}
    for num in nums:
        if num not in res:
            res[num] = 1
        else:
            res[num] += 1
    for key, val in res.items():
        if val == 1:
            return key
    
    
nums = [0, 1, 0, 1, 0, 1, 99]
print(csFindTheSingleNumber(nums))