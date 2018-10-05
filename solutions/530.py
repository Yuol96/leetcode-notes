"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/",
    "beats": 0.8556,
    "category": ["tree"],
    "tags": ["BST"],
    "questions": []
}
"""

"""
ATTENTION
	- `if self.lastValue is not None:` 不能写成 `if self.lastValue:`，因为self.lastValue可能是0
	- 最好避免`if var:`这种写法
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def DFS(self, node):
        if node is None:
            return
        self.DFS(node.left)
        if self.lastValue is not None:
            delta = node.val - self.lastValue
            self.minDelta = min(self.minDelta, delta)
        self.lastValue = node.val
        self.DFS(node.right)
    
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.minDelta = float('inf')
        self.lastValue = None
        self.DFS(root)
        return self.minDelta
