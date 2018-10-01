"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/binary-tree-inorder-traversal/description/",
    "beats": 0.9807,
    "category": ["tree"],
    "tags": ["DFS","traversal"],
    "questions": []
}
"""

"""
思路
	- 压栈时记录递归方向state
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [(root, 0)]
        lst = []
        while len(stack)>0:
            node, state = stack.pop()
            if node is None:
                continue
            if state == 0:
                stack.append((node, 1))
                stack.append((node.left, 0))
            else:
                lst.append(node.val)
                stack.append((node.right, 0))
        return lst