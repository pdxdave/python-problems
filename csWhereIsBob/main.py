'''
Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

Examples:

csWhereIsBob(["Jimmy", "Layla", "Bob"]) ➞ 2
csWhereIsBob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
csWhereIsBob(["Jimmy", "Layla", "James"]) ➞ -1

'''
def csWhereIsBob(names):

    # 1
    # objective 10 - loops
    for i in names:
        if i == 'Bob':
            return i
    return -1

    # 2
    # The enumerate() function adds a counter as the key of
    # the enumerate object.  So we get 0 Kelly, 1 Pete, 2 Bob
    for key,value in enumerate(names):
        if value == "Bob":
            return key 
    return -1

    # 3
    # The range() function returns a sequence of numbers,
    # starting from 0 by default, and increments
    # by 1 (by default), and stops before a specified number.
    # The len() function returns the numbers of the items in
    # an object
    for i in range(len(names)):
        if names[i] == "Bob":
            return i
    return -1


    # 4
    # Objectiv 11 - list comprehensions
    person = [key for (key, value) in enumerate(names) if value == "Bob"]
    return person

names = ["Kelly", "Pete", "Bob"]
print(csWhereIsBob(names))

