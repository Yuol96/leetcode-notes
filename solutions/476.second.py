"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/number-complement/description/",
    "beats": 0.9911,
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
        mask = 1<<30
        while mask&num==0:
            mask >>= 1
        mask = (mask<<1)-1
        return num^mask