# Write a function that takes a string as input and returns
# that string in reverse order with the opposit casing for 
# each letter

# Python has a built-in method to swap character cases swapcase()
# [::-1] will reverse all the characters

# Objective 8 - perform basic string operations. Shows reverse.

# solution 1
def csOppositeReverse(txt):

    test = txt.swapcase()
    return test[:: -1]

txt = "Hello World"
txt = "ReVeRsE"
print(csOppositeReverse(txt))


# Solution 2
def csOppositeReverse(txt):

    word = ""
    for letter in txt:
        if letter != letter.upper():
            word += letter.upper()
        else:
            word += letter.lower()
    return word[:: -1]

# txt = "Hello World"
txt = "ReVeRsE"
print(csOppositeReverse(txt))
