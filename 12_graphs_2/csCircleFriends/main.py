'''
There are N students in a baking class together. Some of them are friends, while some are not friends. The students' friendship can be considered transitive. This means that if Ami is a direct friend of Bill, and Bill is a direct friend of Casey, Ami is an indirect friend of Casey. A friend circle is a group of students who are either direct or indirect friends.

Given a N*N matrix M representing the friend relationships between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.

You need to write a function that can output the total number of friend circles among all the students.

Each row is a person, as is each column.
Person 0 is a friend with themself and person 1, but not person 2
Person 1 is a friend with themself and person 1, but not person 2
Person 2 is a friend with themself, but not person 1 or 2
Output: 2

[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 1]]
'''
def csFriendCircles(friendships):
    
    # BFS
    
    students = set(list(range(len(friendships))))
    circles = 0
    while len(students)>0:
        student = students.pop()
        queue = [student]
        while queue:
            student = queue.pop(0)
            for ind, is_friend in enumerate(friendships[student]):
                if is_friend and ind in students:
                    queue.append(ind)
                    students.remove(ind)
        circles += 1
            
    return circles

friendships:
[[1,1,0], 
 [1,1,0], 
 [0,0,1]]
 # output is 2

    # DFS
'''


'''
def csFriendCircles(friendships):
    
    count = 0  # for groups
    seen = set()
    
    for person in range(len(friendships)):
        if person not in seen:
            count += 1
            dfs(person, friendships, seen)
    return count

def dfs(node, friendship, seen):
    for person, is_friend in enumerate(friendship[node]):
        if is_friend and person not in seen:
            seen.add(person)
            dfs(person, friendship, seen)

http://pythontutor.com/visualize.html#code=def%20csFriendCircles%28friendships%29%3A%0A%20%20%20%20%0A%20%20%20%20count%20%3D%200%20%20%23%20for%20groups%0A%20%20%20%20seen%20%3D%20set%28%29%0A%20%20%20%20%0A%20%20%20%20for%20person%20in%20range%28len%28friendships%29%29%3A%0A%20%20%20%20%20%20%20%20if%20person%20not%20in%20seen%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20count%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20dfs%28person,%20friendships,%20seen%29%0A%20%20%20%20return%20count%0A%0Adef%20dfs%28node,%20friendship,%20seen%29%3A%0A%20%20%20%20for%20person,%20is_friend%20in%20enumerate%28friendship%5Bnode%5D%29%3A%0A%20%20%20%20%20%20%20%20if%20is_friend%20and%20person%20not%20in%20seen%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20seen.add%28person%29%0A%20%20%20%20%20%20%20%20%20%20%20%20dfs%28person,%20friendship,%20seen%29%0A%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%0Afriendships%20%3D%20%5B%5B1,1,0%5D,%20%5B1,1,0%5D,%20%5B0,0,1%5D%5D%20%20%0Aprint%28csFriendCircles%28friendships%29%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

# 3 another DFS solution

def csFriendCircles(friendships):
    
    count = 0  # for groups
    seen = set()
    
    def dfs(person):
        for i in range(len(friendships)):
            if friendships[person][i] and i not in seen:
                seen.add(i)
                dfs(i)
    
    for i in range(len(friendships)):
        if i not in seen:
            count += 1
            seen.add(i)
            dfs(i)
    return count
    
friendships = [
    [1,1,0], 
    [1,1,0], 
    [0,0,1]
    ]
print(csFriendCircles(friendships))

'''
A couple of things we need to solve
1. We need a counter for the groups
2. We need to see if we've seen a person so we don't find ourselves in a loop.
3. We need to be able to loop through each person, and also the associations w/in each person
'''
'''
friendships = [
[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
]
returns 8

'''