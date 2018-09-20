"""
{
    "author": "Yucheng Huang",
    "difficulty": "hard",
    "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/",
    "beats": 0.0978,
    "category": ["dynamic-programming"],
    "tags": ["state-machine"],
    "questions": []
}
"""

"""
ATTENTION
	- 对于k>=int(prices)//2的情况，直接用2状态的state machine会更快，否则会超时
"""

class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if prices:
            if k==0:
                return 0
            if k>=len(prices)//2:
                s = [0,-prices[0]]
                for i in range(1, len(prices)):
                    a = max(s[0], s[1]+prices[i])
                    b = max(s[1], s[0]-prices[i])
                    s = [a,b]
                return s[0]
                
            s = [float('-inf') for __ in range(2*k+1)]
            s[0] = 0
            s[1] = -prices[0]
            for i in range(1, len(prices)):
                news = [0 for __ in range(2*k+1)]
                for j in range(1, 2*k+1):
                    if j%2==1:
                        # buy
                        news[j] = max(s[j], s[j-1]-prices[i])
                    else:
                        # sell
                        news[j] = max(s[j], s[j-1]+prices[i])
                s = news
            return max(s)
        return 0

