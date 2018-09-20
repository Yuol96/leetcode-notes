"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/2-keys-keyboard/description/",
    "beats": 0.1029,
    "category": ["dynamic-programming"],
    "tags": ["string"],
    "questions": []
}
"""

"""
思路
	- dp[i] 得到i个A的最小总step数
	    for j in range(1,i):
	        if i%j==0:
	            dp[i] = max(dp[i], dp[j]+i//j)
"""

class Solution:
    
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf') for __ in range(n+1)]
        dp[1] = 0
        for i in range(2, n+1):
            for j in range(1, i):
                if i%j==0:
                    dp[i] = min(dp[i], dp[j]+i//j)
        # print(dp)
        return dp[n]