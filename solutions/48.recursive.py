"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/rotate-image/description/",
    "beats": 0.4723,
    "category": ["array"],
    "tags": ["in-place"],
    "questions": []
}
"""

"""
思路
	- 用递归的方式，一层层旋转
"""

class Solution:
    def recurr(self, matrix, l, r):
        if r-l<1:
            return
        self.recurr(matrix, l+1, r-1)
        for i in range(r-l):
            matrix[l+i][r],matrix[r][r-i],matrix[r-i][l],matrix[l][l+i] = \
            matrix[l][l+i],matrix[l+i][r],matrix[r][r-i],matrix[r-i][l]
    
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        self.recurr(matrix,0,n-1)