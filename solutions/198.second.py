"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/house-robber/description/",
    "category": ["dynamic-programming"],
    "tags": ["fibonacci"],
    "questions": []
}
"""

"""
思路：
	- 从左向右考虑抢劫第i家时的最大收益 DP(i) = max(DP(i-2)+nums[i], DP(i-3)+nums[i])
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[1], nums[0]+nums[2])
        self.DParray = [nums[0], max(nums[0], nums[1]), max(nums[1], nums[0]+nums[2])]
        for i in range(3, len(nums)):
            self.DParray.append(max(
                self.DParray[i-2] + nums[i],
                self.DParray[i-3] + nums[i],
            ))
        return max(self.DParray[-2:])
