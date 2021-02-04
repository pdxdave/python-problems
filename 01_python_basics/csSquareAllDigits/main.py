# Create a function that given an integer, returns an integer
# where every digit in the input integer is squared

'''
'n' is passed in as an integer.  For this reason it is
not interable.  If we conver it to a string, we will be able
to iterate over it.

As a string though, we cannot get the power of a string.  We
need to take the variable and turn it into an integer so we
can get the number.

Next, we take that numberand turn it back into a string and add
it to the result variable

To return the answer, we turn it back into an integer
'''

def csSquareAllDigits(n):

    result = ""
    for test in str(n):
        result += str(int(test) ** 2)
    return int(result)


n = 9119 #  returns 811181
n = 2483 # returns 416649
print(csSquareAllDigits(n))
