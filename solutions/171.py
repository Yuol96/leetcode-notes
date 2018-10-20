"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/excel-sheet-column-number/description/",
    "beats": 1.0000,
    "category": ["array"],
    "tags": ["excel","进制"],
    "questions": []
}
"""

"""
思路
	- 26(A-Z) + 26*26(AA-ZZ) + 26*26*26(AAA-ZZZ) + ...
"""

class Solution:
    def char2num(self, c):
        return ord(c)-ord('A')
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in range(1,len(s)):
            num += 26**i
        for idx,c in enumerate(reversed(s)):
            num += self.char2num(c) * (26**idx)
        num += 1
        return num
