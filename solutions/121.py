"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/",
    "beats": 0.5448,
    "category": ["dynamic-programming"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 用low数组的第i个元素（从1开始）来记录prices[:i]数组中的最小值，同时计算prices[i]-low[i]，在对i循环的过程中，记下prices[i]-low[i]的最大值，即为答案
	- dp[i]为截止到以index为i的元素结尾的subarray的最大单次交易profit
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = [prices[0] for idx in range(len(prices))]
        ret = 0
        for idx in range(1,len(prices)):
            low[idx] = min(low[idx-1], prices[idx])
            if ret < prices[idx]-low[idx]:
                ret = prices[idx]-low[idx]
        return ret


