"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/count-binary-substrings/description/",
    "beats": 0.0189,
    "category": ["string"],
    "tags": ["palindrome"],
    "questions": []
}
"""

"""
思路
	- please refer to `647.py`
"""

class Solution:
    def countCenterAt(self, s, i):
        l,r = i,i+1
        if s[l] == s[r]:
            return
        while l>=0 and r<len(s) and s[l]==s[i] and s[r]==s[i+1]:
            self.count += 1
            l -= 1
            r += 1
    
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.count = 0
        for idx in range(len(s)-1):
            self.countCenterAt(s, idx)
        return self.count