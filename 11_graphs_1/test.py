# Example 1
'''
   A - F - C
    \     / \
     \  /    \
       B ---- D
        \
         E
'''
graph_list = {
    'A': {'B'},
    'B': {'C', 'D', 'E'},
    'C': {'D'},
    'D': {},
    'E': {}
}

graph_list['F'] = {'C'}
graph_list['A'].add('F')
graph_list['C'].add('F')

def print_paths(graph, start_vertex, current_path):
    current_path = [start_vertex]

    if len(graph[start_vertex]) == 0:
        print(current_path)

    # for each neighbor, call print_paths, with the current_path containing our current_vertex
    for neighbor in graph[start_vertex]:
        print_paths(graph, neighbor, current_path)