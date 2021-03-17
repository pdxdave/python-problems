'''
Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.
Example

For sequence = "()", the output should be validBracketSequence(sequence) = true;
For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
For sequence = "(]", the output should be validBracketSequence(sequence) = false;
For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.

If the current character is a starting bracket (‘(‘ or ‘{‘ or ‘[‘) then push it to stack.
If the current character is a closing bracket (‘)’ or ‘}’ or ‘]’) then pop from stack and if the popped character is the matching starting bracket then it is True, otherwise it's False.
'''
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
sequence = "[[(({()}))]]{()}[({})]" # True
print(validBracketSequence(sequence))