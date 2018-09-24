"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/minimum-depth-of-binary-tree/description/",
    "beats": 0.8909,
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
    def DFS(self, node, currDepth):
        assert node is not None
        if node.left is None and node.right is None:
            self.minDepth = min(self.minDepth, currDepth+1)
            return
        if node.left:
            self.DFS(node.left, currDepth+1)
        if node.right:
            self.DFS(node.right, currDepth+1)
    
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.minDepth = float('inf')
        self.DFS(root, 0)
        return self.minDepth