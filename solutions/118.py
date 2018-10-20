"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/pascals-triangle/description/",
    "beats": 1.0000,
    "category": ["string"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows==1:
            return [[1]]
        ret = self.generate(numRows-1)
        lastRow = ret[-1]
        row = [1 for __ in range(numRows)]
        for idx in range(len(lastRow)-1):
            row[idx+1] = lastRow[idx]+lastRow[idx+1]
        ret.append(row)
        return ret