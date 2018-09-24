"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/symmetric-tree/description/",
    "beats": 0.6577,
    "category": ["tree"],
    "tags": ["DFS"],
    "questions": []
}
"""

"""
思路
	- 同时递归比较root.left和root.right
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DFS(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.DFS(left.left, right.right) and self.DFS(left.right, right.left)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.DFS(root.left, root.right)
