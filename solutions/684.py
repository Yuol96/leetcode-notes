"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/redundant-connection/description/",
    "beats": 0.7612,
    "category": ["graph"],
    "tags": ["union-find","*685"],
    "questions": []
}
"""

class Solution:
    def find(self, lst, i):
        j = i
        while lst[j] is not None:
            j = lst[j]
        while lst[i] is not None:
            tmp = lst[i]
            lst[i] = j
            i = tmp
        return j
    
    def union(self, lst, a, b):
        a = self.find(lst, a)
        b = self.find(lst, b)
        if a!=b:
            lst[b] = a
    
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        lst = [None for __ in range(N)]
        # print(N)
        for edge in edges:
            a = self.find(lst, edge[0]-1)
            b = self.find(lst, edge[1]-1)
            if a==b:
                lastEdge = edge
                continue
            self.union(lst, a, b)
        return lastEdge