'''
Given two strings a and b, determine if they are isomorphic.

Two strings are isomorphic if the characters in a can be replaced to get b.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: 
a = "odd"
b = "egg"

Output:
true
Example 2:

Input:
a = "foo"
b = "bar"

Output:
false
'''

def csIsomorphicStrings(a, b):
    
    if len(a) != len(b):
        return False
    dic={}
    for i,x in enumerate(a):
        if x in dic.keys() and dic[x]!=b[i]:
            return  False
        elif x not in dic.keys() and b[i] in dic.values():
            return False
        else:
            dic[x]=b[i]
                
    return True
    
  
a = "add"
b = "egg"
print(csIsomorphicStrings(a, b))