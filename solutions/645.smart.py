"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/set-mismatch/description/",
    "beats": 0.3298,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 巧妙利用nums在[1,n]而且只有一个duplicate和missing的条件，给nums排序
	- 时间复杂度O(n)，空间复杂度O(1)
Attention
	- 不能直接写`nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]`，因为左边的nums的index中有nums[i]，所以nums[i]的改变会改变赋值对象！
"""

def swap(nums, i,j):
    nums[i],nums[j] = nums[j], nums[i]

class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            while nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                swap(nums, i, nums[i]-1)
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i+1]