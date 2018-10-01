"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/",
    "beats": 0.7111,
    "category": ["tree"],
    "tags": ["BST"],
    "questions": []
}
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val > max(p.val,q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val,q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else :
            return root