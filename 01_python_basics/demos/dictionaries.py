"""
In its most basic form, a dictionary is like an object in Javascript

something = {
    "thing": "car",
    "food": "apple",
    "color": "green"
}

Dictionary collections are unordered and changeable. 
There are no duplicates
"""
# 1
def dictTest(something):
    
    for key, value in something.items():
        print(key, ':', value)
    
something = {
    "thing": "car",
    "food": "apple",
    "color": "green"
}
dictTest(something)

# 2
"""
Dictionaries can be used to identify duplictes in a list and count
the number of duplicates.  Returned as a dictionary.
"""
def dictTest(names):
    
    namesDict = {}
    
    for i in range(len(names)):
        namesDict[names[i]] = names.count(names[i])
        
    return namesDict
    
names = ['sara', 'frank', 'peter','alen', 'kelly','frank', 'peter','sara', 'frank']
print(dictTest(names))
""" {'sara': 2, 'frank': 3, 'peter': 2, 'alen': 1, 'kelly': 1} """

# 3
"""
What if we were to take the same problem above, but return the names
sorted.  Notice how they're returned in a list as tuples. This is because
dictionaries are unordered.  To sort the data, they're returned as tuples. 
"""

def dictTest(names):
    
    namesDict = {}
    
    for i in range(len(names)):
        namesDict[names[i]] = names.count(names[i])
        
    sorted_names = sorted(namesDict.items(), key=lambda kv: kv[0])
    
    return sorted_names
    
names = ['sara', 'frank', 'peter','alen', 'kelly','frank', 'peter','sara', 'frank']
print(dictTest(names))
"""[('alen', 1), ('frank', 3), ('kelly', 1), ('peter', 2), ('sara', 2)]"""