"""
{
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/max-area-of-island/description/",
    "category": ["DFS"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def DFS(self, grid, i, j, h, w):
        if grid[i][j] == 0:
            return 0
        num = 1
        grid[i][j] = 0
        if i>0:
            num += self.DFS(grid, i-1, j, h, w)
        if i<h-1:
            num += self.DFS(grid, i+1, j, h, w)
        if j>0:
            num += self.DFS(grid, i, j-1, h, w)
        if j<w-1:
            num += self.DFS(grid, i, j+1, h, w)
        return num
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])
        maxArea = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j]:
                    maxArea = max(self.DFS(grid, i, j, h, w), maxArea)
        return maxArea