"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/happy-number/description/",
    "beats": 0.9901,
    "category": ["math"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def recurr(self, n):
        if n==1:
            return True
        if n in self.st:
            return False
        self.st.add(n)
        num = 0
        while n>0:
            tmp = n%10
            num += tmp*tmp
            n //= 10
        return self.recurr(num)
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.st = set()
        return self.recurr(n)
