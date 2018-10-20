"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/roman-to-integer/submissions/",
    "beats": 0.5378,
    "category": ["Very Easy Questions"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def nextToken(self, s, i):
        if i<len(s)-1 and s[i:i+2] in self.subtraction:
            return self.dct[s[i:i+2]], i+2
        return self.dct[s[i]], i+1
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.subtraction = set(['IV','IX','XL','XC','CD','CM'])
        self.dct = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        i = 0
        num = 0
        while i<len(s):
            delta, i = self.nextToken(s,i)
            num += delta
        return num