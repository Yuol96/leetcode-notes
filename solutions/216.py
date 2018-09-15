"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/combination-sum-iii/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
思路：
	- nums需要是有序的！
	- 由于选择的数不能重复，所以每次递归只能选被选择的数之后的数（不能回头，不能原地）
"""

def DFS(nums, k, n, currSelection, lst):
    if k==0 and n==0:
        lst.append(currSelection)
        return
    if k==0:
        return
    
    for idx,num in enumerate(nums):
        if n-num < k-1:
            break
        DFS(nums[idx+1:], k-1, n-num, currSelection+[num], lst)

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1,10)]
        lst = []
        DFS(nums, k, n, [], lst)
        return lst