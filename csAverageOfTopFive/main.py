'''
Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average student `1` is `87`.
The average of student `2` is `88.6`, but with integer division is `88`.

The key of the map will be the students ID, and the value of the map will be the score.

1. Let's put the user id's and scores in their own list.  For instance, {1: [91, 92], 2: [93, 97]}
How could we do this?

2. Then we can order the key,values in a tuple using score_map.items().  It would give us something like 
([(1, [91, 92, 60, 65, 87, 100]), (2, [93, 97, 77, 100, 76])])

3. We can then sort the values in reverse order giving us [100, 92, 91, 87, 65, 60]

4. 
'''


def csAverageOfTopFive(items):
    
        
        score_map = {}
        for item in items:
            if item[0] in score_map:
                score_map[item[0]].append(item[1])
            else:
                score_map[item[0]] = [item[1]]
                
        result = []
        for key, value in score_map.items():
            value.sort(reverse=True)
            if len(value) >= 5:
                average = value[:5]
            else:
                average = value
            score_map[key] = sum(average)//len(average)
            result.append([key, score_map[key] ])
        
        return result
        
items=[[1,91], [1,92], [2,93], [2,97], [1,60], [2,77], [1,65], [1,87], [1,100], [2,100], [2,76]]
print(csAverageOfTopFive(items))