# Given a sorted array (in ascending order) of integers and a target, write  function that finds the two integers that up to the target

def csSortedTwoSum(numbers, target):

    my_table = {}

    '''
    The first for loop goes through the length of the numbers array
    and populates the my_table dictionary with the key/value pairs
    of the elements in the array. For instance, {3:0, 4:1, 5:2}
    '''
    '''
    The second for loop goes through the array and grabs the incoming
    target number.  It takes that taget and subtracts the number 
    associated with the index.  From there it compares the number
    in the table in the index to the number it needs to get the value
    needed.
    '''
    for i in range(len(numbers)):
        my_table[numbers[i]] = i

    for i in range(len(numbers)):
        compliment = target - numbers[i]

        if compliment in my_table and my_table[compliment] != i:
            return [i, my_table[compliment]]

numbers = [3,8,12,16]
target = 11
print(csSortedTwoSum(numbers, target))