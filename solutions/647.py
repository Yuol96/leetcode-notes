"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/palindromic-substrings/description/",
    "beats": 0.4989,
    "category": ["string"],
    "tags": ["palindrome"],
    "questions": []
}
"""

"""
思路
	- palindrome有两种，奇数个的，和偶数个的
	- 对所有i，考虑以(i,i)和(i,i+1)为中心的两种palindrome
"""

class Solution:
    def countCenterAt(self, s, i, j):
        while i>=0 and j<len(s) and s[i] == s[j]:
            self.count += 1
            i -= 1
            j += 1
    
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.count = 0
        for i in range(len(s)):
            self.countCenterAt(s, i, i)
            self.countCenterAt(s, i, i+1)
        return self.count