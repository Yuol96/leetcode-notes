"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/binary-number-with-alternating-bits/description/",
    "beats": 0.7788,
    "category": ["bit manipulation"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- n ^ (n>>1)得到全11111这种形式
"""

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = n ^ (n>>1)
        return tmp&(tmp+1)==0