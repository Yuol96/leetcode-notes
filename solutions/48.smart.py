"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/rotate-image/description/",
    "beats": 0.9942,
    "category": ["array"],
    "tags": ["in-place"],
    "questions": []
}
"""

"""
思路
	- 先把matrix的行反序，即matrix[::-1]
	- 再沿对角线交换元素
"""

class Solution:
    def reverseRow(self, matrix,n):
        for i in range(n//2):
            matrix[i],matrix[n-1-i] = matrix[n-1-i],matrix[i]
    
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        self.reverseRow(matrix,n)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]