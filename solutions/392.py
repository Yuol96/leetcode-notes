"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/is-subsequence/description/",
    "category": ["greedy"],
    "tags": ["two-pointers"],
    "questions": []
}
"""

class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,j = 0,0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else :
                j += 1
        if i == len(s):
            return True
        return False