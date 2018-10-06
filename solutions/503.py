"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/next-greater-element-ii/description/",
    "beats": 0.1228,
    "category": ["stack and array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- please refer to `739.stack.py`
"""

class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = [-1 for __ in range(len(nums))]
        stack = []
        for idx, num in enumerate(nums):
            while len(stack)>0 and nums[stack[-1]]<num:
                lst[stack[-1]] = num
                stack.pop()
            stack.append(idx)
            
        for idx, num in enumerate(nums):
            if len(stack)==0:
                break
            while len(stack)>0 and nums[stack[-1]]<num:
                lst[stack[-1]] = num
                stack.pop()
        return lst