"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/path-sum/description/",
    "beats": 0.3325,
    "category": ["tree"],
    "tags": ["DFS"],
    "questions": []
}
"""

"""
ATTENTION
	- only root-to-LEAF paths are valid!!!
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DFS(self, node, currSum):
        if node.left is None and node.right is None:
            return currSum + node.val == self.target
        res = False
        if node.left:
            res |= self.DFS(node.left, currSum + node.val)
        if node.right:
            res |= self.DFS(node.right, currSum + node.val)
        return res
    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        self.target = sum
        return self.DFS(root, 0)