"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/add-binary/description/",
    "beats": 0.4412,
    "category": ["math"],
    "tags": ["binary","string-number"],
    "questions": []
}
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, base=2)
        b = int(b, base=2)
        ans = a+b
        lst = []
        while ans > 0:
            lst.append(str((ans & 1)))
            ans >>= 1
        if len(lst)==0:
            return "0"
        return ''.join(reversed(lst))