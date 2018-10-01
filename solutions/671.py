"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/",
    "beats": 0.9961,
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
        if node.val > self.minValue:
            self.ans = min(self.ans, node.val)
            return 
        if node.left is not None:
            self.DFS(node.left)
            self.DFS(node.right)
    
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.minValue = root.val
        self.ans = float('inf')
        self.DFS(root)
        if self.ans == float('inf'):
            return -1
        return self.ans