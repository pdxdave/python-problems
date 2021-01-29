'''
Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average student `1` is `87`.
The average of student `2` is `88.6`, but with integer division is `88`.
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