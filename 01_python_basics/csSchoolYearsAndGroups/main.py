# Imagine a school that children attend for years.  In each year,
# there are a certain number of groups started, marked with
# the letters.  So if years = 7 and groups = 4 for the the first
# year, the groups are 1a, 1b, 1c, 1d and the last year 7a, 7b,
# 7c, 7d

'''
The chr() method returns a character (a string) from an integer (the unicode numeric representation of the character )
chr(97) = 'a'

The ord() method returns an integer representing the Unicode character
ord('a') = 97
'''

def csSchoolYearsAndGroups(years, groups):
    results = ""

    for year in range(1, years + 1):
        for group in [chr(i) for i in range(ord('a'), ord(chr(97 + groups)))]:
            results += (str(year) + group + ", ")
    return results[: -2]


years = 4
groups = 2
# returns 1a, 1b, 2a, 2b, 3a, 3b, 4a, 4b
print(csSchoolYearsAndGroups(years, groups))

'''
A walkthrough of the solution. Two loops. One for years and one for groups.

Line 18 loops through the range of years.  We need years + 1, because we're starting with
year 1.  Range normally starts with 0. If we didn't, the above years would be passed through
as 1 to 3. 

Line 19 is another loop to handle the groups.
Starting with the range. ord('a') will return 97. ord(chr(97 + groups))) will first take in the numeric value from groups and add to 97; for instance, 97 + 1 = 98, 98 + 1 = 98. chr will turn those into letters, then ord will turn them into integers.  chr(i) takes that integer and turns it into a string (e.g., a, b, c, etc).

The results [: -2] returns the solution without the trailing comma and quote mark.
'''

#2

def csSchoolYearsAndGroups(years, groups):

    res = []

    for i in range(1, years + 1):
        for j in range(97. groups + 97):
            res.append(f"{i}{chr(j)}")
    return ", ".join(res)
