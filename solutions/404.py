"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/sum-of-left-leaves/description/",
    "beats": 0.4776,
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
    def DFS(self, node, isLeft):
        assert node is not None
        if node.left is None and node.right is None and isLeft:
            self.ans += node.val
            return
        if node.left:
            self.DFS(node.left, True)
        if node.right:
            self.DFS(node.right, False)
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        if root is None:
            return 0
        self.DFS(root, False)
        return self.ans