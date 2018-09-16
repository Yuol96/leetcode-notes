"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/unique-paths/description/",
    "category": ["dynamic-programming"],
    "tags": ["matrix-path"],
    "questions": []
}
"""

"""
思路：
	- path[i][j] = path[i-1][j] + path[i][j-1]
"""

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.path = [[0 for __ in range(n)] for __ in range(m)]
        self.path[0][0] = 1
        for k in range(1, n):
            self.path[0][k] = 1
        for k in range(1, m):
            self.path[k][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                self.path[i][j] = self.path[i-1][j] + self.path[i][j-1]
        return self.path[-1][-1]