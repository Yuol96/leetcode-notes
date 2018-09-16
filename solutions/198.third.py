"""
{
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/house-robber/description/",
    "category": ["dynamic-programming"],
    "tags": ["fibonacci"],
    "questions": []
}
"""

"""
思路：
	- 从左向右考虑抢劫第i家(不一定抢第i家)时的最大收益 DP(i) = max(DP(i-2)+nums[i], DP(i-1))
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        self.DPArray = [nums[0], max(nums[0],nums[1])]
        for i in range(2, len(nums)):
            self.DPArray.append(max(
                self.DPArray[i-2] + nums[i],
                self.DPArray[i-1]
            ))
        return self.DPArray[-1]
        