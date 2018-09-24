"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/subtree-of-another-tree/description/",
    "beats": 0.1450,
    "category": ["tree"],
    "tags": ["DFS"],
    "questions": []
}
"""

"""
思路
	- 通过树高来判断需不需要比较
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root, currDepth):
        if root is None:
            return currDepth
        return max(self.maxDepth(root.left, currDepth+1), self.maxDepth(root.right, currDepth+1))
    
    def isSame(self, s, t):
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        if s.val != t.val:
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
        
    
    def DFS(self, s, sDepth):
        if sDepth < self.tDepth:
            return False
        if sDepth == self.tDepth:
            return self.isSame(s, self.t)
        res = False
        if s.left:
            res |= self.DFS(s.left, self.maxDepth(s.left, 0))
        if s.right:
            res |= self.DFS(s.right, self.maxDepth(s.right, 0))
        return res
            
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.t = t
        self.tDepth = self.maxDepth(t, 0)
        return self.DFS(s, self.maxDepth(s, 0))