"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/toeplitz-matrix/",
    "beats": 0.2970,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def check(self, matrix, i, j):
        v = matrix[i][j]
        step = 1
        while i+step<self.M and j+step<self.N:
            if matrix[i+step][j+step]!=v:
                return False
            step += 1
        return True
    
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        self.M = len(matrix)
        self.N = len(matrix[0])
        for i in range(self.M):
            if not self.check(matrix, i, 0):
                return False
        for j in range(1,self.N):
            if not self.check(matrix, 0, j):
                return False
        return True
            