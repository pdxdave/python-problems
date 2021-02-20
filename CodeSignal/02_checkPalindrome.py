# solution 1
'''
This is a pythonic type of solution using regex.    
The casefold() removes all uppercase letters.   
The sub() filters out all non-letters using regex.
'''
import re
def checkPalindrome(inputString):
    
    is_palin = re.sub("[^a-z]+", "", inputString.casefold())
    
    if is_palin == is_palin[::-1]:
        return True
    else:
        return False

inputString = "Top spots"
print(checkPalindrome(inputString))



# solution 2
'''
This is more of an algorithmic approach. It still uses regex.
'''
import re
def checkPalindrome(inputString):
    
    test = re.sub('[^A-Za-z0-9]+','', inputString.lower() )
    for i in range(0, int(len(test)/2)):
        if test[i] != test[len(test)-i-1]:
            return False
    return True

inputString = "Eva, can I see bees in a cave?"
print(checkPalindrome(inputString))

