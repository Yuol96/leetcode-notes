"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/combinations/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
思路：
	- 和排列不同，这里nums需要排序，然后每次选完一个数之后，只能选它后面的数（不能回头，不能原地踏步）
"""

def DFS(nums, k, currCombination, lst):
    if k==0:
        lst.append(currCombination)
        return 
    if len(nums) < k:
        return 
    for idx,num in enumerate(nums):
        DFS(nums[idx+1:], k-1, currCombination + [num], lst)
    

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k==0:
            return []
        lst = []
        nums = [i for i in range(1,n+1)]
        DFS(nums, k, [], lst)
        return lst