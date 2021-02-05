'''
https://www.youtube.com/watch?v=VtidkqqPAXQ&list=PL0TTS7q_BAXVVDcBxPcLrNyddAokMWHdk&index=5&t=5284s
'''

"""
# 1

Create a function that takes two numbers as arguments and return their sum.

Examples: 
- additon(3,2) -> 5
- addtion(-3, -9) -> -9
- addtion(7,3) -> 10
"""
def addition(a,b):
    # solve = a + b
    # return solve
    return a + b
print(addition(3,2))



"""
# 2

Write a function that takes an integer 'minutes' and converts it to seconds

Examples: 
- convert(5) -> 300
- convert(3) -> 180
- convert(2) -> 120
"""
def convert(minutes):
    # seconds = 60
    # return minutes * seconds
    return minutes * 60
print(convert(5))



"""
# 3

Create a function that takes a string and returns it as an integer

Examples: 
- string_int("6") -> 6
- string_int("1000") -> 1000
- string_int("12") -> 12
"""
def string_int(txt):
    return int(txt)

print(string_int("6"))



"""
# 4

Create a function that takes length and width and finds the perimter of a rectangle

Examples: 
- find_perimeter(6,7) -> 26
- find_perimeter(20, 10) -> 60
- find_perimeter(2,9) -> 22
"""
def find_perimeter(length, width):
    return (length + width) * 2
    
print(find_perimeter(6,7))

"""
# 5

Create a function that returns a list of strings sorted by length in ascending order

Examples: 
- sort_by_length(["a", "ccc", "dddd", "bb"]) -> ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) -> ["pie", "apple", "shortcake"]
- sort_by_length([]) -> []

* The sort() method sorts the list ascending by default.
* list.sort(reverse=True|False, key=myFunc)
* key is optional. A function to specify the sorting criteria(s)
"""
def sort_by_length(lst):

    lst.sort()
    print(f"this is sort {lst}")
    
sort_by_length(["a", "ccc", "dddd", "bb"])

def sort_by_length(lst):

    lst.sort(reverse=True)
    print(f"this is sort with reverse {lst}")
    
sort_by_length(["a", "ccc", "dddd", "bb"])

"""
sort() vs sorted()

sort() will modify the list it is called on.  The sorted() function will create
a new list containing the sorted version of the given list.

sorted() will return a list so you must assign the returned data to a new
variable.

"""
def sort_by_length(lst):

    newSort = sorted(lst)
    print(f"this is sorted {newSort}")
    
sort_by_length(["a", "ccc", "dddd", "bb"])

def sort_by_length(lst):

    newSort = sorted(lst, reverse=True)
    print(f"this is sorted with reverse {newSort}")
    
sort_by_length(["a", "ccc", "dddd", "bb"])

"""
An example using the key parameter with sorted
"""
def sort_by_length(lst):

    newSort = sorted(lst, key=len)
    return newSort
    
print(sort_by_length(["aaaaaaaa", "ccc", "dddd", "bbbbbbb"]))
# ['ccc', 'dddd', 'bbbbbbb', 'aaaaaaaa']

"""
An example using the key parameter with sort
"""
def sort_by_length(lst):

    lst.sort(key=len)
    return lst
    
print(sort_by_length(["aaaaaaaa", "ccc", "dddd", "bbbbbbb"]))
# ['ccc', 'dddd', 'bbbbbbb', 'aaaaaaaa']

"""

And we can use key with a lambda function.  What is a lambda function?

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
* lambda arguments : expression
"""

# 1
test1 = lambda x: 3*x + 1
print(test1(2))

#2
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("   joe", "SMITH"))


"""
# 9

Write a function that creates a dictionary with each (key, value) pair being
the (lower case, upper case) versions of a letter.

mapping(["a", "b", "c"]) => {"a": "A", "b": "B", "c": "C"}
"""
def mapping(letters):

    lst = {}
    for i in letters:
        lst[i] = i.upper()

    return lst

letters = ["a", "b", "c"]
print(mapping(letters))




