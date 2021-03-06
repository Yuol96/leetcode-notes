"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/ones-and-zeroes/description/",
    "beats": -1,
    "category": ["dynamic-programming"],
    "tags": ["knapsack"],
    "questions": ["WHY NOT PASS???"]
}
"""

"""
思路
	- dp[i][j][k] 前i个str消耗j个0和k个1之后的最大output
	- dp[i][0][0] = 0
	- dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-num_zeros][k-num_ones] + 1)
"""

class Solution:
    def parseStr(self, s):
        a,b = 0,0
        for c in s:
            if c == "0":
                a+=1
            else :
                b+=1
        return a,b
    
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        self.parsedStr = []
        for s in strs:
            self.parsedStr.append(self.parseStr(s))
        
        dp = [[0 for __ in range(n+1)] for __ in range(m+1)]
        i = 0
        while i < len(self.parsedStr):
            num_zeros, num_ones = self.parsedStr[i]
            for j in range(m, num_zeros-1, -1):
                for k in range(n, num_ones-1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-num_zeros][k-num_ones] + 1)
            i+=1
        return dp[m][n]
                    
