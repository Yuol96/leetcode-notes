"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/power-of-three/description/",
    "beats": 0.7727,
    "category": ["math"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 1162261467是int范围内最大的power of 3
	- 1162261467 % n
"""

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and 1162261467%n == 0