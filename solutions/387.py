"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/first-unique-character-in-a-string/description/",
    "beats": 0.5997,
    "category": ["Very Easy Questions"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- character belongs to 0-255
"""

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = [0 for __ in range(256)]
        for c in s:
            lst[ord(c)] += 1
        for idx,c in enumerate(s):
            if lst[ord(c)] == 1:
                return idx
        return -1