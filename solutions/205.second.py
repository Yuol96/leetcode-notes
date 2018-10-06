"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/isomorphic-strings/description/",
    "beats": 0.4701,
    "category": ["string"],
    "tags": [],
    "questions": []
}
"""

"""
思路：
	- 分别记录两个字符串中idx位置的字符上次出现的位置，如果都相同，说明同构
"""

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dct1 = {}
        dct2 = {}
        for i in range(len(s)):
            if s[i] in dct1 and t[i] in dct2:
                if dct1[s[i]] != dct2[t[i]]:
                    return False
            elif s[i] in dct1 or t[i] in dct2:
                return False
            else:
                dct1[s[i]] = i
                dct2[t[i]] = i
        return True
