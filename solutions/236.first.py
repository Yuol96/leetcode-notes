"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/",
    "beats": 0.4091,
    "category": ["tree"],
    "tags": ["DFS"],
    "questions": []
}
"""

"""
思路
	- DFS返回符合条件的结点个数
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
            return 0
        if (node is self.p) or (node is self.q):
            if self.DFS(node.left) or self.DFS(node.right):
                self.ans = node
                return 2
            return 1
        else:
            a = self.DFS(node.left)
            b = self.DFS(node.right)
            if a==1 and b==1:
                self.ans = node
                return 2
            return a+b

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.p = p
        self.q = q
        self.DFS(root)
        return self.ans
