"""
In its most basic form, a dictionary is like an object in Javascript

something = {
    "thing": "car",
    "food": "apple",
    "color": "green"
}

Dictionary collections are unordered and changeable. 
There are no duplicates
To loop through a dictionary getting both keys and values, use .items(),
otherwise .values()
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
sorted. We'll get a return of tuples b/c dictionaries are not sorted. 
"""

def dictTest(names):
    
    namesDict = {}
    
    for i in range(len(names)):
        namesDict[names[i]] = names.count(names[i])
        
    sorted_names = sorted(namesDict.items())
    
    return sorted_names
    
names = ['sara', 'frank', 'peter','alen', 'kelly','frank', 'peter','sara', 'frank']
print(dictTest(names))
"""[('alen', 1), ('frank', 3), ('kelly', 1), ('peter', 2), ('sara', 2)]"""

# 4
"""
What if we were to take the same problem above, but return the names by value?
Here we can use a lambda anonymous function. 
"""

def dictTest(names):
    
    namesDict = {}
    
    for i in range(len(names)):
        namesDict[names[i]] = names.count(names[i])
        
    sorted_names = sorted(namesDict.items(), key=lambda kv: kv[1])
    
    return sorted_names
    
names = ['sara', 'frank', 'peter','alen', 'kelly','frank', 'peter','sara', 'frank']
print(dictTest(names))
"""[('alen', 1), ('kelly', 1), ('sara', 2), ('peter', 2), ('frank', 3)]"""


#5 
"""
What if you have a list of dictionaries, but there are duplicates?  
This is one way to remove them.
"""

def dictTest(names):
    
    seen = set()
    result = []
    for n in names:
        get_items = tuple(n.items())
        if get_items not in seen:
            seen.add(get_items)
            result.append(n)
    
    return result

names = [
    {'frank': 123},
    {'steve': 456},
    {'frank': 123},
    {'kelly': 789}
]
print(dictTest(names))
"""[{'frank': 123}, {'steve': 456}, {'kelly': 789}]"""