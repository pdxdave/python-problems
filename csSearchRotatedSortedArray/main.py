def csSearchRotatedSortedArray(nums, target):
    
    # example [6,7,0,1,2,3,4,5]
    # target 3
    
    # edge case
    if not nums:
        return -1
        
    # set low and high values
    low = 0
    high = len(nums) -1
    
    
    # use while loop
    while low <= high:
        
        # set mid point. here it's index 3, number 1
        mid = (low + high) // 2
        
        # hail mary 
        if target == nums[mid]:
            return mid 
        # first pass.
        #         6           1
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # first pass
            #        1         3             5
            if nums[mid] <= target <= nums[high]:
                # first pass
                # now the low starts a index 4.  that's because the mid was at index 3, now it's index 3 + 1
                # that makes our new search range from number 2 to 5. The process starts again.
                low = mid + 1
            else:
                high = mid - 1
    return -1


nums = [6,7,0,1,2,3,4,5]
target = 3
print(csSearchRotatedSortedArray(nums, target))