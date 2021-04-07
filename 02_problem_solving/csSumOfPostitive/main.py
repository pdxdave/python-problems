'''
Given an array of integers, return the sum of all the positive integers in the array.

Examples:

csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
csSumOfPositive([-3, -2, -1, 0, 1]) -> 1
csSumOfPositive([-3, -2]) -> 0
'''

def csSumOfPositive(input_arr):

    # Solution 1
    sum = 0

    for key, value in enumerate(input_arr):
        if value <= 0:
            continue
        else:
            sum += value 
    return sum 

    # Solution 2
    '''
    This uses a lambda function.  It's like an anonymous JS function.
    lambda x is the argument and to the right side of : is the expression.  input_arr is asking for numbers that are greate than
    zero, then create a list of numbers greater than zero. From there
    we sum the result and return the answer
    '''

    result = list(filter(lambda x: x > 0, input_arr))
    return sum(result)


    # solution 3
    sum = 0
    for i in input_arr:
        if i >= 0:
            sum += i 
    return sum


input_arr = ([1,2,3,-4,5])
print(csSumOfPositive(input_arr))