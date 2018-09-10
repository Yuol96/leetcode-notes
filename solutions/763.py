"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/partition-labels/description/",
    "category": ["greedy"],
    "tags": [],
    "questions": []
}
"""

"""
思路：
    - 与non-overlapping intervals正好相反，本题类似于取并集
    - 先统计出每个character的scope
    - 按照scope开始的坐标对这些scope排序，overlap的scope取并集
"""

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        scope = {}
        for idx,c in enumerate(S):
            if c not in scope:
                scope[c] = [idx,idx]
            else :
                scope[c][1] = idx
        scopeList = sorted(list(scope.values()), key=lambda lst: lst[0])
        lastStart = scopeList[0][0]
        lastEnd = scopeList[0][1]
        ret = []
        for idx in range(1,len(scopeList)):
            scope = scopeList[idx]
            if scope[0] < lastEnd:
                lastEnd = max(lastEnd, scope[1])
            else :
                ret.append(lastEnd - lastStart + 1)
                lastStart = scope[0]
                lastEnd = scope[1]
        ret.append(lastEnd - lastStart + 1)
        return ret
            