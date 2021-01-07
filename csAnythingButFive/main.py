# Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all the integers in the range (excpet integers that contain the digit 5)

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