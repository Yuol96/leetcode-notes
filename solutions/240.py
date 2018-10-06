"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/search-a-2d-matrix-ii/description/",
    "beats": 0.1394,
    "category": ["array"],
    "tags": ["BST"],
    "questions": []
}
"""

"""
思路
	- 从右上角开始，类似BST的搜索
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        i,j = 0,n-1
        while i<m and j>=0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False