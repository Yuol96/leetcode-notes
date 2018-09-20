"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/",
    "beats": 0.4658,
    "category": ["dynamic-programming"],
    "tags": ["state-machine"],
    "questions": []
}
"""

"""
思路
	- 状态机, space-optimized,
    - 有两种状态：S0(观望), S1(bought)
	- 边：S0->S0, S0->S1, S1->S1, S1->S0
"""

class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if prices:
            s = [0, -prices[0]-fee]
            for i in range(len(prices)):
                a = max(s[0], s[1]+prices[i])
                b = max(s[0]-prices[i]-fee, s[1])
                s = [a,b]
            return s[0]
        return 0