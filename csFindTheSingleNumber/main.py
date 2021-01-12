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