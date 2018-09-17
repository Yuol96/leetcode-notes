"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/permutations/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

def DFS(nums, currPermutation, lst):
    if len(nums) == 0:
        lst.append(currPermutation)
        return
    for idx,num in enumerate(nums):
        DFS(nums[:idx]+nums[idx+1:], currPermutation+[num], lst)

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums:
            lst = []
            DFS(nums, [], lst)
            return lst
        else :
            return []