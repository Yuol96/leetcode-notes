"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/maximum-length-of-pair-chain/description/",
    "beats": 0.0320,
    "category": ["dynamic-programming", "greedy"],
    "tags": ["overlapping-intervals"],
    "questions": []
}
"""

"""
思路：
	- 先对pairs排序
	- dp[i]表示pairs[:i+1]的最长pair chain的长度
"""

class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        
        pairs.sort()
        dp = [1]*len(pairs)
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j]+1
        return dp[-1]
