"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/subtree-of-another-tree/description/",
    "beats": 0.3564,
    "category": ["tree"],
    "tags": ["DFS"],
    "questions": []
}
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSame(self, s, t):
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        if s.val != t.val:
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None and t is not None:
            return False
        return self.isSame(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)