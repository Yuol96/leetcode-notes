"""
{
	"author": "Yucheng Huang",
    "id": 680,
	"name": "Valid Palindrome II",
	"difficulty": "easy",
	"link": "https://leetcode.com/problems/valid-palindrome-ii/description/",
	"category": ["two pointers"],
    "tags": ["palindrome"]
}
"""
class Solution:
    def isPalindrome(self,s):
        i,j = 0,len(s)-1
        while i<j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True
    
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,j = 0,len(s)-1
        while i<j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else :
                return self.isPalindrome(s[i:j]) or self.isPalindrome(s[i+1:j+1])
        return True