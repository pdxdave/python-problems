'''
Given an array of strings strs, write a function that can group the anagrams. The groups should be ordered such that the larger groups come first, with subsequent groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input:
strs = ["apt","pat","ear","tap","are","arm"]

Output:
[["apt","pat","tap"],["ear","are"],["arm"]]
Example 2:

Input:
strs = [""]

Output:
[[""]]

'''

def csGroupAnagrams(strs):
    
    dict = {}
    result = []
    
    for word in strs:
        sortme = "".join(sorted(word))
        
        if sortme not in dict:
            dict[sortme] = [word]
            
        else:
            dict[sortme].append(word)
            
        
    for item in dict.values():
        result.append(item)
    return result


strs = ["apt", "pat", "ear", "tap", "are", "arm"]
print(csGroupAnagrams(strs))