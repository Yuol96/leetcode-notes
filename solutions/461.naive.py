"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/hamming-distance/description/",
    "beats": 0.3946,
    "category": ["bit manipulation"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        tmp = x^y
        count = 0
        while tmp>0:
            count += (tmp&1)
            tmp >>= 1
        return count