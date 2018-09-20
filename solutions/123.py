"""
{
    "author": "Yucheng Huang",
    "difficulty": "hard",
    "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/",
    "beats": 0.0752,
    "category": ["dynamic-programming"],
    "tags": ["state-machine"],
    "questions": []
}
"""

"""
思路
	- state machine
	s0 -- initial state
    s1 -- first buy
    s2 -- finish first transaction
    s3 -- second buy
    s4 -- finish second transaction
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices:
            s = [0,-prices[0],float('-inf'),float('-inf'),float('-inf')]
            for i in range(1, len(prices)):
                # s[0] remains unchanged
                a = s[0]
                b = max(s[0]-prices[i], s[1])
                c = max(s[2], s[1] + prices[i])
                d = max(s[3], s[2] - prices[i])
                e = max(s[4], s[3] + prices[i])
                s = [a,b,c,d,e]
            return max(s[0],s[2],s[4])
        return 0
