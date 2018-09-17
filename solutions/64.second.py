"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/minimum-path-sum/description/",
    "category": ["dynamic-programming"],
    "tags": ["matrix-path"],
    "questions": []
}
"""

"""
思路：
	- mat[i][j] = min(mat[i-1][j], mat[i][j-1]) + grid[i][j]
"""

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        self.path = [[0 for __ in range(self.n)] for __ in range(self.m)]
        self.path[0][0] = grid[0][0]
        for k in range(1, self.n):
            self.path[0][k] = self.path[0][k-1] + grid[0][k]
        for k in range(1, self.m):
            self.path[k][0] = self.path[k-1][0] + grid[k][0]
        for i in range(1,self.m):
            for j in range(1,self.n):
                self.path[i][j] = min(self.path[i-1][j], self.path[i][j-1]) + grid[i][j]
        return self.path[-1][-1]