"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/maximum-depth-of-binary-tree/description/",
    "beats": 0.1657,
    "category": ["tree"],
    "tags": ["DFS","backtracking"],
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
    def DFS(self, node, currDepth):
        if node.left is None and node.right is None:
            self.maxDepth = max(self.maxDepth, currDepth)
        if node.left:
            self.DFS(node.left, currDepth+1)
        if node.right:
            self.DFS(node.right, currDepth+1)
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.maxDepth = 0
        self.DFS(root, 1)
        return self.maxDepth
