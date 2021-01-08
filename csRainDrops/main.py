# Given a number, write a function that converts that
# number into a string that contains "raindrop sounds" 
# corresponding to certain potential factors.  A factor
# is a number that evenly divides into another number,
# leaving no remainder.

# if factor of 3 add Pling to result
# if factor of 5 add Pling to result
# if factor of 7 add Pling to result

def csRaindrops(number):
    result = ""

    if number %3 == 0:
        result += "Pling"
    if number %5 == 0:
        result += "Plang"
    if number %7 == 0:
        result += "Plong"

    if result == "":
        return str(number)

    return result

number = 28
print(csRaindrops(number))