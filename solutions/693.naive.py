"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/binary-number-with-alternating-bits/description/",
    "beats": 0.2565,
    "category": ["bit manipulation"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lastBit = n&1
        n >>= 1
        while n>0:
            if lastBit == n&1:
                return False
            lastBit = n&1
            n >>= 1
        return True