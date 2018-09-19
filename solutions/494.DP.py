"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/target-sum/description/",
    "beats": 0.1034,
    "category": ["dynamic-programming","DFS"],
    "tags": ["0/1knapsack"],
    "questions": []
}
"""

"""
思路
	dp[i][j] def: 前i个num组成target j 的总方法数
	dp[i][j] = dp[i-1][j+nums[i]] + dp[i-1][j-nums[i]]
"""

class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        maxS = sum(nums)
        if abs(S)>maxS:
            return 0
        totLen = 2*maxS + 1
        lastdp = [0 for __ in range(totLen)]
        lastdp[0] = 1
        for i in range(len(nums)):
            dp = [0 for __ in range(totLen)]
            for j in range(-maxS, maxS+1):
                tmp = 0
                if j+nums[i] <= maxS:
                    tmp += lastdp[j+nums[i]]
                if j-nums[i] >= -maxS:
                    tmp += lastdp[j-nums[i]]
                dp[j] = tmp
            lastdp = dp
        return lastdp[S]
