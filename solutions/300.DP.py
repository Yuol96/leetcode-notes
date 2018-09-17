"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/longest-increasing-subsequence/description/",
    "beats": 0.1446,
    "category": ["dynamic-programming"],
    "tags": ["subsequence"],
    "questions": []
}
"""

"""
思路：
	- DP[i] = subarray，nums[:i+1]的最长递增子序列的长度
"""

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lis = [1]
        for i in range(1, len(nums)):
            maxLen = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    maxLen = max(lis[j]+1, maxLen)
            lis.append(maxLen)
        # print(lis)
        return max(lis)