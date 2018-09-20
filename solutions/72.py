"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/edit-distance/description/",
    "beats": 0.1401,
    "category": ["dynamic-programming"],
    "tags": ["string"],
    "questions": ["How does 'deleting a character' being considered???"]
}
"""

"""
思路
	- dp[i][j] = min([dp[i-1][j-1], dp[i][j-1], dp[i-1][j]]) + 1
"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for __ in range(len(word2)+1)] for __ in range(len(word1)+1)]
        dp[0][0] = 0
        for i in range(1, len(word1)+1):
            dp[i][0] = i
        for j in range(1, len(word2)+1):
            dp[0][j] = j
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min([dp[i-1][j-1], dp[i][j-1], dp[i-1][j]]) + 1
        return dp[len(word1)][len(word2)]