"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/wiggle-subsequence/description/",
    "beats": 0.24,
    "category": ["dynamic-programming"],
    "tags": ["subsequence"],
    "questions": []
}
"""

"""
思路：
	- 有两种wiggle，先上升后下降 + 先下降后上升，这两种情况分开考虑
	- 对每一种情况，记录它当前符合要求的子序列，以upFirst为例，
		- 如果子序列upFirst长度为奇数
			- 如果下一个nums中的元素比upFirst[-1]大，那么就把这个元素append到upFirst中
			- 如果下一个nums中的元素小于等于upFirst[-1]，那么就用这个元素替换掉upFirst中最后一个元素
	- 时间复杂度为O(n)
"""

class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        upFirst = [nums[0]]
        downFirst = [nums[0]]
        
        for i in range(1, n):
            if len(upFirst)%2==1:
                if nums[i] <= upFirst[-1]:
                    upFirst[-1] = nums[i]
                else:
                    upFirst.append(nums[i])
            else:
                if nums[i] >= upFirst[-1]:
                    upFirst[-1] = nums[i]
                else :
                    upFirst.append(nums[i])
            
            if len(downFirst)%2==0:
                if nums[i] <= downFirst[-1]:
                    downFirst[-1] = nums[i]
                else:
                    downFirst.append(nums[i])
            else:
                if nums[i] >= downFirst[-1]:
                    downFirst[-1] = nums[i]
                else :
                    downFirst.append(nums[i])

        # print(upFirst)
        # print(downFirst)
        return max(len(upFirst), len(downFirst))
            
                
