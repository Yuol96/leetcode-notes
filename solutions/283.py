"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/move-zeroes/description/",
    "beats": 0.9741,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 本题需要置后的只有0，因此不需要类似冒泡排序的算法。
	- 可以直接把非零元素按顺序填入位置，剩下的位置就全填入0
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0