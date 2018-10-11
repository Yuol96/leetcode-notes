"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/find-all-duplicates-in-an-array/description/",
    "beats": 0.1975,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- please refer to `645.smart.py`
"""

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            while nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]:
                swap(nums, i, nums[i]-1)
        lst = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                lst.append(nums[i])
        return lst