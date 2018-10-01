"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/convert-bst-to-greater-tree/description/",
    "beats": 0.9411,
    "category": ["tree"],
    "tags": ["BST"],
    "questions": []
}
"""

"""
思路
	- 反向的InOrder遍历，即right->root->left
	- visit结点的过程是累加
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
        self.DFS(node.right)
        self.cumulativeSum += node.val
        node.val = self.cumulativeSum
        self.DFS(node.left)
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.cumulativeSum = 0
        self.DFS(root)
        return root