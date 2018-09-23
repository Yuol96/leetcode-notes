"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/merge-two-binary-trees/description/",
    "beats": 0.7414,
    "category": ["tree"],
    "tags": ["DFS"],
    "questions": []
}
"""

"""
思路
	- 同时DFS两个树的相同位置的结点
	- 如果DFS中只有一个结点不是None，那么就直接返回这个结点！！！
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DFS(self, t1, t2):
        if not t1 and not t2:
            return None
        if t1 and t2:
            left = self.DFS(t1.left, t2.left)
            right = self.DFS(t1.right, t2.right)
            node = TreeNode(t1.val+t2.val)
            node.left, node.right = left, right
            return node
        if t1:
            return t1
        if t2:
            return t2
        
    
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.DFS(t1, t2)