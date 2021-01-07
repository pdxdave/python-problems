def csWhereIsBob(names):

    # One solution
    # The enumerate() function adds a counter as the key of
    # the enumerate object.  So we get 0 Kelly, 1 Pete, 2 Bob
    for key,value in enumerate(names):
        if value == "Bob":
            return key 
    return -1

    # A second solution
    # The range() function returns a sequence of numbers,
    # starting from 0 by default, and increments
    # by 1 (by default), and stops before a specified number.
    # The len() function returns the numbers of the items in
    # an object

    for i in range(len(names)):
        if names[i] == "Bob":
            return i
    return -1

names = ["Kelly", "Pete", "Bob"]
print(csWhereIsBob(names))

