# Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.

# Every eight bits in the binary string represents one character on the ASCII table

def csBinaryToASCII(binary):

    if binary == "":
        return ""
    
    split_binary = [binary[i:i+8] for i in range(0, len(binary), 8)]
    decoded_str = ""
    for bin_letter in split_binary:
        letter = chr(int(bin_letter, 2))
        decoded_str += letter
    return decoded_str



binary = "011011000110000101101101011000100110010001100001"
print(csBinaryToASCII(binary))

'''
split_binary

range() can take three arguments( start, stop, step). Here it'll step through the binary number every 8 digits.

binary[i:i+8] is taking each slice [0:8],[9:16],[17:24], etc, that the range is going through.

int(bin_letter, 2) takes the binary number, sets it to base of two and returns
it as an int.  So something like "01100001" would return 97.

chr() takes the unicode number of 97 and converts it to the letter "l"

'''

#2 like the one above, but I brown down the for loop
def csSortedTwoSum(numbers):
 
    container = []
    
    for i in range(0, len(numbers), 8):
        numberSets = numbers[i:i+8]
        container += [numberSets]
        
    decoded = ""
    for binary_letter in container:
        letter = chr(int(binary_letter, 2))
        decoded += letter
    return decoded
    # return container
 
 
numbers = "011011000110000101101101011000100110010001100001"
print(csSortedTwoSum(numbers))