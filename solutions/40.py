"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/combination-sum-ii/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
思路：
	- 因为是组合，不能重复，所以需要对candidates排序
	- 每次递归遇到相同元素需要略过，即同一元素只能递归一次
	- 递归时只要被选择元素后面的元素
"""

def DFS(candidates, target, currSelection, lst):
    if target == 0:
        lst.append(currSelection)
        return
    
    for idx,candidate in enumerate(candidates):
        if candidate > target:
            break
        if idx > 0 and candidate == lastCandidate:
            continue
        lastCandidate = candidate
        DFS(candidates[idx+1:], target-candidate, currSelection+[candidate], lst)

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        lst = []
        DFS(candidates, target, [], lst)
        return lst