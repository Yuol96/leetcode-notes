"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/balanced-binary-tree/description/",
    "beats": 0.5338,
    "category": ["tree"],
    "tags": ["DFS"],
    "questions": []
}
"""

"""
思路
	- 递归地从最底层开始向上检查每个结点
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def maxDepth(self, node, currDepth):
    #     if node is None:
    #         return currDepth
    #     return max(self.maxDepth(node.left, currDepth+1), self.maxDepth(node.right, currDepth+1))
    
    def DFS(self, node):
        if node is None:
            return True, 0
        leftFlag, leftDepth = self.DFS(node.left)
        rightFlag, rightDepth = self.DFS(node.right)
        if not leftFlag or not rightFlag:
            return False, None
        if abs(leftDepth-rightDepth)>1:
            return False, 0
        return True, max(leftDepth, rightDepth) + 1
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        flag, depth = self.DFS(root)
        return flag