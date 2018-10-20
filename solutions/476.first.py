"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/number-complement/description/",
    "beats": 0.3761,
    "category": ["bit manipulation"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 此问题归结为求补码
	- 利用最长32位的特点
"""

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = num
        mask |= mask>>1
        mask |= mask>>2
        mask |= mask>>4
        mask |= mask>>8
        mask |= mask>>16
        return num^mask