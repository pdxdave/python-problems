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
    return lst
    
print(sort_by_length(["a", "ccc", "dddd", "bb"]))

"""
A bigger discussion on sort() vs sorted()


"""
