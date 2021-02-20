'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

Note on max: max() iterates over a list. For this reason,
I appended the output to the container, then passed that through
the max function.

By using the range(len()), we get both an index for the list    
and the length. 
'''

def adjacentElementsProduct(inputArray):
     container = []
     for i in range(len(inputArray)-1):
         container.append(inputArray[i] * inputArray[i + 1])
     return max(container)

inputArray = [3, 6, -2, -5, 7, 3]
print(adjacentElementsProduct(inputArray))