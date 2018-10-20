"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/course-schedule-ii/description/",
    "beats": 0.1097,
    "category": ["graph"],
    "tags": ["DAG","*"],
    "questions": []
}
"""

"""
思路
	- 拓扑排序
"""

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        degrees = [0 for __ in range(numCourses)]
        graph = [[] for __ in range(numCourses)]
        for edge in prerequisites:
            degrees[edge[0]] += 1
            graph[edge[1]].append(edge[0])
        # print(degrees)
        # print(graph)
        lst = []
        taken = set()
        while True:
            count = 0
            for i in range(numCourses):
                if degrees[i]==0 and i not in taken:
                    count += 1
                    taken.add(i)
                    lst.append(i)
                    for j in graph[i]:
                        degrees[j] -= 1
            if count == 0:
                break
        # print(lst,taken,degrees)
        if len(lst) == numCourses:
            return lst
        return []