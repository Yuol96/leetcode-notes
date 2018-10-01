"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/",
    "beats": 0.5669,
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
    def count(self, node):
        if node is None:
            return 0
        return 1+self.count(node.left)+self.count(node.right)
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return 
        tmp = self.count(root.left)
        if tmp < k-1:
            return self.kthSmallest(root.right, k-tmp-1)
        elif tmp > k-1:
            return self.kthSmallest(root.left, k)
        else :
            return root.val