"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/missing-number/description/",
    "beats": 0.7076,
    "category": ["bit manipulation","array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- please refer to `136.py`
"""

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        for idx,num in enumerate(nums):
            tmp ^= idx^num
        return tmp^(len(nums))