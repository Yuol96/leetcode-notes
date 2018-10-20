"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/power-of-four/description/",
    "beats": 0.9952,
    "category": ["bit manipulation"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- (num&(-num)==num)保证是2^x
	- (num&1431655765>0)保证只在偶数位上为1
	- please refer to `231.py`
"""

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num>0 and (num&(-num)==num) and (num&1431655765>0)