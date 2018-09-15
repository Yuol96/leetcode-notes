"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/subsets/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
思路：
	- 每次递归，为nums的第一个元素考虑两种情况，即是否放进currSelection
"""

def DFS(nums, currSelection, lst):
    if len(nums) == 0:
        lst.append(currSelection)
        return
    
    DFS(nums[1:], currSelection,lst)
    DFS(nums[1:], currSelection+[nums[0]],lst)

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = []
        DFS(nums, [], lst)
        return lst