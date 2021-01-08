# You are given a parentheses sequnece.

# ()()(()) = true
# ()()()) = false
# )()() = false

def validParenthesesSequence(s):

    count = 0

    for item in s:
        if item == "(":
            count += 1
        elif item == ")":
            count -= 1
        if count == -1:
            return False
    if count == 0:
        return True
    else:
        return False

s= ")()()("
print(validParenthesesSequence(s))

'''
The trick to this problem is to give "(" and ")" values.
In this case the value of "(" is 1 and ")" is -1. The goal is to end up with a total count of 0, which indicates an equal amount of open/close parentheses. 
'''