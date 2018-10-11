"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/",
    "beats": 0.1051,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- please refer to `645.smart.py`
"""

def swap(nums, i,j):
    nums[i], nums[j] = nums[j], nums[i]

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            while nums[i] != i+1 and nums[nums[i]-1]!=nums[i]:
                swap(nums, i, nums[i]-1)
        lst = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                lst.append(i+1)
        return lst