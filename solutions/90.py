"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/subsets-ii/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
思路：
	- nums需要sort
	- 每次递归，找到当前nums中第一个相同元素的子序列（假设这个子序列长度为k），然后做k+1次递归，分别让currSelection后面concatenate从0到k个nums[0]
"""

def DFS(nums, currSelection, lst):
    if len(nums) == 0:
        lst.append(currSelection)
        return
    
    idx = 1
    while idx < len(nums):
        if nums[idx] != nums[0]:
            break
        idx += 1
    for i in range(idx+1):
        DFS(nums[idx:], currSelection+nums[:i], lst)

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        lst = []
        DFS(nums, [], lst)
        return lst