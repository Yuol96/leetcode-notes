"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/valid-parentheses/description/",
    "beats": 0.6346,
    "category": ["stack and array"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        for c in s:
            if c in mapping:
                stack.append(c)
            elif len(stack) == 0 or mapping[stack.pop()] != c:
                return False
        return len(stack) == 0