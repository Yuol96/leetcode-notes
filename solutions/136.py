"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/single-number/description/",
    "beats": 0.9905,
    "category": ["bit manipulation"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- x^0 == x
	- x^x == 0
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        for num in nums:
            tmp ^= num
        return tmp
