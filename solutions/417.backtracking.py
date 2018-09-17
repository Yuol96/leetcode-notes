"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/pacific-atlantic-water-flow/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
思路：
	- 用二进制数表示是否能流到Pacific(2)或Atlantic(1)
	- 由于water flow的条件是Height小于等于，那么很可能在等于的情况下出现循环递归，导致递归栈超过最大限制，
	因此沿着每个点递归时要记录层数；而且每条路径中已经访问的点，不能再次递；只有层数为0的递归结果才计入record
"""

def DFS(matrix, i, j, m, n, record, mark, currLen):
    """
    用二进制数表示是否能流到Pacific(2)或Atlantic(1)
    """
    if (i,j) in record:
        return record[(i,j)]
    mark.add((i,j))
    ret = 0
    if i==0 or j==0:
        ret |= 2
    if i==m-1 or j==n-1:
        ret |= 1
    # print(i,j, ret, mark)
    if i>0 and (i-1,j) not in mark and matrix[i-1][j] <= matrix[i][j]:
        ret |= DFS(matrix, i-1, j, m, n, record, mark, currLen+1)
    if i<m-1 and (i+1,j) not in mark and matrix[i+1][j] <= matrix[i][j]:
        ret |= DFS(matrix, i+1, j, m, n, record, mark, currLen+1)
    if j>0 and (i,j-1) not in mark and matrix[i][j-1] <= matrix[i][j]:
        ret |= DFS(matrix, i, j-1, m, n, record, mark, currLen+1)
    if j<n-1 and (i,j+1) not in mark and matrix[i][j+1] <= matrix[i][j]:
        ret |= DFS(matrix, i, j+1, m, n, record, mark, currLen+1)
    if currLen == 0:
        record[(i,j)] = ret
    return ret

class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix:
            ans = []
            m = len(matrix)
            n = len(matrix[0])
            record = {}
            record[(0,n-1)] = 3
            record[(m-1,0)] = 3
            for i in range(m):
                for j in range(n):
                    mark = set()
                    if DFS(matrix, i, j, m, n, record, mark, 0) == 3:
                        ans.append([i,j])
            return ans
        else:
            return []
