"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/",
    "beats": 0.7332,
    "category": ["tree"],
    "tags": ["BST"],
    "questions": []
}
"""

"""
思路
	- 前序遍历得到正常顺序，取第k个
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.k = 0
    
    def DFS(self, node):
        if node is None:
            return
        self.DFS(node.left)
        self.k += 1
        if self.k == self.target:
            self.ans = node.val
            return 
        self.DFS(node.right)
        
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.target = k
        self.DFS(root)
        return self.ans
