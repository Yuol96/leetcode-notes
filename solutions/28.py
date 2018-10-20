"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/implement-strstr/description/",
    "beats": 1.0000,
    "category": ["string"],
    "tags": ["*stringMatch"],
    "questions": []
}
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except:
            return -1