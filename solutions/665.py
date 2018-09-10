"""
{
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/non-decreasing-array/description/",
    "category": ["greedy"],
    "tags": ["adjacent"],
    "questions": []
}
"""

"""
思路：
	- 边界：float('-inf')和float('inf')的使用
	- 对于一个相邻的逆序对(a,b)，要考虑修改a还是修改b这两种情况
"""

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = len(nums)
        chance = 1
        nums = [float('-inf')] + nums + [float('inf')]
        for idx in range(1,L):
            if nums[idx] > nums[idx+1]:
                if nums[idx-1] <= nums[idx+1]:
                    chance -= 1
                elif nums[idx] <= nums[idx+2]:
                    chance -= 1
                else :
                    return False
            if chance < 0:
                return False
        return True
                    