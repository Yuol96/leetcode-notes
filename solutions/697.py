"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/degree-of-an-array/submissions/",
    "beats": 0.7052,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        minIdx = {}
        maxIdx = {}
        for idx, num in enumerate(nums):
            if num not in dct:
                minIdx[num] = idx
                maxIdx[num] = idx
                dct[num] = 1
            else:
                maxIdx[num] = idx
                dct[num] += 1
        maxCount = max(dct.values())
        ans = float('inf')
        for num,count in dct.items():
            if count == maxCount:
                ans = min(ans, maxIdx[num]-minIdx[num]+1)
        return ans