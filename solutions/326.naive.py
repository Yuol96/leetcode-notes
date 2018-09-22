"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/power-of-three/description/",
    "beats": 0.1752,
    "category": ["math"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = 1
        while res <= n:
            if res == n:
                return True
            res *= 3
        return False