'''
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

What's happening here. First we sort the array to [2, 3, 6, 8].     
Next, we point our pointer on index 1 and compare it to index 0.    
If there's a difference of more than 1, then we subtract index 0 from 1    
and shave off one additional.  The reason for this is because we're looking    
for how many numbers are needed to close the gap.
For instance, 6 - 3 = 3, but from 3 to 6 only requires to additional     
numbers: 4 and 5.  In this case, it takes two numbers to close that gap.
'''
def makeArrayConsecutive2(statues):
    count = 0
    statues.sort()
    for i in range(0, len(statues)-1):
        if statues[i+1] - statues[i] > 1:
            count += statues[i+1] - statues[i] - 1
            
    return count 

statues = [6,2,3,8]
print(makeArrayConsecutive2(statues))