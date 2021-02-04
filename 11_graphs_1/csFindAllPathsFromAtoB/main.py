'''
You are given a directed acyclic graph (DAG) that contains N nodes.

Write a function that can find all the possible paths from node 0 to node N - 1. You can return the path in any order.

graph[a] is a list of all nodes b for which the edge a -> b exists.

Example:
 
      0   ->   1

      |        |

      2   ->   3

               |

               4
                  
Input: graph = [[1, 2],[3],[3],[4],[]]
Output: [[0,1,3,4], [0,2,3,4]]
'''

   
'''
     [1,2] means that 0 has an outgoing edge to 1 and 2
     [3]   means that 1 has an outgoing edge to 3
     [3]   means that 2 has an outgoing edge to 3
     [4]   means that 3 has an outgoing edge to 4
     []    means that 4 does not have an outgoing edge

  Start with the source node 0. This would be [1,2]
'''
#1 
def csFindAllPathsFromAToB(graph):
    
    result = list()
    
    def depthFirst(start, temp):
        if graph[start] == []:
            temp += graph[start]
            result.append(temp[:])
            return
    
        test = graph[start]
        for connection in test:
            temp.append(connection)
            depthFirst(connection, temp)
            temp.pop()
        
    depthFirst(0, [0])
    return result


# 2

def csFindAllPathsFromAToB(graph):
    
    result = []
    
    def depthfirst(n = 0, starting = [0]):
        if n < len(graph)-1:
            for i in graph[n]:
                depthfirst(i, starting+[i])
        else:
            result.append(starting)
    depthfirst()
    return result
        
    #       0    1   2   3   4
graph = [[1, 2],[3],[3],[4],[]]
print(csFindAllPathsFromAToB(graph))