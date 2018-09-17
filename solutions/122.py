"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/",
    "category": ["greedy"],
    "tags": ["adjacent-element"],
    "questions": []
}
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for idx in range(len(prices)-1):
            profit += max(0, prices[idx+1] - prices[idx])
        return profit