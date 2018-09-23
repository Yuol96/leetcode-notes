"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/diameter-of-binary-tree/description/",
    "beats": 0.9911,
    "category": ["tree"],
    "tags": ["DFS"],
    "questions": []
}
"""

"""
思路
	- 每颗子树内，最大路径是左子树的最大高度 + 右子树最大高度。
	- 对所有子树递归地考虑一遍即可
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
            return 0
        leftPath = self.DFS(node.left)
        rightPath = self.DFS(node.right)  
        self.maxPath = max(leftPath+rightPath, self.maxPath)
        return max(leftPath, rightPath) + 1
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPath = 0
        self.DFS(root)
        return self.maxPath
