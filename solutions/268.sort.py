"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/missing-number/description/",
    "beats": 0.2812,
    "category": ["bit manipulation","array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- sort in place
	- please refer to `645.smart.py`
"""

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

class Solution:
    
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(None)
        for idx in range(len(nums)):
            while nums[idx] is not None and nums[idx] != idx:
                swap(nums, idx, nums[idx])
        for idx in range(len(nums)):
            if nums[idx] is None:
                return idx