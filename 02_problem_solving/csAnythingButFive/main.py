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
    temp = [x for x in range(start, end + 1)]
    count = 0
    for i in temp:
        if '5' in str(i):
            continue
        else:
            count += 1
    return count
    
start = 1
end = 9
print(csAnythingButFive(start, end))

# 3
def csAnythingButFive(start, end):
    
    temp = [x for x in range(start, end + 1) if '5' not in str(x)]
    
    return (len(temp))
    
start = 1
end = 9
print(csAnythingButFive(start, end))