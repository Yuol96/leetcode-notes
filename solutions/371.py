"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/sum-of-two-integers/description/",
    "beats": 0.1032,
    "category": ["bit manipulation"],
    "tags": ["**"],
    "questions": []
}
"""

"""
思路
	- 不考虑进位的情况下，a^b就是两个数的和
	- 而(a&b)<<1就是两个数的进位
	- 如果用c++或者java中的int类型，就不需要mask来限制负数
"""

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = (1<<32)-1
        if b == 0:
            return a
        if b > mask:
            return a&mask
        return self.getSum(a^b,(a&b)<<1)