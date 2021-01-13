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