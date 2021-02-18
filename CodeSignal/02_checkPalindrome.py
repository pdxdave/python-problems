def checkPalindrome(inputString):

    for i in range(0, int(len(inputString)/2)):
        if inputString[i] != inputString[len(inputString)-i-1]:
            return False
    return True

inputString = "abba"
print(checkPalindrome(inputString))

'''
Not the simplest solution, but the best for checking very
long palindromes.

The for loop sets the range. It starts with 0 and the endpoint
is the length of the string cut in half and converted to an int.
The if then checks the first character of the string, and compares
it with the last character of the string.  It then moves inward 
on both sides to compare characters.  
'''