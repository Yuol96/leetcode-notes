"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/maximum-subarray/description/",
    "category": ["dynamic-programming"],
    "tags": ["subarray"],
    "questions": []
}
"""

"""
思路：
	- 找到以第i个元素为结尾的数组区间的最大和
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        self.L = len(nums)
        self.largestSum = [0 for __ in range(self.L)]
        self.largestSum[0] = nums[0]
        for i in range(1,self.L):
            self.largestSum[i] = max(self.largestSum[i-1] + nums[i], nums[i])
        return max(self.largestSum)