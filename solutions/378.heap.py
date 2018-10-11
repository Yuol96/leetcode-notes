"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/",
    "beats": 0.0417,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 把matrix看成n个列，用min heap去存储每列的队首（即每列最小元素）
	- 然后pop k次min heap，每次pop之后用pop出来的元素的那一列的后一个元素填充。
"""

from queue import PriorityQueue

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        q = PriorityQueue()
        for i in range(n):
            q.put((matrix[0][i], 0, i))
        rank = 0
        while True:
            rank += 1
            val, i, j = q.get()
            # print(rank, val, i, j)
            if rank == k:
                return val
            if i<n-1:
                q.put((matrix[i+1][j], i+1, j))
