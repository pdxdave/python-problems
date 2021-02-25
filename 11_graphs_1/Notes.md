#### What is a graph?
- It holds data
- It discribes relationships

```
    person 1  -----   person 2
                      /
                     /
                 person 3
```
In this example there is a relationship between person1     
and person2, and person2 and person3.  But no relationship    
between person1 and person3. 

#### How to describe graphs
```
     vertex    edge    vertex
    person 1  <----->   person 2
                       / 
                      / edge
                     /
                 person 3
                   vertex
```

'''
The most important consideration when creating a graph is,    
given some vertex can I find my neighbors?
'''
## Example
```
   A       C
    \     / \
     \  /    \
       B ---- D
        \
         E
```
```
Two ways to code up this relationship
- adjacency matrix
- adjacency list
```


## Adjacency matrix
```
        A  B  C  D  E
    A   0  1  0  0  0
    B   1  0  1  1  1
    C   0  1  0  1  0
    D   0  1  1  0  0
    E   0  1  0  0  0 
   
   zero is no relationship, one is a relationship

graph_matrix = [
    [0,1,0,0,0],
    [1,0,1,1,1],
    [0,1,0,1,0],
    [0,1,1,0,0],
    [0,1,0,0,0],
]
```
### What are the neighbors for A?      
graph_matrix[0] gives all the neighbors for A

### Is B and C connected?     
graph_matrix[1][2] == 1

### Add a connection from A to C
graph_matris[0][2] = 1

## Adjacency List
```
        A  B  C  D  E
    A   0  1  0  0  0
    B   1  0  1  1  1
    C   0  1  0  1  0
    D   0  1  1  0  0
    E   0  1  0  0  0 
   
   zero is no relationship, one is a relationship
```
This particular matrix contains a lot of zeros because     
there are not a lot of connections.  In this case, an       
adjacency list might be a better option.     

Consider using a dictionary    
keys -> vertcies
```
  graph_list = {
      'A': {'B'},
      'B': {'A', 'C', 'D', 'E'},
      'C': {'B', 'D'},
      'D': {'B', 'C'}
      'E': {'B'}
  }
```
### What are the neighbors for A?
graph_list['A']

### Is B and C connected?
'C' in graph_list['B']  // will return true

### Add a connection from A to C?
graph_list['A'].add('C')

### Add a new vertex and connect A and C to it     
graph_list['F] = {'A','C'}     
graph_list['A'].add('F')      
graph_list['C'].add('F')