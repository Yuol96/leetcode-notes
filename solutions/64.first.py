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
动态规划：
	- mat[i][j] = min(mat[i-1][j], mat[i][j-1]) + grid[i][j]
"""

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        mat = [[0 for j in range(num_cols)] for i in range(num_rows)]
        mat[0][0] = grid[0][0]
        for j in range(1,num_cols):
            mat[0][j] = mat[0][j-1] + grid[0][j]
        for i in range(1,num_rows):
            mat[i][0] = mat[i-1][0] + grid[i][0]
        
        for i in range(1,num_rows):
            for j in range(1,num_cols):
                mat[i][j] = min(mat[i-1][j], mat[i][j-1]) + grid[i][j]
        return mat[num_rows-1][num_cols-1]
    