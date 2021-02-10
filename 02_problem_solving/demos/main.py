"""
U.P.E.R.
- Understand
- Plan
- Execute
- Reflect
"""

"""
Effectively ask for help
- giving the expected vs experienced behavior
- explaing what specific actions they taken so far
- providing all relevant info and code
"""

# challenge 1
'''
Write a function that retrieves the last n elements from a list
Examples
- last ([1,2,3,4,5], 1) -> [5]
- last ([4,3,9,9,7,6], 3) -> [9,7,6]
- last ([1,2,3,4,5], 7) -> "invalid"
- last ([1,2,3,4,5], 0) -> []

Notes:
- Return 'invalid' if n exceeds the length of the list
- Return an empty list if n == 0
- Given the examples, we are asked to take a slice of the array (e.g., [9,7,6])
- We know that a slice is [start inclusive: end exclusive]
'''
def last(a, n):

    if n == 0:
        return []
    
    elif n > len(a):
        return("invalid")

    else:
        return a[-n: ]
        

print(last([1,2,3,4,5], 1))
print(last([4,3,9,9,7,6], 3))
print(last([1,2,3,4,5], 7))
print(last([1,2,3,4,5], 0)) 

# Challenge 2
"""
Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.
- The important part: each element's index in the list added to itself
- So this is saying and index 0 to element 1, add index 1 to element 2.
- knowing this, we need to be able to get the index and the element.  
"""


def add_indexes(numbers):
    # Your code here
    newList = []

    for i, item in enumerate(numbers, start=0):
        newList.append(i + item)
    print(newList)

    # or
    # for i in range(len(numbers)):
        # newList.append(i + numbers[i])
    # print(newList)



add_indexes([0, 0, 0, 0, 0])
add_indexes([1, 2, 3, 4, 5])
add_indexes([5, 4, 3, 2, 1])


# Challenge #3:
"""
# list comprehension

something = [number for number in numbers if number > 5]
Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- turn string of numbers into a list of integers
- loop through the list and multiply each successive number in the list

- Bonus: Try to complete this challenge in one line!
"""
def multiply_nums(nums):
    
    test = list(map(int, nums.split(', ')))
    result = 1
    for i in test:
        result *= i
    
    return result

    # or
    # total = 1
    # test = [int(nums) for nums in nums.split(',')]
    # for n in test:
        # total *= n
    #return total

print(multiply_nums("7, 6"))

# Challenge 4:
"""
Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :)
grin -> :D
sad -> :(
mad	-> :P

Examples:
- emotify("Make me smile") ➞ "Make me :D"
- emotify("Make me grin") ➞ "Make me :)"
- emotify("Make me sad") ➞ "Make me :("

Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.
- Consider using a dictionary to store the key/value pairs
    {
        "smile": :)
        "grin": :D
    }
- interate over hash table items extrapolating the key/value of each item
- Python has a replace() method

What's happening is that we're taking in the argument "make me smile".  The loop is grabbing
the key/value pairs of our data dictionary and data.items() turns them into tuples.  
txt.replace(k) is taking the string "make me smile"
and is looking for the word "smile".  If it finds it, it will replace "smile" with the 
emoticon ":)" and return "make me :)".  It doesn't return anything to change the dictionary.
"""
def emotify(txt):
    
    data = {
        "smile": ":)",
        "grin": ":D",
        "sad": ":(",
        "mad": ":/"  
    }

    for k, v in data.items():
        txt = txt.replace(k, v)

    return txt

print(emotify("Make me smile"))
print(emotify("Make me grin"))
print(emotify("Make me sad"))
print(emotify("Make me mad"))

# The same thing could be used to replace multiple words in a sentence
def changeSentence(txt):
    
    data = {
        "Danny": "Craig",
        "Sally": "Kelly", 
        "Helen": "Alison"
    }

    for k, v in data.items():
        txt = txt.replace(k, v)

    return txt

print(changeSentence("Danny told Sally that Helen was out of town"))
## Craig told Kelly that Alison was out of town