"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/valid-perfect-square/description/",
    "beats": 0.2888,
    "category": ["math"],
    "tags": ["square"],
    "questions": []
}
"""

"""
思路
	- 完全平方数的序列的差值序列是个等差数列
"""

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        delta = 1
        while num>0:
            num -= delta
            delta += 2
        if num == 0:
            return True
        return False