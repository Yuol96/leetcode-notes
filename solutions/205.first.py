"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/isomorphic-strings/description/",
    "beats": 0.9933,
    "category": ["string"],
    "tags": [],
    "questions": []
}
"""

"""
ATTENTION
	- s和t的字母顺序不能变
"""

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dct = {}
        st = set()
        for i in range(len(s)):
            if s[i] not in dct:
                if t[i] not in st:
                    dct[s[i]] = t[i]
                    st.add(t[i])
                else:
                    return False
            elif dct[s[i]] != t[i]:
                return False
        return True