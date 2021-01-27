'''
You are given a directed acyclic graph (DAG) that contains N nodes.

Write a function that can find all the possible paths from node 0 to node N - 1. You can return the path in any order.

graph[a] is a list of all nodes b for which the edge a -> b exists.

Example:
 
      0   ->   1

      |        |

      2   ->   2

               |

               4

Input: graph = [[1, 2],[3],[3],[4],[]]
Output: [[0,1,3,4], [0,2,3,4]]
'''


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
