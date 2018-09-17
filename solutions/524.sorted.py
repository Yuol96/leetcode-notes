"""
{
	"id": 524,
	"name": "Longest Word in Dictionary through Deleting",
	"difficulty": "medium",
	"link": "https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/",
	"category": ["two pointers"],
    "tags": []
}
"""
class Solution(object):
    def find(self, s, word):
        i,j = 0,0
        while i<len(s) and j<len(word):
            if s[i]==word[j]:
                i+=1
                j+=1
            else:
                i+=1
        if j == len(word):
            return True
        else:
            return False

def findLongestWord(self, s, d):
    """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
            lst=[]
            for word in d:
            if self.find(s,word):
                lst.append(word)
                    if len(lst)==0:
                        return ''
                            return sorted(lst, key=lambda word:(-len(word),word))[0]

                
