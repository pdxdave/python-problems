# Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

# 417 in binary is 110100001.  Reversing the binary is 100001011, which is 267 in decimal

def csReverseIntegerBits(n):

    # convert the integer to binary.  Remove the first two characters 0b
    binary = bin(n)[2:]

    # reverse the binary numbers
    rev = binary[:: -1]

    # convert the binary to int
    # binary is a base of 2, that's why the 2.  The int() fn
    # takes in a value and a base.
    result = int("".join(str(i) for i in rev), 2)

    return result




n = 417 # returns 267
print(csReverseIntegerBits(n))