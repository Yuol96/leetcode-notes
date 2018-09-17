"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/pacific-atlantic-water-flow/description/",
    "category": ["DFS"],
    "tags": ["border2center"],
    "questions": []
}
"""

"""
思路：
	- 从边界出发，分别考虑所有能被Pacific和Atlantic“reach”到的点，之后对集合joint，就是答案
	- 永远考虑输入为空的情况
"""

def DFS(matrix, i, j, st):
    m = len(matrix)
    n = len(matrix[0])
    st.add((i,j))
    if i>0 and (i-1,j) not in st and matrix[i-1][j] >= matrix[i][j]:
        DFS(matrix, i-1, j, st)
    if i<m-1 and (i+1,j) not in st and matrix[i+1][j] >= matrix[i][j]:
        DFS(matrix, i+1, j, st)
    if j>0 and (i,j-1) not in st and matrix[i][j-1] >= matrix[i][j]:
        DFS(matrix, i, j-1, st)
    if j<n-1 and (i,j+1) not in st and matrix[i][j+1] >= matrix[i][j]:
        DFS(matrix, i, j+1, st)
        

class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            pacific = set()
            atlantic = set()
            for i in range(m):
                DFS(matrix, i, 0, pacific)
                DFS(matrix, i, n-1, atlantic)
            for i in range(n):
                DFS(matrix, 0, i, pacific)
                DFS(matrix, m-1, i, atlantic)
            return [[item[0], item[1]] for item in pacific & atlantic]
        else :
            return []