'''
Given a string, write a function that returns the index of the first unique (non-repeating) character. If there isn't a unique (non-repeating) character, return -1.
'''

def firstUniqChar(input_str):
    
        lookup = {}
        # or lookup = dict()
        
        # The first loop populates the dictionary with counts
        # for each character
        for i in input_str:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
                
        # The second loop identifies the index of the first unique
        # non repeating character
        for index, value in enumerate(input_str):
            if lookup[value] == 1:
                return index
                # return value  to show the character
        
        return -1
                
                
input_str = "lambdaschool"
print(firstUniqChar(input_str))


#2
'''
This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.
A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.
'''
from collections import Counter

def csFirstUniqueChar(input_str):
    
    counter = Counter(input_str)
    
    for index, value in enumerate(input_str):
        if counter[value] == 1:
            return index
    return -1
    
input_str = "lambdaschool"
print(firstUniqChar(input_str))