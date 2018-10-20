"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/generate-parentheses/description/",
    "beats": 0.5971,
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

class Solution:
    def DFS(self, n, left, s):
        if n==0:
            s += ')'*left
            self.lst.append(s)
            return
        self.DFS(n-1,left+1,s+'(')
        if left>0:
            self.DFS(n,left-1,s+')')
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.lst = []
        self.DFS(n,0,"")
        return self.lst
        