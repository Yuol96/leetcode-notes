"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/longest-palindrome/description/",
    "beats": 0.3264,
    "category": ["string"],
    "tags": ["palindrome"],
    "questions": []
}
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {}
        for c in s:
            dct[c] = dct.get(c, 0) + 1
        ret = 0
        odd = 0
        for v in dct.values():
            if v%2 == 1:
                odd = 1
                ret += v-1
            else:
                ret += v
        return ret + odd