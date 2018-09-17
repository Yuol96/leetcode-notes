"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/combination-sum/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
思路：
	- 需要对candidates排序，然后每次选了一个数，之后只能选这个数以及它后面的数（不能回头，可以原地踏步）
"""

def DFS(candidates, leftover, currSelection, lst):
    if leftover == 0:
        lst.append(currSelection)
        return
    
    for idx,candidate in enumerate(candidates):
        if candidate <= leftover:
            DFS(candidates[idx:], leftover-candidate, currSelection+[candidate], lst)

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        lst = []
        candidates.sort()
        DFS(candidates, target, [], lst)
        return lst