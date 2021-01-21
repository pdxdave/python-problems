def fibonacciSimpleSum2(n):
    
    F = [0,1]
    num1 = 0
    num2 = 1
    
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