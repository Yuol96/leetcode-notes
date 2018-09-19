"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/combination-sum-iv/description/",
    "beats": 0.8253,
    "category": ["dynamic-programming"],
    "tags": ["knapsack", "完全背包"],
    "questions": []
}
"""

"""
思路：
	- dp[j] 是target为j时的output
	- 要记得nums需要排序才能在循环中break！！
"""

class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for __ in range(target+1)]
        dp[0] = 1
        nums.sort()
        for j in range(1,target+1):
            for num in nums:
                if j<num:
                    break
                dp[j] += dp[j-num]
        print(dp)
        return dp[-1]
                    
