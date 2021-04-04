'''
def makeArrayConsecutive2(statues):
    count = 0
    statues.sort()
    for i in range(len(statues)-1):
        if statues[i+1] - statues[i] > 1:
            count += statues[i+1] - statues[i] - 1
            
    return count 

statues = [6,2,3,8]
print(makeArrayConsecutive2(statues))
'''

def matrixElementsSum(matrix):

    total = 0
    bad_rooms = list()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                bad_rooms.append(col)
        for col_search in range(len(matrix[0])):
            if col_search not in bad_rooms:
                total += matrix[row][col_search]

    return total



matrix = [
    [1,1,1,0],
    [0,5,0,1],
    [2,1,3,10]
]
print(matrixElementsSum(matrix))

'''
The first for loop handles the rows.  The second for loop handles the columns.
We pull off the first row (e.g., index 0) and see if there are any 0's in the column.
If so, we get the value/index location in the column.
Then we have another separate for loop that goes through index column 0, and if there
are no badrooms in the list, we add those to the total. 
'''

