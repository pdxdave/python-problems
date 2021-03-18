'''
For a given positive integer n determine if it can be represented as a sum of two Fibonacci numbers (possibly equal).

Example

For n = 1, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 1 = 0 + 1 = F0 + F1.

For n = 11, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 11 = 3 + 8 = F4 + F6.

For n = 60, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 60 = 5 + 55 = F5 + F10.

For n = 66, the output should be
fibonacciSimpleSum2(n) = false.


'''
# 1 solution

# We can start a Fibonacci list with 0,1 since all Fibonacci
# lists start with 0,1 anyway.

# Create two variables.  One for 0 and one for 1

# While the last number in our list is less than the n
# parameter that is passed in...
def fibonacciSimpleSum2(n):
    
    F = [0,1]
    num1 = 0
    num2 = 1
    
    # F[-1] is the last number in the list
    while F[-1] <= n:
        if n - F[-1] in F:
            return True
        else:
            next = num1 + num2
            num2 = num1
            num1 = next
            F.append(next)
    return False
    
n = 66
print(fibonacciSimpleSum2(n))

# 2 solution

# A brute force solution

# The while loop checks to make sure that the last number
# in the list is less than the n parameter passed through
# the function.  Next it appends to the list the sum of the
# last and second to the last numbers in the list.  Once
# we exceed the value of n we break out of the while loop.

# Next is a nested for loop.  It will add all the possible
# combinations between x and y to see if it can match the
# n parameter.  This takes a lot of passes -- 107.

def fibonacciSimpleSum2(n):
    
    F = [0,1]
    
    while F[-1] < n:
        F.append(F[-2] + F[-1])
    for x in F:
        for y in F:
            if x + y == n:
                return True
                
    return False
    
n = 66
print(fibonacciSimpleSum2(n))