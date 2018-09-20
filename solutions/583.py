"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/delete-operation-for-two-strings/description/",
    "beats": 0.5748,
    "category": ["dynamic-programming"],
    "tags": ["string"],
    "questions": []
}
"""

"""
思路
	- dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1] else min(dp[i-1][j], dp[i][j-1]) + 1
"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        dp = [[0 for __ in range(len(word2)+1)] for __ in range(len(word1)+1)]
        for j in range(1, len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            dp[i][0] = i
            
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        # for i in range(len(word1)+1):
        #     print(dp[i])
        return dp[len(word1)][len(word2)]
                    
                    
