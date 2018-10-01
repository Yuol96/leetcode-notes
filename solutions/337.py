"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/house-robber-iii/description/",
    "beats": 1.0000,
    "category": ["tree"],
    "tags": ["DFS"],
    "questions": []
}
"""

"""
ATTENTION
	- 注意可能存在连续两个node都不rob的情况！
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
            return 0,0
        leftY, leftN = self.DFS(node.left)
        rightY, rightN = self.DFS(node.right)
        return node.val+leftN+rightN, max(leftY+rightY, leftY+rightN, leftN+rightY, leftN+rightN)
    
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a,b = self.DFS(root)
        return max(a,b)