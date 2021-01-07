def csWhereIsBob(names):

    # One solution
    # The enumerate() function adds a counter as the key of
    # the enumerate object.  So we get 0 Kelly, 1 Pete, 2 Bob
    for key,value in enumerate(names):
        if value == "Bob":
            return key 
    return -1


names = ["Kelly", "Pete", "Bob"]
print(csWhereIsBob(names))

