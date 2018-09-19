"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/word-break/description/",
    "beats": 0.1114,
    "category": ["dynamic-programming"],
    "tags": ["完全背包"],
    "questions": []
}
"""

"""
ATTENTION
    - DFS法会超时：
class Solution:
    def DFS(self, s):
        if len(s) == 0:
            return True
        for idx in range(1, len(s)+1):
            if s[:idx] in self.wordDict and self.DFS(s[idx:]):
                return True
        return False
    
    def wordBreak(self, s, wordDict):
        self.wordDict = set(wordDict)
        return self.DFS(s)
"""

"""
思路
   - dp[i] = index小于等于i的substring能否word break
   - 复杂度 O(N^2)
   - 另一种思路是用完全背包法
"""

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = []
        for i in range(len(s)):
            tmp = False
            if s[:i+1] in wordDict:
                tmp = True
            for j in range(i):
                if dp[j] and s[j+1:i+1] in wordDict:
                    tmp = True
                    break
            dp.append(tmp)
        return dp[-1]

