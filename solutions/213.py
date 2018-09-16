"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/house-robber-ii/description/",
    "category": ["dynamic-programming"],
    "tags": ["fibonacci"],
    "questions": []
}
"""

"""
思路：
	- 分别考虑nums[1:]和nums[:-1]这两种切环的方法，找到各自的最大profit，再取最大
"""

class Solution:
    def DP(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        DPArray = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            DPArray.append(max(
                DPArray[i-2] + nums[i],
                DPArray[i-1]
            ))
        return DPArray[-1]
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.DP(nums[:-1]), self.DP(nums[1:]))
