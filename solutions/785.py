"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/is-graph-bipartite/description/",
    "beats": 0.0213,
    "category": ["graph"],
    "tags": ["bipartite"],
    "questions": []
}
"""

"""
思路
	- BFS，相邻点着不同色
	- 需要考虑可能有不连通的子图的情况
"""

from queue import Queue

class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        N = len(graph)
        groups = [set(),set()]
        q = Queue()
        for i in range(N):
            if i not in groups[0] and i not in groups[1]:
                q.put((i,0))
                while not q.empty():
                    i,group = q.get()
                    # print(i,group)
                    if i in groups[1-group]:
                        return False
                    groups[group].add(i)
                    for j in graph[i]:
                        if j not in groups[0] and j not in groups[1]:
                            q.put((j,1-group))
        return True



