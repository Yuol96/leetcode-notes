"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/",
    "beats": 0.5487,
    "category": ["dynamic-programming"],
    "tags": ["state-machine"],
    "questions": []
}
"""

"""
思路
	- 用状态机
	- 有三种状态：S0(观望), S1(bought), S2(Sold)
	- 边：S0->S0, S0->S1, S1->S1, S1->S2, S2->S0
	- 初始化注意，S2[0]无意义，其初始值不能大于S0[0]
	- 复杂度：O(N)
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices:
            s = [[None for __ in range(len(prices))] for __ in range(3)]
            s[0][0] = 0
            s[1][0] = -prices[0]
            s[2][0] = 0
            for i in range(1, len(prices)):
                s[0][i] = max(s[0][i-1], s[2][i-1])
                s[1][i] = max(s[0][i-1]-prices[i], s[1][i-1])
                s[2][i] = s[1][i-1] + prices[i]
            return max(s[0][len(prices)-1], s[2][len(prices)-1])
        return 0