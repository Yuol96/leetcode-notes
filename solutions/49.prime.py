"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/group-anagrams/",
    "beats": 0.4476,
    "category": ["math","hash table"],
    "tags": ["anagram"],
    "questions": []
}
"""

import math

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        # primelog = list(map(lambda num: math.log(num), prime))
        
        dct = {}
        for word in strs:
            # code = 0
            code = 1
            for c in word:
                idx = ord(c)-ord('a')
                # code += primelog[idx]
                code *= prime[idx]
            # code = round(code,10)
            dct[code] = dct.get(code, []) + [word]
        # print(dct)
        return list(dct.values())