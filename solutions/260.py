"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/single-number-iii/description/",
    "beats": 0.9978,
    "category": ["bit manipulation"],
    "tags": [],
    "questions": []
}
"""

"""
思路
    - https://www.zhihu.com/question/38206659
    假设nums中所有元素的异或为res，两个只出现一次的元素为x和y，那么res = x^y
    对数组按照res的为1的某一位分组，那么x和y肯定在不同的分组里，而且其他元素必然成对出现在同一组内。
    再分别对这两个分组的所有元素求异或和即可得到x和y
    - x&(-x)用来取最右一位
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        for num in nums:
            res ^= num
            
        diff = res&(-res)
        groupA = 0
        groupB = 0
        for num in nums:
            if (num&diff) > 0:
                groupA ^= num
            else :
                groupB ^= num
        return [groupA, groupB]