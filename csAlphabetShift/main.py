# Given a string, your task is to replace each of its
# characters by the next one in the English alphabet, i.e. replace 'a' with 'b', replace 'b' with 'c'. 
# 'z' would be replaced with 'a'

def alphabetShift(inputString):

    results = ""

    for ltr in inputString:

        if ltr == 'z':
            x = ord(ltr) - 25
            results += chr(x)
        
        else:
            x = ord(ltr) + 1
            results += chr(x)

    return results

inputString = "crazy"
print(alphabetShift(inputString))

'''
    Loop through the string.
    
    ord() returns the integer that represents a letter; for instance 'a' would return 97.

    In the case of line 12, 'z' has a unicord number of 122.  If we subtract 25 from 122 that gives us 97, which is an 'a'

    chr() returns the character that represents the unicode number.

'''