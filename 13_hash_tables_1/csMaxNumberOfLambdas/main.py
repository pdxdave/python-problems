'''
Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of instances of "lambda" that can be formed.

Example 1:

Input: text = "mbxcdatlas"
Output: 1
Example 2:

Input: text = "lalaaxcmbdtsumbdav"
Output: 2
Example 3:

Input: text = "sctlamb"
Output: 0
'''

# 1
def csMaxNumberOfLambdas(text):
    
    letters_dict = {"l": 0, "m": 0, "b": 0, "d":0, "a":0}
    
    for letter in text:
        if letter in letters_dict:
            letters_dict[letter] += 1
    
    letters_dict['a'] = letters_dict['a'] / 2
    return min(letters_dict.values())


# 2
d = {"l": 0, "m": 0, "b": 0, "d":0, "a":0}

    for e in text:
        if e in d:
            d[e] += 0.5
        else:
            d[e] += 1
    return int(min(d.values()))