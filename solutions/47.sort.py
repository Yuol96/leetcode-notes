"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/permutations-ii/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
思路：
	- 对数组先排序，每次只考虑distinct number，越过与lastNum相同number
"""

def DFS(nums, currPermutation, lst):
    if len(nums) == 0:
        lst.append(currPermutation)
        return
    for idx,num in enumerate(nums):
        if idx > 0 and num == lastNum:
            continue
        lastNum = num
        DFS(nums[:idx]+nums[idx+1:], currPermutation+[num], lst)

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums:
            nums.sort()
            lst = []
            DFS(nums, [], lst)
            return lst
        else :
            return []