"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/contains-duplicate/description/",
    "beats": 0.8444,
    "category": ["hash table"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        st = set(nums)
        return len(st) < len(nums)