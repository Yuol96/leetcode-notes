"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/counting-bits/description/",
    "beats": 0.9571,
    "category": ["bit manipulation","dynamic-programming"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- x^(x-1)可以去除x的二进制最低位
"""

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0 for __ in range(num+1)]
        for i in range(1,num+1):
            dp[i] = dp[i&(i-1)] + 1
        return dp