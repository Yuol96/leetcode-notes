"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/array-nesting/",
    "beats": 0.1728,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = [0 for __ in range(len(nums))]
        maxCount = 0
        for i in range(len(nums)):
            count = 0
            j = i
            while visited[j]==0:
                visited[j] = 1
                count += 1
                j = nums[j]
            maxCount = max(maxCount, count)
        return maxCount

