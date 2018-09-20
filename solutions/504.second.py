"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/base-7/description/",
    "beats": 0.4979,
    "category": ["math"],
    "tags": ["base-conversion"],
    "questions": []
}
"""

class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        sign = -1 if num<0 else 1
        num = abs(num)
        
        lst = []
        while num>0:
            lst.append(str(num % 7))
            num //= 7
        output = ''.join(reversed(lst))
        
        if sign == -1:
            output = '-' + output
        return output