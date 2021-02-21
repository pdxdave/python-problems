'''
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Walkthrough: 

The first edge case.  One test has [1,1] list as true.  So if the sequence equals    
two, I have that default to true.

In this case, if sequence 3 <= sequence 1, we add one to a counter for a delete.
But, in this situation, it's not.  So we move to the next if statement.

If sequence 1 <= sequence 3, which it is, and 3 >= 0, which it is...     
We move on to the next if statement.
If, in this case, 1 != to the length of the array, which it doesn't,     
and 3 <= 2, which it isn't, we return False.

'''
def almostIncreasingSequence(sequence):
    if len(sequence) == 2:
        return True
    
    counter = 0
    for i in range(0,len(sequence)-1):
        if sequence[i+1] <= sequence[i]:
            counter +=1
            if counter > 1:
                return False
        
        if sequence[i] <= sequence[i-2] and i-2 >=0:
            if i != len(sequence)-1 and sequence[i+1] <= sequence[i-1]:
                return False
    return True


sequence = [1, 3, 2]
print(almostIncreasingSequence(sequence))