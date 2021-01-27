'''
Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

Examples:

csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
'''

# 1
def csAnythingButFive(start, end):

    count = 0

    for num in range(start, end + 1):
        # turn int into str so we can access the last number
        str_num = str(num)
        if '5' in str_num:
            continue 
        else:
            count += 1
    return count 

start = 1
end = 9
print(csAnythingButFive(start, end))

# 2
def csAnythingButFive(start, end):
    temp = [str(x) for x in range(start, end + 1)]
    res = []
    for i in temp:
        if "5" not in i:
            res.append(i)
    return len(res)
    
start = 1
end = 9
print(csAnythingButFive(start, end))