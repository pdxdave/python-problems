'''
Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

Examples:

csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
'''

# 1
def csAnythingButFive(start, end):

    sum = 0
    
    for num in range(start, end + 1):
        if num == 5:
            continue
        else:
            sum += 1
    return sum

start = 1
end = 9
print(csAnythingButFive(start, end))

# 2
def csAnythingButFive(start, end):
    temp = [x for x in range(start, end + 1)]
    res = []
    for i in temp:
        if i != 5:
            res.append(i)
    return len(res)
    
start = 1
end = 9
print(csAnythingButFive(start, end))