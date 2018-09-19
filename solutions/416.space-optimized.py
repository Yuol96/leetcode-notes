"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/partition-equal-subset-sum/description/",
    "beats": 0.1706,
    "category": ["dynamic-programming"],
    "tags": ["0/1knapsack"],
    "questions": []
}
"""

"""
思路
	- 容量为totalSum//2的背包问题
	- dp[i][j] 定义为：是否可以前i个num中可以找到一个子集 s.t. 子集的和为j
	- dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    - 每次只保存dp[i-1]在lastdp
"""

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        totSum = sum(nums)
        if totSum % 2 == 1:
            return False
        halfSum = totSum//2
        
        lastdp = [False for __ in range(halfSum+1)]
        lastdp[0] = True
        for i in range(1, len(nums)+1):
            dp = [False for __ in range(halfSum+1)]
            for j in range(halfSum+1):
                dp[j] = lastdp[j] or (j >= nums[i-1] and lastdp[j-nums[i-1]])
            lastdp = dp
        return lastdp[halfSum]
        