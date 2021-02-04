'''
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search for target in nums. If target exists, then return its index, otherwise, return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
def csBinarySearch(nums, target):
    
    low = 0
    high = len(nums) -1
    
    while low <= high:
        # set middle point
        mid = (low + high) // 2
        
        # hail mary pass
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            low = mid + 1
            
        else:
            high = mid -1
            
    return - 1
    
nums =  [46, 176, 487, 551, 980, 1020, 1098, 1354, 1381, 1414, 1578, 1579, 1596, 1634, 1810, 1882, 1924, 1999, 2021, 2074, 2083, 2269, 2579, 2616, 2626, 2645, 2871, 2874, 2889, 2987, 2999, 3106, 3126, 3191, 3217, 3304, 3342, 3516, 3557, 3579, 3617, 3655, 4022, 4049, 4059, 4386, 4510, 4600, 4792, 4799, 4937, 5257, 5466, 5489, 5574, 5623, 5915, 5929, 5976, 6011, 6047, 6136, 6173, 6175, 6331, 6333, 6368, 6631, 6673, 6847, 6960, 7034, 7042, 7167, 7186, 7352, 7604, 7879, 7945, 7991, 8225, 8226, 8330, 8370, 8394, 8500, 8528, 8563, 8786, 8831, 8837, 8861, 8976, 9236, 9251, 9388, 9436, 9532, 9708, 9891]
target = 2871
print(csBinarySearch(nums, target))