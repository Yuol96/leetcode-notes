"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/valid-perfect-square/description/",
    "beats": 0.0578,
    "category": ["math"],
    "tags": ["square"],
    "questions": []
}
"""

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        for i in range(1, num):
            square = i*i
            if square == num:
                return True
            elif square > num:
                break
        return False