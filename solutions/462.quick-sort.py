"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/",
    "beats": 1.0000,
    "category": ["math"],
    "tags": ["median","quick-select"],
    "questions": []
}
"""

"""
思路
	- 考虑number的rank，即中位数Median
	- 也可以用quick-select找中位数
"""

class Solution:
    def func(self, nums, target):
        tot = 0
        for num in nums:
            tot += abs(target - num)
        return tot
    
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        L = len(nums)
        mid = L//2
        target = nums[mid]
        return self.func(nums, target)            