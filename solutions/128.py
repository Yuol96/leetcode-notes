"""
{
    "author": "Yucheng Huang",
    "difficulty": "hard",
    "link": "https://leetcode.com/problems/longest-consecutive-sequence/description/",
    "beats": 0.5532,
    "category": ["hash table"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 先用dct来存储nums里的distinct number是否出现过
	- 对每一个distinct number，用递归的方式计算比它大的连续sequence的长度，并记录在dct中
"""

class Solution:
    def update(self, dct, num):
        if num not in dct:
            return 0
        if dct[num] is None:
            dct[num] = 1 + self.update(dct, num+1)
        return dct[num]
    
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dct = {}
        for num in nums:
            dct[num] = None
        for num in nums:
            self.update(dct, num)
        # print(dct)
        return max(dct.values())