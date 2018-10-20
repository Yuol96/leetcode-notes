"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/valid-palindrome/description/",
    "beats": 0.2122,
    "category": ["string"],
    "tags": ["palindrome"],
    "questions": []
}
"""

class Solution:
    def upper2lower(self, c):
        return chr(ord(c)-ord('A')+ord('a'))
    
    def isSame(self, a, b):
        if a in self.upper:
            a = self.upper2lower(a)
        if b in self.upper:
            b = self.upper2lower(b)
        return a==b
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.upper = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        self.alphanum = set(list('abcdefghijklmnopqrstuvwxyz1234567890'))
        st = self.upper | self.alphanum
        i,j = 0,len(s)-1
        while i<j:
            while i<j and s[i] not in st:
                i += 1
            while i<j and s[j] not in st:
                j -= 1
            if not self.isSame(s[i],s[j]):
                return False
            i+=1
            j-=1
        return True