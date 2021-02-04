'''
Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

Examples:

csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"
'''

def csLongestPossible(str_1, str_2):

    # concatenate all the letters into one string
    letters = (str_1 + str_2)

    '''
    From the inside, the set() puts the letters into a set like
    {'r','y','t'...}. Next, sorted() sorts them alphabetically.
    And finally, join() joins them with "" around the returned string
    '''

    arrange = "".join(sorted(set(letters)))

    return arrange

str_1 = "aabbbcccdef"
str_2 = "xxyyzzz"
print(csLongestPossible(str_1, str_2))