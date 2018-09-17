"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/maximum-subarray/description/",
    "category": ["dynamic-programming"],
    "tags": ["subarray"],
    "questions": []
}
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seq = [ 0 for idx in range(len(nums))]
        seq[0] = nums[0]
        
        for idx in range(1,len(nums)):
            if seq[idx-1] + nums[idx] <= nums[idx]:
                seq[idx] = nums[idx]
            else :
                seq[idx] = seq[idx-1] + nums[idx]
        
        return max(seq)
        
        '''
        - 简单的动态规划，用seq来存储，seq的第i个元素是以第i个元素结尾的和最大的subarray
        - 递推公式：
            - 如果新来的元素比（以上一个元素结尾的和最大的subarray的数组和）还大，那么就说明新来的元素单独作为一个subarray
            - 否则，应该是（以上一个元素结尾的和最大的subarray）作为新的subarray
        '''