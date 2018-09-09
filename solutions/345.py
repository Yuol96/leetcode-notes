"""
{
	"id": 345,
	"name": "Reverse Vowels of a String",
	"difficulty": "easy",
	"link": "https://leetcode.com/problems/reverse-vowels-of-a-string/description/",
	"category": ["two pointers"]
}
"""
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isVowel(c):
            if c in ['a','e','i','o','u','A','E','I','O','U']:
                return True
            return False
        s = list(s)
        i, j = 0, len(s)-1
        while i<j:
            if isVowel(s[i]) and isVowel(s[j]):
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif not isVowel(s[i]) and isVowel(s[j]):
                i += 1
            elif isVowel(s[i]) and not isVowel(s[j]):
                j -= 1
            else: 
                i += 1
                j -= 1
        return ''.join(s)