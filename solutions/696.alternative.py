"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/count-binary-substrings/description/",
    "beats": 0.2902,
    "category": ["string"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 交替记录preLen和curLen
"""

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        preLen = 0
        curLen = 1
        count = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curLen += 1
            else:
                preLen = curLen
                curLen = 1
            if preLen >= curLen:
                count += 1
        return count