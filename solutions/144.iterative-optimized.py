"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/binary-tree-preorder-traversal/description/",
    "beats": 0.5379,
    "category": ["tree"],
    "tags": ["DFS","traversal"],
    "questions": []
}
"""

"""
思路
	- 先压入右子树，再左子树，保证顺序不错，这样可以避免在栈中记录递归方向
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        lst = []
        stack.append(root)
        while len(stack)>0:
            node = stack.pop()
            if node is None:
                continue
            lst.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return lst