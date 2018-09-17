"""
{
	"difficulty": "medium",
	"link": "https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/",
	"category": ["two pointers"],
    "tags": []
}
"""
class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def isContainWord(s, word):
            i,j = 0,0
            while j<len(word) and i<len(s):
                if s[i] == word[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            if j == len(word):
                return True
            return False
        
        dct = {}
        for word in d:
            dct[len(word)] = dct.get(len(word), []) + [word]
        lst = sorted(list(dct.items()), key=lambda tup:tup[0])
        flag = False
        candidates = []
        for count,wordList in reversed(lst):
            for word in wordList:
                if isContainWord(s,word):
                    flag = True
                    candidates.append(word)
            if flag:
                return sorted(candidates)[0]
        return ""
                
