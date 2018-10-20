"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/maximum-product-of-word-lengths/description/",
    "beats": 0.6756,
    "category": ["bit manipulation"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 用位运算的与操作来判断两个单词是否有公共字符
"""

class Solution:
    def word2num(self, word):
        num = 0
        for c in word:
            idx = ord(c)-ord('a')
            num |= (1<<idx)
        return num
    
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        nums = list(map(self.word2num, words))
        L = len(words)
        maxVal = 0
        for i in range(L-1):
            for j in range(i+1,L):
                if nums[i]&nums[j]==0:
                    maxVal = max(maxVal, len(words[i])*len(words[j]))            
        return maxVal