"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/permutations-ii/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

def DFS(nums, currPermutation, lst):
    if len(nums) == 0:
        lst.add(tuple(currPermutation))
        return
    for idx,num in enumerate(nums):
        DFS(nums[:idx]+nums[idx+1:], currPermutation+[num], lst)

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums:
            lst = set()
            DFS(nums, [], lst)
            return list(map(lambda tup: list(tup), lst))
        else :
            return []