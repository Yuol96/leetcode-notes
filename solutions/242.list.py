"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/valid-anagram/description/",
    "beats": 0.5029,
    "category": ["string"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def count(self, s):
        lst = [0 for __ in range(26)]
        for c in s:
            idx = ord(c) - ord('a')
            lst[idx] += 1
        return lst
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slist = self.count(s)
        tlist = self.count(t)
        return tuple(slist) == tuple(tlist)