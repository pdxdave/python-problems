'''
Given a pattern and a string a, find if a follows the same pattern.

Here, to "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in s.

Example 1:

Input:
pattern = "abba"
a = "lambda school school lambda"

Output: true
Example 2:

Input:
pattern = "abba"
a = "lambda school school coding"

Output:
false

'''


def csWordPattern(pattern, a):
    
    strs = a.split()
    
    if len(pattern) != len(strs):
        return False
        
    d = dict()
    for i, p in enumerate(pattern):
        if p not in d:
            d[p] = strs[i]
        else:
            if d[p] != strs[i]:
                return False
                
    for i, p in enumerate(strs):
        if p not in d:
            d[p] = pattern[i]
        else:
            if d[p] != pattern[i]:
                return False
    return True
    
    
pattern = "abba"
t = "lambda school school lambda"
print(csWordPattern(pattern, t))