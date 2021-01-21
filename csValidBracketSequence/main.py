def validBracketSequence(sequence):
    
    openers = set(['(', '[', '{'])
    closers = set([')', ']', '}'])
    
    pairs = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    stack = []
    
    for char in sequence:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if not stack or pairs[stack.pop()] != char:
                return False 
    return len(stack) == 0
    
sequence = "()[]{}" # true
sequence = "([)]" # false
print(validBracketSequence(sequence))