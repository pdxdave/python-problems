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