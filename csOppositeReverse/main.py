# Write a function that takes a string as input and returns
# that string in revers order with the opposit casing for 
# each letter

# Python has a built-in method to swap character cases swapcase()
# [::-1] will reverse all the characters

def csOppositeReverse(txt):

    test = txt.swapcase()
    return test[:: -1]

txt = "Hello World"
txt = "ReVeRsE"
print(csOppositeReverse(txt))