"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/coin-change/description/",
    "beats": 0.3207,
    "category": ["dynamic-programming"],
    "tags": ["knapsack", "完全背包"],
    "questions": []
}
"""

"""
思路
	- 完全背包问题（物品个数无限）
	- 需要把物品的循环放在最里面
    - 注意物品list需要排序之后才能用if j<coin: break
"""

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf') for __ in range(amount+1)]
        dp[0] = 0
        coins.sort()
        for j in range(1, amount + 1):
            for coin in coins:
                if j<coin:
                    break
                dp[j] = min(dp[j], dp[j-coin]+1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]