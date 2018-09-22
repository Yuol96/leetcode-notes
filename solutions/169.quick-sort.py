"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/majority-element/description/",
    "beats": 0.5829,
    "category": ["math"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 对数组排序，最中间那个数出现次数一定多于 n / 2。
	- 也可以用quick-select
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        L = len(nums)
        medianIdx = L//2
        return nums[medianIdx]