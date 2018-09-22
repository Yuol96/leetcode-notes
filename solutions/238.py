"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/product-of-array-except-self/description/",
    "beats": 0.4188,
    "category": ["math"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 从左边和右边开始各自delay 1个数在遍历累乘一边
	- 从左边开始的遍历，到第i个数，就会使output[i]乘上它左边左右的数的乘积；反之亦然
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = len(nums)
        output = [1 for __ in range(L)]
        left = nums[0]
        for i in range(1, L):
            output[i] *= left
            left *= nums[i]
        right = nums[L-1]
        for i in range(L-2, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output