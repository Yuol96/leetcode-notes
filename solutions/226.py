"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/invert-binary-tree/description/",
    "beats": 0.1241,
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
    def DFS(self, node):
        if node is None:
            return
        self.DFS(node.left)
        self.DFS(node.right)
        node.left, node.right = node.right, node.left
    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.DFS(root)
        return root