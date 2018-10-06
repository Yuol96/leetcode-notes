"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/max-consecutive-ones/description/",
    "beats": 0.6155,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxOnes = 0
        curOnes = 0
        for num in nums:
            if num == 1:
                curOnes += 1
            else:
                maxOnes = max(maxOnes, curOnes)
                curOnes = 0
        maxOnes = max(maxOnes, curOnes)
        return maxOnes