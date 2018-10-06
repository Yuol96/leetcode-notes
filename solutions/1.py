"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/two-sum/description/",
    "beats": 0.8414,
    "category": ["hash table"],
    "tags": ["two pointers"],
    "questions": []
}
"""

"""
ATTENTION
	- 不能`dct = {num:idx for idx,num in enumerate(nums)}`，因为nums里面可能出现重复元素
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = {idx:num for idx,num in enumerate(nums)}
        nums = sorted(dct.items(), key=lambda tup: tup[1])
        i,j = 0,len(nums)-1
        while i<j:
            tmp = nums[i][1] + nums[j][1]
            if tmp > target:
                j -= 1
            elif tmp < target:
                i += 1
            else:
                return [nums[i][0],nums[j][0]]