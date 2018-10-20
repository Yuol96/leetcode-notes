"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/course-schedule/description/",
    "beats": 0.1556,
    "category": ["graph"],
    "tags": ["DAG","*"],
    "questions": []
}
"""

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for __ in range(numCourses)]
        degrees = [0 for __ in range(numCourses)]
        for edge in prerequisites:
            degrees[edge[0]] += 1
            graph[edge[1]].append(edge[0])
        # print(degrees)
        # print(graph)
        taken = set()
        while True:
            count = 0
            for i in range(numCourses):
                if degrees[i]==0 and i not in taken:
                    count += 1
                    taken.add(i)
                    for j in graph[i]:
                        degrees[j] -= 1
            if count == 0:
                break
        return len(taken)==numCourses
