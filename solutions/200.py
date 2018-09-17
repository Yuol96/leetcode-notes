"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/number-of-islands/description/",
    "category": ["DFS"],
    "tags": [],
    "questions": []
}
"""

"""
ATTENTION
	- 输入的gird里面是str！！！而不是integer！！！因此在写if时不能写`if grid[i][j]: xxx`
"""

def DFS(grid, i, j, h, w):
    if grid[i][j] == "1":
        grid[i][j] = 0
        if i>0:
            DFS(grid, i-1, j, h, w)
        if j>0:
            DFS(grid, i, j-1, h, w)
        if i<h-1:
            DFS(grid, i+1, j, h, w)
        if j<w-1:
            DFS(grid, i, j+1, h, w)

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid:
            h = len(grid)
            w = len(grid[0])
            count = 0
            for i in range(h):
                for j in range(w):
                    if grid[i][j] == "1":
                        count += 1
                        DFS(grid, i, j, h, w)
            return count
        return 0