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

#2 like the one above, but I broke down the for loop
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


# link to python tutor working example 
[python tutor](http://pythontutor.com/visualize.html#code=def%20csSortedTwoSum%28numbers%29%3A%0A%20%0A%20%20%20%20container%20%3D%20%5B%5D%0A%20%20%20%20%0A%20%20%20%20for%20i%20in%20range%280,%20len%28numbers%29,%208%29%3A%0A%20%20%20%20%20%20%20%20numberSets%20%3D%20numbers%5Bi%3Ai%2B8%5D%0A%20%20%20%20%20%20%20%20container%20%2B%3D%20%5BnumberSets%5D%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20decoded%20%3D%20%22%22%0A%20%20%20%20for%20binary_letter%20in%20container%3A%0A%20%20%20%20%20%20%20%20letter%20%3D%20chr%28int%28binary_letter,%202%29%29%0A%20%20%20%20%20%20%20%20decoded%20%2B%3D%20letter%0A%20%20%20%20return%20decoded%0A%20%20%20%20%23%20return%20container%0A%20%0A%20%0Anumbers%20%3D%20%22011011000110000101101101011000100110010001100001%22%0Aprint%28csSortedTwoSum%28numbers%29%29&cumulative=false&curInstr=46&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)