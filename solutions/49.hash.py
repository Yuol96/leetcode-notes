"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/group-anagrams/",
    "beats": 0.2347,
    "category": ["math","hash table"],
    "tags": ["anagram"],
    "questions": []
}
"""

class Solution:
    def encode(self, word):
        lst = [0 for __ in range(26)]
        for c in word:
            idx = ord(c) - ord('a')
            lst[idx] += 1
        return tuple(lst)
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dct = {}
        for word in strs:
            code = self.encode(word)
            dct[code] = dct.get(code,[]) + [word]
        return list(dct.values())