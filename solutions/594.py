"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/longest-harmonious-subsequence/description/",
    "beats": 0.3585,
    "category": ["hash table"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dct = {}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
        tupList = sorted(dct.items(), key=lambda tup: tup[0])
        if len(tupList) == 1:
            return 0
        maxLen = 0
        for idx in range(1, len(tupList)):
            if tupList[idx][0] - tupList[idx-1][0] == 1:
                maxLen = max(maxLen, tupList[idx][1] + tupList[idx-1][1])
        return maxLen