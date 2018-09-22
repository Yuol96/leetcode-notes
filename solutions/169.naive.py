"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/majority-element/description/",
    "beats": 0.3106,
    "category": ["math"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
        threshold = len(nums)//2
        for k,v in dct.items():
            if v>threshold:
                return k
